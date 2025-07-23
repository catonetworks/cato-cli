import os
import json
import sys
from datetime import datetime
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID

def strip_ids_recursive(data):
    """Recursively strip id attributes from data structure, but only from objects that contain only 'id' and 'name' keys"""
    try:
        if isinstance(data, dict):
            # Check if this dict should have its 'id' stripped
            # Only strip 'id' if the object contains only 'id' and 'name' keys
            dict_keys = set(data.keys())
            should_strip_id = dict_keys == {'id', 'name'} or dict_keys == {'name', 'id'}
            
            result = {}
            for k, v in data.items():
                if k == 'id' and should_strip_id:
                    # Skip this 'id' key only if this object contains only id and name
                    continue
                else:
                    # Keep the key and recursively process the value
                    result[k] = strip_ids_recursive(v)
            return result
        elif isinstance(data, list):
            return [strip_ids_recursive(item) for item in data]
        else:
            return data
    except Exception as e:
        print(f"Error in strip_ids_recursive: {e}, data type: {type(data)}, data: {str(data)[:100]}")
        raise

def export_if_rules_to_json(args, configuration):
    """
    Export Internet Firewall rules to JSON format
    Adapted from scripts/export_if_rules_to_json.py
    """
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { internetFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } exceptions { name source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin } } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_ifw_rules = makeCall(args, configuration, policy_query)
            
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_ifw_rules)
        
        # Filter out rules with properties[0]=="SYSTEM"
        filtered_rules = []
        for rule_data in processed_data['data']['policy']['internetFirewall']['policy']['rules']:
            rule_properties = rule_data.get('properties', [])
            # Skip rules where the first property is "SYSTEM"
            if rule_properties and rule_properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
            else:
                filtered_rules.append(rule_data)
        
        processed_data['data']['policy']['internetFirewall']['policy']['rules'] = filtered_rules
        
        # Add index_in_section to each rule
        # Handle empty section names by assigning a default section name
        section_counters = {}
        for rule_data in processed_data['data']['policy']['internetFirewall']['policy']['rules']:
            section_name = rule_data['rule']['section']['name']
            # If section name is empty, use "Default Section" as the section name
            if not section_name or section_name.strip() == "":
                section_name = "Default Section"
                rule_data['rule']['section']['name'] = section_name
            
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
            # rule_info["enabled"] = True

        # Add rules_in_sections to the policy structure
        processed_data['data']['policy']['internetFirewall']['policy']['rules_in_sections'] = rules_in_sections
        
        # Reformat sections array to have index, section_id and section_name structure
        # Exclude the first section from export
        sections_with_ids = all_ifw_rules['data']['policy']['internetFirewall']['policy']['sections']
        processed_sections = [] 
        for index, section_data in enumerate(sections_with_ids):
            # print("sections_with_ids",json.dumps(section_data, indent=2))
            if index > 0:  # Skip the first section (index 0)
                processed_sections.append({
                    "section_index": index,
                    "section_name": section_data['section']['name'],
                    "section_id": section_data['section']['id']
                })
        
        # Replace the original sections array with the reformatted one
        processed_data['data']['policy']['internetFirewall']['policy']['sections'] = processed_sections
        
        # Handle timestamp in filename if requested
        filename_template = "all_ifw_rules_and_sections_{account_id}.json"
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_template = "all_ifw_rules_and_sections_{account_id}_" + timestamp + ".json"
            
        output_file = writeDataToFile(
            data=processed_data,
            args=args,
            account_id=account_id,
            default_filename_template=filename_template,
            default_directory="config_data"
        )

        return [{"success": True, "output_file": output_file, "account_id": account_id}]
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_wf_rules_to_json(args, configuration):
    """
    Export WAN Firewall rules to JSON format
    Adapted from scripts/export_wf_rules_to_json.py
    """
    try:
        account_id = getAccountID(args, configuration)
        
        policy_query = {
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { wanFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } direction exceptions { name source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin direction } } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_wf_rules = makeCall(args, configuration, policy_query)
                
        if not all_wf_rules or 'data' not in all_wf_rules:
            raise ValueError("Failed to retrieve data from API")
   
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_wf_rules)
        
        # Filter out rules with properties[0]=="SYSTEM"
        filtered_rules = []
        for rule_data in processed_data['data']['policy']['wanFirewall']['policy']['rules']:
            rule_properties = rule_data.get('properties', [])
            # Skip rules where the first property is "SYSTEM"
            if rule_properties and rule_properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
            else:
                filtered_rules.append(rule_data)
        
        processed_data['data']['policy']['wanFirewall']['policy']['rules'] = filtered_rules
        
        # Add index_in_section to each rule
        # Handle empty section names by assigning a default section name
        section_counters = {}
        for rule_data in processed_data['data']['policy']['wanFirewall']['policy']['rules']:
            section_name = rule_data['rule']['section']['name']
            # If section name is empty, use "Default Section" as the section name
            if not section_name or section_name.strip() == "":
                section_name = "Default Section"
                rule_data['rule']['section']['name'] = section_name
            
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
            # rule_info["enabled"] = True

        # Add rules_in_sections to the policy structure
        processed_data['data']['policy']['wanFirewall']['policy']['rules_in_sections'] = rules_in_sections
        
        # Reformat sections array to have index, section_id and section_name structure
        # Exclude the first section from export
        sections_with_ids = all_wf_rules['data']['policy']['wanFirewall']['policy']['sections']
        processed_sections = [] 
        for index, section_data in enumerate(sections_with_ids):
            processed_sections.append({
                "section_index": index+1,
                "section_name": section_data['section']['name'],
                "section_id": section_data['section']['id']
            })
        
        # Replace the original sections array with the reformatted one
        processed_data['data']['policy']['wanFirewall']['policy']['sections'] = processed_sections
        
        # Handle timestamp in filename if requested
        filename_template = "all_wf_rules_and_sections_{account_id}.json"
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_template = "all_wf_rules_and_sections_{account_id}_" + timestamp + ".json"
            
        output_file = writeDataToFile(
            data=processed_data,
            args=args,
            account_id=account_id,
            default_filename_template=filename_template,
            default_directory="config_data"
        )
        
        return [{"success": True, "output_file": output_file, "account_id": account_id}]
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]
