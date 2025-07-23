import os
import json
import traceback
import sys
from datetime import datetime
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID

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
        settings = {}
        with open(os.path.join(os.path.dirname(__file__), '../../../../settings.json'), 'r', encoding='utf-8') as f:
            settings = json.load(f)

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
        entity_network_interfaces = getEntityLookup(args, configuration, account_id, "networkInterface")
        entity_network_ranges = getEntityLookup(args, configuration, account_id, "siteRange")
        entity_sites = getEntityLookup(args, configuration, account_id, "site")
        
        ##################################################################
        ## Create processed_data object indexed by siteId with location ##
        ##################################################################
        for snapshot_site in snapshot_sites['data']['accountSnapshot']['sites']:
            cur_site = {
                'wan_interfaces': [],
                'lan_interfaces': [],
            }
            site_id = snapshot_site.get('id')
            connectionType = snapshot_site.get('infoSiteSnapshot', {}).get('connType', "")
            if connectionType not in settings["ignore_export_by_socket_type"]:
                cur_site['id'] = site_id
                cur_site['name'] = snapshot_site.get('infoSiteSnapshot', {}).get('name')
                cur_site['description'] = snapshot_site.get('infoSiteSnapshot', {}).get('description')
                cur_site['connectionType'] = connectionType
                cur_site['type'] = snapshot_site.get('infoSiteSnapshot', {}).get('type')
                cur_site = populateSiteLocationData(args, snapshot_site, cur_site)

                site_interfaces = snapshot_site.get('infoSiteSnapshot', {}).get('interfaces', [])
                for wan_ni in site_interfaces:
                    cur_wan_interface = {}
                    role = wan_ni.get('wanRoleInterfaceInfo', "")
                    if role is not None and role[0:3] == "wan":
                        if connectionType == "SOCKET_X1500":
                            cur_wan_interface['id'] = site_id+":"+ wan_ni.get('id', "")
                        else:
                            cur_wan_interface['id'] = site_id+":INT_"+ wan_ni.get('id', "")
                        cur_wan_interface['id'] = site_id+":INT_"+ wan_ni.get('id', "")
                        cur_wan_interface['name'] = wan_ni.get('name', "")
                        cur_wan_interface['upstreamBandwidth'] = wan_ni.get('upstreamBandwidth', 0)
                        cur_wan_interface['downstreamBandwidth'] = wan_ni.get('downstreamBandwidth', 0)
                        cur_wan_interface['destType'] = wan_ni.get('destType', "")
                        cur_wan_interface['role'] = role
                        cur_site['wan_interfaces'].append(cur_wan_interface)

                if site_id:
                    processed_data['sites'].append(cur_site)

        ##################################################################################
        ## Process entity lookup LAN network interfaces adding to site object by site_id##
        ##################################################################################
        interface_map = {}
        for lan_ni in entity_network_interfaces:
            cur_lan_interface = {
                'network_ranges': [],
            }
            site_id = str(lan_ni.get("helperFields","").get('siteId', ""))
            id = str(lan_ni.get('entity', "").get('id', ""))
            interfaceName = lan_ni.get('helperFields', "").get('interfaceName', "")
            cur_lan_interface['id'] = id
            cur_lan_interface['name'] = interfaceName
            # Split interfaceName on " \ " and take the last element
            cur_lan_interface['index'] = lan_ni.get("helperFields","").get('interfaceId', "")
            cur_lan_interface['destType'] = lan_ni.get("helperFields","").get('destType', "")
            
            # Create a composite key for interface mapping that includes site_id
            interface_key = f"{site_id}_{interfaceName}"
            interface_map[interface_key] = id
            
            # Only add interface if the site exists in processed_data
            site_entry = next((site for site in processed_data['sites'] if site['id'] == site_id), None)
            if site_entry:
                site_entry['lan_interfaces'].append(cur_lan_interface)
            else:
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"WARNING: Site {site_id} not found in snapshot data, skipping interface {interfaceName} ({id})")

        #############################################################################
        ## Process entity lookup network ranges populating by network interface id ##
        #############################################################################
        for range in entity_network_ranges:
            if hasattr(args, 'verbose') and args.verbose:
                print(f"Processing network range: {type(range)} - {range}")
            cur_range = {}
            helper_fields = range.get("helperFields", {})
            entity_data = range.get('entity', {})
            
            if hasattr(args, 'verbose') and args.verbose:
                print(f"  helperFields type: {type(helper_fields)}, value: {helper_fields}")
                print(f"  entity type: {type(entity_data)}, value: {entity_data}")
            
            range_id = entity_data.get('id', "")
            site_id = str(helper_fields.get('siteId', ""))
            interface_name = str(helper_fields.get('interfaceName', ""))
            # Use the composite key to lookup interface_id
            interface_key = f"{site_id}_{interface_name}"
            interface_id = str(interface_map.get(interface_key, ""))
            cur_range['id'] = range_id
            range_name = entity_data.get('name', "")
            if range_name and " \\ " in range_name:
                cur_range['rangeName'] = range_name.split(" \\ ").pop()
            else:
                cur_range['rangeName'] = range_name
            cur_range['name'] = range_name
            cur_range['subnet'] = helper_fields.get('subnet', "")
            cur_range['vlanTag'] = helper_fields.get('vlanTag', "")
            cur_range['microsegmentation'] = helper_fields.get('microsegmentation', "")
            
            # Safely add to processed_data with existence checks
            if site_id and interface_id and range_id:
                site_entry = next((site for site in processed_data['sites'] if site['id'] == site_id), None)
                if not site_entry:
                    # print(f"WARNING: Site ID {site_id} not found in processed_data")
                    warning_stats['missing_sites'] += 1
                    continue
                
                # Find the interface in the lan_interfaces array
                interface_entry = next((iface for iface in site_entry['lan_interfaces'] if iface['id'] == interface_id), None)
                if not interface_entry:
                    print(f"WARNING: Interface {interface_id} (name: {interface_name}) not found in site {site_id}. Range {range_id} will be skipped.")
                    warning_stats['missing_interfaces'] += 1
                    warning_stats['missing_interface_details'].append({
                        'interface_id': interface_id,
                        'interface_name': interface_name,
                        'site_id': site_id,
                        'range_id': range_id
                    })
                    if hasattr(args, 'verbose') and args.verbose:
                        available_interfaces = [iface['id'] for iface in site_entry['lan_interfaces']]
                        print(f"  Available interfaces in site {site_id}: {available_interfaces}")
                        print(f"  Looked up interface with key: {interface_key}")
                    continue                
                interface_entry['network_ranges'].append(cur_range)
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"  Successfully added range {range_id} to site {site_id}, interface_name {interface_name} with interface_id {interface_id}")
            else:
                if not interface_id:
                    print(f"WARNING: Interface lookup failed for range {range_id}. Site: {site_id}, Interface name: {interface_name}, Lookup key: {interface_key}")
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"  Available interface keys: {list(interface_map.keys())[:10]}...")  # Show first 10 keys
                else:
                    print(f"WARNING: Missing required data for range: site_id={site_id}, interface_id={interface_id}, range_id={range_id}")
                warning_stats['missing_data'] += 1

        # Print warning summary
        total_warnings = warning_stats['missing_sites'] + warning_stats['missing_interfaces'] + warning_stats['missing_data']
        if total_warnings > 0:
            print(f"\n=== WARNING SUMMARY ===")
            print(f"Total warnings: {total_warnings}")
            print(f"- Missing sites: {warning_stats['missing_sites']}")
            print(f"- Missing interfaces: {warning_stats['missing_interfaces']}")
            print(f"- Missing data: {warning_stats['missing_data']}")
            
            if warning_stats['missing_interfaces'] > 0:
                print(f"\nMissing interface details:")
                unique_interfaces = {}
                for detail in warning_stats['missing_interface_details']:
                    key = f"{detail['interface_id']} ({detail['interface_name']})"
                    if key not in unique_interfaces:
                        unique_interfaces[key] = []
                    unique_interfaces[key].append(detail['site_id'])
                
                for interface, sites in unique_interfaces.items():
                    print(f"  - Interface {interface} missing in sites: {', '.join(sites)}")
            
            print(f"\nThese warnings indicate network ranges that reference interfaces that don't exist in the site data.")
            print(f"This is usually caused by data inconsistencies and can be safely ignored if the export completes successfully.")
            print(f"=========================\n")
        
        # Handle timestamp in filename if requested
        filename_template = "socket_sites_{account_id}.json"
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_template = "socket_sites_{account_id}_" + timestamp + ".json"
            
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

    ## siteLocation attributes
    cur_site['site_location'] = {}
    cur_site['site_location']['address'] = site_data.get('infoSiteSnapshot', {}).get('address')
    cur_site['site_location']['city'] = site_data.get('infoSiteSnapshot', {}).get('cityName')                
    cur_site['site_location']['stateName'] = site_data.get('infoSiteSnapshot', {}).get('countryStateName')
    cur_site['site_location']['countryCode'] = site_data.get('infoSiteSnapshot', {}).get('countryCode')
    cur_site['site_location']['countryName'] = site_data.get('infoSiteSnapshot', {}).get('countryName')

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
    
    if hasattr(args, 'verbose') and args.verbose:
        if location_data:
            print(f"  Found location data: {location_data}")
        else:
            print(f"  No location data found for key: {lookup_key}")
            # Try to find similar keys for debugging
            similar_keys = [k for k in site_location_data.keys() if country_name in k and (not city or city in k)][:5]
            if similar_keys:
                print(f"  Similar keys found: {similar_keys}")

    cur_site['stateCode'] = location_data.get('stateCode', None)

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
        raise ValueError("No sites found in account snapshot data from API")

    return response