import sys
import csv
import subprocess
import json
import os
import argparse
import catolib

# Configuration variables
DESTINATION_DIR = "config_data"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Export WAN rules to JSON')
    parser.add_argument('account_id', help='Account ID to export rules from')
    args = parser.parse_args()
    
    ACCOUNT_ID = args.account_id
    JSON_OUTPUT_FILE = f"all_wf_rules_and_sections_{ACCOUNT_ID}.json"
    # Create destination directory if it doesn't exist
    if not os.path.exists(DESTINATION_DIR):
        print(f"Creating directory: {DESTINATION_DIR}")
        os.makedirs(DESTINATION_DIR)
    
    # Set full file paths
    output_file = os.path.join(DESTINATION_DIR, JSON_OUTPUT_FILE)
    policyQuery = {
        "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { wanFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } direction exceptions { name source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin direction } } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
        "variables": {
            "accountId": ACCOUNT_ID
        },
        "operationName": "policy"
    }
    catocliCommand = "catocli raw '"+json.dumps(policyQuery)+"'"
    print(f"Retrieving all WAN rules and sections for account {ACCOUNT_ID}...")
    allWanRules = catolib.exec_cli(catocliCommand)
    
    ## Processing data to strip id attributes
    processed_data = catolib.strip_ids_recursive(allWanRules)

    ## Preserving section IDs index by section name
    section_id_map = {}
    if 'data' in allWanRules and 'policy' in allWanRules['data'] and 'wanFirewall' in allWanRules['data']['policy']:
        for section_data in allWanRules['data']['policy']['wanFirewall']['policy']['sections']:
            section_id_map[section_data['section']['name']] = section_data['section']['id']
    processed_data['data']['policy']['wanFirewall']['policy']['section_ids'] = section_id_map
    
    ## Filter out rules with properties[0]=="SYSTEM"
    filtered_rules = []
    for rule_data in processed_data['data']['policy']['wanFirewall']['policy']['rules']:
        rule_properties = rule_data.get('properties', [])
        # Skip rules where the first property is "SYSTEM"
        if rule_properties and rule_properties[0] == "SYSTEM":
            print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
        else:
            filtered_rules.append(rule_data)
    processed_data['data']['policy']['wanFirewall']['policy']['rules'] = filtered_rules
    # rules = filtered_rules
    
    # Add index_in_section to each rule
    # Group rules by section and add index_in_section
    section_counters = {}
    for rule_data in processed_data['data']['policy']['wanFirewall']['policy']['rules']:
        section_name = rule_data['rule']['section']['name']
        if section_name not in section_counters:
            section_counters[section_name] = 0
        section_counters[section_name] += 1
        rule_data['rule']['index_in_section'] = section_counters[section_name]
    
    # Create rules_in_sections array
    rules_in_sections = []
    for rule_data in processed_data['data']['policy']['wanFirewall']['policy']['rules']:
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
    processed_data['data']['policy']['wanFirewall']['policy']['rules_in_sections'] = rules_in_sections
    
    # Reformat sections array to have index, section_id and section_name structure
    # Exclude the first section from export, excluding first section
    
    processed_sections = []
    # Add first section containing reserved SYSTEM rules as section_to_start_after_id
    for index, section_data in enumerate(processed_data['data']['policy']['wanFirewall']['policy']['sections']):
        processed_sections.append({
            "section_index": index,
            "section_name": section_data['section']['name']
        })

    if len(processed_data['data']['policy']['wanFirewall']['policy']['sections']) > 0:
        print(f"Excluded first section: {processed_data['data']['policy']['wanFirewall']['policy']['sections'][0]['section']['name']} containing reserved SYSTEM rules")
    
    # Replace the original sections array with the reformatted one
    processed_data['data']['policy']['wanFirewall']['policy']['sections'] = processed_sections
        
    # Write the processed data to the new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)    
    print(f"Successfully created {output_file}")
    

if __name__ == "__main__":
    main()

