import os
import json
import traceback
import sys
import ipaddress
import csv
import shutil
from datetime import datetime
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID
from ....Utils.cliutils import load_cli_settings

def calculateLocalIp(subnet):
    """
    Calculate the first usable IP address from a subnet/CIDR notation.
    Returns the network address + 1 (first host IP).
    
    Args:
        subnet (str): Subnet in CIDR notation (e.g., "192.168.1.0/24")
    
    Returns:
        str: First usable IP address, or None if invalid subnet
    """
    if not subnet or subnet == "":
        return None
        
    try:
        # Parse the subnet
        network = ipaddress.IPv4Network(subnet, strict=False)
        
        # Get the first usable IP (network address + 1)
        # For /31 and /32 networks, return the network address itself
        if network.prefixlen >= 31:
            return str(network.network_address)
        else:
            # Return network + 1 (first host address)
            first_host = network.network_address + 1
            return str(first_host)
            
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as e:
        # Invalid subnet format
        return None

def generate_template(args):
    """
    Generate template files from embedded templates directory
    """
    try:
        # Get the directory of this script to locate templates
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Try multiple possible template directory locations
        # 1. Development mode: go up 4 directories
        # 2. Installed package: templates should be in the package root
        possible_template_dirs = [
            os.path.join(script_dir, '..', '..', '..', '..', 'templates'),  # Development
            os.path.join(os.path.dirname(script_dir.split('catocli')[0]), 'catocli', 'templates'),  # Installed package
        ]
        
        templates_dir = None
        for potential_dir in possible_template_dirs:
            normalized_dir = os.path.normpath(potential_dir)
            if os.path.exists(normalized_dir):
                templates_dir = normalized_dir
                break
        
        if templates_dir is None:
            # Fallback: look for templates directory in catocli package
            import catocli
            catocli_root = os.path.dirname(os.path.abspath(catocli.__file__))
            fallback_templates_dir = os.path.join(catocli_root, 'templates')
            if os.path.exists(fallback_templates_dir):
                templates_dir = fallback_templates_dir
            else:
                raise Exception(f"Templates directory not found. Searched locations: {possible_template_dirs} and {fallback_templates_dir}")
        
        # Get the template format from export_format argument (defaults to json)
        template_format = getattr(args, 'export_format', 'json')
        
        # Determine output directory
        output_dir = getattr(args, 'output_directory', None)
        if output_dir is None:
            output_dir = '.'
        if not os.path.isabs(output_dir):
            output_dir = os.path.join(os.getcwd(), output_dir)
        
        os.makedirs(output_dir, exist_ok=True)
        
        copied_files = []
        
        if template_format == 'csv':
            # Copy CSV template files
            template_files = ['socket_sites.csv', 'Test_network_ranges.csv']
            for template_file in template_files:
                src_path = os.path.join(templates_dir, template_file)
                dst_path = os.path.join(output_dir, template_file)
                
                if os.path.exists(src_path):
                    shutil.copy2(src_path, dst_path)
                    copied_files.append(dst_path)
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"Copied template: {src_path} -> {dst_path}")
                else:
                    print(f"Warning: Template file not found: {src_path}")
        
        elif template_format == 'json':
            # Copy JSON template file
            template_file = 'socket_sites.json'
            src_path = os.path.join(templates_dir, template_file)
            dst_path = os.path.join(output_dir, template_file)
            
            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)
                copied_files.append(dst_path)
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Copied template: {src_path} -> {dst_path}")
            else:
                print(f"Warning: Template file not found: {src_path}")
        
        if copied_files:
            print(f"Successfully generated {template_format.upper()} template files:")
            for file_path in copied_files:
                print(f"  {file_path}")
            return [{"success": True, "template_format": template_format, "copied_files": copied_files}]
        else:
            return [{"success": False, "error": f"No template files found for format: {template_format}"}]
    
    except Exception as e:
        print(f"Error generating template: {str(e)}")
        return [{"success": False, "error": str(e)}]

def export_socket_sites_dispatcher(args, configuration):
    """
    Dispatcher function that routes to JSON or CSV export based on format argument
    """
    # Check if template generation is requested
    if hasattr(args, 'generate_template') and args.generate_template:
        return generate_template(args)
    
    export_format = getattr(args, 'export_format', 'json')
    
    if export_format == 'csv':
        return export_socket_site_to_csv(args, configuration)
    else:
        return export_socket_site_to_json(args, configuration)


def export_socket_site_to_json(args, configuration):
    """
    Export consolidated site and socket data to JSON format
    """
    processed_data = {'sites':[]}
    warning_stats = {
        'missing_sites': 0,
        'missing_interfaces': 0,
        'missing_data': 0,
        'missing_interface_details': []
    }

    try:
        # Load CLI settings using the robust function
        settings = load_cli_settings()
        # Note: load_cli_settings() now returns embedded defaults if file cannot be loaded
        
        account_id = getAccountID(args, configuration)
        # Get account snapshot with siteIDs if provided
        # Get siteIDs from args if provided (comma-separated string)
        site_ids = []
        if hasattr(args, 'siteIDs') and args.siteIDs:
            # Parse comma-separated string into list, removing whitespace
            site_ids = [site_id.strip() for site_id in args.siteIDs.split(',') if site_id.strip()]
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Filtering snapshot for site IDs: {site_ids}")
        
        ###############################################################
        ## Call APIs to retrieve sites, interface and network ranges ##
        ###############################################################
        snapshot_sites = getAccountSnapshot(args, configuration, account_id, site_ids)
        
        # Check if no sites were found and handle gracefully
        sites_list = snapshot_sites['data']['accountSnapshot']['sites']
        if not sites_list or len(sites_list) == 0:
            if site_ids:
                # User provided specific site IDs but none were found
                print(f"No sites found matching the provided site IDs: {', '.join(site_ids)}")
                print("Please verify the site IDs are correct and that they exist in this account.")
                return [{"success": False, "message": f"No sites found for the specified site IDs: {', '.join(site_ids)}", "sites_requested": site_ids}]
            else:
                # No site filter was provided but no sites exist at all
                print("No sites found in this account.")
                return [{"success": False, "message": "No sites found in account", "account_id": account_id}]
        
        if hasattr(args, 'verbose') and args.verbose:
            if site_ids:
                print(f"Found {len(sites_list)} site(s) matching the provided site IDs")
            else:
                print(f"Found {len(sites_list)} site(s) in account")
        
        entity_network_interfaces = getEntityLookup(args, configuration, account_id, "networkInterface")
        entity_network_ranges = getEntityLookup(args, configuration, account_id, "siteRange")
        entity_sites = getEntityLookup(args, configuration, account_id, "site")
        
        ##################################################################
        ## Create processed_data object indexed by siteId with location ##
        ##################################################################
        for snapshot_site in snapshot_sites['data']['accountSnapshot']['sites']:
            site_id = snapshot_site.get('id')
            connectionType = snapshot_site.get('infoSiteSnapshot', {}).get('connType', "")
            # # Placeholder code to rename what the API returns if export should support cloud deployments 
            # if connectionType=="VSOCKET_VGX_AWS":
            #     connectionType = "SOCKET_AWS1500"
            # elif connectionType=="VSOCKET_VGX_AZURE":
            #     connectionType = "SOCKET_AZ1500"
            # elif connectionType=="VSOCKET_VGX_ESX":
            #     connectionType = "SOCKET_ESX1500"            

            cur_site = {
                'wan_interfaces': [],
                'lan_interfaces': [],
                'native_range': {}
            }

            if connectionType in settings["export_by_socket_type"]:
                cur_site['id'] = site_id
                cur_site['name'] = snapshot_site.get('infoSiteSnapshot', {}).get('name')
                cur_site['description'] = snapshot_site.get('infoSiteSnapshot', {}).get('description')
                cur_site['connection_type'] = connectionType
                cur_site['type'] = snapshot_site.get('infoSiteSnapshot', {}).get('type')
                cur_site = populateSiteLocationData(args, snapshot_site, cur_site)
                # print("connectionType={connectionType} site_id={site_id} site_name={site_name}".format(connectionType=connectionType, site_id=site_id, site_name=cur_site['name']))
                # if connectionType in settings["default_socket_interface_map"]:
                #     print("default_interface__index="+settings["default_socket_interface_map"][connectionType])
                
                # Create a map of interfaces from account snapshot for native range lookup
                site_interfaces = snapshot_site.get('infoSiteSnapshot', {}).get('interfaces', [])
                interface_lookup = {}  # Map interface ID to interface data
                lan_lag_member_count = 0  # Count LAN_LAG_MEMBER interfaces for lag calculation
                
                for interface in site_interfaces:
                    role = interface.get('wanRoleInterfaceInfo', "")
                    dest_type = interface.get('destType', "")
                    interfaceName = interface.get('id', "")
                    
                    # Store interface data for lookup
                    interface_lookup[interfaceName] = {
                        'dest_type': dest_type,
                        'name': interface.get('name', ""),
                        'role': role
                    }
                    
                    # Count LAN_LAG_MEMBER interfaces for lag calculation
                    if dest_type == "LAN_LAG_MEMBER":
                        lan_lag_member_count += 1
                    
                    # Process WAN interfaces
                    if role is not None and role[0:3] == "wan":
                        cur_wan_interface = {}
                        if interfaceName[0:3] in ("WAN", "USB", "LTE"):
                            cur_wan_interface['id'] = site_id+":"+ interface.get('id', "")
                        else:
                            cur_wan_interface['id'] = site_id+":INT_"+ interface.get('id', "")
                        # Format WAN interface index: INT_X for numeric values, keep as-is for non-numeric
                        wan_interface_id = interface.get('id', "")
                        if isinstance(wan_interface_id, (int, str)) and str(wan_interface_id).isdigit():
                            cur_wan_interface['index'] = f"INT_{wan_interface_id}"
                        else:
                            cur_wan_interface['index'] = wan_interface_id
                        cur_wan_interface['name'] = interface.get('name', "")
                        cur_wan_interface['upstream_bandwidth'] = interface.get('upstreamBandwidth', 0)
                        cur_wan_interface['downstream_bandwidth'] = interface.get('downstreamBandwidth', 0)
                        cur_wan_interface['dest_type'] = dest_type
                        cur_wan_interface['role'] = role
                        # Not supported via API to be populated later when available
                        cur_wan_interface['precedence'] = "ACTIVE"
                        cur_site['wan_interfaces'].append(cur_wan_interface)
                    
                    # Process LAN_LAG_MEMBER interfaces
                    elif dest_type == "LAN_LAG_MEMBER":
                        cur_lan_interface = {
                            'network_ranges': []
                        }
                        # LAN_LAG_MEMBER interfaces don't have a numeric ID, only index and name
                        cur_lan_interface['id'] = None  # Set to null for LAN_LAG_MEMBER
                        cur_lan_interface['name'] = interface.get('name', "")
                        # Format interface index: INT_X for numeric values, keep as-is for non-numeric
                        interface_id = interface.get('id', "")
                        if isinstance(interface_id, (int, str)) and str(interface_id).isdigit():
                            cur_lan_interface['index'] = f"INT_{interface_id}"
                        else:
                            cur_lan_interface['index'] = interface_id
                        cur_lan_interface['dest_type'] = dest_type
                        cur_site['lan_interfaces'].append(cur_lan_interface)
                
                # Store the interface lookup and LAN_LAG_MEMBER count for later use
                cur_site['_interface_lookup'] = interface_lookup
                cur_site['_lan_lag_member_count'] = lan_lag_member_count

                if site_id:
                    processed_data['sites'].append(cur_site)

        ##################################################################################
        ## Process entity lookup LAN network interfaces adding to site object by site_id##
        ##################################################################################
        for lan_ni in entity_network_interfaces:
            # Only add interface if the site exists in processed_data
            lan_ni_helper_fields = lan_ni.get("helperFields", {})
            lan_ni_entity_data = lan_ni.get('entity', {})
            lan_ni_site_id = str(lan_ni_helper_fields.get('siteId', ""))
            cur_site_entry = next((site for site in processed_data['sites'] if site['id'] == lan_ni_site_id), None)
            if cur_site_entry:
                cur_lan_interface = {
                    'network_ranges': []
                }
                ni_interface_id = lan_ni_entity_data.get('id', "")
                ni_interface_name = lan_ni_helper_fields.get('interfaceName', "")
                lan_ni_subnet = str(lan_ni_helper_fields.get('subnet', ""))
                ni_index = lan_ni_helper_fields.get('interfaceId', "")
                ni_index = f"INT_{ni_index}" if isinstance(ni_index, (int, str)) and str(ni_index).isdigit() else ni_index
                if cur_site_entry["connection_type"] in settings["default_socket_interface_map"] and ni_index in settings["default_socket_interface_map"][cur_site_entry["connection_type"]]:
                    cur_native_range = cur_site_entry["native_range"]
                    cur_site_entry["native_range"]["interface_id"] = ni_interface_id
                    cur_site_entry["native_range"]["interface_name"] = ni_interface_name
                    cur_site_entry["native_range"]["subnet"] = lan_ni_subnet
                    cur_site_entry["native_range"]["index"] = ni_index
                    
                    # Get interface details from the stored lookup data
                    interface_lookup = cur_site_entry.get('_interface_lookup', {})
                    interface_details = interface_lookup.get(str(lan_ni_helper_fields.get('interfaceId', '')), {})
                    native_range_dest_type = interface_details.get('dest_type', '')
                    cur_site_entry["native_range"]["dest_type"] = native_range_dest_type
                    
                    # Calculate lag_min_links for native range interface if it's LAN_LAG_MASTER
                    lag_min_links = ''
                    if native_range_dest_type == 'LAN_LAG_MASTER':
                        lan_lag_member_count = cur_site_entry.get('_lan_lag_member_count', 0)
                        lag_min_links = str(lan_lag_member_count) if lan_lag_member_count > 0 else ''
                    cur_site_entry["native_range"]["lag_min_links"] = lag_min_links
                    
                    # Add entry to lan interfaces for default_lan
                    cur_site_entry['lan_interfaces'].append({"network_ranges": [],"default_lan":True})
                else:
                    cur_lan_interface['id'] = ni_interface_id
                    cur_lan_interface['name'] = ni_interface_name
                    cur_lan_interface['index'] = ni_index
                    cur_lan_interface['dest_type'] = lan_ni_helper_fields.get('destType', "")
                    # temporarily add subnet to interface to be used later to flas native range_range
                    cur_lan_interface['subnet'] = lan_ni_subnet
                    cur_site_entry['lan_interfaces'].append(cur_lan_interface)
            else:
                if hasattr(args, 'verbose') and args.verbose:
                    ni_interface_name = lan_ni_helper_fields.get('interfaceName', "")
                    ni_interface_id = lan_ni_entity_data.get('id', "")
                    print(f"WARNING: Site {lan_ni_site_id} not found in snapshot data, skipping interface {ni_interface_name} ({ni_interface_id})")

        #############################################################################
        ## Process entity lookup network ranges populating by network interface id ##
        #############################################################################
        for range in entity_network_ranges:
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Processing network range: {type(range)} - {range}")
            nr_helper_fields = range.get("helperFields", {})
            nr_entity_data = range.get('entity', {})
            nr_interface_name = str(nr_helper_fields.get('interfaceName', ""))
            nr_site_id = str(nr_helper_fields.get('siteId', ""))
            range_id = nr_entity_data.get('id', "")
                        
            nr_site_entry = next((site for site in processed_data['sites'] if site['id'] == nr_site_id), None)
            if nr_site_entry:
                nr_subnet = nr_helper_fields.get('subnet', None)
                nr_vlan = nr_helper_fields.get('vlanTag', None)
                nr_mdns_reflector = nr_helper_fields.get('mdnsReflector', False)
                nr_dhcp_microsegmentation = nr_helper_fields.get('microsegmentation', False)
                nr_interface_name = str(nr_helper_fields.get('interfaceName', ""))
                range_name = nr_entity_data.get('name', nr_interface_name)
                if range_name and " \\ " in range_name:
                    range_name = range_name.split(" \\ ").pop()
                range_id = nr_entity_data.get('id', "")

                # the following fields are missing from the schema, populating blank fields in the interim
                nr_dhcp_type = nr_helper_fields.get('XXXXX', "DHCP_DISABLED")
                nr_ip_range = nr_helper_fields.get('XXXXX', None)
                # nr_relay_group_id = nr_helper_fields.get('XXXXX', None)
                nr_relay_group_name = nr_helper_fields.get('XXXXX', None)
                nr_gateway = nr_helper_fields.get('XXXXX', None)
                nr_translated_subnet = nr_helper_fields.get('XXXXX', None)
                nr_internet_only = nr_helper_fields.get('XXXXX', None)  # Default to None for JSON
                nr_local_ip = nr_helper_fields.get('XXXXX', None)
                nr_range_type = nr_helper_fields.get('XXXXX', None)
                # Adding logic to pre-populate with default value
                if nr_vlan!=None:
                    nr_range_type="VLAN"
                else:
                    nr_range_type="Direct"

                # Calculate local IP from subnet if --calculate-local-ip flag is set
                if hasattr(args, 'calculate_local_ip') and args.calculate_local_ip and nr_subnet:
                    calculated_ip = calculateLocalIp(nr_subnet)
                    if calculated_ip:
                        nr_local_ip = calculated_ip
                        if hasattr(args, 'verbose') and args.verbose:
                            print(f"  Calculated local IP for subnet {nr_subnet}: {calculated_ip}")

                site_native_range = nr_site_entry.get('native_range', {}) if nr_site_entry else {}
                
                if site_native_range.get("interface_name", "") == nr_interface_name:
                    if range_name!="Native Range":
                        nr_lan_interface_entry = next((lan_nic for lan_nic in nr_site_entry["lan_interfaces"] if 'default_lan' in lan_nic and lan_nic['default_lan']), None)
                        # print(f"checking range: {network_range_site_id} - {network_range_interface_name}")
                        if nr_lan_interface_entry:
                            cur_range = {}
                            cur_range['id'] = range_id
                            cur_range['name'] = range_name
                            cur_range['subnet'] = nr_subnet
                            cur_range['vlan'] = nr_vlan
                            cur_range['mdns_reflector'] = nr_mdns_reflector
                            ## The folliowing fields are missing from the schema, populating blank fields in the interim
                            cur_range['gateway'] = nr_gateway
                            cur_range['range_type'] = nr_range_type
                            cur_range['translated_subnet'] = nr_translated_subnet
                            cur_range['internet_only'] = nr_internet_only
                            cur_range['local_ip'] = nr_local_ip  # Use the calculated or original value
                            cur_range['dhcp_settings'] = {
                                'dhcp_type': nr_dhcp_type,
                                'ip_range': nr_ip_range,
                                'relay_group_id': None,
                                'relay_group_name': nr_relay_group_name,
                                'dhcp_microsegmentation': nr_dhcp_microsegmentation
                            }
                            nr_lan_interface_entry["network_ranges"].append(cur_range)
                    else:
                        site_native_range['range_name'] = range_name
                        site_native_range['range_id'] = range_id
                        site_native_range['vlan'] = nr_vlan
                        site_native_range['mdns_reflector'] = nr_mdns_reflector
                        # site_native_range['dhcp_microsegmentation'] = nr_dhcp_microsegmentation
                        site_native_range['gateway'] = nr_gateway
                        site_native_range['range_type'] = nr_range_type
                        site_native_range['translated_subnet'] = nr_translated_subnet
                        site_native_range['internet_only'] = nr_internet_only
                        site_native_range['local_ip'] = nr_local_ip
                        site_native_range['dhcp_settings'] = {
                            'dhcp_type': nr_dhcp_type,
                            'ip_range': nr_ip_range,
                            'relay_group_id': None,
                            'relay_group_name': nr_relay_group_name,
                            'dhcp_microsegmentation': nr_dhcp_microsegmentation
                        }
                else:
                    nr_lan_interface_entry = next((lan_nic for lan_nic in nr_site_entry["lan_interfaces"] if ('default_lan' not in lan_nic or not lan_nic['default_lan']) and lan_nic['name'] == nr_interface_name), None)                    
                    if nr_lan_interface_entry:
                        cur_range = {}
                        cur_range['id'] = range_id
                        cur_range['name'] = range_name
                        cur_range['subnet'] = nr_subnet
                        cur_range['vlan'] = nr_vlan
                        cur_range['mdns_reflector'] = nr_mdns_reflector
                        ## The folliowing fields are missing from the schema, populating blank fields in the interim
                        cur_range['gateway'] = nr_gateway
                        cur_range['range_type'] = nr_range_type
                        cur_range['translated_subnet'] = nr_translated_subnet
                        cur_range['internet_only'] = nr_internet_only
                        cur_range['local_ip'] = nr_local_ip  # Use the calculated or original value
                        cur_range['dhcp_settings'] = {
                            'dhcp_type': nr_dhcp_type,
                            'ip_range': nr_ip_range,
                            'relay_group_id': None,
                            'relay_group_name': nr_relay_group_name,
                            'dhcp_microsegmentation': nr_dhcp_microsegmentation
                        }
                        # DEBUG
                        # print(json.dumps(nr_lan_interface_entry,indent=4,sort_keys=True))
                        # print("nr_subnet",nr_subnet)
                        # print('nr_lan_interface_entry["subnet"]='+nr_lan_interface_entry["subnet"])
                        # print(json.dumps(nr_lan_interface_entry,indent=4,sort_keys=True))
                        if "subnet" in nr_lan_interface_entry and nr_subnet==nr_lan_interface_entry["subnet"]:
                            cur_range['native_range'] = True
                            del nr_lan_interface_entry["subnet"]

                        nr_lan_interface_entry["network_ranges"].append(cur_range)
                    else:
                        if hasattr(args, 'verbose') and args.verbose:
                            print(f"Skipping range {nr_entity_data.get('id', '')}: site_id {nr_site_id} and {nr_interface_name} not found in ")
            else:
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Skipping range, site_id is unsupported for export {nr_site_id}")
        
        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            # User provided custom filename
            base_filename = args.json_filename
            # Remove .json extension if provided, we'll add it back
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            # Use default filename template
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"socket_sites_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "socket_sites_{account_id}.json"
        
        if hasattr(args, 'verbose') and args.verbose:
            if hasattr(args, 'json_filename') and args.json_filename:
                print(f"Using custom filename template: {filename_template}")
            else:
                print(f"Using default filename template: {filename_template}")
            
        # Write the processed data to file using the general-purpose function
        output_file = writeDataToFile(
            data=processed_data,
            args=args,
            account_id=account_id,
            default_filename_template=filename_template,
            default_directory="config_data"
        )
        
        return [{"success": True, "output_file": output_file, "account_id": account_id}]
            
    except Exception as e:
        # Get the current exception info
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Get the line number where the error occurred
        line_number = exc_traceback.tb_lineno
        filename = exc_traceback.tb_frame.f_code.co_filename
        function_name = exc_traceback.tb_frame.f_code.co_name
        
        # Get the full traceback as a string
        full_traceback = traceback.format_exc()
        
        # Create detailed error message
        error_details = {
            "error_type": exc_type.__name__,
            "error_message": str(exc_value),
            "line_number": line_number,
            "function_name": function_name,
            "filename": os.path.basename(filename),
            "full_traceback": full_traceback
        }
        
        # Print detailed error information
        print(f"ERROR: {exc_type.__name__}: {str(exc_value)}")
        print(f"Location: {os.path.basename(filename)}:{line_number} in {function_name}()")
        print(f"Full traceback:\n{full_traceback}")
        
        return [{"success": False, "error": str(e), "error_details": error_details}]


def export_socket_site_to_csv(args, configuration):
    """
    Export consolidated site and socket data to CSV format
    Creates main sites CSV and individual network ranges CSV files
    """
    try:
        # Get the processed data directly without creating JSON file
        processed_data = get_processed_site_data(args, configuration)
        
        if not processed_data or not processed_data.get('sites'):
            return [{"success": False, "error": "No sites data found to export"}]
        
        account_id = getAccountID(args, configuration)
        output_files = []
        
        # Export main sites CSV
        sites_csv_file = export_sites_to_csv(processed_data['sites'], args, account_id)
        output_files.append(sites_csv_file)
        
        # Export individual network ranges CSV files for each site
        for site in processed_data['sites']:
            ranges_csv_file = export_network_ranges_to_csv(site, args, account_id)
            if ranges_csv_file:
                output_files.append(ranges_csv_file)
        
        return [{"success": True, "output_files": output_files, "account_id": account_id}]
        
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        filename = exc_traceback.tb_frame.f_code.co_filename
        function_name = exc_traceback.tb_frame.f_code.co_name
        full_traceback = traceback.format_exc()
        
        error_details = {
            "error_type": exc_type.__name__,
            "error_message": str(exc_value),
            "line_number": line_number,
            "function_name": function_name,
            "filename": os.path.basename(filename),
            "full_traceback": full_traceback
        }
        
        print(f"ERROR: {exc_type.__name__}: {str(exc_value)}")
        print(f"Location: {os.path.basename(filename)}:{line_number} in {function_name}()")
        print(f"Full traceback:\n{full_traceback}")
        
        return [{"success": False, "error": str(e), "error_details": error_details}]


def get_processed_site_data(args, configuration):
    """
    Get processed site data without writing to JSON file
    Reuses the logic from export_socket_site_to_json but returns data instead
    """
    processed_data = {'sites': []}
    
    # Load CLI settings
    settings = load_cli_settings()
    # Note: load_cli_settings() now returns embedded defaults if file cannot be loaded
    
    account_id = getAccountID(args, configuration)
    
    # Get siteIDs from args if provided
    site_ids = []
    if hasattr(args, 'siteIDs') and args.siteIDs:
        site_ids = [site_id.strip() for site_id in args.siteIDs.split(',') if site_id.strip()]
    
    # Call APIs to retrieve sites, interface and network ranges
    snapshot_sites = getAccountSnapshot(args, configuration, account_id, site_ids)
    sites_list = snapshot_sites['data']['accountSnapshot']['sites']
    
    if not sites_list or len(sites_list) == 0:
        return processed_data
    
    entity_network_interfaces = getEntityLookup(args, configuration, account_id, "networkInterface")
    entity_network_ranges = getEntityLookup(args, configuration, account_id, "siteRange")
    entity_sites = getEntityLookup(args, configuration, account_id, "site")
    
    # Process sites (reuse existing logic)
    for snapshot_site in snapshot_sites['data']['accountSnapshot']['sites']:
        site_id = snapshot_site.get('id')
        connectionType = snapshot_site.get('infoSiteSnapshot', {}).get('connType', "")
        
        cur_site = {
            'wan_interfaces': [],
            'lan_interfaces': [],
            'native_range': {}
        }
        
        if connectionType in settings["export_by_socket_type"]:
            cur_site['id'] = site_id
            cur_site['name'] = snapshot_site.get('infoSiteSnapshot', {}).get('name')
            cur_site['description'] = snapshot_site.get('infoSiteSnapshot', {}).get('description')
            cur_site['connection_type'] = connectionType
            cur_site['type'] = snapshot_site.get('infoSiteSnapshot', {}).get('type')
            cur_site = populateSiteLocationData(args, snapshot_site, cur_site)
            
            # Create a map of interfaces from account snapshot for native range lookup
            site_interfaces = snapshot_site.get('infoSiteSnapshot', {}).get('interfaces', [])
            interface_lookup = {}  # Map interface ID to interface data
            lan_lag_member_count = 0  # Count LAN_LAG_MEMBER interfaces for lag calculation
            
            if hasattr(args, 'verbose') and args.verbose:        
                print(f"DEBUG: Processing site {site_id} ({cur_site['name']}) with {len(site_interfaces)} interfaces")
            
            for interface in site_interfaces:
                role = interface.get('wanRoleInterfaceInfo', "")
                dest_type = interface.get('destType', "")
                interfaceName = interface.get('id', "")
                
                # Store interface data for lookup
                interface_lookup[interfaceName] = {
                    'dest_type': dest_type,
                    'name': interface.get('name', ""),
                    'role': role
                }
                
                # Count LAN_LAG_MEMBER interfaces for lag calculation
                if dest_type == "LAN_LAG_MEMBER":
                    lan_lag_member_count += 1
                
                # Process WAN interfaces
                if role is not None and role[0:3] == "wan":
                    cur_wan_interface = {}
                    if interfaceName[0:3] in ("WAN", "USB", "LTE"):
                        cur_wan_interface['id'] = site_id+":"+ interface.get('id', "")
                    else:
                        cur_wan_interface['id'] = site_id+":INT_"+ interface.get('id', "")
                    # Format WAN interface index: INT_X for numeric values, keep as-is for non-numeric
                    wan_interface_id = interface.get('id', "")
                    if isinstance(wan_interface_id, (int, str)) and str(wan_interface_id).isdigit():
                        cur_wan_interface['index'] = f"INT_{wan_interface_id}"
                    else:
                        cur_wan_interface['index'] = wan_interface_id
                    cur_wan_interface['name'] = interface.get('name', "")
                    cur_wan_interface['upstream_bandwidth'] = interface.get('upstreamBandwidth', 0)
                    cur_wan_interface['downstream_bandwidth'] = interface.get('downstreamBandwidth', 0)
                    cur_wan_interface['dest_type'] = dest_type
                    cur_wan_interface['role'] = role
                    cur_wan_interface['precedence'] = "ACTIVE"
                    cur_site['wan_interfaces'].append(cur_wan_interface)
                
                # Process LAN_LAG_MEMBER interfaces
                elif dest_type == "LAN_LAG_MEMBER":
                    if hasattr(args, 'verbose') and args.verbose:            
                        print(f"DEBUG: Processing LAN_LAG_MEMBER interface for site {site_id}: {interface.get('name', '')} (id: {interface.get('id', '')})")
                    cur_lan_interface = {
                        'network_ranges': []
                    }
                    # LAN_LAG_MEMBER interfaces don't have a numeric ID, only index and name
                    cur_lan_interface['id'] = ''  # No ID for LAN_LAG_MEMBER
                    cur_lan_interface['name'] = interface.get('name', "")
                    # Format interface index: INT_X for numeric values, keep as-is for non-numeric
                    interface_id = interface.get('id', "")
                    if isinstance(interface_id, (int, str)) and str(interface_id).isdigit():
                        cur_lan_interface['index'] = f"INT_{interface_id}"
                    else:
                        cur_lan_interface['index'] = interface_id
                    cur_lan_interface['dest_type'] = dest_type
                    cur_site['lan_interfaces'].append(cur_lan_interface)
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"DEBUG: Added LAN_LAG_MEMBER interface: {cur_lan_interface}")
            
            # Store the interface lookup and LAN_LAG_MEMBER count for later use
            cur_site['_interface_lookup'] = interface_lookup
            cur_site['_lan_lag_member_count'] = lan_lag_member_count
            
            if site_id:
                processed_data['sites'].append(cur_site)
                if hasattr(args, 'verbose') and args.verbose:        
                    print(f"DEBUG: Added site {site_id} ({cur_site['name']}) with {len(cur_site['lan_interfaces'])} LAN interfaces (including {lan_lag_member_count} LAN_LAG_MEMBER interfaces)")
    
    # Print summary of LAN_LAG_MEMBER interfaces found
    total_lag_members = sum(len([intf for intf in site['lan_interfaces'] if intf.get('dest_type') == 'LAN_LAG_MEMBER']) for site in processed_data['sites'])
    if hasattr(args, 'verbose') and args.verbose:
        print(f"DEBUG: Total LAN_LAG_MEMBER interfaces found across all sites: {total_lag_members}")
    
    # Process LAN interfaces (reuse existing logic)
    for lan_ni in entity_network_interfaces:
        lan_ni_helper_fields = lan_ni.get("helperFields", {})
        lan_ni_entity_data = lan_ni.get('entity', {})
        lan_ni_site_id = str(lan_ni_helper_fields.get('siteId', ""))
        cur_site_entry = next((site for site in processed_data['sites'] if site['id'] == lan_ni_site_id), None)
        if cur_site_entry:
            cur_lan_interface = {'network_ranges': []}
            ni_interface_id = lan_ni_entity_data.get('id', "")
            ni_interface_name = lan_ni_helper_fields.get('interfaceName', "")
            lan_ni_subnet = str(lan_ni_helper_fields.get('subnet', ""))
            ni_index = lan_ni_helper_fields.get('interfaceId', "")
            ni_index = f"INT_{ni_index}" if isinstance(ni_index, (int, str)) and str(ni_index).isdigit() else ni_index
            
            if cur_site_entry["connection_type"] in settings["default_socket_interface_map"] and ni_index in settings["default_socket_interface_map"][cur_site_entry["connection_type"]]:
                cur_site_entry["native_range"]["interface_id"] = ni_interface_id
                cur_site_entry["native_range"]["interface_name"] = ni_interface_name
                cur_site_entry["native_range"]["subnet"] = lan_ni_subnet
                cur_site_entry["native_range"]["index"] = ni_index
                
                # Get interface details from the stored lookup data
                interface_lookup = cur_site_entry.get('_interface_lookup', {})
                interface_details = interface_lookup.get(str(lan_ni_helper_fields.get('interfaceId', '')), {})
                native_range_dest_type = interface_details.get('dest_type', '')
                cur_site_entry["native_range"]["dest_type"] = native_range_dest_type
                
                # Calculate lag_min_links for native range interface if it's LAN_LAG_MASTER
                lag_min_links = ''
                if native_range_dest_type == 'LAN_LAG_MASTER':
                    lan_lag_member_count = cur_site_entry.get('_lan_lag_member_count', 0)
                    lag_min_links = str(lan_lag_member_count) if lan_lag_member_count > 0 else ''
                cur_site_entry["native_range"]["lag_min_links"] = lag_min_links
                
                cur_site_entry['lan_interfaces'].append({"network_ranges": [], "default_lan": True})
            else:
                cur_lan_interface['id'] = ni_interface_id
                cur_lan_interface['name'] = ni_interface_name
                cur_lan_interface['index'] = ni_index
                cur_lan_interface['dest_type'] = lan_ni_helper_fields.get('destType', "")
                cur_lan_interface['subnet'] = lan_ni_subnet
                cur_site_entry['lan_interfaces'].append(cur_lan_interface)
    
    # Process network ranges (reuse existing logic)
    for range in entity_network_ranges:
        nr_helper_fields = range.get("helperFields", {})
        nr_entity_data = range.get('entity', {})
        nr_interface_name = str(nr_helper_fields.get('interfaceName', ""))
        nr_site_id = str(nr_helper_fields.get('siteId', ""))
        range_id = nr_entity_data.get('id', "")
        
        nr_site_entry = next((site for site in processed_data['sites'] if site['id'] == nr_site_id), None)
        if nr_site_entry:
            nr_subnet = nr_helper_fields.get('subnet', None)
            nr_vlan = nr_helper_fields.get('vlanTag', None)
            nr_mdns_reflector = nr_helper_fields.get('mdnsReflector', False)
            nr_dhcp_microsegmentation = nr_helper_fields.get('microsegmentation', False)
            range_name = nr_entity_data.get('name', nr_interface_name)
            if range_name and " \\ " in range_name:
                range_name = range_name.split(" \\ ").pop()
            
            # Set defaults for missing fields
            nr_dhcp_type = "DHCP_DISABLED"
            nr_ip_range = None
            nr_relay_group_name = None
            nr_gateway = None
            nr_translated_subnet = None
            nr_internet_only = None  # Default to None for JSON
            nr_local_ip = None
            nr_range_type = "VLAN" if nr_vlan != None else "Direct"
            
            # Calculate local IP if requested
            if hasattr(args, 'calculate_local_ip') and args.calculate_local_ip and nr_subnet:
                calculated_ip = calculateLocalIp(nr_subnet)
                if calculated_ip:
                    nr_local_ip = calculated_ip
            
            site_native_range = nr_site_entry.get('native_range', {})
            
            if site_native_range.get("interface_name", "") == nr_interface_name:
                if range_name != "Native Range":
                    nr_lan_interface_entry = next((lan_nic for lan_nic in nr_site_entry["lan_interfaces"] if 'default_lan' in lan_nic and lan_nic['default_lan']), None)
                    if nr_lan_interface_entry:
                        cur_range = {
                            'id': range_id, 'name': range_name, 'subnet': nr_subnet, 'vlan': nr_vlan,
                            'mdns_reflector': nr_mdns_reflector, 'gateway': nr_gateway, 'range_type': nr_range_type,
                            'translated_subnet': nr_translated_subnet, 'internet_only': nr_internet_only, 'local_ip': nr_local_ip,
                            'dhcp_settings': {
                                'dhcp_type': nr_dhcp_type, 'ip_range': nr_ip_range, 'relay_group_id': None,
                                'relay_group_name': nr_relay_group_name, 'dhcp_microsegmentation': nr_dhcp_microsegmentation
                            }
                        }
                        nr_lan_interface_entry["network_ranges"].append(cur_range)
                else:
                    site_native_range['range_name'] = range_name
                    site_native_range['range_id'] = range_id
                    site_native_range['vlan'] = nr_vlan
                    site_native_range['mdns_reflector'] = nr_mdns_reflector
                    site_native_range['gateway'] = nr_gateway
                    site_native_range['range_type'] = nr_range_type
                    site_native_range['translated_subnet'] = nr_translated_subnet
                    site_native_range['internet_only'] = nr_internet_only
                    site_native_range['local_ip'] = nr_local_ip
                    site_native_range['dhcp_settings'] = {
                        'dhcp_type': nr_dhcp_type, 'ip_range': nr_ip_range, 'relay_group_id': None,
                        'relay_group_name': nr_relay_group_name, 'dhcp_microsegmentation': nr_dhcp_microsegmentation
                    }
            else:
                nr_lan_interface_entry = next((lan_nic for lan_nic in nr_site_entry["lan_interfaces"] if ('default_lan' not in lan_nic or not lan_nic['default_lan']) and lan_nic['name'] == nr_interface_name), None)
                if nr_lan_interface_entry:
                    cur_range = {
                        'id': range_id, 'name': range_name, 'subnet': nr_subnet, 'vlan': nr_vlan,
                        'mdns_reflector': nr_mdns_reflector, 'gateway': nr_gateway, 'range_type': nr_range_type,
                        'translated_subnet': nr_translated_subnet, 'internet_only': nr_internet_only, 'local_ip': nr_local_ip,
                        'dhcp_settings': {
                            'dhcp_type': nr_dhcp_type, 'ip_range': nr_ip_range, 'relay_group_id': None,
                            'relay_group_name': nr_relay_group_name, 'dhcp_microsegmentation': nr_dhcp_microsegmentation
                        }
                    }
                    
                    if "subnet" in nr_lan_interface_entry and nr_subnet == nr_lan_interface_entry["subnet"]:
                        cur_range['native_range'] = True
                        del nr_lan_interface_entry["subnet"]
                    
                    nr_lan_interface_entry["network_ranges"].append(cur_range)
    
    return processed_data


def export_sites_to_csv(sites, args, account_id):
    """
    Export main sites data to CSV file in bulk-sites format
    One row per WAN interface, site attributes only on first row per site
    """
    # Handle custom filename and timestamp
    if hasattr(args, 'csv_filename') and args.csv_filename:
        base_filename = args.csv_filename
        if base_filename.endswith('.csv'):
            base_filename = base_filename[:-4]
        
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_template = f"{base_filename}_{timestamp}.csv"
        else:
            filename_template = f"{base_filename}.csv"
    else:
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_template = f"socket_sites_{{account_id}}_{timestamp}.csv"
        else:
            filename_template = "socket_sites_{account_id}.csv"
    
    # Replace account_id placeholder
    filename = filename_template.format(account_id=account_id)
    
    # Determine output directory
    output_dir = getattr(args, 'output_directory', None)
    if not output_dir:
        output_dir = 'config_data'
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(os.getcwd(), output_dir)
    
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    # Define CSV headers matching bulk-sites.csv format
    headers = [
        'site_id',
        'site_name',
        'wan_interface_id',
        'wan_interface_index',
        'wan_interface_name', 
        'wan_upstream_bw',
        'wan_downstream_bw',
        'wan_role',
        'wan_precedence',
        'site_description',
        'native_range_subnet',
        'native_range_name',
        'native_range_id',
        'native_range_vlan',
        'native_range_mdns_reflector',
        'native_range_gateway',
        'native_range_type',
        'native_range_translated_subnet',
        'native_range_interface_id',
        'native_range_interface_index',
        'native_range_interface_name',
        'native_range_interface_dest_type',
        'native_range_interface_lag_min_links',
        'native_range_dhcp_type',
        'native_range_dhcp_ip_range',
        'native_range_dhcp_relay_group_id',
        'native_range_dhcp_relay_group_name',
        'native_range_dhcp_microsegmentation',
        'native_range_local_ip',
        'site_type',
        'connection_type',
        'site_location_address',
        'site_location_city',
        'site_location_country_code',
        'site_location_state_code',
        'site_location_timezone'
    ]
    
    rows = []
    total_interfaces = 0
    
    for site in sites:
        site_name = site.get('name', '')
        wan_interfaces = site.get('wan_interfaces', [])
        
        # Sort WAN interfaces to ensure 'wan_1' role appears first
        # This organizes the CSV so wan_1 interfaces are on the first line for each site
        def wan_interface_sort_key(interface):
            role = interface.get('role', '').lower()
            if role == 'wan_1':
                return 0  # wan_1 comes first
            elif role == 'wan_2':
                return 1
            elif role == 'wan_3':
                return 2
            elif role == 'wan_4':
                return 3
            else:
                return 9  # Unknown/other roles come last
        
        wan_interfaces.sort(key=wan_interface_sort_key)
        
        # If no WAN interfaces, create one empty row for the site
        if not wan_interfaces:
            wan_interfaces = [{}]  # Empty interface to ensure site is included
        
        for idx, wan_interface in enumerate(wan_interfaces):
            # Site-specific attributes only on first row per site
            is_first_interface = (idx == 0)
            
            # Calculate local IP from native range subnet if available
            native_range = site.get('native_range', {})
            native_subnet = native_range.get('subnet', '')
            local_ip = ''
            if native_subnet and hasattr(args, 'calculate_local_ip') and args.calculate_local_ip:
                calculated_ip = calculateLocalIp(native_subnet)
                if calculated_ip:
                    local_ip = calculated_ip
            elif native_range.get('local_ip'):
                local_ip = native_range.get('local_ip', '')
            
            row = {
                'site_id': site.get('id', '') if is_first_interface else '',
                'site_name': site_name,
                'wan_interface_id': wan_interface.get('id', '') if wan_interface else '',
                'wan_interface_index': wan_interface.get('index', '') if wan_interface else '',
                'wan_interface_name': wan_interface.get('name', '') if wan_interface else '',
                'wan_upstream_bw': wan_interface.get('upstream_bandwidth', '') if wan_interface else '',
                'wan_downstream_bw': wan_interface.get('downstream_bandwidth', '') if wan_interface else '',
                'wan_role': wan_interface.get('role', '') if wan_interface else '',
                'wan_precedence': wan_interface.get('precedence', '') if wan_interface else '',
                
                # Site attributes - only populate on first interface row
                'site_description': site.get('description', '') if is_first_interface else '',
                'native_range_subnet': native_subnet if is_first_interface else '',
                'native_range_name': native_range.get('range_name', '') if is_first_interface else '',
                'native_range_id': native_range.get('range_id', '') if is_first_interface else '',
                'native_range_vlan': native_range.get('vlan', '') if is_first_interface else '',
                'native_range_mdns_reflector': str(native_range.get('mdns_reflector', '')).upper() if is_first_interface and native_range.get('mdns_reflector') != '' else '' if is_first_interface else '',
                'native_range_gateway': native_range.get('gateway', '') if is_first_interface else '',
                'native_range_type': native_range.get('range_type', '') if is_first_interface else '',
                'native_range_translated_subnet': native_range.get('translated_subnet', '') if is_first_interface else '',
                'native_range_interface_id': native_range.get('interface_id', '') if is_first_interface else '',
                'native_range_interface_index': native_range.get('index', '') if is_first_interface else '',
                'native_range_interface_name': native_range.get('interface_name', '') if is_first_interface else '',
                'native_range_interface_dest_type': native_range.get('dest_type', '') if is_first_interface else '',
                'native_range_interface_lag_min_links': native_range.get('lag_min_links', '') if is_first_interface else '',
                'native_range_dhcp_type': native_range.get('dhcp_settings', {}).get('dhcp_type', '') if is_first_interface else '',
                'native_range_dhcp_ip_range': native_range.get('dhcp_settings', {}).get('ip_range', '') if is_first_interface else '',
                'native_range_dhcp_relay_group_id': native_range.get('dhcp_settings', {}).get('relay_group_id', '') if is_first_interface else '',
                'native_range_dhcp_relay_group_name': native_range.get('dhcp_settings', {}).get('relay_group_name', '') if is_first_interface else '',
                'native_range_dhcp_microsegmentation': str(native_range.get('dhcp_settings', {}).get('dhcp_microsegmentation', '')).upper() if is_first_interface and native_range.get('dhcp_settings', {}).get('dhcp_microsegmentation') != '' else '' if is_first_interface else '',
                'native_range_local_ip': local_ip if is_first_interface else '',
                'site_type': site.get('type', '') if is_first_interface else '',
                'connection_type': site.get('connection_type', '') if is_first_interface else '',
                'site_location_address': site.get('site_location', {}).get('address', '') if is_first_interface else '',
                'site_location_city': site.get('site_location', {}).get('city', '') if is_first_interface else '',
                'site_location_country_code': site.get('site_location', {}).get('countryCode', '') if is_first_interface else '',
                'site_location_state_code': site.get('site_location', {}).get('stateCode', '') if is_first_interface else '',
                'site_location_timezone': site.get('site_location', {}).get('timezone', '') if is_first_interface else ''
            }
            
            rows.append(row)
            total_interfaces += 1 if wan_interface else 0
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    if hasattr(args, 'verbose') and args.verbose:
        print(f"Exported {len(sites)} sites with {total_interfaces} WAN interfaces to {filepath}")
    
    return filepath


def export_network_ranges_to_csv(site, args, account_id):
    """
    Export network ranges for a single site to CSV file
    Structure: LAN interface as parent with network ranges as children
    First row per interface contains interface details, subsequent rows contain only network range details
    """
    site_name = site.get('name', '')
    if not site_name:
        return None
    
    # Sanitize site name for filename
    safe_site_name = "".join(c for c in site_name if c.isalnum() or c in ('-', '_')).rstrip()
    
    # Determine output directory
    output_dir = getattr(args, 'output_directory', None)
    if not output_dir:
        output_dir = 'config_data'
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(os.getcwd(), output_dir)
    
    # Create sites_config subdirectory with account ID
    sites_config_dir = os.path.join(output_dir, f'sites_config_{account_id}')
    os.makedirs(sites_config_dir, exist_ok=True)
    
    filename = f"{safe_site_name}_network_ranges.csv"
    filepath = os.path.join(sites_config_dir, filename)
    
    # Define CSV headers - Reordered LAN interface columns first, then network range columns
    headers = [
        # LAN Interface columns (first 3 columns, lag_min_links 4th, is_native_range 5th, lan_interface_index 6th)
        'lan_interface_id', 'lan_interface_name', 'lan_interface_dest_type', 'lag_min_links', 'is_native_range', 'lan_interface_index',
        # Network Range columns (populated on all rows)
        'network_range_id', 'network_range_name', 'subnet', 'vlan', 'mdns_reflector', 
        'gateway', 'range_type', 'translated_subnet', 'internet_only', 'local_ip', 
        'dhcp_type', 'dhcp_ip_range', 'dhcp_relay_group_id', 'dhcp_relay_group_name', 'dhcp_microsegmentation'
    ]
    
    rows = []
    
    # Get the native range subnet from the site to exclude it from detailed CSV
    native_range_subnet = site.get('native_range', {}).get('subnet', '')
    
    # Count LAN_LAG_MEMBER interfaces for lag_min_links calculation
    lan_lag_member_count = len([intf for intf in site.get('lan_interfaces', []) 
                               if intf.get('dest_type', '') == 'LAN_LAG_MEMBER'])
    
    # Process default LAN interface (from native_range) - ONLY if it has additional networks
    native_range = site.get('native_range', {})
    native_range_index = native_range.get('index', '')  # The default interface index from parent CSV
    default_lan_interfaces = [lan_nic for lan_nic in site.get('lan_interfaces', []) if lan_nic.get('default_lan', False)]
    
    if default_lan_interfaces:
        for default_lan_interface in default_lan_interfaces:
            interface_id = native_range.get('interface_id', '')
            interface_name = native_range.get('interface_name', '')
            interface_index = native_range.get('index', '')  # Use actual interface index like INT_5
            interface_dest_type = 'LAN'
            
            network_ranges = default_lan_interface.get('network_ranges', [])
            
            # For default_lan interfaces, process all ranges but skip native range
            # Only process non-native ranges (additional ranges)
            if network_ranges:
                # Process all ranges and only include non-native ranges
                for idx, network_range in enumerate(network_ranges):
                    current_subnet = network_range.get('subnet', '')
                    
                    # Skip the native range since it's managed at parent level
                    if current_subnet == native_range_subnet:
                        continue
                        
                    # First row for this interface includes interface details
                    is_first_range = (idx == 0)
                    
                    # For default_lan interfaces, all ranges are additional (is_native_range=FALSE)
                    # because the native range is already defined in the parent CSV
                    
                    row = {
                        # LAN Interface details - for default LAN interfaces, don't populate interface ID, name, type since managed at parent level
                        'lan_interface_id': '',  # Empty for default LAN interfaces (managed at parent level)
                        'lan_interface_name': '',  # Empty for default LAN interfaces (managed at parent level)
                        'lan_interface_dest_type': '',  # Empty for default LAN interfaces (managed at parent level)
                        'lag_min_links': '',  # Empty for default interfaces
                        'is_native_range': '',  # Always empty for default LAN interfaces (native is managed at parent level)
                        'lan_interface_index': interface_index,  # Populated for every row
                        
                        # Network Range details (on all rows)
                        'network_range_id': network_range.get('id', ''),
                        'network_range_name': network_range.get('name', ''),
                        'subnet': network_range.get('subnet', ''),
                        'vlan': network_range.get('vlan', ''),
                        'mdns_reflector': str(network_range.get('mdns_reflector', False)).upper(),
                        'gateway': network_range.get('gateway', ''),
                        'range_type': network_range.get('range_type', ''),
                        'translated_subnet': network_range.get('translated_subnet', ''),
                        'internet_only': network_range.get('internet_only', ''),
                        'local_ip': network_range.get('local_ip', ''),
                        'dhcp_type': network_range.get('dhcp_settings', {}).get('dhcp_type', ''),
                        'dhcp_ip_range': network_range.get('dhcp_settings', {}).get('ip_range', ''),
                        'dhcp_relay_group_id': network_range.get('dhcp_settings', {}).get('relay_group_id', ''),
                        'dhcp_relay_group_name': network_range.get('dhcp_settings', {}).get('relay_group_name', ''),
                        'dhcp_microsegmentation': str(network_range.get('dhcp_settings', {}).get('dhcp_microsegmentation', False)).upper()
                    }
                    rows.append(row)
    
    # Process regular LAN interfaces and their network ranges
    for lan_interface in site.get('lan_interfaces', []):
        is_default_lan = lan_interface.get('default_lan', False)
        
        # Skip default_lan interfaces (already processed above)
        if is_default_lan:
            continue
            
        interface_id = lan_interface.get('id', '')
        interface_name = lan_interface.get('name', '')
        interface_index = lan_interface.get('index', '')
        interface_dest_type = lan_interface.get('dest_type', '')
        
        # Special handling for LAN_LAG_MEMBER interfaces
        if interface_dest_type == 'LAN_LAG_MEMBER':
            if hasattr(args, 'verbose') and args.verbose:
                print(f"DEBUG: Processing LAN_LAG_MEMBER interface in CSV export for site {site.get('name', '')}: {interface_name} (index: {interface_index})")
            # LAN_LAG_MEMBER interfaces get their own row with only interface details
            # They don't have is_native_range=TRUE and have no network range data
            row = {
                # LAN Interface details - only populate specific fields for LAN_LAG_MEMBER
                'lan_interface_id': '',  # LAN_LAG_MEMBER interfaces don't have IDs
                'lan_interface_name': interface_name,
                'lan_interface_dest_type': interface_dest_type,
                'lag_min_links': '',  # Empty for LAN_LAG_MEMBER
                'is_native_range': '',  # Empty - LAN_LAG_MEMBER should NOT have is_native_range=TRUE
                'lan_interface_index': interface_index,
                
                # Network Range details (all empty for LAN_LAG_MEMBER)
                'network_range_id': '',
                'network_range_name': '',
                'subnet': '',
                'vlan': '',
                'mdns_reflector': '',
                'gateway': '',
                'range_type': '',
                'translated_subnet': '',
                'internet_only': '',
                'local_ip': '',
                'dhcp_type': '',
                'dhcp_ip_range': '',
                'dhcp_relay_group_id': '',
                'dhcp_relay_group_name': '',
                'dhcp_microsegmentation': ''
            }
            rows.append(row)
            if hasattr(args, 'verbose') and args.verbose:
                print(f"DEBUG: Added LAN_LAG_MEMBER row to CSV: {row}")
            continue  # Skip to next interface
        
        # Handle regular (non-LAN_LAG_MEMBER) LAN interfaces
        network_ranges = lan_interface.get('network_ranges', [])
        
        # If no network ranges at all, create at least one row with just the LAN interface info  
        # For regular LAN interfaces, mark as native range if this is the first/only interface
        if not network_ranges:
            # Calculate lag_min_links for LAN_LAG_MASTER interfaces
            lag_min_links_value = ''
            if interface_dest_type == 'LAN_LAG_MASTER':
                lag_min_links_value = str(lan_lag_member_count) if lan_lag_member_count > 0 else ''
            
            row = {
                # LAN Interface details - first 3 columns reordered, lag_min_links 4th, is_native_range 5th, lan_interface_index 6th
                'lan_interface_id': interface_id,
                'lan_interface_name': interface_name,
                'lan_interface_dest_type': interface_dest_type,
                'lag_min_links': lag_min_links_value,  # Populated only for LAN_LAG_MASTER
                'is_native_range': 'TRUE',  # Mark as native range for non-default LAN interfaces with no additional ranges
                'lan_interface_index': interface_index,
                
                # Network Range details (empty since no additional ranges)
                'network_range_id': '',
                'network_range_name': '',
                'subnet': '',
                'vlan': '',
                'mdns_reflector': '',
                'gateway': '',
                'range_type': '',
                'translated_subnet': '',
                'internet_only': '',
                'local_ip': '',
                'dhcp_type': '',
                'dhcp_ip_range': '',
                'dhcp_relay_group_id': '',
                'dhcp_relay_group_name': '',
                'dhcp_microsegmentation': ''
            }
            rows.append(row)
        else:
            # Sort network ranges to put "Native Range" first
            def sort_network_ranges(nr):
                # Native Range should come first (return 0), all others come after (return 1)
                range_name = nr.get('name', '')
                return 0 if range_name == 'Native Range' else 1
            
            sorted_network_ranges = sorted(network_ranges, key=sort_network_ranges)
            
            # Process all network ranges and identify which one is the native range
            # Native range is identified by the range name being "Native Range" 
            for idx, network_range in enumerate(sorted_network_ranges):
                # First row for this interface includes interface details
                is_first_range = (idx == 0)
                
                # Identify native range by checking if the range name is "Native Range"
                current_range_name = network_range.get('name', '')
                is_native_range = (current_range_name == 'Native Range')
                
                # Calculate lag_min_links for LAN_LAG_MASTER interfaces (only on first row)
                lag_min_links_value = ''
                if is_first_range and interface_dest_type == 'LAN_LAG_MASTER':
                    lag_min_links_value = str(lan_lag_member_count) if lan_lag_member_count > 0 else ''
                
                row = {
                    # LAN Interface details - first 3 columns reordered, lag_min_links 4th, is_native_range 5th, lan_interface_index 6th
                    'lan_interface_id': interface_id if is_first_range else '',
                    'lan_interface_name': interface_name if is_first_range else '',
                    'lan_interface_dest_type': interface_dest_type if is_first_range else '',
                    'lag_min_links': lag_min_links_value if is_first_range else '',  # Populated only for LAN_LAG_MASTER on first row
                    'is_native_range': 'TRUE' if is_native_range else '',  # TRUE only for native range, empty for others
                    'lan_interface_index': interface_index,  # Populated for every row
                    
                    # Network Range details (on all rows)
                    'network_range_id': network_range.get('id', ''),
                    'network_range_name': network_range.get('name', ''),
                    'subnet': network_range.get('subnet', ''),
                    'vlan': network_range.get('vlan', ''),
                    'mdns_reflector': str(network_range.get('mdns_reflector', False)).upper(),
                    'gateway': network_range.get('gateway', ''),
                    'range_type': network_range.get('range_type', ''),
                    'translated_subnet': network_range.get('translated_subnet', ''),
                    'internet_only': network_range.get('internet_only', ''),
                    'local_ip': network_range.get('local_ip', ''),
                    'dhcp_type': network_range.get('dhcp_settings', {}).get('dhcp_type', ''),
                    'dhcp_ip_range': network_range.get('dhcp_settings', {}).get('ip_range', ''),
                    'dhcp_relay_group_id': network_range.get('dhcp_settings', {}).get('relay_group_id', ''),
                    'dhcp_relay_group_name': network_range.get('dhcp_settings', {}).get('relay_group_name', ''),
                    'dhcp_microsegmentation': str(network_range.get('dhcp_settings', {}).get('dhcp_microsegmentation', False)).upper()
                }
                rows.append(row)
    
    # If still no rows, it means the site only has the default LAN interface (managed at parent level)
    # In this case, create an empty CSV file - no entries needed since default interface is handled in parent CSV
    # This is correct behavior: sites with only default LAN interfaces should have empty site-level CSV files
    
    # Always create file now (removed the early return)
    # if not rows:
    #     return None
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    if hasattr(args, 'verbose') and args.verbose:
        print(f"Exported {len(rows)} network ranges for site '{site_name}' to {filepath}")
    
    return filepath


##########################################################################
########################### Helper functions #############################
##########################################################################

def populateSiteLocationData(args, site_data, cur_site):
    # Load site location data for timezone and state code lookups
    site_location_data = {}
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(script_dir, '..', '..', '..', '..', 'models')
        location_file = os.path.join(models_dir, 'query.siteLocation.json')
        
        if os.path.exists(location_file):
            with open(location_file, 'r', encoding='utf-8') as f:
                site_location_data = json.load(f)
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Loaded {len(site_location_data)} location entries from {location_file}")
        else:
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Warning: Site location file not found at {location_file}")
    except Exception as e:
        if hasattr(args, 'verbose') and args.verbose:
            print(f"Warning: Could not load site location data: {e}")

    address = site_data.get('infoSiteSnapshot', {}).get('address')
    city = site_data.get('infoSiteSnapshot', {}).get('cityName')                
    
    ## siteLocation attributes
    cur_site['site_location'] = {}
    cur_site['site_location']['stateName'] = site_data.get('infoSiteSnapshot', {}).get('countryStateName')
    cur_site['site_location']['countryCode'] = site_data.get('infoSiteSnapshot', {}).get('countryCode')
    cur_site['site_location']['countryName'] = site_data.get('infoSiteSnapshot', {}).get('countryName')
    cur_site['site_location']['address'] = address if address != "" else None
    cur_site['site_location']['city'] = city if city != "" else None

    # Look up timezone and state code from location data
    country_name = cur_site['site_location']['countryName']
    state_name = cur_site['site_location']['stateName']
    city = cur_site['site_location']['city']

    # Create lookup key based on available data
    if state_name:
        lookup_key = f"{country_name}___{state_name}___{city}"
    else:
        lookup_key = f"{country_name}___{city}"
    
    # Debug output for lookup
    if hasattr(args, 'verbose') and args.verbose:
        print(f"Site {cur_site['name']}: Looking up '{lookup_key}'")

    # Look up location details
    location_data = site_location_data.get(lookup_key, {})
    
    # Now that location_data is defined, we can set stateCode
    cur_site['site_location']['stateCode'] = location_data.get('stateCode', None)
    
    if hasattr(args, 'verbose') and args.verbose:
        if location_data:
            print(f"  Found location data: {location_data}")
        else:
            print(f"  No location data found for key: {lookup_key}")
            # Try to find similar keys for debugging
            similar_keys = [k for k in site_location_data.keys() if country_name in k and (not city or city in k)][:5]
            if similar_keys:
                print(f"  Similar keys found: {similar_keys}")

    
    # Get timezone - always use the 0 element in the timezones array
    timezones = location_data.get('timezone', [])
    cur_site['site_location']['timezone'] = timezones[0] if timezones else None
    return cur_site

def getEntityLookup(args, configuration, account_id, entity_type):
    """
    Helper function to get entity lookup data for a specific entity type
    """
    #################################
    ## Get entity lookup for sites ##
    #################################
    entity_query = {
        "query": "query entityLookup ( $accountID:ID! $type:EntityType! $sortInput:[SortInput] $lookupFilterInput:[LookupFilterInput] ) { entityLookup ( accountID:$accountID type:$type sort:$sortInput filters:$lookupFilterInput ) { items { entity { id name type } description helperFields } total } }",
        "variables": {
            "accountID": account_id,
            "type": entity_type
        },
        "operationName": "entityLookup"
    }
    response = makeCall(args, configuration, entity_query)

    # Check for GraphQL errors in snapshot response
    if 'errors' in response:
        error_messages = [error.get('message', 'Unknown error') for error in response['errors']]
        raise Exception(f"Snapshot API returned errors: {', '.join(error_messages)}")
    
    if not response or 'data' not in response or 'entityLookup' not in response['data']:
        raise ValueError("Failed to retrieve snapshot data from API")
    
    items = response['data']['entityLookup']['items']
    if items is None:
        items = []
        if hasattr(args, 'verbose') and args.verbose:
            print("No items found in entity lookup - "+ entity_type)
    return items

def getAccountSnapshot(args, configuration, account_id, site_ids=None):
    snapshot_query = {
        "query": "query accountSnapshot ( $siteIDs:[ID!] $accountID:ID ) { accountSnapshot ( accountID:$accountID ) { id sites ( siteIDs:$siteIDs ) { id protoId connectivityStatusSiteSnapshot: connectivityStatus haStatusSiteSnapshot: haStatus { readiness wanConnectivity keepalive socketVersion } operationalStatusSiteSnapshot: operationalStatus lastConnected connectedSince popName devices { id name identifier connected haRole interfaces { connected id name physicalPort naturalOrder popName previousPopID previousPopName tunnelConnectionReason tunnelUptime tunnelRemoteIP tunnelRemoteIPInfoInterfaceSnapshot: tunnelRemoteIPInfo { ip countryCode countryName city state provider latitude longitude } type infoInterfaceSnapshot: info { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRole } cellularInterfaceInfoInterfaceSnapshot: cellularInterfaceInfo { networkType simSlotId modemStatus isModemConnected iccid imei operatorName isModemSuspended apn apnSelectionMethod signalStrength isRoamingAllowed simNumber disconnectionReason isSimSlot1Detected isSimSlot2Detected } } lastConnected lastDuration connectedSince lastPopID lastPopName recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfoRecentConnection: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } type deviceUptime socketInfo { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } interfacesLinkState { id up mediaIn linkSpeed duplex hasAddress hasInternet hasTunnel } osType osVersion version versionNumber releaseGroup mfaExpirationTime mfaCreationTime internalIP } infoSiteSnapshot: info { name type description countryCode region countryName countryStateName cityName address isHA connType creationTime interfaces { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRoleInterfaceInfo: wanRole } sockets { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } ipsec { isPrimary catoIP remoteIP ikeVersion } } hostCount altWanStatus } users { id connectivityStatusUserSnapshot: connectivityStatus operationalStatusUserSnapshot: operationalStatus name deviceName uptime lastConnected version versionNumber popID popName remoteIP remoteIPInfoUserSnapshot: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } internalIP osType osVersion devices { id name identifier connected haRole interfaces { connected id name physicalPort naturalOrder popName previousPopID previousPopName tunnelConnectionReason tunnelUptime tunnelRemoteIP tunnelRemoteIPInfoInterfaceSnapshot: tunnelRemoteIPInfo { ip countryCode countryName city state provider latitude longitude } type infoInterfaceSnapshot: info { id name upstreamBandwidth downstreamBandwidth upstreamBandwidthMbpsPrecision downstreamBandwidthMbpsPrecision destType wanRole } cellularInterfaceInfoInterfaceSnapshot: cellularInterfaceInfo { networkType simSlotId modemStatus isModemConnected iccid imei operatorName isModemSuspended apn apnSelectionMethod signalStrength isRoamingAllowed simNumber disconnectionReason isSimSlot1Detected isSimSlot2Detected } } lastConnected lastDuration connectedSince lastPopID lastPopName recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfoRecentConnection: remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } type deviceUptime socketInfo { id serial isPrimary platformSocketInfo: platform version versionUpdateTime } interfacesLinkState { id up mediaIn linkSpeed duplex hasAddress hasInternet hasTunnel } osType osVersion version versionNumber releaseGroup mfaExpirationTime mfaCreationTime internalIP } connectedInOffice infoUserSnapshot: info { name status email creationTime phoneNumber origin authMethod } recentConnections { duration interfaceName deviceName lastConnected popName remoteIP remoteIPInfo { ip countryCode countryName city state provider latitude longitude } } } timestamp }  }",
        "variables": {
            "accountID": account_id,
            "siteIDs": site_ids
        },
        "operationName": "accountSnapshot"
    }
    response = makeCall(args, configuration, snapshot_query)

    # Check for GraphQL errors in snapshot response
    if 'errors' in response:
        error_messages = [error.get('message', 'Unknown error') for error in response['errors']]
        raise Exception(f"Snapshot API returned errors: {', '.join(error_messages)}")
    
    if not response or 'data' not in response or 'accountSnapshot' not in response['data']:
        raise ValueError("Failed to retrieve snapshot data from API")
    
    if not response or 'sites' not in response['data']['accountSnapshot'] or response['data']['accountSnapshot']['sites'] is None:
        # Instead of raising an exception, return an empty response structure
        response['data']['accountSnapshot']['sites'] = []

    return response