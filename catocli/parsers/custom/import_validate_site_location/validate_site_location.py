#!/usr/bin/env python3
"""
Validate site location data against Cato's location database
"""

import json
import csv
import os
import sys
import argparse
from typing import Dict, List, Tuple, Optional


def load_site_location_data() -> Dict:
    """Load the Cato site location database"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Navigate to the query_siteLocation directory
        location_file = os.path.join(
            current_dir, 
            '..', 
            'query_siteLocation', 
            'query.siteLocation.json'
        )
        
        with open(location_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load site location database: {e}")
        sys.exit(1)


def load_csv_data(file_path: str) -> List[Dict]:
    """Load site data from CSV file"""
    sites = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Start at line 2 (line 1 is the header)
            for line_num, row in enumerate(reader, start=2):
                # Extract location fields from CSV
                # Expected columns: site_location_city, site_location_country_code, 
                # site_location_state_code, site_location_timezone
                site = {
                    'name': row.get('site_name', ''),
                    'city': row.get('site_location_city', ''),
                    'country_code': row.get('site_location_country_code', ''),
                    'state_code': row.get('site_location_state_code', ''),
                    'timezone': row.get('site_location_timezone', ''),
                    'line_number': line_num,
                    'source_type': 'csv'
                }
                sites.append(site)
    except Exception as e:
        print(f"ERROR: Failed to load CSV file '{file_path}': {e}")
        sys.exit(1)
    
    return sites


def load_json_data(file_path: str) -> List[Dict]:
    """Load site data from JSON file"""
    sites = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Handle different JSON structures
        if isinstance(data, dict) and 'sites' in data:
            site_list = data['sites']
        elif isinstance(data, list):
            site_list = data
        else:
            print("ERROR: JSON must contain 'sites' array or be an array of sites")
            sys.exit(1)
        
        for index, site_data in enumerate(site_list, start=1):
            site_location = site_data.get('site_location', {})
            site = {
                'name': site_data.get('name', ''),
                'city': site_location.get('city', ''),
                'country_code': site_location.get('countryCode', ''),
                'state_code': site_location.get('stateCode', ''),
                'timezone': site_location.get('timezone', ''),
                'line_number': index,
                'source_type': 'json'
            }
            sites.append(site)
            
    except Exception as e:
        print(f"ERROR: Failed to load JSON file '{file_path}': {e}")
        sys.exit(1)
    
    return sites


def validate_location(site: Dict, location_db: Dict, verbose: bool = False) -> Tuple[bool, List[str]]:
    """
    Validate a site location against the Cato location database
    
    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    
    city = site.get('city', '').strip()
    country_code = site.get('country_code', '').strip()
    state_code = site.get('state_code', '').strip()
    timezone = site.get('timezone', '').strip()
    
    # Check if required fields are present
    if not city:
        errors.append("Missing city")
    if not country_code:
        errors.append("Missing country code")
    if not timezone:
        errors.append("Missing timezone")
    
    if errors:
        return False, errors
    
    # Search for exact match in location database
    match_found = False
    matched_entry = None
    
    for key, location_entry in location_db.items():
        # Match country code and city (case-sensitive exact match)
        if (location_entry.get('countryCode') == country_code and 
            location_entry.get('city') == city):
            
            # Check state if provided in both site and database
            state_matches = True
            if state_code:
                # State code in database might be in stateCode field
                db_state_code = location_entry.get('stateCode', '')
                if db_state_code:
                    state_matches = (db_state_code == state_code)
                else:
                    # If state is provided by user but not in DB, that's an issue
                    errors.append(f"State code '{state_code}' provided but location has no state")
                    state_matches = False
            
            if state_matches:
                match_found = True
                matched_entry = location_entry
                break
    
    if not match_found:
        errors.append(f"Location not found: {city}, {country_code}" + 
                     (f", {state_code}" if state_code else ""))
        return False, errors
    
    # Validate timezone
    db_timezones = matched_entry.get('timezone', [])
    if isinstance(db_timezones, str):
        db_timezones = [db_timezones]
    
    if timezone not in db_timezones:
        errors.append(f"Invalid timezone '{timezone}'. Valid options: {', '.join(db_timezones)}")
        return False, errors
    
    # If we got here, everything is valid
    if verbose:
        country_name = matched_entry.get('countryName', country_code)
        state_name = matched_entry.get('stateName', state_code) if state_code else None
        location_str = f"{city}, "
        if state_name:
            location_str += f"{state_name}, "
        location_str += f"{country_name} ({timezone})"
        
    return True, []


def validate_site_location(args, configuration=None):
    """Main validation function called by CLI"""

    # Extract arguments
    file_path = args.file_path
    file_format = args.format
    verbose = args.verbose
    show_valid = args.show_valid
    output_file = args.output if hasattr(args, 'output') else None

    # Load site location database
    print("Loading Cato location database...")
    location_db = load_site_location_data()
    print(f"Loaded {len(location_db)} locations from database\n")

    # Load site data from file
    print(f"Loading site data from {file_path}...")
    if file_format == 'csv':
        sites = load_csv_data(file_path)
    else:  # json
        sites = load_json_data(file_path)

    print(f"Loaded {len(sites)} sites\n")

    # Validate each site
    print("=" * 80)
    print("VALIDATION RESULTS")
    print("=" * 80)

    valid_sites = []
    invalid_sites = []
    skipped_sites = []

    for idx, site in enumerate(sites, 1):
        # Check if all location fields are empty
        city = site.get('city', '').strip()
        country_code = site.get('country_code', '').strip()
        state_code = site.get('state_code', '').strip()
        timezone = site.get('timezone', '').strip()

        if not city and not country_code and not state_code and not timezone:
            # Skip this row - all location fields are empty
            skipped_sites.append(site)
            if verbose:
                # Format line reference based on source type
                if site.get('source_type') == 'csv':
                    line_ref = f" (CSV line {site.get('line_number', 'unknown')})"
                elif site.get('source_type') == 'json':
                    line_ref = f" (JSON index {site.get('line_number', 'unknown')})"
                else:
                    line_ref = ""
                print(f"\n[-] Site {idx}: {site.get('name', 'Unnamed')}{line_ref}")
                print("    Status: SKIPPED (all location fields empty)")
            continue

        is_valid, errors = validate_location(site, location_db, verbose)

        # Format line reference based on source type
        if site.get('source_type') == 'csv':
            line_ref = f" (CSV line {site.get('line_number', 'unknown')})"
        elif site.get('source_type') == 'json':
            line_ref = f" (JSON index {site.get('line_number', 'unknown')})"
        else:
            line_ref = ""

        if is_valid:
            valid_sites.append(site)
            if show_valid or verbose:
                print(f"\n[✓] Site {idx}: {site.get('name', 'Unnamed')}{line_ref}")
                print(f"    Location: {site['city']}, {site['country_code']}" +
                      (f", {site['state_code']}" if site.get('state_code') else ""))
                print(f"    Timezone: {site['timezone']}")
                print("    Status: VALID")
        else:
            invalid_sites.append({'site': site, 'errors': errors})
            print(f"\n[✗] Site {idx}: {site.get('name', 'Unnamed')}{line_ref}")
            print(f"    Location: {site['city']}, {site['country_code']}" +
                  (f", {site['state_code']}" if site.get('state_code') else ""))
            print(f"    Timezone: {site['timezone']}")
            print("    Status: INVALID")
            for error in errors:
                print(f"    - {error}")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total sites processed: {len(sites)}")
    print(f"Valid sites: {len(valid_sites)} ({len(valid_sites)/len(sites)*100:.1f}%)")
    print(f"Invalid sites: {len(invalid_sites)} ({len(invalid_sites)/len(sites)*100:.1f}%)")
    if skipped_sites:
        print(f"Skipped sites: {len(skipped_sites)} ({len(skipped_sites)/len(sites)*100:.1f}%)")

    # Show skipped sites section if there are any
    if skipped_sites:
        print("\n" + "=" * 80)
        print("SKIPPED ROWS (all location fields empty)")
        print("=" * 80)
        for site in skipped_sites:
            # Format line reference based on source type
            if site.get('source_type') == 'csv':
                line_ref = f" (CSV line {site.get('line_number', 'unknown')})"
            elif site.get('source_type') == 'json':
                line_ref = f" (JSON index {site.get('line_number', 'unknown')})"
            else:
                line_ref = ""
            print(f"  - {site.get('name', 'Unnamed')}{line_ref}")
    
    # Write output file if requested
    if output_file:
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Line/Index', 'Site Name', 'City', 'Country Code', 'State Code',
                               'Timezone', 'Status', 'Errors'])

                for site in valid_sites:
                    writer.writerow([
                        site.get('line_number', ''),
                        site.get('name', ''),
                        site['city'],
                        site['country_code'],
                        site.get('state_code', ''),
                        site['timezone'],
                        'VALID',
                        ''
                    ])

                for item in invalid_sites:
                    site = item['site']
                    errors = item['errors']
                    writer.writerow([
                        site.get('line_number', ''),
                        site.get('name', ''),
                        site['city'],
                        site['country_code'],
                        site.get('state_code', ''),
                        site['timezone'],
                        'INVALID',
                        '; '.join(errors)
                    ])

                for site in skipped_sites:
                    writer.writerow([
                        site.get('line_number', ''),
                        site.get('name', ''),
                        site.get('city', ''),
                        site.get('country_code', ''),
                        site.get('state_code', ''),
                        site.get('timezone', ''),
                        'SKIPPED',
                        'All location fields empty'
                    ])

            print(f"\nValidation results written to: {output_file}")
        except Exception as e:
            print(f"\nWARNING: Failed to write output file: {e}")
    
    # Exit with error code if there are invalid sites
    if invalid_sites:
        print("\n" + "=" * 80)
        print("HOW TO FIX INVALID LOCATIONS")
        print("=" * 80)
        print("Use the following catocli query to search for valid locations:")
        print("\n  catocli query siteLocation -h")
        sys.exit(1)
    else:
        print("\n✓ All sites validated successfully")
        sys.exit(0)


if __name__ == '__main__':
    # For testing purposes
    parser = argparse.ArgumentParser(description='Validate site location data')
    parser.add_argument('file_path', help='Path to CSV or JSON file')
    parser.add_argument('-f', '--format', choices=['json', 'csv'], required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--show-valid', action='store_true')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    validate_site_location(args)
