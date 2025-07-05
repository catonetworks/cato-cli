import sys
import csv
import subprocess
import json
import os
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client import Configuration
from graphql_client.api_client import ApiException
import catocli

# Configuration variables
DESTINATION_DIR = "config_data"

def strip_ids_recursive(data):
    """Recursively strip id attributes from data structure"""
    if isinstance(data, dict):
        return {k: strip_ids_recursive(v) for k, v in data.items() if k != 'id'}
    elif isinstance(data, list):
        return [strip_ids_recursive(item) for item in data]
    else:
        return data

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Export IFW rules to JSON')
    parser.add_argument('-accountID', help='Account ID to export rules from', required=True)
    parser.add_argument('--output-file-path', help='Full path including filename and extension for output file. If not specified, uses default: config_data/all_ifw_rules_and_sections_{account_id}.json')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()
    
    ACCOUNT_ID = args.accountID
    
    # Setup API client configuration
    if "CATO_TOKEN" not in os.environ:
        print("Missing authentication, please set the CATO_TOKEN environment variable with your api key.")
        sys.exit(1)
    
    configuration = Configuration()
    configuration.verify_ssl = False
    configuration.api_key["x-api-key"] = os.getenv("CATO_TOKEN")
    configuration.host = "{}".format(catocli.__cato_host__)
    configuration.accountID = ACCOUNT_ID
    
    # Set up output file path
    if args.output_file_path:
        # Use output file path if provided
        output_file = args.output_file_path
        destination_dir = os.path.dirname(output_file)
        if args.verbose:
            print(f"Using output file path: {output_file}")
    else:
        # Use default path and filename
        destination_dir = 'config_data'
        json_output_file = f"all_ifw_rules_and_sections_{ACCOUNT_ID}.json"
        output_file = os.path.join(destination_dir, json_output_file)
        if args.verbose:
            print(f"Using default path: {output_file}")
    
    # Create destination directory if it doesn't exist
    if destination_dir and not os.path.exists(destination_dir):
        if args.verbose:
            print(f"Creating directory: {destination_dir}")
        os.makedirs(destination_dir)
    policyQuery = {
        "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { internetFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } exceptions { name source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin } } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
        "variables": {
            "accountId": ACCOUNT_ID
        },
        "operationName": "policy"
    }
    print(f"Retrieving all IFW rules and sections for account {ACCOUNT_ID}...")
    
    # Create API client instance
    instance = CallApi(ApiClient(configuration))
    
    # Create params object for the API call
    params = {
        'v': False,  # verbose mode
        'f': 'json',  # format
        'p': False,  # pretty print
        't': False   # test mode
    }
    
    try:
        # Call the API directly
        response = instance.call_api(policyQuery, params)
        allIfwRules = response[0] if response else {}
        
        if not allIfwRules or 'data' not in allIfwRules:
            print("ERROR: Failed to retrieve data from API")
            sys.exit(1)
            
    except ApiException as e:
        print(f"ERROR: API call failed - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error - {e}")
        sys.exit(1)
    
    # First, preserve section IDs before stripping them
    section_id_map = {}
    sections_with_ids = allIfwRules['data']['policy']['internetFirewall']['policy']['sections']
    for section_data in sections_with_ids:
        section_id_map[section_data['section']['name']] = section_data['section']['id']
    
    # Get the first section ID for section_to_start_after_id
    section_to_start_after_id = None
    if len(sections_with_ids) > 0:
        section_to_start_after_id = sections_with_ids[0]['section']['id']
        print(f"Excluding first section with system rule: {sections_with_ids[0]['section']['name']}")
    
    ## Processing data to strip id attributes
    processed_data = strip_ids_recursive(allIfwRules)
    
    ## Filter out rules with properties[0]=="SYSTEM"
    filtered_rules = []
    for rule_data in processed_data['data']['policy']['internetFirewall']['policy']['rules']:
        rule_properties = rule_data.get('properties', [])
        # Skip rules where the first property is "SYSTEM"
        if rule_properties and rule_properties[0] == "SYSTEM":
            print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
        else:
            filtered_rules.append(rule_data)
    processed_data['data']['policy']['internetFirewall']['policy']['rules'] = filtered_rules
    # rules = filtered_rules
    
    # Add index_in_section to each rule
    # Group rules by section and add index_in_section
    section_counters = {}
    for rule_data in processed_data['data']['policy']['internetFirewall']['policy']['rules']:
        section_name = rule_data['rule']['section']['name']
        if section_name not in section_counters:
            section_counters[section_name] = 0
        section_counters[section_name] += 1
        rule_data['rule']['index_in_section'] = section_counters[section_name]
    
    # Create rules_in_sections array
    rules_in_sections = []
    for rule_data in processed_data['data']['policy']['internetFirewall']['policy']['rules']:
        rule_info = rule_data['rule']
        rules_in_sections.append({
            "index_in_section": rule_info['index_in_section'],
            "section_name": rule_info['section']['name'],
            "rule_name": rule_info['name']
        })
        rule_info.pop("index_in_section", None)
        rule_info.pop("index", None)
        rule_info["enabled"] = True

    # Add rules_in_sections to the policy structure
    processed_data['data']['policy']['internetFirewall']['policy']['rules_in_sections'] = rules_in_sections
    
    # Reformat sections array to have index, section_id and section_name structure
    # Exclude the first section from export
    processed_sections = [] 
    # Add first section containing reserved SYSTEM rules as section_to_start_after_id
    for index, section_data in enumerate(processed_data['data']['policy']['internetFirewall']['policy']['sections']):
        if index == 0:
            # Skip the first section which contains reserved SYSTEM rules
            continue
        else:
            processed_sections.append({
                "section_index": index,
                "section_name": section_data['section']['name']
            })
    
    # Add preserved section IDs and section_to_start_after_id
    processed_data['data']['policy']['internetFirewall']['policy']['section_ids'] = section_id_map
    if section_to_start_after_id:
        processed_data['data']['policy']['internetFirewall']['policy']['section_to_start_after_id'] = section_to_start_after_id

    if len(sections_with_ids) > 0:
        print(f"Excluded first section: {sections_with_ids[0]['section']['name']} containing reserved SYSTEM rules")
    
    # Replace the original sections array with the reformatted one
    processed_data['data']['policy']['internetFirewall']['policy']['sections'] = processed_sections
        
    # Write the processed data to the new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)    
    print(f"Successfully created {output_file}")
    

if __name__ == "__main__":
    main()

