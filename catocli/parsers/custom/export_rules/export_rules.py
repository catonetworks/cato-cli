import os
import json
import sys
from datetime import datetime
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID

def strip_ids_recursive(data):
    """Recursively strip id attributes from data structure, but only from objects that contain only 'id' and 'name' keys.
    If a name contains a backslash character, keep the id and remove the name instead."""
    try:
        if isinstance(data, dict):
            # Check if this dict should have its 'id' stripped
            # Only strip 'id' if the object contains only 'id' and 'name' keys
            dict_keys = set(data.keys())
            should_strip_id = dict_keys == {'id', 'name'} or dict_keys == {'name', 'id'}
            
            # Check if name contains backslash
            name_has_backslash = should_strip_id and 'name' in data and isinstance(data['name'], str) and '\\' in data['name']
            
            result = {}
            for k, v in data.items():
                if name_has_backslash:
                    # If name contains backslash, keep id and skip name
                    if k == 'name':
                        continue
                    else:
                        result[k] = strip_ids_recursive(v)
                elif k == 'id' and should_strip_id:
                    # Normal case: Skip id key if this object contains only id and name
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
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { internetFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled activePeriod { effectiveFrom expiresAt useEffectiveFrom useExpiresAt } source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } exceptions { name source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } destination { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } country { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } remoteAsn containers { fqdnContainer { id name } ipAddressRangeContainer { id name } } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin } } properties ruleType subPolicy { id name } } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } subPolicies { policy { id name description enabled policyLevel } } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_ifw_rules = makeCall(args, configuration, policy_query)
            
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_ifw_rules)
        policy_node = processed_data['data']['policy']['internetFirewall']['policy']

        # Filter out rules with properties[0]=="SYSTEM"
        filtered_rules = []
        for rule_data in policy_node['rules']:
            rule_properties = rule_data.get('properties', [])
            # Skip rules where the first property is "SYSTEM"
            if rule_properties and rule_properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
            else:
                filtered_rules.append(rule_data)

        # The first section returned by the API is the account's built-in default
        # section (e.g. "Default Outbound Internet"). It cannot be created or
        # managed by the bulk terraform module, so exports always exclude it from
        # sections[] (same spirit as excluding SYSTEM rules), and any non-SYSTEM
        # rules or sub-policy scope rows that live in it are re-homed to the top
        # remaining main section so no rules_in_sections row references the
        # excluded section. rules[] arrives in exact policy order (default
        # section first), so re-homed rows number ahead of the top section's own
        # rules and relative order is preserved.
        sections_raw = policy_node.get('sections') or []
        default_section_name = sections_raw[0]['section']['name'] if sections_raw else None
        top_section_name = next(
            (s['section']['name'] for s in sections_raw[1:]
             if not s['section'].get('subPolicyId')),
            None
        )

        # Single-section tenant (new deployment): the default section is the only
        # one, so there is no "next section down" to re-home into. If anything
        # non-SYSTEM lives in it (plain rules or sub-policy scope rows - the path
        # split happens later, so filtered_rules still contains both), synthesize
        # a new managed section named "Corporate Rules" (section_id "" - it does
        # not exist live; terraform creates it on first apply, after which
        # re-exports see it as a normal top section and this branch never fires
        # again). A pristine tenant (only SYSTEM rules) synthesizes nothing.
        synthesize_top_section = False
        if top_section_name is None and default_section_name:
            needs_home = any(
                (rd['rule'].get('section') or {}).get('name') == default_section_name
                for rd in filtered_rules
            )
            if needs_home:
                top_section_name = "Corporate Rules"
                synthesize_top_section = True

        # Top-level sub-policy metadata (populated only on accounts that use sub-policies).
        # strip_ids_recursive does NOT strip ids here because each entry has more than
        # just {id, name} keys, so the real ids survive.
        sub_policies_meta = policy_node.pop('subPolicies', None) or []
        has_sub_policies = len(sub_policies_meta) > 0
        meta_by_name = {m['policy']['name']: m['policy'] for m in sub_policies_meta if m.get('policy')}

        if not has_sub_policies:
            # ---------------------------------------------------------------
            # LEGACY/FLAT PATH: byte-identical to today's shape, plus the new
            # (always-empty) "sub_policies" key. No other behavior changes.
            # ---------------------------------------------------------------
            # Add index_in_section to each rule
            # Handle empty section names by assigning a default section name
            section_counters = {}
            for rule_data in filtered_rules:
                rule_info = rule_data['rule']
                # Drop fields only relevant to sub-policy accounts so legacy
                # output stays byte-identical to today's shape.
                rule_data.pop('ruleType', None)
                rule_data.pop('subPolicy', None)
                rule_info['section'].pop('subPolicyId', None)

                section_name = rule_info['section']['name']
                # If section name is empty, use "Default Section" as the section name
                if not section_name or section_name.strip() == "":
                    section_name = "Default Section"
                    rule_info['section']['name'] = section_name
                elif section_name == default_section_name and top_section_name:
                    # Non-SYSTEM rule living in the excluded default section:
                    # re-home it to the top remaining section.
                    section_name = top_section_name
                    rule_info['section']['name'] = section_name

                if section_name not in section_counters:
                    section_counters[section_name] = 0
                section_counters[section_name] += 1
                rule_info['index_in_section'] = section_counters[section_name]

            # Create rules_in_sections array
            rules_in_sections = []
            for rule_data in filtered_rules:
                rule_info = rule_data['rule']
                rules_in_sections.append({
                    "index_in_section": rule_info['index_in_section'],
                    "section_name": rule_info['section']['name'],
                    "rule_name": rule_info['name']
                })
                rule_info.pop("index_in_section", None)
                rule_info.pop("index", None)
                # rule_info["enabled"] = True

            policy_node['rules'] = filtered_rules
            policy_node['rules_in_sections'] = rules_in_sections

            # Reformat sections array to have index, section_id and section_name structure
            # Exclude the first section from export
            sections_with_ids = policy_node['sections']
            processed_sections = []
            for index, section_data in enumerate(sections_with_ids):
                section_data['section'].pop('subPolicyId', None)
                if index > 0:  # Skip the first section (index 0)
                    processed_sections.append({
                        "section_index": index,
                        "section_name": section_data['section']['name'],
                        "section_id": section_data['section']['id']
                    })

            if synthesize_top_section:
                # Single-section tenant: emit the synthetic "Corporate Rules"
                # section the default-section rules were re-homed into.
                processed_sections.insert(0, {
                    "section_index": 1,
                    "section_name": top_section_name,
                    "section_id": ""
                })

            policy_node['sections'] = processed_sections
            policy_node['sub_policies'] = []
        else:
            # ---------------------------------------------------------------
            # SUB-POLICY PATH: see docs/ifw-sub-policy-json-design.md.
            # ---------------------------------------------------------------
            SCOPE_FIELDS = [
                'source', 'connectionOrigin', 'country', 'device', 'deviceOS',
                'deviceAttributes', 'connectionsOriginList'
            ]

            # --- sections: main sections and sub-sections, one flat array,
            # numbering restarts per-parent (no "skip the first" behavior here) ---
            main_counter = 0
            sub_section_counters = {}
            processed_sections = []
            for section_data in policy_node['sections']:
                section_info = section_data['section']
                sub_policy_id = section_info.get('subPolicyId')
                if not sub_policy_id:
                    if section_info['name'] == default_section_name:
                        # Always exclude the account's default section (same as
                        # the legacy path's skip-the-first behavior).
                        continue
                    main_counter += 1
                    processed_sections.append({
                        "section_index": main_counter,
                        "section_name": section_info['name'],
                        "section_id": section_info['id']
                    })
                else:
                    sub_policy_name = next(
                        (m['policy']['name'] for m in sub_policies_meta
                         if m.get('policy', {}).get('id') == sub_policy_id),
                        ''
                    )
                    sub_section_counters.setdefault(sub_policy_name, 0)
                    sub_section_counters[sub_policy_name] += 1
                    processed_sections.append({
                        "section_index": sub_section_counters[sub_policy_name],
                        "section_name": section_info['name'],
                        "section_id": section_info['id'],
                        "sub_policy_name": sub_policy_name
                    })
            if synthesize_top_section:
                # Single-section tenant: emit the synthetic "Corporate Rules"
                # section the default-section rules/scope rows were re-homed into.
                processed_sections.insert(0, {
                    "section_index": 1,
                    "section_name": top_section_name,
                    "section_id": ""
                })
            policy_node['sections'] = processed_sections

            # The API auto-creates a cleanup rule pinned LAST inside every
            # sub-policy (addSubPolicy materializes it). Its identity is
            # positional — the sub-policy's last rule (max rule.index) — so it
            # survives renames and manual moves. It is not exported as a normal
            # rule: it nests under its sub_policies[] entry as "cleanup_rule",
            # matching the cato_if_sub_policy resource which embeds and manages
            # it (like a socket site's default interface).
            cleanup_rule_ids = {}
            _cleanup_last_index = {}
            for rd in filtered_rules:
                if rd.get('ruleType') == 'SUB_POLICY_SCOPE':
                    continue
                spref = rd.get('subPolicy')
                if not spref or not spref.get('name'):
                    continue
                spn = spref['name']
                idx = rd['rule'].get('index', 0)
                if spn not in _cleanup_last_index or idx > _cleanup_last_index[spn]:
                    _cleanup_last_index[spn] = idx
                    cleanup_rule_ids[spn] = rd['rule'].get('id')
            cleanup_rules_out = {}

            # --- rules / sub_policies / rules_in_sections: single pass over
            # the flat rules[] array in exact API/UI order ---
            final_rules = []
            sub_policies_out = []
            rules_in_sections = []
            group_counters = {}

            for rule_data in filtered_rules:
                rule_info = rule_data['rule']
                rule_type = rule_data.pop('ruleType', 'POLICY_RULE')
                sub_policy_ref = rule_data.pop('subPolicy', None)

                if rule_type == 'SUB_POLICY_SCOPE':
                    sub_policy_name = rule_info['name']
                    section_name = rule_info['section']['name']
                    if section_name == default_section_name and top_section_name:
                        # Scope row living in the excluded default section:
                        # re-home it to the top remaining main section.
                        section_name = top_section_name

                    group_key = ('', section_name)
                    group_counters.setdefault(group_key, 0)
                    group_counters[group_key] += 1
                    rules_in_sections.append({
                        "index_in_section": group_counters[group_key],
                        "section_name": section_name,
                        "entry_type": "sub_policy",
                        "sub_policy_name": sub_policy_name
                    })

                    meta = meta_by_name.get(sub_policy_name, {})
                    scope = {
                        field: rule_info[field]
                        for field in SCOPE_FIELDS
                        if rule_info.get(field) is not None
                    }
                    # Two distinct enabled flags:
                    #   enabled       = subPolicies[].policy.enabled - the policy
                    #                   object's own flag; NOT settable via the
                    #                   public API (addSubPolicy has no enabled,
                    #                   there is no updateSubPolicy, and
                    #                   updatePolicy{state} has no policy
                    #                   selector) - informational only.
                    #   scope_enabled = the SUB_POLICY_SCOPE rule's enabled -
                    #                   manageable via updateRule; this is what
                    #                   terraform drives.
                    sub_policies_out.append({
                        "sub_policy_name": sub_policy_name,
                        "sub_policy_id": meta.get('id', ''),
                        "scope_rule_id": rule_info.get('id', ''),
                        "description": meta.get('description', rule_info.get('description', '')),
                        "enabled": meta.get('enabled', True),
                        "scope_enabled": rule_info.get('enabled', True),
                        "scope": scope
                    })
                    # Scope rows are not cato_if_rule resources - excluded from rules[].
                    continue

                # Normal rule (main-policy rule or sub-policy rule)
                sub_policy_name = sub_policy_ref.get('name') if sub_policy_ref else None
                section_name = rule_info['section']['name']

                # Sub-policy cleanup rule (the sub-policy's LAST rule): nest it
                # under sub_policies[] instead of emitting it as a normal rule.
                if sub_policy_name and rule_info.get('id') and rule_info['id'] == cleanup_rule_ids.get(sub_policy_name):
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"Nesting sub-policy cleanup rule under {sub_policy_name}: {rule_info['name']}")
                    rule_info.pop('index', None)
                    rule_info['section'] = {"name": section_name}
                    cleanup_rules_out[sub_policy_name] = rule_data
                    continue

                if not sub_policy_name:
                    # Main-policy rule: preserve the legacy empty-section fallback.
                    if not section_name or section_name.strip() == "":
                        section_name = "Default Section"
                    elif section_name == default_section_name and top_section_name:
                        # Re-home rules from the excluded default section.
                        section_name = top_section_name
                    rule_info['section'] = {"name": section_name}
                else:
                    # Sub-policy rule: "" is a valid, meaningful section name
                    # (sub-policy with no explicit sub-section) - don't rewrite it.
                    rule_info['section'] = {"name": section_name}

                group_key = (sub_policy_name or '', section_name)
                group_counters.setdefault(group_key, 0)
                group_counters[group_key] += 1

                ris_entry = {
                    "index_in_section": group_counters[group_key],
                    "section_name": section_name,
                    "rule_name": rule_info['name']
                }
                if sub_policy_name:
                    ris_entry["sub_policy_name"] = sub_policy_name
                rules_in_sections.append(ris_entry)

                rule_info.pop("index", None)
                if sub_policy_name:
                    rule_data["sub_policy_name"] = sub_policy_name
                final_rules.append(rule_data)

            # Attach each sub-policy's cleanup rule to its metadata entry.
            for sp in sub_policies_out:
                cleanup_entry = cleanup_rules_out.get(sp['sub_policy_name'])
                if cleanup_entry is not None:
                    sp['cleanup_rule'] = cleanup_entry

            policy_node['rules'] = final_rules
            policy_node['rules_in_sections'] = rules_in_sections
            policy_node['sub_policies'] = sub_policies_out

        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            # User provided custom filename
            base_filename = args.json_filename
            # Remove .json extension if provided, we'll add it back
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            # Use default filename template
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_ifw_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_ifw_rules_and_sections_{account_id}.json"
        
        if hasattr(args, 'verbose') and args.verbose:
            if hasattr(args, 'json_filename') and args.json_filename:
                print(f"Using custom filename template: {filename_template}")
            else:
                print(f"Using default filename template: {filename_template}")
            
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
        
        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            # User provided custom filename
            base_filename = args.json_filename
            # Remove .json extension if provided, we'll add it back
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            # Use default filename template
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_wf_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_wf_rules_and_sections_{account_id}.json"
        
        if hasattr(args, 'verbose') and args.verbose:
            if hasattr(args, 'json_filename') and args.json_filename:
                print(f"Using custom filename template: {filename_template}")
            else:
                print(f"Using default filename template: {filename_template}")
            
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

def export_wnw_rules_to_json(args, configuration):
    """
    Export WAN Network rules to JSON format
    """
    try:
        account_id = getAccountID(args, configuration)
        
        policy_query = {
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { wanNetwork { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled ruleType routeType source { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } site { id name } siteNetworkSubnet { id name } subnet systemGroup { id name } user { id name } usersGroup { id name } } destination { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } site { id name } siteNetworkSubnet { id name } subnet systemGroup { id name } user { id name } usersGroup { id name } } application { appCategory { id name } application { id name } customApp { id name } customCategory { id name } customService { port portRange { from to } protocol } customServiceIp { name ip ipRange { from to } } domain fqdn service { id name } } configuration { activeTcpAcceleration allocationIp { id name } backhaulingSite { id name } packetLossMitigation popLocation { id name } preserveSourcePort primaryTransport { primaryInterfaceRole secondaryInterfaceRole transportType } secondaryTransport { primaryInterfaceRole secondaryInterfaceRole transportType } } bandwidthPriority { id name } exceptions { name source { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } site { id name } siteNetworkSubnet { id name } subnet systemGroup { id name } user { id name } usersGroup { id name } } destination { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } site { id name } siteNetworkSubnet { id name } subnet systemGroup { id name } user { id name } usersGroup { id name } } application { appCategory { id name } application { id name } customApp { id name } customCategory { id name } customService { port portRange { from to } protocol } customServiceIp { name ip ipRange { from to } } domain fqdn service { id name } } } } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_wnw_rules = makeCall(args, configuration, policy_query)
                
        if not all_wnw_rules or 'data' not in all_wnw_rules:
            raise ValueError("Failed to retrieve data from API")
   
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_wnw_rules)
        
        # Filter out rules with properties[0]=="SYSTEM"
        filtered_rules = []
        for rule_data in processed_data['data']['policy']['wanNetwork']['policy']['rules']:
            rule_properties = rule_data.get('properties', [])
            # Skip rules where the first property is "SYSTEM"
            if rule_properties and rule_properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
            else:
                filtered_rules.append(rule_data)
        
        processed_data['data']['policy']['wanNetwork']['policy']['rules'] = filtered_rules
        
        # Add index_in_section to each rule
        # Handle empty section names by assigning a default section name
        section_counters = {}
        for rule_data in processed_data['data']['policy']['wanNetwork']['policy']['rules']:
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
        for rule_data in processed_data['data']['policy']['wanNetwork']['policy']['rules']:
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
        processed_data['data']['policy']['wanNetwork']['policy']['rules_in_sections'] = rules_in_sections
        
        # Reformat sections array to have index, section_id and section_name structure
        # Exclude the first section from export
        sections_with_ids = all_wnw_rules['data']['policy']['wanNetwork']['policy']['sections']
        processed_sections = [] 
        for index, section_data in enumerate(sections_with_ids):
            processed_sections.append({
                "section_index": index+1,
                "section_name": section_data['section']['name'],
                "section_id": section_data['section']['id']
            })
        
        # Replace the original sections array with the reformatted one
        processed_data['data']['policy']['wanNetwork']['policy']['sections'] = processed_sections
        
        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            # User provided custom filename
            base_filename = args.json_filename
            # Remove .json extension if provided, we'll add it back
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            # Use default filename template
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_wnw_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_wnw_rules_and_sections_{account_id}.json"
        
        if hasattr(args, 'verbose') and args.verbose:
            if hasattr(args, 'json_filename') and args.json_filename:
                print(f"Using custom filename template: {filename_template}")
            else:
                print(f"Using default filename template: {filename_template}")
            
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

def export_tls_rules_to_json(args, configuration):
    """
    Export TLS Inspection rules to JSON format
    Adapted from scripts/export_tls_rules_to_json.py
    """
    try:
        account_id = getAccountID(args, configuration)
        
        policy_query = {
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { tlsInspect { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name } enabled source { user { id name } floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } subnet ipRangeTlsInspectSource: ipRange { from to } networkInterface { id name } site { id name } systemGroup { id name } usersGroup { id name } ip siteNetworkSubnet { id name } } platform country { id name } devicePostureProfile { id name } connectionOrigin application { application { id name } appCategory { id name } country { id name } customApp { id name } customCategory { id name } customServiceIp { name ip ipRange { from to } } domain fqdn subnet ip ipRangeTlsInspectApplication: ipRange { from to } globalIpRange { id name } customService { port portRange { from to } protocol } remoteAsn service { id name } tlsInspectCategory } action untrustedCertificateAction } properties } sections { audit { updatedTime updatedBy } section { id name } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } additionalAttributes { defaultRuleAction defaultRuleUntrustedCertificateAction } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_tls_rules = makeCall(args, configuration, policy_query)
                
        if not all_tls_rules or 'data' not in all_tls_rules:
            raise ValueError("Failed to retrieve data from API")
   
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_tls_rules)
        
        # Filter out rules with properties[0]=="SYSTEM"
        filtered_rules = []
        for rule_data in processed_data['data']['policy']['tlsInspect']['policy']['rules']:
            rule_properties = rule_data.get('properties', [])
            # Skip rules where the first property is "SYSTEM"
            if rule_properties and rule_properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule']['name']}")
            else:
                filtered_rules.append(rule_data)
        
        processed_data['data']['policy']['tlsInspect']['policy']['rules'] = filtered_rules
        
        # Add index_in_section to each rule
        # Handle empty section names by assigning a default section name
        section_counters = {}
        for rule_data in processed_data['data']['policy']['tlsInspect']['policy']['rules']:
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
        for rule_data in processed_data['data']['policy']['tlsInspect']['policy']['rules']:
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
        processed_data['data']['policy']['tlsInspect']['policy']['rules_in_sections'] = rules_in_sections
        
        # Reformat sections array to have index, section_id and section_name structure
        # Exclude the first section from export
        sections_with_ids = all_tls_rules['data']['policy']['tlsInspect']['policy']['sections']
        processed_sections = [] 
        for index, section_data in enumerate(sections_with_ids):
            processed_sections.append({
                "section_index": index+1,
                "section_name": section_data['section']['name'],
                "section_id": section_data['section']['id']
            })
        
        # Replace the original sections array with the reformatted one
        processed_data['data']['policy']['tlsInspect']['policy']['sections'] = processed_sections
        
        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            # User provided custom filename
            base_filename = args.json_filename
            # Remove .json extension if provided, we'll add it back
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            # Use default filename template
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_tls_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_tls_rules_and_sections_{account_id}.json"
        
        if hasattr(args, 'verbose') and args.verbose:
            if hasattr(args, 'json_filename') and args.json_filename:
                print(f"Using custom filename template: {filename_template}")
            else:
                print(f"Using default filename template: {filename_template}")
            
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