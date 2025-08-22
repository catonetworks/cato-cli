#!/usr/bin/env python3
"""
Direct Terraform Import Script using Python
Imports socket sites, WAN interfaces, and network ranges directly using subprocess calls to terraform import
Reads from JSON structure exported from Cato API
Adapted from scripts/import_if_rules_to_tfstate.py for CLI usage
"""

import json
import subprocess
import sys
import re
import time
import glob
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
    """Extract socket sites, WAN interfaces, and network ranges from the sites data"""
    sites = []
    lan_interfaces = []
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
            
            # Transform native_range data
            native_range = {
                'native_network_range': site.get('native_network_range', ''),
                'local_ip': site.get('local_ip', ''),
                'translated_subnet': site.get('translated_subnet', ''),
                'native_network_range_id': site.get('native_network_range_id', '')
            }
            
            # Handle dhcp_settings - ensure it's a proper object with required fields
            dhcp_settings = site.get('dhcp_settings')
            if dhcp_settings and isinstance(dhcp_settings, dict) and dhcp_settings.get('dhcp_type'):
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
                'connection_type': site.get('connectionType', ''),
                'site_type': site.get('type', ''),
                'site_location': transformed_location,
                'native_range': native_range
            })
        
        # Extract WAN interfaces for this site
        for wan_interface in site.get('wan_interfaces', []):
            if wan_interface.get('id') and wan_interface.get('name'):
                wan_interfaces.append({
                    'site_id': site['id'],
                    'site_name': site['name'],
                    'interface_id': wan_interface['id'],
                    'name': wan_interface['name'],
                    'upstream_bandwidth': wan_interface.get('upstreamBandwidth', 25),
                    'downstream_bandwidth': wan_interface.get('downstreamBandwidth', 25),
                    'dest_type': wan_interface.get('destType', 'CATO'),
                    'role': wan_interface.get('id', 'wan_1'),  # Use interface ID as role
                    'precedence': 'ACTIVE'
                })
        
        # Extract network ranges for this site
        for lan_interface in site.get('lan_interfaces', []):
            interface_id = lan_interface.get('id', '')
            interface_name = lan_interface.get('name', '')
            lan_interfaces.append({
                'site_id': site['id'],
                'interface_id': lan_interface['id'],
                'name': lan_interface['name'],
                'dest_type': lan_interface.get('destType', 'CATO'),
                'subnet': lan_interface.get('subnet', ''),
                'local_ip': lan_interface.get('local_ip', ''),
            })
            
            for network_range in lan_interface.get('network_ranges', []):
                if network_range.get('id') and network_range.get('subnet'):
                    network_ranges.append({
                        'site_id': site['id'],
                        'site_name': site['name'],
                        'interface_id': interface_id,
                        'interface_name': interface_name,
                        'network_range_id': network_range['id'],
                        'name': network_range.get('rangeName', ''),
                        'subnet': network_range['subnet'],
                        'vlan_tag': network_range.get('vlanTag', ''),
                        'range_type': 'VLAN' if network_range.get('vlanTag') and network_range.get('vlanTag') != '' else 'Native',
                        'microsegmentation': network_range.get('microsegmentation', False)
                    })
    
    return sites, wan_interfaces, network_ranges


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


def find_rule_index(rules, rule_name):
    """Find rule index by name."""
    for index, rule in enumerate(rules):
        if rule['name'] == rule_name:
            return index
    return None


def import_sections(sections, module_name, resource_type,
                    resource_name="sections", verbose=False):
    """Import all sections"""
    print("\nStarting section imports...")
    total_sections = len(sections)
    successful_imports = 0
    failed_imports = 0
    
    for i, section in enumerate(sections):
        section_id = section['section_id']
        section_name = section['section_name']
        section_index = section['section_index']
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{section_name}"]'
        print(f"\n[{i+1}/{total_sections}] Section: {section_name} (index: {section_index})")

        # For sections, we use the section name as the ID since that's how Cato identifies them
        success, stdout, stderr = run_terraform_import(resource_address, section_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
    
    print(f"\nSection Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_rules(rules, module_name, verbose=False,
                resource_type="cato_if_rule", resource_name="rules",
                batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all rules in batches"""
    print("\nStarting rule imports...")
    successful_imports = 0
    failed_imports = 0
    total_rules = len(rules)
    
    for i, rule in enumerate(rules):
        rule_id = rule['id']
        rule_name = rule['name']
        rule_index = find_rule_index(rules, rule_name)
        terraform_key = sanitize_name_for_terraform(rule_name)
        
        # Use array index syntax instead of rule ID
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(rule_name)}"]'
        print(f"\n[{i+1}/{total_rules}] Rule: {rule_name} (index: {rule_index})")
        
        success, stdout, stderr = run_terraform_import(resource_address, rule_id, verbose=verbose)
        
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
        if (i + 1) % batch_size == 0 and i < total_rules - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\n Rule Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_if_rules_to_tf(args, configuration):
    """Main function to orchestrate the import process"""
    try:
        print(" Terraform Import Tool - Cato IFW Rules & Sections")
        print("=" * 60)
        
        # Load data
        print(f" Loading data from {args.json_file}...")
        policy_data = load_json_data(args.json_file)
        
        # Extract rules and sections
        rules, sections = extract_rules_and_sections(policy_data)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"section_ids: {json.dumps(policy_data.get('section_ids', {}), indent=2)}")
        
        print(f" Found {len(rules)} rules")
        print(f"  Found {len(sections)} sections")
        
        if not rules and not sections:
            print(" No rules or sections found. Exiting.")
            return [{"success": False, "error": "No rules or sections found"}]
        
        # Validate Terraform environment before proceeding
        validate_terraform_environment(args.module_name, verbose=args.verbose)
        
        # Ask for confirmation (unless auto-approved)
        if not args.rules_only and not args.sections_only:
            print(f"\n Ready to import {len(sections)} sections and {len(rules)} rules.")
        elif args.rules_only:
            print(f"\n Ready to import {len(rules)} rules only.")
        elif args.sections_only:
            print(f"\n Ready to import {len(sections)} sections only.")
        
        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]
        
        total_successful = 0
        total_failed = 0
        
        # Import sections first (if not skipped)
        if not args.rules_only and sections:
            successful, failed = import_sections(sections, module_name=args.module_name, resource_type="cato_if_section", verbose=args.verbose)
            total_successful += successful
            total_failed += failed
        
        # Import rules (if not skipped)
        if not args.sections_only and rules:
            successful, failed = import_rules(rules, module_name=args.module_name, 
                                            verbose=args.verbose, batch_size=args.batch_size, 
                                            delay_between_batches=args.delay,
                                            auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Final summary
        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
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
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def load_wf_json_data(json_file):
    """Load WAN Firewall data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['wanFirewall']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def import_wf_sections(sections, module_name, verbose=False,
                      resource_type="cato_wf_section", resource_name="sections"):
    """Import all WAN Firewall sections"""
    print("\nStarting WAN Firewall section imports...")
    total_sections = len(sections)
    successful_imports = 0
    failed_imports = 0
    
    for i, section in enumerate(sections):
        section_id = section['section_id']
        section_name = section['section_name']
        section_index = section['section_index']
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{section_name}"]'
        print(f"\n[{i+1}/{total_sections}] Section: {section_name} (index: {section_index})")

        # For sections, we use the section name as the ID since that's how Cato identifies them
        success, stdout, stderr = run_terraform_import(resource_address, section_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
    
    print(f"\nWAN Firewall Section Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_wf_rules(rules, module_name, verbose=False,
                   resource_type="cato_wf_rule", resource_name="rules",
                   batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all WAN Firewall rules in batches"""
    print("\nStarting WAN Firewall rule imports...")
    successful_imports = 0
    failed_imports = 0
    total_rules = len(rules)
    
    for i, rule in enumerate(rules):
        rule_id = rule['id']
        rule_name = rule['name']
        rule_index = find_rule_index(rules, rule_name)
        terraform_key = sanitize_name_for_terraform(rule_name)
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'

        # Use array index syntax instead of rule ID
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(rule_name)}"]'
        print(f"\n[{i+1}/{total_rules}] Rule: {rule_name} (index: {rule_index})")
        
        success, stdout, stderr = run_terraform_import(resource_address, rule_id, verbose=verbose)
        
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
        if (i + 1) % batch_size == 0 and i < total_rules - 1:
            print(f"\n   Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nWAN Firewall Rule Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_wf_rules_to_tf(args, configuration):
    """Main function to orchestrate the WAN Firewall import process"""
    try:
        print(" Terraform Import Tool - Cato WF Rules & Sections")
        print("=" * 60)
        
        # Load data
        print(f" Loading data from {args.json_file}...")
        policy_data = load_wf_json_data(args.json_file)
        
        # Extract rules and sections
        rules, sections = extract_rules_and_sections(policy_data)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"section_ids: {json.dumps(policy_data.get('section_ids', {}), indent=2)}")
        
        print(f" Found {len(rules)} rules")
        print(f"  Found {len(sections)} sections")
        
        if not rules and not sections:
            print(" No rules or sections found. Exiting.")
            return [{"success": False, "error": "No rules or sections found"}]
        
        # Add module. prefix if not present
        module_name = args.module_name
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)
        
        # Ask for confirmation (unless auto-approved)
        if not args.rules_only and not args.sections_only:
            print(f"\n Ready to import {len(sections)} sections and {len(rules)} rules.")
        elif args.rules_only:
            print(f"\n Ready to import {len(rules)} rules only.")
        elif args.sections_only:
            print(f"\n Ready to import {len(sections)} sections only.")
        
        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]
        
        total_successful = 0
        total_failed = 0
        
        # Import sections first (if not skipped)
        if not args.rules_only and sections:
            successful, failed = import_wf_sections(sections, module_name=args.module_name, verbose=args.verbose)
            total_successful += successful
            total_failed += failed
        
        # Import rules (if not skipped)
        if not args.sections_only and rules:
            successful, failed = import_wf_rules(rules, module_name=args.module_name, 
                                                verbose=args.verbose, batch_size=args.batch_size, 
                                                delay_between_batches=args.delay,
                                                auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Final summary
        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
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
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


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
                         resource_type="cato_wan_interface", resource_name="wan_interfaces",
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
        
        # Use correct resource addressing for WAN interfaces
        # WAN interfaces use the interface role as the key
        wan_role = interface['role']
        resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_wan_interface.wan["{wan_role}"]'
        
        # WAN interface import needs site_id:interface_id format
        # Check if interface_id is already in the correct format (contains ':')
        if ':' in interface_id:
            import_id = interface_id  # Already in correct format
        else:
            import_id = f"{site_id}:{interface_id}"  # Need to add site_id
        print(f"\n[{i+1}/{total_interfaces}] WAN Interface: {interface_name} on {site_name} (ID: {import_id})")
        
        success, stdout, stderr = run_terraform_import(resource_address, import_id, verbose=verbose)
        
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
        if (i + 1) % batch_size == 0 and i < total_interfaces - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nWAN Interface Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_lan_interfaces(lan_interfaces, module_name, verbose=False,
                         resource_type="cato_lan_interface", resource_name="lan_interfaces",
                         batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all WAN interfaces in batches"""
    print("\nStarting WAN interface imports...")
    successful_imports = 0
    failed_imports = 0
    total_interfaces = len(lan_interfaces)

    for i, interface in enumerate(lan_interfaces):
        site_id = interface['site_id']
        interface_id = interface['id']
        interface_index = interface['index']
        interface_name = interface['name']
        site_name = interface['site_name']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Use correct resource addressing for WAN interfaces
        # WAN interfaces use the interface role as the key
        lan_role = interface['role']
        resource_address = f'{module_name}.module.socket-site["{site_name}"].cato_lan_interface.lan["{interface_index}"]'

        print(f"\n[{i+1}/{total_interfaces}] LAN Interface: {interface_name} on {site_name} (ID: {interface_id})")

        success, stdout, stderr = run_terraform_import(resource_address, interface_id, verbose=verbose)
        
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
        if (i + 1) % batch_size == 0 and i < total_interfaces - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\nWAN Interface Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_network_ranges(network_ranges, module_name, verbose=False,
                         resource_type="cato_network_range", resource_name="network_ranges",
                         batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all network ranges in batches"""
    print("\nStarting network range imports...")
    successful_imports = 0
    failed_imports = 0
    total_ranges = len(network_ranges)
    
    for i, network_range in enumerate(network_ranges):
        network_range_id = network_range['network_range_id']
        range_name = network_range['name']
        site_name = network_range['site_name']
        subnet = network_range['subnet']
        
        # Add module. prefix if not present
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        
        # Use correct resource addressing for network ranges
        # Based on terraform plan output, network ranges are structured as:
        # module.sites.module.socket-site["site_name"].module.lan_interfaces["interface_id"].module.network_range["subnet"].cato_network_range.no_dhcp[0]
        interface_id = network_range['interface_id']
        # Convert interface_id to the format used in terraform (e.g., "161570" -> "INT_5")
        if interface_id.isdigit():
            # This is a numeric interface ID, need to convert to INT_X format
            # For now, we'll use the interface_id as is and let terraform handle the mapping
            terraform_interface_id = interface_id
        else:
            terraform_interface_id = interface_id
        
        resource_address = f'{module_name}.module.socket-site["{site_name}"].module.lan_interfaces["{terraform_interface_id}"].module.network_range["{network_range_id}"].cato_network_range.no_dhcp[0]'
        
        print(f"\n[{i+1}/{total_ranges}] Network Range: {range_name} - {subnet} ({network_range_id}) on {site_name} (ID: {network_range_id})")
        
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
        
        # Load data
        print(f" Loading data from {args.json_file}...")
        sites_data = load_json_data(args.json_file)
        
        # Extract sites, WAN interfaces, and network ranges
        sites, wan_interfaces, network_ranges = extract_socket_sites_data(sites_data)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"\nExtracted data summary:")
            print(f"  Sites: {len(sites)}")
            print(f"  WAN Interfaces: {len(wan_interfaces)}")
            print(f"  Network Ranges: {len(network_ranges)}")
        
        print(f" Found {len(sites)} sites")
        print(f" Found {len(wan_interfaces)} WAN interfaces")
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
        import_summary = []
        if not args.sites_only and not args.interfaces_only and not args.network_ranges_only:
            import_summary.append(f"{len(sites)} sites")
            import_summary.append(f"{len(wan_interfaces)} WAN interfaces")
            import_summary.append(f"{len(network_ranges)} network ranges")
        elif args.sites_only:
            import_summary.append(f"{len(sites)} sites only")
        elif args.lan_interfaces_only:
            import_summary.append(f"{len(lan_interfaces)} LAN interfaces only")
        elif args.network_ranges_only:
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
        
        # Import sites first (if not skipped)
        if not args.interfaces_only and not args.network_ranges_only and sites:
            successful, failed = import_socket_sites(sites, module_name=args.module_name, 
                                                   verbose=args.verbose, batch_size=args.batch_size, 
                                                   delay_between_batches=args.delay,
                                                   auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Import WAN interfaces (if not skipped)
        if not args.sites_only and not args.network_ranges_only and wan_interfaces:
            successful, failed = import_wan_interfaces(wan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=args.batch_size, 
                                                      delay_between_batches=args.delay,
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed

        # Import LAN interfaces (if not skipped)
        if not args.sites_only and not args.network_ranges_only and lan_interfaces:
            successful, failed = import_lan_interfaces(lan_interfaces, module_name=args.module_name, 
                                                      verbose=args.verbose, batch_size=args.batch_size, 
                                                      delay_between_batches=args.delay,
                                                      auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
     
        # Import network ranges (if not skipped)
        if not args.sites_only and not args.interfaces_only and network_ranges:
            successful, failed = import_network_ranges(network_ranges, module_name=args.module_name, 
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
