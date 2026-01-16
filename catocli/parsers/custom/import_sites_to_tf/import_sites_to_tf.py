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
from ..customLib import validate_terraform_environment, clean_csv_file
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException

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


def validate_cato_api_auth(configuration, verbose=False):
    """
    Validate Cato API authentication by making a test entityLookup query
    
    Args:
        configuration: API configuration object with credentials
        verbose: Whether to show verbose output
    
    Returns:
        tuple: (success: bool, error_message: str)
    """
    try:
        if verbose:
            print("\nValidating Cato API authentication...")
        
        # Create API client instance
        api_client = ApiClient(configuration)
        instance = CallApi(api_client)
        
        # Prepare entityLookup query (simple query to test auth)
        query = {
            "query": "query entityLookup ( $accountID:ID! $type:EntityType! ) { entityLookup ( accountID:$accountID type:$type ) { items { entity { id name type } } total } }",
            "operationName": "entityLookup",
            "variables": {
                "accountID": configuration.accountID,
                "type": "account"
            }
        }
        
        # Call the API
        params = {
            'v': False,  # verbose mode off for validation
            'f': 'json',
            'p': False,
            't': False
        }
        
        response = instance.call_api(query, params)
        
        # Check response structure
        if not response or len(response) == 0:
            return False, "Empty response from API"
        
        response_data = response[0]
        
        # Check for authentication errors
        if 'errors' in response_data:
            error_messages = [error.get('message', 'Unknown error') for error in response_data['errors']]
            return False, f"API authentication failed: {', '.join(error_messages)}"
        
        # Check for valid data structure
        if 'data' not in response_data:
            return False, "Invalid response structure from API"
        
        if 'entityLookup' not in response_data['data']:
            return False, "Invalid response structure: missing entityLookup"
        
        entity_lookup = response_data['data']['entityLookup']
        if 'items' not in entity_lookup or 'total' not in entity_lookup:
            return False, "Invalid response structure: missing items or total"
        
        if verbose:
            print("✓ Cato API authentication validated successfully")
            print(f"  Account ID: {configuration.accountID}")
        
        return True, None
        
    except ApiException as e:
        return False, f"API Exception: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error during authentication validation: {str(e)}"


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
                        # Extract DHCP settings from network_range (stored in dhcp_settings object)
                        dhcp_settings = network_range.get('dhcp_settings')

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
                            'microsegmentation': network_range.get('microsegmentation', False),
                            'dhcp_settings': dhcp_settings  # Pass full dhcp_settings object for import resource determination
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
        print(f"terraform import '{resource_address}' {resource_id}")
        
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
        
        # Check if site_id is empty or blank
        if not site_id or not str(site_id).strip():
            print(f"\n[{i+1}/{total_sites}] Skipping site '{site_name}' - ID is empty or blank")
            continue

        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'

        # Use site_name as the key for readability in state
        # This matches the updated Terraform module logic which uses site.name for indexing
        site_key = site_name

        # Use correct resource addressing for nested module
        resource_address = f'{module_name}.module.socket-site["{site_key}"].cato_socket_site.site'
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
        
        # Check if interface_id is empty or blank
        if not interface_id or not str(interface_id).strip():
            print(f"\n[{i+1}/{total_interfaces}] Skipping WAN interface '{interface_name}' on {site_name} - ID is empty or blank")
            continue
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'

        # Use site_name as the site key for readability in state
        site_key = site_name

        # In the module, cato_wan_interface.wan is now keyed by interface_index, which we
        # format from the JSON "index" field. Use interface_index as the key.
        wan_key = interface.get('interface_index', interface_id)  # Use formatted index, fallback to ID
        resource_address = f'{module_name}.module.socket-site["{site_key}"].cato_wan_interface.wan["{wan_key}"]'
        
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
        
        # Check if interface_index is empty or blank (LAG members use index for import)
        if not interface_index or not str(interface_index).strip():
            print(f"\n[{i+1}/{total_interfaces}] Skipping LAN LAG member '{interface_name}' on {site_name} - Index is empty or blank")
            continue
        
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

        # Use site_name as the site key for readability in state
        site_key = site_name

        # LAN LAG member addressing pattern from state file:
        # module.sites_from_csv.module.socket-site["site_name"].cato_lan_interface_lag_member.lag_lan_members["interface_index"]
        # Use formatted interface_index for keying
        lag_key = formatted_index
        resource_address = f'{module_name}.module.socket-site["{site_key}"].cato_lan_interface_lag_member.lag_lan_members["{lag_key}"]'

        print(f"\n[{i+1}/{total_interfaces}] LAN LAG Member: {interface_name} on {site_name} (Index: {interface_index}, ID: {interface_id})")

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
        
        # Check if interface_id is empty or blank
        if not interface_id or not str(interface_id).strip():
            print(f"\n[{i+1}/{total_interfaces}] Skipping LAN interface '{interface_name}' on {site_name} - ID is empty or blank")
            continue
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'

        # Updated addressing to use interface_index-based indexing for resource addressing:
        # module.sites.module.socket-site[site_name].module.lan_interfaces[interface_index].cato_lan_interface.interface[interface_index]
        # Apply the same index formatting logic as the Terraform module
        try:
            # If index is a number, format as INT_X
            int(interface_index)
            formatted_index = f"INT_{interface_index}"
        except (ValueError, TypeError):
            # If not a number or None, use as-is
            formatted_index = interface_index if interface_index else interface_id

        # Use site_name as the site key for readability in state
        site_key = site_name

        # The resource address uses interface_index for keying
        # This matches the updated Terraform module logic: interface.interface_index
        lan_key = formatted_index
        resource_address = f'{module_name}.module.socket-site["{site_key}"].module.lan_interfaces["{lan_key}"].cato_lan_interface.interface["{formatted_index}"]'

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
        site_id = network_range['site_id']
        subnet = network_range['subnet']
        interface_index = network_range['interface_index']
        calculated_index = network_range['calculated_index']
        
        # Check if network_range_id is empty or blank
        if not network_range_id or not str(network_range_id).strip():
            print(f"\n[{i+1}/{total_ranges}] Skipping network range '{range_name}' ({subnet}) on {site_name} - ID is empty or blank")
            continue
        
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
        matching_lan_interface = None
        for lan in lan_interfaces:
            if lan['site_name'] == site_name and lan['index'] == interface_index:
                matching_lan_interface = lan
                break

        is_default_interface = matching_lan_interface is None

        # Generate the correct key format to match the Terraform module logic
        # The module uses "${network_range.name}_${idx}" as the key
        # Use the range name and calculated index to create a consistent key
        range_key = f"{range_name}_{calculated_index}"

        # Determine if this network range has DHCP settings
        # Check if dhcp_settings object exists and has a dhcp_type field
        # The module creates with_dhcp[0] if dhcp_settings != null, no_dhcp[0] if dhcp_settings == null
        dhcp_settings = network_range.get('dhcp_settings')
        has_dhcp = (
            dhcp_settings is not None and 
            isinstance(dhcp_settings, dict) and 
            dhcp_settings.get('dhcp_type') is not None
        )
        dhcp_resource = 'with_dhcp' if has_dhcp else 'no_dhcp'

        # Use site_name as the site key to match Terraform module logic (module indexes by site.name)
        site_key = site_name

        # Determine the correct resource addressing based on whether this is a default interface
        if is_default_interface:
            # Default interface network ranges are addressed directly under the socket-site module
            resource_address = f'{module_name}.module.socket-site["{site_key}"].cato_network_range.default_interface_ranges["{range_key}"]'
        else:
            # Regular interface network ranges go through the lan_interfaces module
            # Use interface_index (formatted) for LAN interface key to match Terraform module logic
            lan_key = formatted_index
            # Use with_dhcp[0] or no_dhcp[0] based on whether DHCP settings exist
            resource_address = f'{module_name}.module.socket-site["{site_key}"].module.lan_interfaces["{lan_key}"].module.network_ranges.module.network_range["{range_key}"].cato_network_range.{dhcp_resource}[0]'
        
        print(f"\n[{i+1}/{total_ranges}] Network Range: {range_name} - {subnet} ({network_range_id}) on {site_name}")
        print(f"  'terraform import {resource_address}' {network_range_id}")
        
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
        validate_only = getattr(args, 'validate', False)
        
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
        
        # If validation mode, run validation and exit
        if validate_only:
            if data_type == 'json':
                if not json_file:
                    raise ValueError("JSON validation requires --json-file argument")
                success, errors, warnings = validate_json_file(json_file, verbose=getattr(args, 'verbose', False))
            elif data_type == 'csv':
                if not csv_file:
                    raise ValueError("CSV validation requires --csv-file argument")
                success, errors, warnings = validate_csv_files(csv_file, csv_folder, verbose=getattr(args, 'verbose', False))
            else:
                raise ValueError(f"Unsupported data type for validation: {data_type}")
            
            # Return validation results
            if success:
                print("\n✓ Validation completed successfully. Files are ready for import.")
                return [{
                    "success": True,
                    "validation_passed": True,
                    "errors": errors,
                    "warnings": warnings
                }]
            else:
                print("\n❌ Validation failed. Please fix the errors above before importing.")
                return [{
                    "success": False,
                    "validation_passed": False,
                    "errors": errors,
                    "warnings": warnings
                }]
        
        # Validate Cato API authentication (skip if validation-only mode)
        auth_success, auth_error = validate_cato_api_auth(configuration, verbose=getattr(args, 'verbose', False))
        if not auth_success:
            print(f"\nERROR: Cato API authentication failed")
            print(f"  {auth_error}")
            print("\nPlease check your API credentials and try again.")
            return [{"success": False, "error": f"Authentication failed: {auth_error}"}]
        
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


def validate_csv_files(csv_file, sites_config_dir=None, verbose=False):
    """
    Validate CSV files for import processing
    
    Args:
        csv_file: Main sites CSV file
        sites_config_dir: Directory containing network ranges CSV files
        verbose: Show detailed validation output
    
    Returns:
        tuple: (success: bool, errors: list, warnings: list)
    """
    errors = []
    warnings = []
    
    print("\n" + "=" * 80)
    print(" CSV VALIDATION")
    print("=" * 80)
    
    # Validate main CSV file
    print(f"\nValidating main CSV file: {csv_file}")
    if not os.path.exists(csv_file):
        errors.append(f"Main CSV file not found: {csv_file}")
        return False, errors, warnings
    
    try:
        # Check file encoding
        with open(csv_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for trailing newlines
        if content.endswith('\r\n'):
            warnings.append(f"Main CSV has trailing newline (will be cleaned automatically)")
        
        # Check for empty lines
        lines = content.splitlines()
        empty_lines = 0
        for idx, line in enumerate(lines, 1):
            test_line = line.replace(',', '').strip()
            if not test_line:
                empty_lines += 1
                if verbose:
                    warnings.append(f"Empty line found at line {idx} (will be cleaned automatically)")
        
        if empty_lines > 0:
            warnings.append(f"Found {empty_lines} empty line(s) in main CSV (will be cleaned automatically)")
        
        # Parse CSV and validate required fields
        # Base required fields that all rows must have
        base_required_fields = [
            'site_name',
            'wan_interface_index',
            'wan_interface_name',
            'wan_upstream_bw',
            'wan_downstream_bw',
            'wan_role',
            'wan_precedence'
        ]
        
        # Additional fields required when site_type is specified (full site record)
        site_type_required_fields = [
            'site_type',
            'connection_type',
            'native_range_subnet',
            'native_range_local_ip',
            'native_range_type',
            'native_range_interface_index',
            'native_range_interface_name',
            'native_range_interface_dest_type',
            'native_range_dhcp_type',
            'site_location_city',
            'site_location_country_code',
            'site_location_timezone'
        ]
        
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            
            if not headers:
                errors.append("CSV file has no headers")
                return False, errors, warnings
            
            # Check for base required fields in headers
            missing_base = [field for field in base_required_fields if field not in headers]
            if missing_base:
                errors.append(f"Missing required fields in main CSV: {', '.join(missing_base)}")
            
            # Check if site_type fields are in headers (to determine what kind of CSV this is)
            has_site_type_fields = 'site_type' in headers
            if has_site_type_fields:
                missing_site_type = [field for field in site_type_required_fields if field not in headers]
                if missing_site_type:
                    warnings.append(f"CSV appears to have site_type but missing some site fields: {', '.join(missing_site_type)}")
            
            # Validate data rows
            row_count = 0
            for row_idx, row in enumerate(reader, 2):  # Start at 2 (header is row 1)
                row_count += 1
                
                # Check for empty site_name (critical field)
                if not row.get('site_name', '').strip():
                    if verbose:
                        warnings.append(f"Row {row_idx}: Empty site_name (will be skipped)")
                    continue
                
                # Validate based on whether this row has site_type
                has_site_type = row.get('site_type', '').strip() != ''
                
                # Check base required fields
                for field in base_required_fields:
                    if not row.get(field, '').strip():
                        errors.append(f"Row {row_idx} ({row.get('site_name', 'unknown')}): Missing required field '{field}'")
                
                # If row has site_type, check additional site fields
                if has_site_type:
                    for field in site_type_required_fields:
                        if field in headers and not row.get(field, '').strip():
                            errors.append(f"Row {row_idx} ({row.get('site_name', 'unknown')}): Missing required site field '{field}'")
                    
                    # Validate DHCP-related fields for native range
                    native_dhcp_type = row.get('native_range_dhcp_type', '').strip()
                    if native_dhcp_type == 'DHCP_RANGE':
                        if not row.get('native_range_dhcp_ip_range', '').strip():
                            errors.append(f"Row {row_idx} ({row.get('site_name', 'unknown')}): native_range_dhcp_type is DHCP_RANGE but missing native_range_dhcp_ip_range")
                    elif native_dhcp_type == 'DHCP_RELAY':
                        relay_id = row.get('native_range_dhcp_relay_group_id', '').strip()
                        relay_name = row.get('native_range_dhcp_relay_group_name', '').strip()
                        if not relay_id and not relay_name:
                            errors.append(f"Row {row_idx} ({row.get('site_name', 'unknown')}): native_range_dhcp_type is DHCP_RELAY but missing native_range_dhcp_relay_group_id or native_range_dhcp_relay_group_name")
                        if relay_id and relay_name:
                            warnings.append(f"Row {row_idx} ({row.get('site_name', 'unknown')}): Both native_range_dhcp_relay_group_id and native_range_dhcp_relay_group_name are specified (should use only one)")
        
        print(f"  ✓ Main CSV validated: {row_count} data rows found")
        
    except UnicodeDecodeError as e:
        errors.append(f"Main CSV encoding error: {str(e)}")
    except csv.Error as e:
        errors.append(f"Main CSV parsing error: {str(e)}")
    except Exception as e:
        errors.append(f"Main CSV validation error: {str(e)}")
    
    # Validate network ranges CSV files if directory provided
    if sites_config_dir:
        print(f"\nValidating network ranges CSV files in: {sites_config_dir}")
        
        if not os.path.exists(sites_config_dir):
            warnings.append(f"Network ranges directory not found: {sites_config_dir}")
        else:
            csv_files = [f for f in os.listdir(sites_config_dir) if f.endswith('_network_ranges.csv')]
            
            if not csv_files:
                warnings.append(f"No network ranges CSV files found in {sites_config_dir}")
            else:
                print(f"  Found {len(csv_files)} network ranges CSV file(s)")
                
                for csv_filename in csv_files:
                    csv_filepath = os.path.join(sites_config_dir, csv_filename)
                    
                    try:
                        with open(csv_filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Check for trailing newlines and empty lines
                        if content.endswith('\r\n'):
                            if verbose:
                                warnings.append(f"{csv_filename}: Has trailing newline (will be cleaned)")
                        
                        lines = content.splitlines()
                        empty_lines = sum(1 for line in lines if not line.replace(',', '').strip())
                        if empty_lines > 0 and verbose:
                            warnings.append(f"{csv_filename}: {empty_lines} empty line(s) (will be cleaned)")
                        
                        # Parse and validate structure
                        with open(csv_filepath, 'r', newline='', encoding='utf-8') as f:
                            reader = csv.DictReader(f)
                            headers = reader.fieldnames
                            
                            if not headers:
                                errors.append(f"{csv_filename}: No headers found")
                                continue
                            
                            # Check if this is a LAN interface + native range file or just network ranges
                            has_lan_interface_dest_type = 'lan_interface_dest_type' in headers
                            
                            # Base required fields for all network range files
                            base_range_fields = [
                                'lan_interface_index',
                                'subnet',
                                'local_ip',
                                'range_type'
                            ]
                            # Support both 'name' and 'network_range_name' for the name field
                            has_name_field = 'name' in headers or 'network_range_name' in headers
                            
                            # Additional fields required when lan_interface_dest_type is present (LAN interface + native range)
                            lan_interface_fields = [
                                'lan_interface_name',
                                'lan_interface_dest_type',
                                'is_native_range',
                                'lan_interface_index'
                            ]
                            
                            # Check base required fields
                            missing = [field for field in base_range_fields if field not in headers]
                            if missing:
                                errors.append(f"{csv_filename}: Missing required fields: {', '.join(missing)}")
                            
                            if not has_name_field:
                                errors.append(f"{csv_filename}: Missing required field: 'name' or 'network_range_name'")
                            
                            # If LAN interface fields are present, check them too
                            if has_lan_interface_dest_type:
                                missing_lan = [field for field in lan_interface_fields if field not in headers]
                                if missing_lan:
                                    errors.append(f"{csv_filename}: Has lan_interface_dest_type but missing LAN interface fields: {', '.join(missing_lan)}")
                            
                            # Validate data rows
                            for row_idx, row in enumerate(reader, 2):
                                # Check if row has any data at all
                                has_data = any(row.get(field, '').strip() for field in row.keys())
                                if not has_data:
                                    continue  # Skip completely empty rows
                                
                                # Determine record type based on lan_interface_dest_type
                                has_lan_dest_type = row.get('lan_interface_dest_type', '').strip() != ''
                                lan_dest_type_value = row.get('lan_interface_dest_type', '').strip()
                                range_type = row.get('range_type', '').strip()
                                range_name = row.get('network_range_name', '') or row.get('name', '')
                                lan_interface_idx = row.get('lan_interface_index', '').strip()
                                
                                # If this is a LAN interface record (has lan_interface_dest_type)
                                if has_lan_dest_type:
                                    # Special handling for LAN_LAG_MEMBER - only requires 3 fields
                                    if lan_dest_type_value == 'LAN_LAG_MEMBER':
                                        lag_required_fields = ['lan_interface_name', 'lan_interface_dest_type', 'lan_interface_index']
                                        for field in lag_required_fields:
                                            if not row.get(field, '').strip():
                                                if verbose:
                                                    errors.append(f"{csv_filename} row {row_idx}: LAN_LAG_MEMBER missing required field '{field}'")
                                        # Skip remaining validation for LAG members
                                        continue
                                    
                                    # For other LAN interface records, validate LAN interface fields
                                    for field in lan_interface_fields:
                                        if field in headers and not row.get(field, '').strip():
                                            if verbose:
                                                errors.append(f"{csv_filename} row {row_idx}: LAN interface record missing required field '{field}'")
                                    # Skip network range validation for LAN interface records
                                    continue
                                
                                # Check required fields (except local_ip which is conditional)
                                for field in base_range_fields:
                                    if field == 'local_ip':
                                        # local_ip is required for VLAN ranges, NOT for Direct, Native, or Routed
                                        if range_type not in ['Direct', 'Native', 'Routed'] and not row.get('local_ip', '').strip():
                                            if verbose:
                                                errors.append(f"{csv_filename} row {row_idx} ({range_name}): Missing required field 'local_ip' (required for {range_type} ranges)")
                                    else:
                                        if not row.get(field, '').strip():
                                            if verbose:
                                                errors.append(f"{csv_filename} row {row_idx} ({range_name}): Missing required field '{field}'")
                                
                                # Conditional validations based on range_type
                                if range_type == 'Routed':
                                    if not row.get('gateway', '').strip():
                                        if verbose:
                                            errors.append(f"{csv_filename} row {row_idx} ({range_name}): range_type is Routed but missing 'gateway'")
                                elif range_type == 'VLAN':
                                    # VLAN is NOT required for native range records (those with lan_interface_dest_type)
                                    # but IS required for regular network ranges
                                    if not has_lan_dest_type and not row.get('vlan', '').strip():
                                        if verbose:
                                            errors.append(f"{csv_filename} row {row_idx} ({range_name}): range_type is VLAN but missing 'vlan' (not required for native ranges)")
                                
                                # Validate DHCP-related fields
                                dhcp_type = row.get('dhcp_type', '').strip()
                                if dhcp_type == 'DHCP_RANGE':
                                    if not row.get('dhcp_ip_range', '').strip():
                                        if verbose:
                                            errors.append(f"{csv_filename} row {row_idx} ({range_name}): dhcp_type is DHCP_RANGE but missing 'dhcp_ip_range'")
                                elif dhcp_type == 'DHCP_RELAY':
                                    relay_id = row.get('dhcp_relay_group_id', '').strip()
                                    relay_name = row.get('dhcp_relay_group_name', '').strip()
                                    if not relay_id and not relay_name:
                                        if verbose:
                                            errors.append(f"{csv_filename} row {row_idx} ({range_name}): dhcp_type is DHCP_RELAY but missing dhcp_relay_group_id or dhcp_relay_group_name")
                                    if relay_id and relay_name:
                                        if verbose:
                                            warnings.append(f"{csv_filename} row {row_idx} ({range_name}): Both dhcp_relay_group_id and dhcp_relay_group_name are specified (should use only one)")
                                
                                # Check name field
                                if not range_name.strip():
                                    if verbose:
                                        errors.append(f"{csv_filename} row {row_idx}: Missing network range name")
                        
                        if verbose:
                            print(f"    ✓ {csv_filename}")
                    
                    except Exception as e:
                        errors.append(f"{csv_filename}: Validation error: {str(e)}")
                
                if not verbose:
                    print(f"  ✓ All network ranges CSV files validated")
    
    # Summary
    print("\n" + "=" * 80)
    print(" VALIDATION SUMMARY")
    print("=" * 80)
    
    if errors:
        print(f"\n❌ VALIDATION FAILED: {len(errors)} error(s) found")
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print(f"\n✓ VALIDATION PASSED")
    
    if warnings:
        print(f"\n⚠  {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  WARNING: {warning}")
    
    print("=" * 80 + "\n")
    
    return len(errors) == 0, errors, warnings


def validate_json_file(json_file, verbose=False):
    """
    Validate JSON file for import processing
    
    Args:
        json_file: Path to JSON file
        verbose: Show detailed validation output
    
    Returns:
        tuple: (success: bool, errors: list, warnings: list)
    """
    errors = []
    warnings = []
    
    print("\n" + "=" * 80)
    print(" JSON VALIDATION")
    print("=" * 80)
    
    print(f"\nValidating JSON file: {json_file}")
    
    if not os.path.exists(json_file):
        errors.append(f"JSON file not found: {json_file}")
        return False, errors, warnings
    
    try:
        # Check file encoding and read content
        with open(json_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON format: {str(e)}")
            return False, errors, warnings
        
        print(f"  ✓ JSON file is well-formed")
        
        # Validate structure
        if not isinstance(data, dict):
            errors.append("JSON root must be an object/dict")
            return False, errors, warnings
        
        if 'sites' not in data:
            errors.append("JSON must contain 'sites' key")
            return False, errors, warnings
        
        sites = data['sites']
        if not isinstance(sites, list):
            errors.append("'sites' must be an array/list")
            return False, errors, warnings
        
        print(f"  ✓ JSON structure is valid")
        print(f"  ✓ Found {len(sites)} site(s) in JSON")
        
        # Validate each site
        required_site_fields = ['id', 'name', 'connection_type', 'type']
        
        for idx, site in enumerate(sites):
            site_name = site.get('name', f'Site #{idx+1}')
            
            # Check required fields
            missing_fields = [field for field in required_site_fields if not site.get(field)]
            if missing_fields:
                errors.append(f"Site '{site_name}': Missing required fields: {', '.join(missing_fields)}")
            
            # Check native_range structure
            if 'native_range' in site:
                native_range = site['native_range']
                if not isinstance(native_range, dict):
                    errors.append(f"Site '{site_name}': native_range must be an object")
                else:
                    # Check for required native_range fields
                    if not native_range.get('subnet'):
                        errors.append(f"Site '{site_name}': native_range missing 'subnet'")
                    if not native_range.get('local_ip'):
                        errors.append(f"Site '{site_name}': native_range missing 'local_ip'")
                    
                    # Validate DHCP-related fields for native range
                    dhcp_settings = native_range.get('dhcp_settings')
                    if dhcp_settings and isinstance(dhcp_settings, dict):
                        dhcp_type = dhcp_settings.get('dhcp_type')
                        if dhcp_type == 'DHCP_RANGE':
                            if not dhcp_settings.get('ip_range'):
                                errors.append(f"Site '{site_name}': native_range dhcp_type is DHCP_RANGE but missing 'ip_range'")
                        elif dhcp_type == 'DHCP_RELAY':
                            relay_id = dhcp_settings.get('relay_group_id')
                            relay_name = dhcp_settings.get('relay_group_name')
                            if not relay_id and not relay_name:
                                errors.append(f"Site '{site_name}': native_range dhcp_type is DHCP_RELAY but missing relay_group_id or relay_group_name")
                            if relay_id and relay_name:
                                warnings.append(f"Site '{site_name}': native_range has both relay_group_id and relay_group_name (should use only one)")
            else:
                warnings.append(f"Site '{site_name}': Missing 'native_range' object")
            
            # Check WAN interfaces
            wan_interfaces = site.get('wan_interfaces', [])
            if not wan_interfaces:
                warnings.append(f"Site '{site_name}': No WAN interfaces defined")
            
            for wan_idx, wan in enumerate(wan_interfaces):
                if not wan.get('id'):
                    errors.append(f"Site '{site_name}' WAN #{wan_idx+1}: Missing 'id'")
                if not wan.get('index'):
                    errors.append(f"Site '{site_name}' WAN #{wan_idx+1}: Missing 'index'")
                if not wan.get('name'):
                    if verbose:
                        warnings.append(f"Site '{site_name}' WAN #{wan_idx+1}: Missing 'name'")
            
            # Check LAN interfaces and network ranges
            lan_interfaces = site.get('lan_interfaces', [])
            for lan_idx, lan in enumerate(lan_interfaces):
                is_default = lan.get('default_lan', False)
                lan_index = lan.get('index', f'#{lan_idx+1}')
                
                # Validate network ranges within this LAN interface
                network_ranges = lan.get('network_ranges', [])
                for nr_idx, nr in enumerate(network_ranges):
                    range_name = nr.get('name', f'Range #{nr_idx+1}')
                    range_type = nr.get('range_type', '')
                    
                    # Required fields for network ranges
                    if not nr.get('subnet'):
                        errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': Missing 'subnet'")
                    if not nr.get('range_type'):
                        errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': Missing 'range_type'")
                    if not nr.get('name'):
                        errors.append(f"Site '{site_name}' LAN {lan_index} range #{nr_idx+1}: Missing 'name'")
                    
                    # Conditional local_ip validation
                    if range_type not in ['Direct', 'Native', 'Routed']:
                        if not nr.get('local_ip'):
                            if verbose:
                                errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': Missing 'local_ip' (required for {range_type})")
                    
                    # Range type specific validations
                    if range_type == 'Routed':
                        if not nr.get('gateway'):
                            if verbose:
                                errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': range_type is Routed but missing 'gateway'")
                    elif range_type == 'VLAN':
                        # VLAN not required for default_lan interfaces
                        if not is_default and not nr.get('vlan'):
                            if verbose:
                                errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': range_type is VLAN but missing 'vlan'")
                    
                    # DHCP validations
                    dhcp_settings = nr.get('dhcp_settings')
                    if dhcp_settings and isinstance(dhcp_settings, dict):
                        dhcp_type = dhcp_settings.get('dhcp_type')
                        if dhcp_type == 'DHCP_RANGE':
                            if not dhcp_settings.get('ip_range'):
                                if verbose:
                                    errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': dhcp_type is DHCP_RANGE but missing 'ip_range'")
                        elif dhcp_type == 'DHCP_RELAY':
                            relay_id = dhcp_settings.get('relay_group_id')
                            relay_name = dhcp_settings.get('relay_group_name')
                            if not relay_id and not relay_name:
                                if verbose:
                                    errors.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': dhcp_type is DHCP_RELAY but missing relay_group_id or relay_group_name")
                            if relay_id and relay_name:
                                if verbose:
                                    warnings.append(f"Site '{site_name}' LAN {lan_index} range '{range_name}': Both relay_group_id and relay_group_name specified (should use only one)")
        
        if verbose:
            print(f"\n  Detailed validation:")
            print(f"    - Sites validated: {len(sites)}")
            total_wan = sum(len(site.get('wan_interfaces', [])) for site in sites)
            total_lan = sum(len(site.get('lan_interfaces', [])) for site in sites)
            print(f"    - Total WAN interfaces: {total_wan}")
            print(f"    - Total LAN interfaces: {total_lan}")
    
    except UnicodeDecodeError as e:
        errors.append(f"File encoding error: {str(e)}")
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
    
    # Summary
    print("\n" + "=" * 80)
    print(" VALIDATION SUMMARY")
    print("=" * 80)
    
    if errors:
        print(f"\n❌ VALIDATION FAILED: {len(errors)} error(s) found")
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print(f"\n✓ VALIDATION PASSED")
    
    if warnings:
        print(f"\n⚠  {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  WARNING: {warning}")
    
    print("=" * 80 + "\n")
    
    return len(errors) == 0, errors, warnings


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
        # Clean the main CSV file before loading
        print(f"Cleaning CSV file: {csv_file}")
        clean_csv_file(csv_file)
        
        # Clean all network ranges CSV files if directory provided
        if sites_config_dir and os.path.exists(sites_config_dir):
            print(f"Cleaning network ranges CSV files in: {sites_config_dir}")
            for csv_filename in os.listdir(sites_config_dir):
                if csv_filename.endswith('.csv'):
                    csv_filepath = os.path.join(sites_config_dir, csv_filename)
                    clean_csv_file(csv_filepath)
        
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
                            # 'gateway': row['native_range_gateway'] or None,
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
                    print(f"  - Warning: Network ranges file not found for site '{site_name}'.")
        
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
                        # Keep DHCP fields flat for bulk-sites module compatibility
                        'dhcp_type': row.get('dhcp_type', '') or None,
                        'dhcp_ip_range': row.get('dhcp_ip_range') or None,
                        'dhcp_relay_group_id': row.get('dhcp_relay_group_id') or None,
                        'dhcp_relay_group_name': row.get('dhcp_relay_group_name') or None,
                        'dhcp_microsegmentation': row.get('dhcp_microsegmentation', '').upper() == 'TRUE',
                        # Also create dhcp_settings object for import script compatibility
                        'dhcp_settings': {
                            'dhcp_type': row.get('dhcp_type', '') or None,
                            'ip_range': row.get('dhcp_ip_range') or None,
                            'relay_group_id': row.get('dhcp_relay_group_id') or None,
                            'relay_group_name': row.get('dhcp_relay_group_name') or None,
                            'dhcp_microsegmentation': row.get('dhcp_microsegmentation', '').upper() == 'TRUE'
                        } if row.get('dhcp_type', '').strip() else None
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
        
        # Validate Cato API authentication
        auth_success, auth_error = validate_cato_api_auth(configuration, verbose=getattr(args, 'verbose', False))
        if not auth_success:
            print(f"\nERROR: Cato API authentication failed")
            print(f"  {auth_error}")
            print("\nPlease check your API credentials and try again.")
            return [{"success": False, "error": f"Authentication failed: {auth_error}"}]
        
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
