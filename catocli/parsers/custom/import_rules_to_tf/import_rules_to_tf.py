#!/usr/bin/env python3
"""
Direct Terraform Import Script using Python
Imports firewall rules and sections directly using subprocess calls to terraform import
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
    """Load firewall data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['internetFirewall']['policy']
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


def extract_rules_and_sections(policy_data):
    """Extract rules and sections from the policy data"""
    rules = []
    sections = []
    
    # Extract rules
    for rule_entry in policy_data.get('rules', []):
        rule = rule_entry.get('rule', {})
        if rule.get('id') and rule.get('name'):
            rules.append({
                'id': rule['id'],
                'name': rule['name'],
                'index': rule.get('index', 0),
                'section_name': rule.get('section', {}).get('name', 'Default')
            })
    
    # Extract sections
    for section in policy_data.get('sections', []):
        if section.get('section_name'):
            sections.append({
                'section_name': section['section_name'],
                'section_index': section.get('section_index', 0),
                'section_id': section.get('section_id', '')
            })
    return rules, sections


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
    
    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
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
    
    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]
