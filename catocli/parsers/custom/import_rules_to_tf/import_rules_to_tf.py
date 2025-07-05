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
    section_ids = policy_data.get('section_ids', {})
    for section in policy_data.get('sections', []):
        if section.get('section_name'):
            sections.append({
                'section_name': section['section_name'],
                'section_index': section.get('section_index', 0),
                'section_id': section_ids.get(section['section_name'], '')
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


def import_sections(sections, module_name, verbose=False,
                   resource_type="cato_if_section", resource_name="sections"):
    """Import all sections"""
    print("\nStarting section imports...")
    total_sections = len(sections)
    successful_imports = 0
    failed_imports = 0
    
    for i, section in enumerate(sections):
        section_id = section['section_id']
        section_name = section['section_name']
        section_index = section['section_index']
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(section_index)}"]'
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
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(rule_index)}"]'
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


def check_terraform_binary():
    """Check if terraform binary is available"""
    try:
        result = subprocess.run(['terraform', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip().split('\n')[0]
        else:
            return False, "Terraform binary not found or not working"
    except FileNotFoundError:
        return False, "Terraform binary not found in PATH"
    except Exception as e:
        return False, f"Error checking terraform binary: {e}"


def check_terraform_config_files():
    """Check if Terraform configuration files exist in current directory"""
    tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
    if tf_files:
        return True, tf_files
    else:
        return False, []


def check_terraform_init():
    """Check if Terraform has been initialized"""
    terraform_dir = Path('.terraform')
    if terraform_dir.exists() and terraform_dir.is_dir():
        # Check for providers
        providers_dir = terraform_dir / 'providers'
        if providers_dir.exists():
            return True, "Terraform is initialized"
        else:
            return False, "Terraform directory exists but no providers found"
    else:
        return False, "Terraform not initialized (.terraform directory not found)"


def check_module_exists(module_name):
    """Check if the specified module exists in Terraform configuration"""
    try:
        # Remove 'module.' prefix if present
        clean_module_name = module_name.replace('module.', '')
        
        # Method 1: Check .tf files directly for module definitions
        tf_files = glob.glob('*.tf') + glob.glob('*.tf.json')
        for tf_file in tf_files:
            try:
                with open(tf_file, 'r') as f:
                    content = f.read()
                    # Look for module "module_name" blocks
                    if f'module "{clean_module_name}"' in content or f"module '{clean_module_name}'" in content:
                        return True, f"Module '{clean_module_name}' found in {tf_file}"
            except Exception as e:
                print(f"Warning: Could not read {tf_file}: {e}")
                continue
        
        # Method 2: Try terraform show -json as fallback
        try:
            result = subprocess.run(
                ['terraform', 'show', '-json'],
                capture_output=True,
                text=True,
                cwd=Path.cwd()
            )
            
            if result.returncode == 0:
                state_data = json.loads(result.stdout)
                
                # Check if module exists in configuration
                if 'configuration' in state_data and state_data['configuration']:
                    modules = state_data.get('configuration', {}).get('root_module', {}).get('module_calls', {})
                    if clean_module_name in modules:
                        return True, f"Module '{clean_module_name}' found in Terraform state"
                
                # Also check in planned_values for modules
                if 'planned_values' in state_data and state_data['planned_values']:
                    modules = state_data.get('planned_values', {}).get('root_module', {}).get('child_modules', [])
                    for module in modules:
                        module_addr = module.get('address', '')
                        if clean_module_name in module_addr:
                            return True, f"Module '{clean_module_name}' found in planned values"
        except (subprocess.SubprocessError, json.JSONDecodeError) as e:
            print(f"Warning: Could not check terraform state: {e}")
        
        return False, f"Module '{clean_module_name}' not found in Terraform configuration files"
            
    except Exception as e:
        return False, f"Error checking module existence: {e}"


def validate_terraform_environment(module_name, verbose=False):
    """Validate the complete Terraform environment"""
    print("\n Validating Terraform environment...")
    
    # 1. Check terraform binary
    print("\n Checking Terraform binary...")
    has_terraform, terraform_msg = check_terraform_binary()
    if not has_terraform:
        raise Exception(f" Terraform not available: {terraform_msg}")
    if verbose:
        print(f" {terraform_msg}")
    else:
        print(" Terraform binary found")
    
    # 2. Check for configuration files
    print("\n Checking Terraform configuration files...")
    has_config, config_files = check_terraform_config_files()
    if not has_config:
        raise Exception(" No Terraform configuration files (.tf or .tf.json) found in current directory")
    if verbose:
        print(f" Found {len(config_files)} configuration files: {', '.join(config_files)}")
    else:
        print(f" Found {len(config_files)} Terraform configuration files")
    
    # 3. Check if terraform is initialized
    print("\n Checking Terraform initialization...")
    is_initialized, init_msg = check_terraform_init()
    if not is_initialized:
        raise Exception(f" {init_msg}. Run 'terraform init' first.")
    if verbose:
        print(f" {init_msg}")
    else:
        print(" Terraform is initialized")
    
    # 4. Check if the specified module exists
    print(f"\n Checking if module '{module_name}' exists...")
    module_exists, module_msg = check_module_exists(module_name)
    if not module_exists:
        raise Exception(f" {module_msg}. Please add the module to your Terraform configuration first.")
    if verbose:
        print(f" {module_msg}")
    else:
        print(f" Module '{module_name}' found")
    
    print("\n All Terraform environment checks passed!")


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
            successful, failed = import_sections(sections, module_name=args.module_name, verbose=args.verbose)
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
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(section_index)}"]'
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
        
        # Use array index syntax instead of rule ID
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{str(rule_index)}"]'
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
