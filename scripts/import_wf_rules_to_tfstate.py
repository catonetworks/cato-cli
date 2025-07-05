#!/usr/bin/env python3
"""
Direct Terraform Import Script using Python
Imports firewall rules and sections directly using subprocess calls to terraform import
Reads from JSON structure exported from Cato API
"""

import json
import subprocess
import sys
import re
import time
import argparse
import os
import glob
from pathlib import Path

def load_json_data(json_file):
    """Load firewall data from JSON file"""
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

def check_terraform_initialized(dest_dir):
    """Check if Terraform is initialized in the destination directory"""
    terraform_dir = os.path.join(dest_dir, '.terraform')
    if not os.path.exists(terraform_dir):
        return False, "Terraform directory '.terraform' not found"
    
    # Check for terraform.tfstate or .terraform.lock.hcl
    state_file = os.path.join(dest_dir, 'terraform.tfstate')
    lock_file = os.path.join(dest_dir, '.terraform.lock.hcl')
    
    if not os.path.exists(state_file) and not os.path.exists(lock_file):
        return False, "No terraform state or lock file found"
    
    return True, "Terraform appears to be initialized"

def validate_module_in_tf_files(dest_dir, module_name):
    """Validate that the specified module name exists in .tf files"""
    tf_files = glob.glob(os.path.join(dest_dir, '*.tf'))
    
    if not tf_files:
        return False, "No .tf files found in destination directory"
    
    module_found = False
    files_checked = []
    
    for tf_file in tf_files:
        files_checked.append(os.path.basename(tf_file))
        try:
            with open(tf_file, 'r') as f:
                content = f.read()
                # Look for the module name in various forms
                patterns = [
                    rf'module\s+"{module_name.split(".")[-1]}"',  # module "if_rules"
                    rf'module\s+{module_name.split(".")[-1]}\s+{{',  # module if_rules {
                    rf'{re.escape(module_name)}',  # exact match module.if_rules
                ]
                
                for pattern in patterns:
                    if re.search(pattern, content, re.MULTILINE):
                        module_found = True
                        break
                        
                if module_found:
                    break
        except Exception as e:
            print(f"Warning: Could not read {tf_file}: {e}")
    
    if module_found:
        return True, f"Module '{module_name}' found in Terraform files"
    else:
        return False, f"Module '{module_name}' not found in files: {', '.join(files_checked)}"

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
    print("section_ids",json.dumps(section_ids, indent=2))
    for section in policy_data.get('sections', []):
        if section.get('section_name'):
            sections.append({
                'section_name': section['section_name'],
                'section_index': section.get('section_index', 0),
                'section_id': section_ids.get(section['section_name'], '')
            })  
    return rules, sections

def run_terraform_import(resource_address, resource_id, dest_dir=None, timeout=60):
    """
    Run a single terraform import command
    
    Args:
        resource_address: The terraform resource address
        resource_id: The actual resource ID to import
        timeout: Command timeout in seconds
    
    Returns:
        tuple: (success: bool, output: str, error: str)
    """
    cmd = ['terraform', 'import', resource_address, resource_id]
    print(f"🔧 Command: {' '.join(cmd)}")
    
    try:
        print(f"Importing: {resource_address} <- {resource_id}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=dest_dir if dest_dir else Path.cwd()
        )
        
        if result.returncode == 0:
            print(f"✅ Success: {resource_address}")
            return True, result.stdout, result.stderr
        else:
            print(f"❌ Failed: {resource_address}")
            print(f"Error: {result.stderr}")
            return False, result.stdout, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout: {resource_address} (exceeded {timeout}s)")
        return False, "", f"Command timed out after {timeout} seconds"
    except Exception as e:
        print(f"❌ Unexpected error for {resource_address}: {e}")
        return False, "", str(e)

def find_rule_index(rules, rule_name):
    """Find rule index by name."""
    for index, rule in enumerate(rules):
        if rule['name'] == rule_name:
            return index
    return None

def import_sections(sections, dest_dir, module_name="module.wf_rules", 
                   resource_type="cato_wf_section", resource_name="sections"):
    """Import all sections"""
    print("\n🗂️  Starting section imports...")
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
        success, stdout, stderr = run_terraform_import(resource_address, section_id, dest_dir)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
    
    print(f"\n📊 Section Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def import_rules(rules, dest_dir, module_name="module.wf_rules", 
                resource_type="cato_wf_rule", resource_name="rules",
                batch_size=10, delay_between_batches=2):
    """Import all rules in batches"""
    print("\n📋 Starting rule imports...")
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
        
        success, stdout, stderr = run_terraform_import(resource_address, rule_id, dest_dir)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
            
            # Ask user if they want to continue on failure
            if failed_imports <= 3:  # Only prompt for first few failures
                response = input(f"\nContinue with remaining imports? (y/n): ").lower()
                if response == 'n':
                    print("Import process stopped by user.")
                    break
        
        # Delay between batches
        if (i + 1) % batch_size == 0 and i < total_rules - 1:
            print(f"\n⏸️  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)
    
    print(f"\n📊 Rule Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports

def main():
    """Main function to orchestrate the import process"""
    parser = argparse.ArgumentParser(description='Import Cato WF rules and sections to Terraform state')
    parser.add_argument('json_file', help='Path to the JSON file containing WF rules and sections')
    parser.add_argument('--module-name', required=True, default='module.wf_rules', 
                        help='Terraform module name to import resources into (default: module.wf_rules)')
    parser.add_argument('--batch-size', type=int, default=10, help='Number of imports per batch (default: 10)')
    parser.add_argument('--dest-dir', required=True, help='Destination directory for Terraform state')
    parser.add_argument('--delay', type=int, default=2, help='Delay between batches in seconds (default: 2)')
    parser.add_argument('--rules-only', action='store_true', help='Import only rules, skip sections')
    parser.add_argument('--sections-only', action='store_true', help='Import only sections, skip rules')
    
    args = parser.parse_args()
    
    print("🔧 Terraform Import Tool - Cato WF Rules & Sections")
    print("=" * 60)
    
    # Verify destination directory
    if not os.path.isdir(args.dest_dir):
        print(f"Error: Destination directory '{args.dest_dir}' does not exist.")
        sys.exit(1)

    # Check if Terraform is initialized in the destination directory
    print(f"🔍 Checking Terraform initialization in {args.dest_dir}...")
    tf_initialized, tf_message = check_terraform_initialized(args.dest_dir)
    if not tf_initialized:
        print(f"❌ Error: {tf_message}")
        print("Please run 'terraform init' in the destination directory first.")
        sys.exit(1)
    print(f"✅ {tf_message}")
    
    # Validate module name exists in .tf files
    print(f"🔍 Validating module '{args.module_name}' exists in Terraform files...")
    module_valid, module_message = validate_module_in_tf_files(args.dest_dir, args.module_name)
    if not module_valid:
        print(f"❌ Error: {module_message}")
        print(f"Please ensure the module '{args.module_name}' is defined in your .tf files.")
        sys.exit(1)
    print(f"✅ {module_message}")

    # Load data
    print(f"📂 Loading data from {args.json_file}...")
    policy_data = load_json_data(args.json_file)
    
    # Extract rules and sections
    rules, sections = extract_rules_and_sections(policy_data)
    
    print(f"📄 Found {len(rules)} rules")
    print(f"🗂️  Found {len(sections)} sections")
    
    if not rules and not sections:
        print("❌ No rules or sections found. Exiting.")
        sys.exit(1)
    
    # Ask for confirmation
    if not args.rules_only and not args.sections_only:
        print(f"\n🎯 Ready to import {len(sections)} sections and {len(rules)} rules.")
    elif args.rules_only:
        print(f"\n🎯 Ready to import {len(rules)} rules only.")
    elif args.sections_only:
        print(f"\n🎯 Ready to import {len(sections)} sections only.")
    
    confirm = input(f"\nProceed with import? (y/n): ").lower()
    if confirm != 'y':
        print("Import cancelled.")
        sys.exit(0)
    
    total_successful = 0
    total_failed = 0
    
    # Import sections first (if not skipped)
    if not args.rules_only and sections:
        successful, failed = import_sections(sections, args.dest_dir, module_name=args.module_name)
        total_successful += successful
        total_failed += failed
    
    # Import rules (if not skipped)
    if not args.sections_only and rules:
        successful, failed = import_rules(rules, args.dest_dir, module_name=args.module_name, batch_size=args.batch_size, delay_between_batches=args.delay)
        total_successful += successful
        total_failed += failed
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL IMPORT SUMMARY")
    print("=" * 60)
    print(f"✅ Total successful imports: {total_successful}")
    print(f"❌ Total failed imports: {total_failed}")
    print(f"📈 Overall success rate: {(total_successful / (total_successful + total_failed) * 100):.1f}%" if (total_successful + total_failed) > 0 else "N/A")
    print("\n🎉 Import process completed!")

if __name__ == "__main__":
    main()
