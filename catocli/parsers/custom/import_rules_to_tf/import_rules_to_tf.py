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


def extract_if_rules_resources(policy_data):
    """Extract if_rules resources from the policy data, sub-policy aware.

    Splits sections/rules into main vs. sub (keyed off `sub_policy_name`) and
    also pulls out `sub_policies[]`. Legacy JSON (no `sub_policy_name` on any
    row, no `sub_policies` key) produces exactly `main_rules`/`main_sections`
    equal to what extract_rules_and_sections() would - empty sub_rules/
    sub_sections/sub_policies - so the legacy behavior is unchanged.

    Returns a dict: {main_rules, sub_rules, main_sections, sub_sections, sub_policies}
    """
    main_rules = []
    sub_rules = []
    for rule_entry in policy_data.get('rules', []):
        rule = rule_entry.get('rule', {})
        if not (rule.get('id') and rule.get('name')):
            continue
        entry = {
            'id': rule['id'],
            'name': rule['name'],
            'index': rule.get('index', 0),
            'section_name': rule.get('section', {}).get('name', 'Default')
        }
        sub_policy_name = rule_entry.get('sub_policy_name')
        if sub_policy_name:
            entry['sub_policy_name'] = sub_policy_name
            sub_rules.append(entry)
        else:
            main_rules.append(entry)

    main_sections = []
    sub_sections = []
    for section in policy_data.get('sections', []):
        if not section.get('section_name'):
            continue
        entry = {
            'section_name': section['section_name'],
            'section_index': section.get('section_index', 0),
            'section_id': section.get('section_id', '')
        }
        sub_policy_name = section.get('sub_policy_name')
        if sub_policy_name:
            entry['sub_policy_name'] = sub_policy_name
            sub_sections.append(entry)
        else:
            main_sections.append(entry)

    sub_policies = []
    for sp in policy_data.get('sub_policies', []) or []:
        if sp.get('sub_policy_name') and sp.get('sub_policy_id'):
            entry = {
                'sub_policy_name': sp['sub_policy_name'],
                'sub_policy_id': sp['sub_policy_id']
            }
            # The cleanup rule is embedded in the sub-policy (the API auto-creates
            # it; cato_if_sub_policy manages it as part of the resource). It is
            # NOT imported separately: importing the sub-policy id brings it into
            # state via the provider's last-rule lookup on the first refresh.
            cleanup = sp.get('cleanup_rule') or {}
            cleanup_rule = cleanup.get('rule') or {}
            if cleanup_rule.get('name'):
                entry['cleanup_rule_name'] = cleanup_rule['name']
                entry['cleanup_rule_id'] = cleanup_rule.get('id', '')
            sub_policies.append(entry)

    return {
        'main_rules': main_rules,
        'sub_rules': sub_rules,
        'main_sections': main_sections,
        'sub_sections': sub_sections,
        'sub_policies': sub_policies,
    }


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


# ---------------------------------------------------------------------------
# if_rules-specific: non-blocking import classification.
#
# Terraform import is run per-resource; a single failure must never abort the
# whole job (this makes `catocli import if_rules_to_tf` safely re-runnable:
# a second run reports everything as "already imported" and still exits 0).
# We classify the (already-separate) run_terraform_import() failure by its
# stderr text into one of three buckets:
#   - already_managed: the resource is already in local Terraform state.
#   - not_found:        the id doesn't exist in the live tenant anymore.
#   - other:            anything else (treated as a non-fatal warning).
# This only affects the if_rules import path; run_terraform_import() itself
# (shared with wf/wnw/tls) is untouched.
# ---------------------------------------------------------------------------
ALREADY_MANAGED_MARKERS = (
    "already managed by terraform",
    "already exists in state",
    "resource already managed",
)
NOT_FOUND_MARKERS = (
    "cannot import non-existent remote object",
    "non-existent remote object",
    "could not be found",
    "no matching resource found",
)


def classify_import_failure(stderr):
    """Classify a failed `terraform import` by its stderr text.

    Returns one of: 'already_managed', 'not_found', 'other'.
    """
    text = (stderr or "").lower()
    if any(marker in text for marker in ALREADY_MANAGED_MARKERS):
        return "already_managed"
    if any(marker in text for marker in NOT_FOUND_MARKERS):
        return "not_found"
    return "other"


def ensure_module_prefix(module_name):
    """Add the `module.` auto-prefix if missing (wf/wnw/tls already do this;
    if_rules was missing it - this fixes that inconsistency)."""
    if module_name and not module_name.startswith('module.'):
        return f'module.{module_name}'
    return module_name


def import_sections(sections, module_name, resource_type,
                    resource_name="sections", verbose=False):
    """Import all sections (if_rules path). Non-blocking: a failed import is
    classified and reported, but never stops the run."""
    module_name = ensure_module_prefix(module_name)
    print("\nStarting section imports...")
    total_sections = len(sections)
    tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}

    for i, section in enumerate(sections):
        section_id = section['section_id']
        section_name = section['section_name']
        section_index = section['section_index']
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{section_name}"]'
        print(f"\n[{i+1}/{total_sections}] Section: {section_name} (index: {section_index})")

        if not section_id:
            # Synthetic greenfield section (e.g. "Corporate Rules" emitted by the
            # exporter for single-section tenants) - nothing to import; terraform
            # creates it on first apply.
            print(f"SKIP (no live id - greenfield section, created on apply): {resource_address}")
            tally["not_found"] += 1
            continue

        # For sections, we use the section name as the ID since that's how Cato identifies them
        success, stdout, stderr = run_terraform_import(resource_address, section_id, verbose=verbose)

        if success:
            tally["imported"] += 1
        else:
            kind = classify_import_failure(stderr)
            if kind == "already_managed":
                print(f"SKIP (already imported): {resource_address}")
            elif kind == "not_found":
                print(f"SKIP (not found in tenant): {resource_address} (id {section_id})")
            else:
                print(f"WARNING: import failed for {resource_address}: {stderr.strip() if stderr else 'unknown error'}")
            tally[kind] += 1

    print(f"\nSection Import Summary: {tally['imported']} imported, "
          f"{tally['already_managed']} already-imported, {tally['not_found']} not-found, "
          f"{tally['other']} other failures")
    return tally


def import_rules(rules, module_name, verbose=False,
                resource_type="cato_if_rule", resource_name="rules",
                batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all rules in batches (if_rules path). Non-blocking: failures
    are classified and reported, never stop the run or prompt the user."""
    module_name = ensure_module_prefix(module_name)
    print("\nStarting rule imports...")
    tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}
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
            tally["imported"] += 1
        else:
            kind = classify_import_failure(stderr)
            if kind == "already_managed":
                print(f"SKIP (already imported): {resource_address}")
            elif kind == "not_found":
                print(f"SKIP (not found in tenant): {resource_address} (id {rule_id})")
            else:
                print(f"WARNING: import failed for {resource_address}: {stderr.strip() if stderr else 'unknown error'}")
            tally[kind] += 1
            # Non-blocking: no more "continue? y/n" prompt after N failures.

        # Delay between batches
        if (i + 1) % batch_size == 0 and i < total_rules - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)

    print(f"\n Rule Import Summary: {tally['imported']} imported, "
          f"{tally['already_managed']} already-imported, {tally['not_found']} not-found, "
          f"{tally['other']} other failures")
    return tally


def import_sub_policies(sub_policies, module_name, verbose=False,
                        resource_type="cato_if_sub_policy", resource_name="sub_policies"):
    """Import all sub-policies (if_rules path only). Non-blocking."""
    module_name = ensure_module_prefix(module_name)
    print("\nStarting sub-policy imports...")
    total = len(sub_policies)
    tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}

    for i, sp in enumerate(sub_policies):
        sub_policy_id = sp['sub_policy_id']
        sub_policy_name = sp['sub_policy_name']
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{sub_policy_name}"]'
        print(f"\n[{i+1}/{total}] Sub-policy: {sub_policy_name}")
        if sp.get('cleanup_rule_name'):
            print(f"    includes embedded cleanup rule: {sp['cleanup_rule_name']}"
                  f" (id {sp.get('cleanup_rule_id', '') or 'n/a'}) - imported with the sub-policy,"
                  f" hydrated into state on first refresh")

        success, stdout, stderr = run_terraform_import(resource_address, sub_policy_id, verbose=verbose)

        if success:
            tally["imported"] += 1
        else:
            kind = classify_import_failure(stderr)
            if kind == "already_managed":
                print(f"SKIP (already imported): {resource_address}")
            elif kind == "not_found":
                print(f"SKIP (not found in tenant): {resource_address} (id {sub_policy_id})")
            else:
                print(f"WARNING: import failed for {resource_address}: {stderr.strip() if stderr else 'unknown error'}")
            tally[kind] += 1

    print(f"\nSub-policy Import Summary: {tally['imported']} imported, "
          f"{tally['already_managed']} already-imported, {tally['not_found']} not-found, "
          f"{tally['other']} other failures")
    return tally


def import_sub_rules(sub_rules, module_name, verbose=False,
                     resource_type="cato_if_rule", resource_name="sub_rules",
                     batch_size=10, delay_between_batches=2):
    """Import all sub-policy rules (if_rules path only), keyed by
    "<sub_policy_name>::<rule_name>". Non-blocking."""
    module_name = ensure_module_prefix(module_name)
    print("\nStarting sub-rule imports...")
    tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}
    total = len(sub_rules)

    for i, rule in enumerate(sub_rules):
        rule_id = rule['id']
        composite_key = f"{rule['sub_policy_name']}::{rule['name']}"
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{composite_key}"]'
        print(f"\n[{i+1}/{total}] Sub-rule: {composite_key}")

        success, stdout, stderr = run_terraform_import(resource_address, rule_id, verbose=verbose)

        if success:
            tally["imported"] += 1
        else:
            kind = classify_import_failure(stderr)
            if kind == "already_managed":
                print(f"SKIP (already imported): {resource_address}")
            elif kind == "not_found":
                print(f"SKIP (not found in tenant): {resource_address} (id {rule_id})")
            else:
                print(f"WARNING: import failed for {resource_address}: {stderr.strip() if stderr else 'unknown error'}")
            tally[kind] += 1

        if (i + 1) % batch_size == 0 and i < total - 1:
            print(f"\n  Batch complete. Waiting {delay_between_batches}s before next batch...")
            time.sleep(delay_between_batches)

    print(f"\n Sub-rule Import Summary: {tally['imported']} imported, "
          f"{tally['already_managed']} already-imported, {tally['not_found']} not-found, "
          f"{tally['other']} other failures")
    return tally


def print_skipped_sub_sections(sub_sections, module_name, resource_type="cato_if_section"):
    """Sub-sections aren't managed by the module yet (provider gap - see
    docs/ifw-sub-policy-json-design.md). Print a clear SKIP warning instead
    of attempting to import them."""
    module_name = ensure_module_prefix(module_name)
    if not sub_sections:
        return
    print(f"\nSKIP: {len(sub_sections)} sub-section(s) are not yet importable "
          f"(the module has no {resource_type}.sub_sections resource - provider/module gap):")
    for s in sub_sections:
        composite_key = f"{s['sub_policy_name']}::{s['section_name']}"
        resource_address = f'{module_name}.{resource_type}.sub_sections["{composite_key}"]'
        print(f"  - {resource_address}  (id {s['section_id']})")


def merge_tally(total, part):
    for k, v in part.items():
        total[k] = total.get(k, 0) + v
    return total


def import_if_rules_to_tf(args, configuration):
    """Main function to orchestrate the import process (sub-policy aware).

    Non-blocking by design: a per-resource import failure is classified and
    reported but never aborts the job and never prompts the user - running
    this command twice in a row is expected to be idempotent (the second run
    reports everything as already-imported). The command always returns
    success (and the CLI framework always exits 0 for a non-exception
    result - see catocli/Utils/clidriver.py) - the real outcome is the
    printed summary / the counts in the returned dict, not the exit code.
    """
    try:
        print(" Terraform Import Tool - Cato IFW Rules & Sections")
        print("=" * 60)

        # Load data
        print(f" Loading data from {args.json_file}...")
        policy_data = load_json_data(args.json_file)

        # Extract rules/sections, sub-policy aware
        resources = extract_if_rules_resources(policy_data)
        main_rules = resources['main_rules']
        sub_rules = resources['sub_rules']
        main_sections = resources['main_sections']
        sub_sections = resources['sub_sections']
        sub_policies = resources['sub_policies']

        if hasattr(args, 'verbose') and args.verbose:
            print(f"section_ids: {json.dumps(policy_data.get('section_ids', {}), indent=2)}")

        print(f" Found {len(main_rules)} rule(s), {len(sub_rules)} sub-rule(s)")
        print(f"  Found {len(main_sections)} section(s), {len(sub_sections)} sub-section(s)")
        print(f"  Found {len(sub_policies)} sub-policy(ies)")

        if not main_rules and not sub_rules and not main_sections and not sub_sections and not sub_policies:
            print(" No rules or sections found. Exiting.")
            return [{"success": False, "error": "No rules or sections found"}]

        # Add module. prefix if not present (if_rules was missing this,
        # unlike the wf/wnw/tls variants - fixed here).
        module_name = ensure_module_prefix(args.module_name)

        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)

        # Ask for confirmation (unless auto-approved)
        if not args.rules_only and not args.sections_only:
            print(f"\n Ready to import {len(main_sections)} section(s), {len(sub_policies)} sub-policy(ies), "
                  f"{len(main_rules)} rule(s), and {len(sub_rules)} sub-rule(s).")
            if sub_sections:
                print(f" NOTE: {len(sub_sections)} sub-section(s) will be SKIPPED "
                      f"(not yet supported by the module - see docs/ifw-sub-policy-json-design.md).")
        elif args.rules_only:
            print(f"\n Ready to import {len(main_rules)} rule(s) and {len(sub_rules)} sub-rule(s) only.")
        elif args.sections_only:
            print(f"\n Ready to import {len(main_sections)} section(s) only.")
            if sub_sections:
                print(f" NOTE: {len(sub_sections)} sub-section(s) will be SKIPPED "
                      f"(not yet supported by the module).")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}

        # Import order: sections -> sub_policies -> rules -> sub_rules
        # (sub-sections are skipped with a warning - provider/module gap)
        if not args.rules_only:
            if main_sections:
                merge_tally(grand_tally, import_sections(
                    main_sections, module_name=module_name,
                    resource_type="cato_if_section", verbose=args.verbose))

            print_skipped_sub_sections(sub_sections, module_name)

            if sub_policies:
                merge_tally(grand_tally, import_sub_policies(
                    sub_policies, module_name=module_name, verbose=args.verbose))

        if not args.sections_only:
            if main_rules:
                merge_tally(grand_tally, import_rules(
                    main_rules, module_name=module_name,
                    verbose=args.verbose, batch_size=args.batch_size,
                    delay_between_batches=args.delay))

            if sub_rules:
                merge_tally(grand_tally, import_sub_rules(
                    sub_rules, module_name=module_name, verbose=args.verbose,
                    batch_size=args.batch_size, delay_between_batches=args.delay))

        # Final summary
        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        if sub_sections:
            print(f" Skipped (sub-sections, not yet supported): {len(sub_sections)}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "skipped_sub_sections": len(sub_sections),
            "module_name": module_name
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
    """Main function to orchestrate the import process (sub-policy aware).

    Non-blocking by design: a per-resource import failure is classified and
    reported but never aborts the job and never prompts the user - running
    this command twice in a row is expected to be idempotent (the second run
    reports everything as already-imported). The command always returns
    success (and the CLI framework always exits 0 for a non-exception
    result - see catocli/Utils/clidriver.py) - the real outcome is the
    printed summary / the counts in the returned dict, not the exit code.
    """
    try:
        print(" Terraform Import Tool - Cato WF Rules & Sections")
        print("=" * 60)

        # Load data
        print(f" Loading data from {args.json_file}...")
        policy_data = load_wf_json_data(args.json_file)

        # Extract rules/sections, sub-policy aware
        resources = extract_if_rules_resources(policy_data)
        main_rules = resources['main_rules']
        sub_rules = resources['sub_rules']
        main_sections = resources['main_sections']
        sub_sections = resources['sub_sections']
        sub_policies = resources['sub_policies']

        if hasattr(args, 'verbose') and args.verbose:
            print(f"section_ids: {json.dumps(policy_data.get('section_ids', {}), indent=2)}")

        print(f" Found {len(main_rules)} rule(s), {len(sub_rules)} sub-rule(s)")
        print(f"  Found {len(main_sections)} section(s), {len(sub_sections)} sub-section(s)")
        print(f"  Found {len(sub_policies)} sub-policy(ies)")

        if not main_rules and not sub_rules and not main_sections and not sub_sections and not sub_policies:
            print(" No rules or sections found. Exiting.")
            return [{"success": False, "error": "No rules or sections found"}]

        # Add module. prefix if not present
        module_name = ensure_module_prefix(args.module_name)

        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)

        # Ask for confirmation (unless auto-approved)
        if not args.rules_only and not args.sections_only:
            print(f"\n Ready to import {len(main_sections)} section(s), {len(sub_policies)} sub-policy(ies), "
                  f"{len(main_rules)} rule(s), and {len(sub_rules)} sub-rule(s).")
            if sub_sections:
                print(f" NOTE: {len(sub_sections)} sub-section(s) will be SKIPPED "
                      f"(not yet supported by the module - see docs/ifw-sub-policy-json-design.md).")
        elif args.rules_only:
            print(f"\n Ready to import {len(main_rules)} rule(s) and {len(sub_rules)} sub-rule(s) only.")
        elif args.sections_only:
            print(f"\n Ready to import {len(main_sections)} section(s) only.")
            if sub_sections:
                print(f" NOTE: {len(sub_sections)} sub-section(s) will be SKIPPED "
                      f"(not yet supported by the module).")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}

        # Import order: sections -> sub_policies -> rules -> sub_rules
        # (sub-sections are skipped with a warning - provider/module gap)
        if not args.rules_only:
            if main_sections:
                merge_tally(grand_tally, import_sections(
                    main_sections, module_name=module_name,
                    resource_type="cato_wf_section", verbose=args.verbose))

            print_skipped_sub_sections(sub_sections, module_name, resource_type="cato_wf_section")

            if sub_policies:
                merge_tally(grand_tally, import_sub_policies(
                    sub_policies, module_name=module_name, verbose=args.verbose,
                    resource_type="cato_wf_sub_policy"))

        if not args.sections_only:
            if main_rules:
                merge_tally(grand_tally, import_rules(
                    main_rules, module_name=module_name,
                    resource_type="cato_wf_rule",
                    verbose=args.verbose, batch_size=args.batch_size,
                    delay_between_batches=args.delay))

            if sub_rules:
                merge_tally(grand_tally, import_sub_rules(
                    sub_rules, module_name=module_name, verbose=args.verbose,
                    resource_type="cato_wf_rule",
                    batch_size=args.batch_size, delay_between_batches=args.delay))

        # Final summary
        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        if sub_sections:
            print(f" Skipped (sub-sections, not yet supported): {len(sub_sections)}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "skipped_sub_sections": len(sub_sections),
            "module_name": module_name
        }]

    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]



def load_wnw_json_data(json_file):
    """Load WAN Network data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['wanNetwork']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def import_wnw_sections(sections, module_name, verbose=False,
                       resource_type="cato_wnw_section", resource_name="sections"):
    """Import all WAN Network sections"""
    print("\nStarting WAN Network section imports...")
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

        # For sections, we use the section ID
        success, stdout, stderr = run_terraform_import(resource_address, section_id, verbose=verbose)
        
        if success:
            successful_imports += 1
        else:
            failed_imports += 1
    
    print(f"\nWAN Network Section Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_wnw_rules(rules, module_name, verbose=False,
                    resource_type="cato_wnw_rule", resource_name="rules",
                    batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all WAN Network rules in batches"""
    print("\nStarting WAN Network rule imports...")
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
    
    print(f"\nWAN Network Rule Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_wnw_rules_to_tf(args, configuration):
    """Main function to orchestrate the WAN Network import process"""
    try:
        print("█ Terraform Import Tool - Cato WNW Rules & Sections")
        print("=" * 60)
        
        # Load data
        print(f"█ Loading data from {args.json_file}...")
        policy_data = load_wnw_json_data(args.json_file)
        
        # Extract rules and sections
        rules, sections = extract_rules_and_sections(policy_data)
        
        if hasattr(args, 'verbose') and args.verbose:
            print(f"section_ids: {json.dumps(policy_data.get('section_ids', {}), indent=2)}")
        
        print(f"█ Found {len(rules)} rules")
        print(f"█ Found {len(sections)} sections")
        
        if not rules and not sections:
            print("█ No rules or sections found. Exiting.")
            return [{"success": False, "error": "No rules or sections found"}]
        
        # Add module. prefix if not present
        module_name = args.module_name
        if not module_name.startswith('module.'):
            module_name = f'module.{module_name}'
        # Validate Terraform environment before proceeding
        validate_terraform_environment(module_name, verbose=args.verbose)
        
        # Ask for confirmation (unless auto-approved)
        if not args.rules_only and not args.sections_only:
            print(f"\n█ Ready to import {len(sections)} sections and {len(rules)} rules.")
        elif args.rules_only:
            print(f"\n█ Ready to import {len(rules)} rules only.")
        elif args.sections_only:
            print(f"\n█ Ready to import {len(sections)} sections only.")
        
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
            successful, failed = import_wnw_sections(sections, module_name=args.module_name, verbose=args.verbose)
            total_successful += successful
            total_failed += failed
        
        # Import rules (if not skipped)
        if not args.sections_only and rules:
            successful, failed = import_wnw_rules(rules, module_name=args.module_name, 
                                                 verbose=args.verbose, batch_size=args.batch_size, 
                                                 delay_between_batches=args.delay,
                                                 auto_approve=getattr(args, 'auto_approve', False))
            total_successful += successful
            total_failed += failed
        
        # Final summary
        print("\n" + "=" * 60)
        print("█ FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f"█ Total successful imports: {total_successful}")
        print(f"█ Total failed imports: {total_failed}")
        print(f"█ Overall success rate: {(total_successful / (total_successful + total_failed) * 100):.1f}%" if (total_successful + total_failed) > 0 else "N/A")
        print("\n█ Import process completed!")
        
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


def load_tls_json_data(json_file):
    """Load TLS Inspection data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['tlsInspect']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def import_tls_sections(sections, module_name, verbose=False,
                       resource_type="cato_tls_section", resource_name="sections"):
    """Import all TLS Inspection sections"""
    print("\nStarting TLS Inspection section imports...")
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
    
    print(f"\nTLS Inspection Section Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_tls_rules(rules, module_name, verbose=False,
                    resource_type="cato_tls_rule", resource_name="rules",
                    batch_size=10, delay_between_batches=2, auto_approve=False):
    """Import all TLS Inspection rules in batches"""
    print("\nStarting TLS Inspection rule imports...")
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
    
    print(f"\nTLS Inspection Rule Import Summary: {successful_imports} successful, {failed_imports} failed")
    return successful_imports, failed_imports


def import_tls_rules_to_tf(args, configuration):
    """Main function to orchestrate the TLS Inspection import process"""
    try:
        print(" Terraform Import Tool - Cato TLS Inspection Rules & Sections")
        print("=" * 60)
        
        # Load data
        print(f" Loading data from {args.json_file}...")
        policy_data = load_tls_json_data(args.json_file)
        
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
            successful, failed = import_tls_sections(sections, module_name=args.module_name, verbose=args.verbose)
            total_successful += successful
            total_failed += failed
        
        # Import rules (if not skipped)
        if not args.sections_only and rules:
            successful, failed = import_tls_rules(rules, module_name=args.module_name, 
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


# ---------------------------------------------------------------------------
# LAN Firewall (socketLan) import - consumes the JSON produced by
# `catocli export lan_fw_rules` and imports into the
# terraform-cato-bulk-lan-fw-rules module addresses. Unlike the IFW path,
# sub-sections ARE importable (cato_socket_lan_section supports sub-policy
# ownership via at.ref). The cato_bulk_lf_move_rule ordering resource is not
# importable by design - it is created on first apply.
# ---------------------------------------------------------------------------

def load_lan_json_data(json_file):
    """Load LAN FW (socketLan) policy data from a lan_fw_rules export."""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['socketLan']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def extract_lan_fw_resources(policy_data):
    """Extract importable LAN FW resources from the export's policy node.

    Returns {sections, sub_sections, sub_policies, network_rules,
    firewall_rules}; firewall rules are flattened to composite keys
    "<network_rule_name>::<firewall_rule_name>" (nesting is the parent
    reference; array order is the per-parent order)."""
    sections = []
    sub_sections = []
    for s in policy_data.get('sections', []) or []:
        entry = {
            'section_name': s.get('section_name'),
            'section_id': s.get('section_id', ''),
            'section_index': s.get('section_index', 0),
        }
        if s.get('sub_policy_name'):
            entry['sub_policy_name'] = s['sub_policy_name']
            sub_sections.append(entry)
        else:
            sections.append(entry)

    sub_policies = []
    for sp in policy_data.get('sub_policies', []) or []:
        if sp.get('sub_policy_name') and sp.get('sub_policy_id'):
            sub_policies.append({
                'sub_policy_name': sp['sub_policy_name'],
                'sub_policy_id': sp['sub_policy_id'],
            })

    network_rules = []
    firewall_rules = []
    for nr in policy_data.get('network_rules', []) or []:
        rule = nr.get('rule') or {}
        if not rule.get('name'):
            continue
        network_rules.append({
            'name': rule['name'],
            'id': rule.get('id', ''),
            'sub_policy_name': nr.get('sub_policy_name'),
        })
        for fw in nr.get('firewall_rules', []) or []:
            fw_rule = fw.get('rule') or {}
            if not fw_rule.get('name'):
                continue
            firewall_rules.append({
                'composite_key': f"{rule['name']}::{fw_rule['name']}",
                'name': fw_rule['name'],
                'id': fw_rule.get('id', ''),
                'network_rule_name': rule['name'],
            })

    return {
        'sections': sections,
        'sub_sections': sub_sections,
        'sub_policies': sub_policies,
        'network_rules': network_rules,
        'firewall_rules': firewall_rules,
    }


def import_lan_items(items, module_name, resource_type, resource_name,
                     key_field, id_field, label, verbose=False,
                     batch_size=10, delay_between_batches=2):
    """Generic non-blocking import loop for LAN FW resources."""
    module_name = ensure_module_prefix(module_name)
    print(f"\nStarting {label} imports...")
    total = len(items)
    tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}

    for i, item in enumerate(items):
        resource_id = item.get(id_field, '')
        key = item.get(key_field, '')
        resource_address = f'{module_name}.{resource_type}.{resource_name}["{key}"]'
        print(f"\n[{i+1}/{total}] {label}: {key}")

        if not resource_id:
            # Greenfield entry (no live id) - nothing to import; terraform
            # creates it on first apply.
            print(f"SKIP (no live id - created on apply): {resource_address}")
            tally["not_found"] += 1
            continue

        success, stdout, stderr = run_terraform_import(resource_address, resource_id, verbose=verbose)
        if success:
            tally["imported"] += 1
        else:
            kind = classify_import_failure(stderr)
            if kind == "already_managed":
                print(f"SKIP (already imported): {resource_address}")
            elif kind == "not_found":
                print(f"SKIP (not found in tenant): {resource_address} (id {resource_id})")
            else:
                print(f"WARNING: import failed for {resource_address}: {stderr.strip() if stderr else 'unknown error'}")
            tally[kind] += 1

        if batch_size and (i + 1) % batch_size == 0 and (i + 1) < total:
            time.sleep(delay_between_batches)

    print(f"\n{label} Import Summary: {tally['imported']} imported, "
          f"{tally['already_managed']} already-imported, {tally['not_found']} not-found, "
          f"{tally['other']} other failures")
    return tally


def import_lan_fw_rules_to_tf(args, configuration):
    """Import LAN Firewall (socketLan) resources into terraform state.

    Non-blocking and idempotent, same contract as import_if_rules_to_tf.
    Import order: sections -> sub_policies -> sub_sections -> network rules
    -> firewall rules. The cato_bulk_lf_move_rule ordering resource is not
    importable and is created on the first apply."""
    try:
        print(" Terraform Import Tool - Cato LAN FW Rules & Sections")
        print("=" * 60)

        print(f" Loading data from {args.json_file}...")
        policy_data = load_lan_json_data(args.json_file)

        resources = extract_lan_fw_resources(policy_data)
        sections = resources['sections']
        sub_sections = resources['sub_sections']
        sub_policies = resources['sub_policies']
        network_rules = resources['network_rules']
        firewall_rules = resources['firewall_rules']

        print(f" Found {len(sections)} section(s), {len(sub_sections)} sub-section(s), "
              f"{len(sub_policies)} sub-policy(ies)")
        print(f" Found {len(network_rules)} network rule(s), {len(firewall_rules)} firewall rule(s)")

        if not any([sections, sub_sections, sub_policies, network_rules, firewall_rules]):
            print(" No resources found. Exiting.")
            return [{"success": False, "error": "No resources found"}]

        module_name = ensure_module_prefix(args.module_name)
        validate_terraform_environment(module_name, verbose=args.verbose)

        print(f"\n Ready to import {len(sections)} section(s), {len(sub_sections)} sub-section(s), "
              f"{len(sub_policies)} sub-policy(ies), {len(network_rules)} network rule(s), "
              f"{len(firewall_rules)} firewall rule(s).")
        print(" NOTE: the cato_bulk_lf_move_rule ordering resource is not importable; "
              "it is created on the first apply.")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}
        common = dict(module_name=module_name, verbose=args.verbose,
                      batch_size=args.batch_size, delay_between_batches=args.delay)

        if sections:
            merge_tally(grand_tally, import_lan_items(
                sections, resource_type="cato_socket_lan_section", resource_name="sections",
                key_field='section_name', id_field='section_id', label="Section", **common))
        if sub_policies:
            merge_tally(grand_tally, import_lan_items(
                sub_policies, resource_type="cato_lf_sub_policy", resource_name="sub_policies",
                key_field='sub_policy_name', id_field='sub_policy_id', label="Sub-policy", **common))
        if sub_sections:
            for s in sub_sections:
                s['composite_key'] = f"{s['sub_policy_name']}::{s['section_name']}"
            merge_tally(grand_tally, import_lan_items(
                sub_sections, resource_type="cato_socket_lan_section", resource_name="sub_sections",
                key_field='composite_key', id_field='section_id', label="Sub-section", **common))
        if network_rules:
            merge_tally(grand_tally, import_lan_items(
                network_rules, resource_type="cato_socket_lan_network_rule", resource_name="network_rules",
                key_field='name', id_field='id', label="Network rule", **common))
        if firewall_rules:
            merge_tally(grand_tally, import_lan_items(
                firewall_rules, resource_type="cato_socket_lan_firewall_rule", resource_name="firewall_rules",
                key_field='composite_key', id_field='id', label="Firewall rule", **common))

        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "module_name": module_name,
        }]

    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


# ---------------------------------------------------------------------------
# ZTNA Always-On import - consumes `catocli export ao_rules` JSON and imports
# into the terraform-cato-bulk-ao-rules module addresses. Flat policy:
# sections + rules only. The cato_bulk_ao_move_rule ordering/publishing
# resource is not importable - it is created on first apply.
# ---------------------------------------------------------------------------

def load_ao_json_data(json_file):
    """Load ZTNA Always-On policy data from an ao_rules export."""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['ztnaAlwaysOn']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def extract_ao_resources(policy_data):
    """Extract importable Always-On resources: {sections, rules}."""
    sections = []
    for s in policy_data.get('sections', []) or []:
        if s.get('section_name'):
            sections.append({
                'section_name': s['section_name'],
                'section_id': s.get('section_id', ''),
                'section_index': s.get('section_index', 0),
            })

    rules = []
    for rw in policy_data.get('rules', []) or []:
        rule = rw.get('rule') or {}
        if rule.get('name'):
            rules.append({'name': rule['name'], 'id': rule.get('id', '')})
    return {'sections': sections, 'rules': rules}


def import_ao_rules_to_tf(args, configuration):
    """Import ZTNA Always-On resources into terraform state.

    Non-blocking and idempotent, same contract as the IFW/LAN importers.
    Import order: sections -> rules. cato_bulk_ao_move_rule is created on the
    first apply (not importable)."""
    try:
        print(" Terraform Import Tool - Cato Always-On Rules & Sections")
        print("=" * 60)

        print(f" Loading data from {args.json_file}...")
        policy_data = load_ao_json_data(args.json_file)

        resources = extract_ao_resources(policy_data)
        sections = resources['sections']
        rules = resources['rules']

        print(f" Found {len(sections)} section(s), {len(rules)} rule(s)")
        if not sections and not rules:
            print(" No resources found. Exiting.")
            return [{"success": False, "error": "No resources found"}]

        module_name = ensure_module_prefix(args.module_name)
        validate_terraform_environment(module_name, verbose=args.verbose)

        print(f"\n Ready to import {len(sections)} section(s) and {len(rules)} rule(s).")
        print(" NOTE: cato_bulk_ao_move_rule (ordering + publish) is not importable; "
              "it is created on the first apply.")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}
        common = dict(module_name=module_name, verbose=args.verbose,
                      batch_size=args.batch_size, delay_between_batches=args.delay)

        if sections:
            merge_tally(grand_tally, import_lan_items(
                sections, resource_type="cato_always_on_section", resource_name="sections",
                key_field='section_name', id_field='section_id', label="Section", **common))
        if rules:
            merge_tally(grand_tally, import_lan_items(
                rules, resource_type="cato_always_on_rule", resource_name="rules",
                key_field='name', id_field='id', label="Rule", **common))

        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "module_name": module_name,
        }]

    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


# ---------------------------------------------------------------------------
# Private Access import - consumes `catocli export pa_rules` JSON and imports
# into the terraform-cato-bulk-private-access module addresses. Flat ordered
# rule list (no sections in the terraform surface yet). The
# cato_private_access_rule_bulk ordering/publishing resource is not
# importable - it is created on first apply.
# ---------------------------------------------------------------------------

def load_pa_json_data(json_file):
    """Load Private Access policy data from a pa_rules export."""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data['data']['policy']['privateAccess']['policy']
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Expected JSON structure not found in '{json_file}': {e}")
        sys.exit(1)


def import_pa_rules_to_tf(args, configuration):
    """Import Private Access rules into terraform state.

    Non-blocking and idempotent, same contract as the other importers."""
    try:
        print(" Terraform Import Tool - Cato Private Access Rules")
        print("=" * 60)

        print(f" Loading data from {args.json_file}...")
        policy_data = load_pa_json_data(args.json_file)

        rules = []
        for rw in policy_data.get('rules', []) or []:
            rule = rw.get('rule') or {}
            if rule.get('name'):
                rules.append({'name': rule['name'], 'id': rule.get('id', '')})

        print(f" Found {len(rules)} rule(s)")
        if not rules:
            print(" No rules found. Exiting.")
            return [{"success": False, "error": "No rules found"}]

        module_name = ensure_module_prefix(args.module_name)
        validate_terraform_environment(module_name, verbose=args.verbose)

        print(f"\n Ready to import {len(rules)} rule(s).")
        print(" NOTE: cato_private_access_rule_bulk (ordering + publish) is not importable; "
              "it is created on the first apply.")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = import_lan_items(
            rules, module_name=module_name, verbose=args.verbose,
            batch_size=args.batch_size, delay_between_batches=args.delay,
            resource_type="cato_private_access_rule", resource_name="rules",
            key_field='name', id_field='id', label="Rule")

        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "module_name": module_name,
        }]

    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


# ---------------------------------------------------------------------------
# Application Control / App Tenant Restriction imports - flat sections+rules
# policies; bulk move resources are created on first apply.
# ---------------------------------------------------------------------------

def _import_flat_policy_to_tf(args, policy_root_key, label,
                              section_resource_type, rule_resource_type):
    """Shared implementation for flat sections+rules policy importers."""
    try:
        print(f" Terraform Import Tool - Cato {label} Rules & Sections")
        print("=" * 60)

        print(f" Loading data from {args.json_file}...")
        try:
            with open(args.json_file, 'r') as f:
                policy_data = json.load(f)['data']['policy'][policy_root_key]['policy']
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading '{args.json_file}': {e}")
            sys.exit(1)

        sections = [
            {'section_name': s['section_name'], 'section_id': s.get('section_id', ''),
             'section_index': s.get('section_index', 0)}
            for s in (policy_data.get('sections') or []) if s.get('section_name')
        ]
        rules = [
            {'name': rw['rule']['name'], 'id': rw['rule'].get('id', '')}
            for rw in (policy_data.get('rules') or []) if (rw.get('rule') or {}).get('name')
        ]

        print(f" Found {len(sections)} section(s), {len(rules)} rule(s)")
        if not sections and not rules:
            print(" No resources found. Exiting.")
            return [{"success": False, "error": "No resources found"}]

        module_name = ensure_module_prefix(args.module_name)
        validate_terraform_environment(module_name, verbose=args.verbose)

        print(f"\n Ready to import {len(sections)} section(s) and {len(rules)} rule(s).")
        print(" NOTE: the bulk move/publish resource is not importable; it is created on the first apply.")

        if hasattr(args, 'auto_approve') and args.auto_approve:
            print("\nAuto-approve enabled, proceeding with import...")
        else:
            confirm = input(f"\nProceed with import? (y/n): ").lower()
            if confirm != 'y':
                print("Import cancelled.")
                return [{"success": False, "error": "Import cancelled by user"}]

        grand_tally = {"imported": 0, "already_managed": 0, "not_found": 0, "other": 0}
        common = dict(module_name=module_name, verbose=args.verbose,
                      batch_size=args.batch_size, delay_between_batches=args.delay)

        if sections:
            merge_tally(grand_tally, import_lan_items(
                sections, resource_type=section_resource_type, resource_name="sections",
                key_field='section_name', id_field='section_id', label="Section", **common))
        if rules:
            merge_tally(grand_tally, import_lan_items(
                rules, resource_type=rule_resource_type, resource_name="rules",
                key_field='name', id_field='id', label="Rule", **common))

        print("\n" + "=" * 60)
        print(" FINAL IMPORT SUMMARY")
        print("=" * 60)
        print(f" Imported:             {grand_tally['imported']}")
        print(f" Already imported:     {grand_tally['already_managed']}")
        print(f" Not found in tenant:  {grand_tally['not_found']}")
        print(f" Other failures:       {grand_tally['other']}")
        print("\n Import process completed!")

        return [{
            "success": True,
            "imported": grand_tally['imported'],
            "already_managed": grand_tally['already_managed'],
            "not_found": grand_tally['not_found'],
            "other_failures": grand_tally['other'],
            "module_name": module_name,
        }]

    except KeyboardInterrupt:
        print("\nImport process cancelled by user (Ctrl+C).")
        print("Partial imports may have been completed.")
        return [{"success": False, "error": "Import cancelled by user"}]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def import_apc_rules_to_tf(args, configuration):
    """Import Application Control resources into terraform state."""
    return _import_flat_policy_to_tf(
        args, 'applicationControl', 'Application Control',
        'cato_application_control_section', 'cato_application_control_rule')


def import_atr_rules_to_tf(args, configuration):
    """Import App Tenant Restriction resources into terraform state."""
    return _import_flat_policy_to_tf(
        args, 'appTenantRestriction', 'App Tenant Restriction',
        'cato_app_tenant_restriction_section', 'cato_app_tenant_restriction_rule')


def import_ts_rules_to_tf(args, configuration):
    """Import Terminal Server resources into terraform state."""
    return _import_flat_policy_to_tf(
        args, 'terminalServer', 'Terminal Server',
        'cato_terminal_server_section', 'cato_terminal_server_rule')


def import_amfh_rules_to_tf(args, configuration):
    """Import Anti-Malware File Hash resources into terraform state."""
    return _import_flat_policy_to_tf(
        args, 'antiMalwareFileHash', 'Anti-Malware File Hash',
        'cato_anti_malware_file_hash_section', 'cato_anti_malware_file_hash_rule')


def import_ssia_rules_to_tf(args, configuration):
    """Import SDP Static IP Allocation resources into terraform state."""
    return _import_flat_policy_to_tf(
        args, 'sdpStaticIpAllocation', 'SDP Static IP Allocation',
        'cato_sdp_static_ip_allocation_section', 'cato_sdp_static_ip_allocation_rule')
