#!/usr/bin/env python3
"""
Direct Terraform Import Script using Python
Imports socket sites, WAN interfaces, LAN interfaces and network ranges directly using subprocess calls to terraform import
Reads from JSON structure exported from Cato API
Adapted from scripts/import_if_rules_to_tfstate.py for CLI usage
"""

import json
import subprocess
import sys
import re
import time
import glob
import csv
import os
import argparse
from pathlib import Path
from ..customLib import validate_terraform_environment

def load_json_data(json_file):
    """Load socket sites data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['sites']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def sanitize_name_for_terraform(name):
    """Sanitize rule/section name to create valid Terraform resource key"""
    # Replace spaces and special characters with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    # Remove multiple consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    return sanitized


def extract_socket_sites_data(sites_data):
    """Extract socket sites, WAN interfaces, and network ranges from the sites data.
    Supports both legacy (camelCase) and new (snake_case) JSON formats."""
    sites = []
    lan_interfaces = []
    lan_lag_members = []
    wan_interfaces = []
    network_ranges = []
    
    for site in sites_data:
        if site.get('id') and site.get('name'):
            # Transform site_location to match provider expectations
            site_location = site.get('site_location', {})
            transformed_location = {
                'country_code': site_location.get('countryCode', site_location.get('country_code', '')),
                'state_code': site.get('stateCode', site_location.get('state_code', '')),
                'timezone': site_location.get('timezone', ''),
                'city': site_location.get('city', ''),
                'address': site_location.get('address', '')
            }
            
            # Transform native_range data (handle both shapes)
            native_range = {
                'native_network_range': site.get('native_network_range', site.get('native_range', {}).get('subnet', '')),
                'local_ip': site.get('local_ip', site.get('native_range', {}).get('local_ip', '')),
                'translated_subnet': site.get('translated_subnet', site.get('native_range', {}).get('translated_subnet', '')),
                'native_network_range_id': site.get('native_network_range_id', site.get('native_range', {}).get('range_id', ''))
            }
            # Optional DHCP
            dhcp_settings = site.get('dhcp_settings', site.get('native_range', {}).get('dhcp_settings'))
            if dhcp_settings and isinstance(dhcp_settings, dict) and (dhcp_settings.get('dhcp_type') or dhcp_settings.get('ip_range') or dhcp_settings.get('relay_group_id')):
                native_range['dhcp_settings'] = {
                    'dhcp_type': dhcp_settings.get('dhcp_type', ''),
                    'ip_range': dhcp_settings.get('ip_range', ''),
                    'relay_group_id': dhcp_settings.get('relay_group_id', '')
                }
            else:
                native_range['dhcp_settings'] = None
            
            sites.append({
                'id': site['id'],
                'name': site['name'],
                'description': site.get('description', ''),
                'connection_type': site.get('connectionType', site.get('connection_type', '')),
                'site_type': site.get('type', ''),
                'site_location': transformed_location,
                'native_range': native_range
            })
        
        # Extract WAN interfaces for this site
        for wan_interface in site.get('wan_interfaces', []):
            # Accept both key styles
            name = wan_interface.get('name')
            wid = wan_interface.get('id')
            index = wan_interface.get('index')
            if wid and name and index:
                # Apply the same index formatting logic as the Terraform module
                try:
                    # If index is a number, format as INT_X
                    int(index)
                    formatted_index = f"INT_{index}"
                except ValueError:
                    # If not a number, use as-is
                    formatted_index = index
                
                wan_interfaces.append({
                    'site_id': site['id'],
                    'site_name': site['name'],
                    'interface_id': wid,  # Full ID for actual import
                    'interface_index': formatted_index,  # Formatted index for Terraform key
                    'name': name,
                    'upstream_bandwidth': wan_interface.get('upstreamBandwidth', wan_interface.get('upstream_bandwidth', 25)),
                    'downstream_bandwidth': wan_interface.get('downstreamBandwidth', wan_interface.get('downstream_bandwidth', 25)),
                    'dest_type': wan_interface.get('destType', wan_interface.get('dest_type', 'CATO')),
                    'role': wan_interface.get('role', 'wan_1'),
                    'precedence': 'ACTIVE'
                })
        
        # Extract LAN interfaces and network ranges for this site
        # Process LAN interfaces first to determine which ones will be created as separate resources
        valid_lan_interfaces = []
        
        for lan_interface in site.get('lan_interfaces', []):
            interface_id = lan_interface.get('id', None)
            interface_name = lan_interface.get('name', None)
            interface_index = lan_interface.get('index', None)
            is_default_lan = lan_interface.get('default_lan', False)
            dest_type = lan_interface.get('destType', lan_interface.get('dest_type', 'LAN'))
            
            # If this is a default_lan interface, get interface info from native_range
            if is_default_lan:
                native_range = site.get('native_range', {})
                interface_id = native_range.get('interface_id')
                interface_name = native_range.get('interface_name')
                interface_index = native_range.get('index')
            
            # Check if this interface matches the site's default native range (should be excluded)
            native_range_data = site.get('native_range', {})
            is_site_default_native = (
                is_default_lan and 
                interface_index == native_range_data.get('index') and
                interface_name == native_range_data.get('interface_name')
            )
            
            # Check if this is a LAN LAG member interface
            if dest_type == 'LAN_LAG_MEMBER':
                # LAN LAG members are handled separately
                lan_lag_members.append({
                    'site_id': site['id'],
                    'site_name': site['name'],
                    'id': interface_id,
                    'index': interface_index,
                    'name': interface_name,
                    'dest_type': dest_type
                })
                continue  # Skip to next interface
            
            # Only include interfaces that:
            # 1. Have both interface_index and interface_id
            # 2. Are NOT the site's default native range interface
            # 3. Are NOT LAN_LAG_MEMBER interfaces (handled separately)
            will_create_interface = (interface_index is not None and interface_id and not is_site_default_native and dest_type != 'LAN_LAG_MEMBER')
            
            if will_create_interface:
                # For default_lan interfaces, get additional info from the interface itself or native_range
                subnet = lan_interface.get('subnet', '')
                local_ip = lan_interface.get('local_ip', '')
                
                # If this is a default_lan interface and we don't have subnet/local_ip, get from native_range
                if is_default_lan:
                    native_range_data = site.get('native_range', {})
                    if not subnet:
                        subnet = native_range_data.get('subnet', '')
                    if not local_ip:
                        local_ip = native_range_data.get('local_ip', '')
                
                lan_interfaces.append({
                    'site_id': site['id'],
                    'id': interface_id,
                    'index': interface_index,
                    'name': interface_name,
                    'dest_type': lan_interface.get('destType', lan_interface.get('dest_type', 'LAN')),
                    'subnet': subnet,
                    'local_ip': local_ip,
                    'role': interface_index or interface_name,
                    'site_name': site.get('name', ''),
                    'is_default_lan': is_default_lan  # Add this for debugging
                })
                
                valid_lan_interfaces.append((interface_index, interface_name, interface_id, is_default_lan))
            
            # Process network ranges for interfaces that will be created as separate resources
            # OR for any interface that has network ranges (including virtual interfaces)
            has_network_ranges = len(lan_interface.get('network_ranges', [])) > 0
            should_process_ranges = will_create_interface or has_network_ranges
            
            if should_process_ranges:
                for network_range in lan_interface.get('network_ranges', []):
                    subnet = network_range.get('subnet')
                    if network_range.get('id') and subnet:
                        # Skip native ranges - these are managed at the site level, not as separate network range resources
                        is_native_range = network_range.get('native_range', False)
                        if is_native_range:
                            continue
                        
                        # Use the same interface info logic for network ranges
                        range_interface_id = interface_id
                        range_interface_index = interface_index
                        range_interface_name = interface_name
                        
                        # If this is a default_lan interface, use native_range info
                        if is_default_lan:
                            native_range = site.get('native_range', {})
                            range_interface_id = native_range.get('interface_id')
                            range_interface_name = native_range.get('interface_name')
                            range_interface_index = native_range.get('index')
                        
                        # print(f"Processing Network Range subnet={subnet}, interface_index={range_interface_index}, network_range_id={network_range['id']}, will_create_interface={will_create_interface}")
                        network_ranges.append({
                            'site_id': site['id'],
                            'site_name': site['name'],
                            'interface_id': range_interface_id,  # Use actual interface ID, not index
                            'interface_index': range_interface_index,  # Also pass interface index separately
                            'interface_name': range_interface_name,
                            'network_range_id': network_range['id'],
                            'name': network_range.get('rangeName', network_range.get('name', '')),
                            'subnet': subnet,
                            'vlan_tag': network_range.get('vlanTag', network_range.get('vlan', '')),
                            'range_type': 'VLAN' if (network_range.get('vlanTag') or network_range.get('vlan')) else 'Native',
                            'microsegmentation': network_range.get('microsegmentation', False)
                        })
    
    return sites, wan_interfaces, lan_interfaces, network_ranges, lan_lag_members


def run_terraform_import(resource_address, resource_id, timeout=60, verbose=False):
    """
    Run a single terraform import command
    
    Args:
        resource_address: The terraform resource address
        resource_id: The actual resource ID to import
        timeout: Command timeout in seconds
        verbose: Whether to show verbose output
    
    Returns:
        tuple: (success: bool, output: str, error: str)
    """
    cmd = ['terraform', 'import', resource_address, resource_id]
    if verbose:
        print(f"Command: {' '.join(cmd)}")
    
    try:
        print(f"Importing: {resource_address} <- {resource_id}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=Path.cwd()
        )
        
        if result.returncode == 0:
            print(f"Success: {resource_address}")
            return True, result.stdout, result.stderr
        else:
            print(f"Failed: {resource_address}")
            print(f"Error: {result.stderr}")
            return False, result.stdout, result.stderr
            
    except KeyboardInterrupt:
        print(f"\nImport cancelled by user (Ctrl+C)")
        raise  # Re-raise to allow higher-level handling
    except subprocess.TimeoutExpired:
        print(f"Timeout: {resource_address} (exceeded {timeout}s)")
        return False, "", f"Command timed out after {timeout} seconds"
    except Exception as e:
        print(f"Unexpected error for {resource_address}: {e}")
        return False, "", str(e)

def import_socket_sites(sites, module_name, verbose=False,
                       resource_type="cato_socket_site", resource_name="socket-site",
                       batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all socket sites in batches"""
    print("\nStarting socket site imports...")
    successful_imports = 0
    failed_imports = 0
    total_sites = len(sites)
    
    for i, site in enumerate(sites):
        site_id = site['id']
        site_name = site['name']
        terraform_key = sanitize_name_for_terraform(site_name)
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Use correct resource addressing for nested module
        resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_socket_site.site'
        print(f"\n[{i+1}/{total_sites}] Site: {site_name} (ID: {site_id})")
        
        success, stdout, stderr = run_terraform_import(resource_address, site_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            # Ask user if they want to continue on failure (unless auto-approved)
            if failed_imports <= 3 and not auto_approve:  # Only prompt for first few failures
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        # Delay between batches
        if (i + 1) % batch_size == 0 and i < total_sites - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nSocket Site Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_wan_interfaces(wan_interfaces, module_name, verbose=False,
                         resource_type="cato_wan_interface", resource_name="wan",
                         batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all WAN interfaces in batches"""
    print("\nStarting WAN interface imports...")
    successful_imports = 0
    failed_imports = 0
    total_interfaces = len(wan_interfaces)
    
    for i, interface in enumerate(wan_interfaces):
        site_id = interface['site_id']
        interface_id = interface['interface_id']
        interface_name = interface['name']
        site_name = interface['site_name']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # In the module, cato_wan_interface.wan is now keyed by interface_index, which we
        # format from the JSON "index" field. Use interface_index as the key.
        wan_key = interface.get('interface_index', interface_id)  # Use formatted index, fallback to ID
        resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_wan_interface.wan["{wan_key}"]'
        
        # WAN import id must be "site_id:interface_part"
        if ':' in interface_id:
            import_id = interface_id
        else:
            import_id = f"{site_id}:{interface_id}"
        print(f"\n[{i+1}/{total_interfaces}] WAN Interface: {interface_name} on {site_name} (Key: {wan_key})")
        
        success, stdout, stderr = run_terraform_import(resource_address, import_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            if failed_imports <= 3 and not auto_approve:
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        if (i + 1) % batch_size == 0 and i < total_interfaces - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nWAN Interface Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_lan_lag_members(lan_lag_members, module_name, verbose=False,
                          resource_type="cato_lan_interface_lag_member", resource_name="lag_lan_members",
                          batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all LAN LAG member interfaces in batches"""
    print("\nStarting LAN LAG member imports...")
    successful_imports = 0
    failed_imports = 0
    total_interfaces = len(lan_lag_members)

    for i, interface in enumerate(lan_lag_members):
        site_id = interface['site_id']
        interface_id = interface['id'] if interface.get('id') else interface.get('interface_id', '')
        interface_index = interface['index']
        interface_name = interface['name']
        site_name = interface['site_name']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Apply the same index formatting logic as the Terraform module
        try:
            # If index is a number, format as INT_X
            int(interface_index)
            formatted_index = f"INT_{interface_index}"
        except (ValueError, TypeError):
            # If not a number or None, use as-is
            formatted_index = interface_index if interface_index else interface_id
        
        # LAN LAG member addressing pattern from state file:
        # module.sites_from_csv.module.socket-site["Test"].cato_lan_interface_lag_member.lag_lan_members["INT_6"]
        resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_lan_interface_lag_member.lag_lan_members["{formatted_index}"]'

        print(f"\n[{i+1}/{total_interfaces}] LAN LAG Member: {interface_name} on {site_name} (Index: {interface_index})")

        # For LAN LAG members, the import ID format is site_id:interface_index
        import_id = f"{site_id}:{formatted_index}"
        success, stdout, stderr = run_terraform_import(resource_address, import_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            if failed_imports <= 3 and not auto_approve:
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        if (i + 1) % batch_size == 0 and i < total_interfaces - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nLAN LAG Member Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_lan_interfaces(lan_interfaces, module_name, verbose=False,
                         resource_type="cato_lan_interface", resource_name="interface",
                         batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all LAN interfaces in batches"""
    print("\nStarting LAN interface imports...")
    successful_imports = 0
    failed_imports = 0
    total_interfaces = len(lan_interfaces)

    for i, interface in enumerate(lan_interfaces):
        site_id = interface['site_id']
        interface_id = interface['id']  # Actual interface ID from CSV
        interface_index = interface['index']
        interface_name = interface['name']
        site_name = interface['site_name']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Updated addressing to use interface_index-based indexing for resource addressing:
        # module.sites.module.socket-site[site].module.lan_interfaces[interface_index].cato_lan_interface.interface[0]
        # Apply the same index formatting logic as the Terraform module
        try:
            # If index is a number, format as INT_X
            int(interface_index)
            formatted_index = f"INT_{interface_index}"
        except (ValueError, TypeError):
            # If not a number or None, use as-is
            formatted_index = interface_index if interface_index else interface_id
        
        # The resource address uses interface_index for both the module key and the for_each key
        resource_address = f'{module_name}.module.socket-site["{site_name}"].module.lan_interfaces["{formatted_index}"].cato_lan_interface.interface["{formatted_index}"]'

        print(f"\n[{i+1}/{total_interfaces}] LAN Interface: {interface_name} on {site_name} (Index: {interface_index}, ID: {interface_id})")

        # Use the actual interface_id for importing, not the formatted index
        success, stdout, stderr = run_terraform_import(resource_address, interface_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            if failed_imports <= 3 and not auto_approve:
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        if (i + 1) % batch_size == 0 and i < total_interfaces - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nLAN Interface Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_network_ranges(network_ranges, lan_interfaces, module_name, verbose=False,
                         resource_type="cato_network_range", resource_name="network_range",
                         batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all network ranges in batches"""
    print("\nStarting network range imports...")
    successful_imports = 0
    failed_imports = 0
    total_ranges = len(network_ranges)
    
    # Pre-calculate indices for network ranges to match Terraform module logic
    # The Terraform module generates keys like: "${interface_index}-${name}-${idx}"
    # We need to group by interface and calculate the index within each interface
    interface_range_indices = {}
    
    for network_range in network_ranges:
        interface_key = f"{network_range['site_name']}-{network_range['interface_index']}"
        if interface_key not in interface_range_indices:
            interface_range_indices[interface_key] = 0
        else:
            interface_range_indices[interface_key] += 1
        network_range['calculated_index'] = interface_range_indices[interface_key]
    
    for i, network_range in enumerate(network_ranges):
        network_range_id = network_range['network_range_id']
        range_name = network_range['name']
        site_name = network_range['site_name']
        subnet = network_range['subnet']
        interface_index = network_range['interface_index']
        calculated_index = network_range['calculated_index']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Apply the same index formatting logic as the Terraform module
        try:
            # If index is a number, format as INT_X
            int(interface_index)
            formatted_index = f"INT_{interface_index}"
        except (ValueError, TypeError):
            # If not a number or None, use as-is (fallback to interface_id if needed)
            formatted_index = interface_index if interface_index else network_range['interface_id']
        
        # Determine if this is a default interface range (connected to native/default interface)
        # Check if this network range has a corresponding LAN interface resource that was extracted
        # If no LAN interface was created for this interface_index, it's a default interface range
        lan_interface_exists = any(
            lan['index'] == interface_index for lan in lan_interfaces 
            if lan['site_name'] == site_name
        )
        
        is_default_interface = not lan_interface_exists
        
        # Generate the correct key format based on whether this is a default interface range
        sanitized_range_name = range_name.replace(" ", "_")
        if is_default_interface:
            # For default interface ranges, use "DEFAULT" as the prefix to match socket module logic
            # Include the calculated index to match Terraform module key generation
            range_key = f"DEFAULT-{sanitized_range_name}-{calculated_index}"
        else:
            # For regular LAN interface ranges, use the formatted interface index with calculated index
            # This matches the Terraform module pattern: "${interface_index}-${name}-${idx}"
            range_key = f"{formatted_index}-{sanitized_range_name}-{calculated_index}"
        
        # Determine the correct resource addressing based on whether this is a default interface
        if is_default_interface:
            # Default interface network ranges are addressed directly under the socket-site module
            resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_network_range.default_interface_ranges["{range_key}"]'
        else:
            # Regular interface network ranges go through the lan_interfaces module
            resource_address = f'{module_name}.module.socket-site["{site_name}"].module.lan_interfaces["{formatted_index}"].module.network_ranges.module.network_range["{range_key}"].cato_network_range.no_dhcp[0]'
        
        print(f"\n[{i+1}/{total_ranges}] Network Range: {range_name} - {subnet} ({network_range_id}) on {site_name}")
        print(f"  Resource Address: {resource_address}")
        
        success, stdout, stderr = run_terraform_import(resource_address, network_range_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            # Ask user if they want to continue on failure (unless auto-approved)
            if failed_imports <= 3 and not auto_approve:  # Only prompt for first few failures
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        # Delay between batches
        if (i + 1) % batch_size == 0 and i < total_ranges - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nNetwork Range Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def generate_terraform_import_files(sites, output_dir="./imported_sites"):
    """Generate Terraform configuration files for imported sites"""
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate main.tf with socket site resources
    main_tf_content = []
    
    for site in sites:
        site_name = sanitize_name_for_terraform(site['name'])
        site_location = site['site_location']
        native_range = site['native_range']
        
        # Build site_location block
        location_attrs = []
        if site_location.get('country_code'):
            location_attrs.append(f'    country_code = "{site_location["country_code"]}"')
        if site_location.get('state_code'):
            location_attrs.append(f'    state_code = "{site_location["state_code"]}"')
        if site_location.get('timezone'):
            location_attrs.append(f'    timezone = "{site_location["timezone"]}"')
        if site_location.get('city'):
            location_attrs.append(f'    city = "{site_location["city"]}"')
        if site_location.get('address'):
            location_attrs.append(f'    address = "{site_location["address"]}"')
        
        # Build native_range block - these are required fields
        native_range_attrs = []
        # Always include required fields, even if empty
        native_range_attrs.append(f'    native_network_range = "{native_range.get("native_network_range", "")}"')
        native_range_attrs.append(f'    local_ip = "{native_range.get("local_ip", "")}"')
        if native_range.get('translated_subnet'):
            native_range_attrs.append(f'    translated_subnet = "{native_range["translated_subnet"]}"')
        
        # Add dhcp_settings if present
        if native_range.get('dhcp_settings'):
            dhcp_settings = native_range['dhcp_settings']
            dhcp_attrs = []
            if dhcp_settings.get('dhcp_type'):
                dhcp_attrs.append(f'      dhcp_type = "{dhcp_settings["dhcp_type"]}"')
            if dhcp_settings.get('ip_range'):
                dhcp_attrs.append(f'      ip_range = "{dhcp_settings["ip_range"]}"')
            if dhcp_settings.get('relay_group_id'):
                dhcp_attrs.append(f'      relay_group_id = "{dhcp_settings["relay_group_id"]}"')
            
            if dhcp_attrs:
                native_range_attrs.append('    dhcp_settings = {')
                native_range_attrs.extend(dhcp_attrs)
                native_range_attrs.append('    }')
        
        # Generate resource block
        resource_block = f"""resource "cato_socket_site" "{site_name}" {{
  name = "{site['name']}"
  description = "{site.get('description', '')}"
  site_type = "{site.get('site_type', '')}"
  connection_type = "{site.get('connection_type', '')}"
  
  site_location = {{
{chr(10).join(location_attrs)}
  }}
  
  native_range = {{
{chr(10).join(native_range_attrs)}
  }}
}}
"""
        
        main_tf_content.append(resource_block)
    
    # Write main.tf
    with open(os.path.join(output_dir, "main.tf"), "w") as f:
        f.write(chr(10).join(main_tf_content))
    
    # Generate import.tf with import blocks
    import_tf_content = []
    
    for site in sites:
        site_name = sanitize_name_for_terraform(site['name'])
        import_block = f"""import {{
  to = cato_socket_site.{site_name}
  id = "{site['id']}"
}}
"""
        import_tf_content.append(import_block)
    
    # Write import.tf
    with open(os.path.join(output_dir, "import.tf"), "w") as f:
        f.write(chr(10).join(import_tf_content))
    
    print(f"\nGenerated Terraform configuration files in {output_dir}:")
    print(f"  - main.tf: {len(sites)} socket site resources")
    print(f"  - import.tf: {len(sites)} import blocks")
    
    return output_dir


def import_socket_sites_to_tf(args, configuration):
    """Main function to orchestrate the socket sites import process"""
    try:
        print(" Terraform Import Tool - Cato Socket Sites, WAN Interfaces & Network Ranges")
        print("=" * 80)
        
        # Determine data source and load data
        data_type = getattr(args, 'data_type', None)
        json_file = getattr(args, 'json_file', None) or getattr(args, 'json_file_legacy', None)
        csv_file = getattr(args, 'csv_file', None)
        csv_folder = getattr(args, 'csv_folder', None)
        
        # Validate input arguments
        if data_type:
            # If data type is explicitly specified, validate corresponding file arguments
            if data_type == 'json' and not json_file:
                raise ValueError("--data-type json requires --json-file argument")
            elif data_type == 'csv' and not csv_file:
                raise ValueError("--data-type csv requires --csv-file argument")
            elif data_type == 'json' and csv_file:
                raise ValueError("Cannot specify both --data-type json and --csv-file")
            elif data_type == 'csv' and json_file:
                raise ValueError("Cannot specify both --data-type csv and --json-file")
        else:
            # Auto-detect data type if not specified
            if json_file and csv_file:
                raise ValueError("Cannot specify both JSON and CSV files. Use --data-type to specify which format to use.")
            elif json_file and json_file.endswith('.json'):
                data_type = 'json'
                print(" Auto-detected JSON format from file extension")
            elif csv_file and csv_file.endswith('.csv'):
                data_type = 'csv'
                print(" Auto-detected CSV format from file extension")
            elif json_file:
                data_type = 'json'
                print(" Auto-detected JSON format")
            elif csv_file:
                data_type = 'csv'
                print(" Auto-detected CSV format")
            else:
                print("\nERROR: No input file specified.\n")
                print("Please provide either:")
                print("  JSON: --json-file <file> or positional argument")
                print("  CSV:  --csv-file <file> [--csv-folder <folder>]\n")
                print("Use 'catocli import socket_sites_to_tf -h' for detailed help and examples.")
                raise ValueError("No input file provided")
        
        # Validate inputs based on data type
        if data_type == 'json':
            if not json_file:
                raise ValueError("JSON import requires --json-file or positional json_file argument")
            print(f" Loading JSON data from {json_file}...")
            sites_data = load_json_data(json_file)
        elif data_type == 'csv':
            if not csv_file:
                raise ValueError("CSV import requires --csv-file argument")
            print(f" Loading CSV data from {csv_file}...")
            if csv_folder:
                print(f" Loading network ranges from {csv_folder}...")
            sites_data = load_csv_data(csv_file, csv_folder)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        
        # Extract sites, WAN interfaces, LAN interfaces, and network ranges
        sites, wan_interfaces, lan_interfaces, network_ranges, lan_lag_members = extract_socket_sites_data(sites_data)
        if hasattr(args, 'verbose') and args.verbose:
            print("\n==================== DEBUG =====================\n")
            print("sites",json.dumps( sites, indent=2))
            print("wan_interfaces",json.dumps( wan_interfaces, indent=2))
            print("lan_interfaces",json.dumps( lan_interfaces, indent=2))
            print("network_ranges",json.dumps( network_ranges, indent=2))
            print("\n==================== DEBUG =====================\n")
            print(f"\nExtracted data summary:")
            print(f"  Sites: {len(sites)}")
            print(f"  WAN Interfaces: {len(wan_interfaces)}")
            print(f"  LAN Interfaces: {len(lan_interfaces)}")
            print(f"  Network Ranges: {len(network_ranges)}")
        
        print(f" Found {len(sites)} sites")
        print(f" Found {len(wan_interfaces)} WAN interfaces")
        print(f" Found {len(lan_interfaces)} LAN interfaces")
        print(f" Found {len(lan_lag_members)} LAN LAG members")
        print(f" Found {len(network_ranges)} network ranges")
        
        if not sites and not wan_interfaces and not network_ranges:
            print(" No sites, interfaces, or network ranges found. Exiting.")
            return [{"success": False, "error": "No data found to import"}]
        
        # Add module. prefix if not present
        module_name = args.module_name
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Generate Terraform configuration files if requested
        if hasattr(args, 'generate_only') and args.generate_only:
            print("\nGenerating Terraform configuration files...")
            output_dir = generate_terraform_import_files(sites, output_dir=getattr(args, 'output_dir', './imported_sites'))
            print(f"\nTerraform configuration files generated successfully in {output_dir}")
            print("\nNext steps:")
            print(f"  1. Copy the generated files to your Terraform project directory")
            print(f"  2. Run 'terraform init' to initialize")
            print(f"  3. Run 'terraform plan -generate-config-out=generated.tf' to generate configuration")
            print(f"  4. Run 'terraform apply' to import the resources")
            
            return [{
                "success": True,
                "total_generated": len(sites),
                "output_dir": output_dir
            }]
        
        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)
        
        # Ask for confirmation (unless auto-approved)
        # Determine which categories to import based on flags
        sites_only = getattr(args, 'sites_only', False)
        wan_only = getattr(args, 'wan_interfaces_only', False)
        lan_only = getattr(args, 'lan_interfaces_only', False)
        ranges_only = getattr(args, 'network_ranges_only', False)

        import_summary = []
        if not (sites_only or wan_only or lan_only or ranges_only):
            import_summary.append(f"{len(sites)} sites")
            import_summary.append(f"{len(wan_interfaces)} WAN interfaces")
            import_summary.append(f"{len(lan_interfaces)} LAN interfaces")
            import_summary.append(f"{len(network_ranges)} network ranges")
        elif sites_only:
            import_summary.append(f"{len(sites)} sites only")
        elif wan_only:
            import_summary.append(f"{len(wan_interfaces)} WAN interfaces only")
        elif lan_only:
            import_summary.append(f"{len(lan_interfaces)} LAN interfaces only")
        elif ranges_only:
            import_summary.append(f"{len(network_ranges)} network ranges only")
        
        print(f"\n Ready to import {', '.join(import_summary)}.")
        
        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]
        
        total_successful = 0
        total_failed = 0
        
        # Import sites first (if selected)
        if (sites_only or not (wan_only or lan_only or ranges_only)) and sites:
            successful, failed = import_socket_sites(sites, module_name=args.module_name, 
                                                   verbose=args.verbose, batch_size=args.batch_size, 
                                                   delay_between_batches=args.delay,
                                                   auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Import WAN interfaces (if selected)
        if (wan_only or (not sites_only and not lan_only and not ranges_only)) and wan_interfaces:
            successful, failed = import_wan_interfaces(wan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=args.batch_size, 
                                                      delay_between_batches=args.delay,
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed

        # Import LAN interfaces (if selected)
        if (lan_only or (not sites_only and not wan_only and not ranges_only)) and lan_interfaces:
            successful, failed = import_lan_interfaces(lan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=args.batch_size, 
                                                      delay_between_batches=args.delay,
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed

        # Import LAN LAG members (if any found and not in selective mode)
        if (not (sites_only or wan_only or lan_only or ranges_only)) and lan_lag_members:
            successful, failed = import_lan_lag_members(lan_lag_members, module_name=args.module_name, 
                                                       verbose=args.verbose, batch_size=args.batch_size, 
                                                       delay_between_batches=args.delay,
                                                       auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
     
        # Import network ranges (if selected)
        if (ranges_only or (not sites_only and not wan_only and not lan_only)) and network_ranges:
            successful, failed = import_network_ranges(network_ranges, lan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=args.batch_size, 
                                                      delay_between_batches=args.delay,
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Final summary
        print("\n" + "=" * 80)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 80)
        print(f" Total successful imports: {total_successful}")
        print(f" Total failed imports: {total_failed}")
        print(f" Overall success rate: {(total_successful / (total_successful + total_failed) * 100):.1f}%" if (total_successful + total_failed) > 0 else "N/A")
        print("\n Import process completed!")
        
        return [{
            "success": True, 
            "total_successful": total_successful,
            "total_failed": total_failed,
            "module_name": args.module_name
        }]
    
    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def load_csv_data(csv_file, sites_config_dir=None):
    """
    Load socket sites data from CSV files
    
    Args:
        csv_file: Main sites CSV file
        sites_config_dir: Directory containing network ranges CSV files
    
    Returns:
        List of sites in JSON format compatible with existing functions
    """
    try:
        # Load main sites CSV and group by site
        sites_dict = {}
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row['site_name'].strip():
                    continue
                
                site_name = row['site_name']
                site_id = row['site_id'].strip()
                
                # If this is the first row for this site (has site_id), create the site entry
                if site_id and site_name not in sites_dict:
                    sites_dict[site_name] = {
                        'id': site_id,
                        'name': site_name,
                        'description': row['site_description'],
                        'type': row['site_type'],
                        'connection_type': row['connection_type'],
                        'site_location': {
                            'countryCode': row['site_location_country_code'],
                            'stateCode': row['site_location_state_code'],
                            'city': row['site_location_city'],
                            'address': row['site_location_address'],
                            'timezone': row['site_location_timezone']
                        },
                        'native_range': {
                            'interface_id': row.get('native_range_interface_id', ''),  # May not be in parent CSV
                            'interface_name': row['native_range_interface_name'],
                            'subnet': row['native_range_subnet'],
                            'index': row['native_range_interface_index'],
                            'range_name': row.get('native_range_name', ''),
                            'range_id': row.get('native_range_id', ''),
                            'vlan': row.get('native_range_vlan', None),
                            'mdns_reflector': row['native_range_mdns_reflector'].upper() == 'TRUE' if row['native_range_mdns_reflector'] else False,
                            'gateway': row['native_range_gateway'] or None,
                            'range_type': row['native_range_type'],
                            'translated_subnet': row['native_range_translated_subnet'] or None,
                            'local_ip': row['native_range_local_ip'],
                            'dhcp_settings': {
                                'dhcp_type': row['native_range_dhcp_type'] or 'DHCP_DISABLED',
                                'ip_range': row['native_range_dhcp_ip_range'] or None,
                                'relay_group_id': row['native_range_dhcp_relay_group_id'] or None,
                                'relay_group_name': row['native_range_dhcp_relay_group_name'] or None,
                                'dhcp_microsegmentation': row['native_range_dhcp_microsegmentation'].upper() == 'TRUE' if row['native_range_dhcp_microsegmentation'] else False
                            }
                        },
                        'wan_interfaces': [],
                        'lan_interfaces': []
                    }
                    
                    # Add default LAN interface from parent CSV native range data
                    # This ensures every site has its default LAN interface for import
                    # Note: interface_id may be provided later from site-specific CSV files
                    if row['native_range_interface_index']:
                        default_lan_interface = {
                            'id': row.get('native_range_interface_id', ''),  # May be empty, will be filled from site CSV
                            'name': row['native_range_interface_name'],
                            'index': row['native_range_interface_index'],
                            'dest_type': 'LAN',
                            'default_lan': True,
                            'network_ranges': []  # Default interfaces typically don't have additional ranges
                        }
                        sites_dict[site_name]['lan_interfaces'].append(default_lan_interface)
                
                # Add WAN interface from current row if WAN interface data exists
                wan_id = row.get('wan_interface_id', '')
                if wan_id.strip() and site_name in sites_dict:
                    wan_interface = {
                        'id': wan_id,
                        'index': row.get('wan_interface_index', ''),
                        'name': row.get('wan_interface_name', ''),
                        'upstream_bandwidth': int(row['wan_upstream_bw']) if row.get('wan_upstream_bw', '').strip() else 25,
                        'downstream_bandwidth': int(row['wan_downstream_bw']) if row.get('wan_downstream_bw', '').strip() else 25,
                        'dest_type': 'CATO',  # Default, not available in current CSV format
                        'role': row.get('wan_role', ''),
                        'precedence': row.get('wan_precedence', 'ACTIVE')
                    }
                    sites_dict[site_name]['wan_interfaces'].append(wan_interface)
        
        # Convert sites dictionary to list
        sites = list(sites_dict.values())
        
        # Load network ranges CSV files if sites_config_dir is provided
        if sites_config_dir and os.path.exists(sites_config_dir):
            # Get list of all CSV files in the directory
            available_files = [f for f in os.listdir(sites_config_dir) if f.endswith('_network_ranges.csv')]
            
            for site in sites:
                site_name = site['name']
                ranges_file_found = None
                
                # Try different filename patterns to find the matching file
                potential_names = [
                    site_name,  # Exact name
                    site_name.replace(' ', '-'),  # Spaces to dashes
                    site_name.replace(' ', '_'),  # Spaces to underscores
                    site_name.replace('-', '_'),  # Dashes to underscores
                    site_name.replace('/', '-'),  # Slashes to dashes
                    site_name.replace('/', '_'),  # Slashes to underscores
                    # Additional transformations for special cases
                    re.sub(r'[^a-zA-Z0-9_-]', '_', site_name),  # Replace all special chars with underscores
                    re.sub(r'[^a-zA-Z0-9_-]', '-', site_name),  # Replace all special chars with dashes
                    re.sub(r'[^a-zA-Z0-9]', '', site_name),     # Remove all special chars
                    site_name.replace(' ', ''),  # Remove all spaces
                ]
                
                # Look for matching file
                for potential_name in potential_names:
                    expected_filename = f"{potential_name}_network_ranges.csv"
                    if expected_filename in available_files:
                        ranges_file_found = os.path.join(sites_config_dir, expected_filename)
                        break
                
                if ranges_file_found:
                    load_site_network_ranges_csv(site, ranges_file_found)
                else:
                    print(f"Warning: Network ranges file not found for site '{site_name}'. Tried: {[f'{name}_network_ranges.csv' for name in potential_names]}")
                    print(f"  Available files: {available_files}")
        
        return sites
        
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading CSV data from '{csv_file}': {e}")
        sys.exit(1)


def load_site_network_ranges_csv(site, ranges_csv_file):
    """
    Load network ranges for a site from CSV file and add to site data structure
    New CSV structure: 
    - Rows with lan_interface_id create/define LAN interfaces
    - Rows with network_range_id add network ranges to the current interface
    - is_native_range indicates if a network range is native for that interface
    
    Args:
        site: Site dictionary to add ranges to
        ranges_csv_file: Path to network ranges CSV file
    """
    try:
        # Load CLI settings to get default interface mapping
        from ....Utils.cliutils import load_cli_settings
        settings = load_cli_settings()
        # Note: load_cli_settings() now returns embedded defaults if file cannot be loaded
        if not settings.get("default_socket_interface_map"):
            print(f"Warning: No default socket interface mapping found for site {site['name']}")
        
        with open(ranges_csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Store interfaces by lan_interface_index for processing
            interfaces = {}
            current_interface_index = None
            current_interface_data = None
            
            for row in reader:
                # Clean up row data (remove carriage returns)
                cleaned_row = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
                row = cleaned_row
                
                # Check if this row defines a LAN interface (has lan_interface_id)
                has_lan_interface_id = bool(row.get('lan_interface_id', '').strip())
                lan_interface_index = row.get('lan_interface_index', '').strip()
                
                # Check if this is a default LAN interface (no interface ID but has index matching default)
                is_default_interface = False
                if not has_lan_interface_id and lan_interface_index:
                    connection_type = site.get('connection_type', '')
                    default_interface_index = settings.get("default_socket_interface_map", {}).get(connection_type)
                    if default_interface_index and lan_interface_index == default_interface_index:
                        is_default_interface = True
                
                # Check if this is a LAN_LAG_MEMBER interface (special case)
                is_lan_lag_member = row.get('lan_interface_dest_type', '').strip() == 'LAN_LAG_MEMBER'
                
                # If this row has a LAN interface ID, create/update the interface
                # OR if this is a default interface, get details from parent CSV
                # OR if this is a LAN_LAG_MEMBER interface
                if (has_lan_interface_id or is_default_interface or is_lan_lag_member) and lan_interface_index:
                    
                    # Create or get the interface data
                    if lan_interface_index not in interfaces:
                        if is_default_interface:
                            # For default interfaces, get details from parent CSV native_range
                            native_range = site.get('native_range', {})
                            interfaces[lan_interface_index] = {
                                'id': native_range.get('interface_id', ''),
                                'name': native_range.get('interface_name', ''),
                                'index': lan_interface_index,
                                'dest_type': 'LAN',  # Default for default interfaces
                                'default_lan': True,  # Mark as default interface
                                'network_ranges': []
                            }
                        elif is_lan_lag_member:
                            # For LAN_LAG_MEMBER interfaces, they don't have interface_id but need to be tracked for import
                            interfaces[lan_interface_index] = {
                                'id': None,  # LAN LAG members don't have interface_id in CSV
                                'name': row.get('lan_interface_name', ''),
                                'index': lan_interface_index,
                                'dest_type': row.get('lan_interface_dest_type', 'LAN_LAG_MEMBER'),
                                'default_lan': False,
                                'network_ranges': [],
                                'is_lag_member': True  # Special flag for LAN LAG members
                            }
                        else:
                            # For regular interfaces, get details from CSV row
                            interfaces[lan_interface_index] = {
                                'id': row['lan_interface_id'],
                                'name': row.get('lan_interface_name', ''),
                                'index': lan_interface_index,
                                'dest_type': row.get('lan_interface_dest_type', 'LAN'),
                                'default_lan': False,  # Will be determined by presence in native_range
                                'network_ranges': []
                            }
                    
                    current_interface_index = lan_interface_index
                    current_interface_data = interfaces[lan_interface_index]
                
                # If no new interface but we have a lan_interface_index, use existing interface
                elif lan_interface_index and lan_interface_index in interfaces:
                    # This row continues with the same interface (no new lan_interface_id but same index)
                    current_interface_index = lan_interface_index
                    current_interface_data = interfaces[lan_interface_index]
                    
                    # If this CSV row doesn't have a lan_interface_id but has network ranges,
                    # mark the interface as virtual so network ranges get processed
                    if not has_lan_interface_id and row.get('network_range_id', '').strip():
                        current_interface_data['virtual_interface'] = True
                # If we have a lan_interface_index but no interface entry, create a virtual interface for processing network ranges
                elif lan_interface_index and row.get('network_range_id', '').strip():
                    # Create a virtual interface entry for network range processing
                    # This interface won't create a LAN interface resource, but allows network ranges to be processed
                    if lan_interface_index not in interfaces:
                        interfaces[lan_interface_index] = {
                            'id': None,  # No interface resource will be created
                            'name': f"Virtual-{lan_interface_index}",
                            'index': lan_interface_index,
                            'dest_type': 'LAN',
                            'default_lan': False,
                            'network_ranges': [],
                            'virtual_interface': True  # Mark as virtual
                        }
                    current_interface_index = lan_interface_index
                    current_interface_data = interfaces[lan_interface_index]
                    
                    # Also mark this interface as virtual if it wasn't created with an interface ID
                    if not current_interface_data.get('id'):
                        current_interface_data['virtual_interface'] = True
                
                # Process network range data if present and we have a current interface
                if current_interface_data and row.get('network_range_id', '').strip():
                    
                    network_range = {
                        'id': row['network_range_id'],
                        'name': row.get('network_range_name', ''),
                        'subnet': row.get('subnet', ''),
                        'vlan': int(row['vlan']) if row.get('vlan', '').strip() else None,
                        'mdns_reflector': row.get('mdns_reflector', '').upper() == 'TRUE',
                        'gateway': row.get('gateway') or None,
                        'range_type': row.get('range_type', ''),
                        'translated_subnet': row.get('translated_subnet') or None,
                        'local_ip': row.get('local_ip', ''),
                        'native_range': row.get('is_native_range', '').upper() == 'TRUE', # update this to support json native_range=true
                        'dhcp_settings': {
                            'dhcp_type': row.get('dhcp_type', '') or 'DHCP_DISABLED',
                            'ip_range': row.get('dhcp_ip_range') or None,
                            'relay_group_id': row.get('dhcp_relay_group_id') or None,
                            'relay_group_name': row.get('dhcp_relay_group_name') or None,
                            'dhcp_microsegmentation': row.get('dhcp_microsegmentation', '').upper() == 'TRUE'
                        }
                    }
                    
                    # Add network range to current interface
                    current_interface_data['network_ranges'].append(network_range)
                    
                    # Check if this interface should be marked as default_lan
                    # by checking if this is marked as a native range
                    is_native_range = row.get('is_native_range', '').upper() == 'TRUE'
                    if is_native_range:
                        native_range = site.get('native_range', {})
                        interface_matches_native = (
                            current_interface_data['index'] == native_range.get('index') or
                            current_interface_data['name'] == native_range.get('interface_name')
                        )
                        if interface_matches_native:
                            current_interface_data['default_lan'] = True
                            # IMPORTANT: Do not add this network range to the interface's network_ranges
                            # because it's the site's native range and will be handled separately
                            # Remove it from the network_ranges list - it was just added above
                            current_interface_data['network_ranges'].pop()
                            # Skip processing this network range further
                            continue
            
            # Add interfaces to site, but first merge with any existing default interface
            existing_interfaces = site.get('lan_interfaces', [])
            new_interfaces = list(interfaces.values())
            
            # Check for default LAN interface conflicts and merge
            final_interfaces = []
            default_interface_found = False
            
            # First add existing interfaces, updating any that match new interfaces
            for existing_interface in existing_interfaces:
                if existing_interface.get('default_lan', False):
                    # This is the default interface from parent CSV
                    default_interface_found = True
                    existing_index = existing_interface.get('index')
                    
                    # Check if we have new data for the same interface
                    matching_new_interface = None
                    for new_interface in new_interfaces:
                        if (new_interface.get('index') == existing_index or 
                            new_interface.get('id') == existing_interface.get('id')):
                            matching_new_interface = new_interface
                            break
                    
                    if matching_new_interface:
                        # Merge the interfaces - keep default_lan=True from existing, but use any additional network ranges from new
                        merged_interface = existing_interface.copy()
                        merged_interface['network_ranges'] = matching_new_interface.get('network_ranges', [])
                        # Preserve the virtual_interface flag from the new interface if present
                        if matching_new_interface.get('virtual_interface'):
                            merged_interface['virtual_interface'] = True
                        final_interfaces.append(merged_interface)
                        # Remove the matching interface from new_interfaces to avoid duplication
                        new_interfaces.remove(matching_new_interface)
                    else:
                        # No new data for default interface, keep as-is
                        final_interfaces.append(existing_interface)
                else:
                    # Non-default existing interface, keep as-is
                    final_interfaces.append(existing_interface)
            
            # Add any remaining new interfaces that didn't match existing ones
            final_interfaces.extend(new_interfaces)
            
            # Update site's lan_interfaces
            site['lan_interfaces'] = final_interfaces
            
    except FileNotFoundError:
        print(f"Warning: Network ranges file '{ranges_csv_file}' not found for site {site['name']}")
    except Exception as e:
        print(f"Error loading network ranges from '{ranges_csv_file}': {e}")
        import traceback
        traceback.print_exc()


def import_socket_sites_from_csv(args, configuration):
    """
    Main function to orchestrate the socket sites import process from CSV files
    """
    try:
        print(" Terraform Import Tool - Cato Socket Sites from CSV")
        print("=" * 70)
        
        # Determine sites config directory
        sites_config_dir = None
        if hasattr(args, 'sites_config_dir') and args.sites_config_dir:
            sites_config_dir = args.sites_config_dir
        else:
            # Try to find sites_config directory relative to CSV file
            csv_dir = os.path.dirname(os.path.abspath(args.csv_file))
            potential_config_dir = os.path.join(csv_dir, 'sites_config')
            if os.path.exists(potential_config_dir):
                sites_config_dir = potential_config_dir
        
        # Load data from CSV
        print(f" Loading data from {args.csv_file}...")
        if sites_config_dir:
            print(f" Loading network ranges from {sites_config_dir}...")
        
        sites_data = load_csv_data(args.csv_file, sites_config_dir)
        
        # Extract sites, WAN interfaces, LAN interfaces, and network ranges using existing function
        sites, wan_interfaces, lan_interfaces, network_ranges, lan_lag_members = extract_socket_sites_data(sites_data)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"\nExtracted data summary:")
            print(f"  Sites: {len(sites)}")
            print(f"  WAN Interfaces: {len(wan_interfaces)}")
            print(f"  LAN Interfaces: {len(lan_interfaces)}")
            print(f"  Network Ranges: {len(network_ranges)}")
        
        print(f" Found {len(sites)} sites")
        print(f" Found {len(wan_interfaces)} WAN interfaces")
        print(f" Found {len(lan_interfaces)} LAN interfaces")
        print(f" Found {len(lan_lag_members)} LAN LAG members")
        print(f" Found {len(network_ranges)} network ranges")
        
        if not sites and not wan_interfaces and not network_ranges:
            print(" No sites, interfaces, or network ranges found. Exiting.")
            return [{"success": False, "error": "No data found to import"}]
        
        # Add module. prefix if not present
        module_name = args.module_name
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Generate Terraform configuration files if requested
        if hasattr(args, 'generate_only') and args.generate_only:
            print("\nGenerating Terraform configuration files...")
            output_dir = generate_terraform_import_files(sites, output_dir=getattr(args, 'output_dir', './imported_sites'))
            print(f"\nTerraform configuration files generated successfully in {output_dir}")
            print("\nNext steps:")
            print(f"  1. Copy the generated files to your Terraform project directory")
            print(f"  2. Run 'terraform init' to initialize")
            print(f"  3. Run 'terraform plan -generate-config-out=generated.tf' to generate configuration")
            print(f"  4. Run 'terraform apply' to import the resources")
            
            return [{
                "success": True,
                "total_generated": len(sites),
                "output_dir": output_dir
            }]
        
        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)
        
        # Ask for confirmation (unless auto-approved)
        # Determine which categories to import based on flags
        sites_only = getattr(args, 'sites_only', False)
        wan_only = getattr(args, 'wan_interfaces_only', False)
        lan_only = getattr(args, 'lan_interfaces_only', False)
        ranges_only = getattr(args, 'network_ranges_only', False)

        import_summary = []
        if not (sites_only or wan_only or lan_only or ranges_only):
            import_summary.append(f"{len(sites)} sites")
            import_summary.append(f"{len(wan_interfaces)} WAN interfaces")
            import_summary.append(f"{len(lan_interfaces)} LAN interfaces")
            import_summary.append(f"{len(network_ranges)} network ranges")
        elif sites_only:
            import_summary.append(f"{len(sites)} sites only")
        elif wan_only:
            import_summary.append(f"{len(wan_interfaces)} WAN interfaces only")
        elif lan_only:
            import_summary.append(f"{len(lan_interfaces)} LAN interfaces only")
        elif ranges_only:
            import_summary.append(f"{len(network_ranges)} network ranges only")
        
        print(f"\n Ready to import {', '.join(import_summary)}.")
        
        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]
        
        total_successful = 0
        total_failed = 0
        
        # Import sites first (if selected)
        if (sites_only or not (wan_only or lan_only or ranges_only)) and sites:
            successful, failed = import_socket_sites(sites, module_name=args.module_name, 
                                                   verbose=args.verbose, batch_size=getattr(args, 'batch_size', 10), 
                                                   delay_between_batches=getattr(args, 'delay', 2),
                                                   auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Import WAN interfaces (if selected)
        if (wan_only or (not sites_only and not lan_only and not ranges_only)) and wan_interfaces:
            successful, failed = import_wan_interfaces(wan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=getattr(args, 'batch_size', 10), 
                                                      delay_between_batches=getattr(args, 'delay', 2),
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed

        # Import LAN interfaces (if selected)
        if (lan_only or (not sites_only and not wan_only and not ranges_only)) and lan_interfaces:
            successful, failed = import_lan_interfaces(lan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=getattr(args, 'batch_size', 10), 
                                                      delay_between_batches=getattr(args, 'delay', 2),
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed

        # Import LAN LAG members (if any found and not in selective mode)
        if (not (sites_only or wan_only or lan_only or ranges_only)) and lan_lag_members:
            successful, failed = import_lan_lag_members(lan_lag_members, module_name=args.module_name, 
                                                       verbose=args.verbose, batch_size=getattr(args, 'batch_size', 10), 
                                                       delay_between_batches=getattr(args, 'delay', 2),
                                                       auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
     
        # Import network ranges (if selected)
        if (ranges_only or (not sites_only and not wan_only and not lan_only)) and network_ranges:
            successful, failed = import_network_ranges(network_ranges, lan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=getattr(args, 'batch_size', 10), 
                                                      delay_between_batches=getattr(args, 'delay', 2),
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Final summary
        print("\n" + "=" * 70)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 70)
        print(f" Total successful imports: {total_successful}")
        print(f" Total failed imports: {total_failed}")
        print(f" Overall success rate: {(total_successful / (total_successful + total_failed) * 100):.1f}%" if (total_successful + total_failed) > 0 else "N/A")
        print("\n Import process completed!")
        
        return [{
            "success": True, 
            "total_successful": total_successful,
            "total_failed": total_failed,
            "module_name": args.module_name
        }]
    
    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def convert_csv_to_json(args, configuration):
    """
    Convert CSV data to JSON format compatible with existing import tools
    """
    try:
        print(" CSV to JSON Converter - Cato Socket Sites")
        print("=" * 50)
        
        # Determine sites config directory
        sites_config_dir = None
        if hasattr(args, 'sites_config_dir') and args.sites_config_dir:
            sites_config_dir = args.sites_config_dir
        else:
            # Try to find sites_config directory relative to CSV file
            csv_dir = os.path.dirname(os.path.abspath(args.csv_file))
            potential_config_dir = os.path.join(csv_dir, 'sites_config')
            if os.path.exists(potential_config_dir):
                sites_config_dir = potential_config_dir
        
        # Load data from CSV
        print(f" Loading data from {args.csv_file}...")
        if sites_config_dir:
            print(f" Loading network ranges from {sites_config_dir}...")
        
        sites_data = load_csv_data(args.csv_file, sites_config_dir)
        
        # Create JSON structure
        json_data = {"sites": sites_data}
        
        # Determine output filename
        if hasattr(args, 'output_file') and args.output_file:
            output_file = args.output_file
        else:
            # Generate output filename based on input CSV
            csv_base = os.path.splitext(os.path.basename(args.csv_file))[0]
            output_file = f"{csv_base}_converted.json"
        
        # Write JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        
        print(f" Converted {len(sites_data)} sites to JSON format")
        print(f" Output written to: {output_file}")
        
        return [{
            "success": True,
            "input_file": args.csv_file,
            "output_file": output_file,
            "sites_count": len(sites_data)
        }]
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]
