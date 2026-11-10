import copy
import os
import json
import shutil
import sys
from datetime import datetime, timezone
from graphql_client.api.call_api import ApiClient, CallApi
from graphql_client.api_client import ApiException
from ..customLib import writeDataToFile, makeCall, getAccountID
from ..export_deps.export_deps import (
    strip_groups_ids,
    strip_global_ip_ranges_ids,
    strip_custom_apps_ids,
    strip_fqdn_containers_ids,
    strip_ip_range_containers_ids,
    strip_mailing_lists_ids,
    strip_subscription_groups_ids,
    strip_dhcp_relay_groups_ids,
    strip_static_hosts_ids,
    strip_webhooks_ids,
)
from ..export_sites.export_sites import strip_socket_site_ids

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


def _find_policy_node(data):
    """Locate the single policy-family node inside a raw `catocli export
    <rules_type>` JSON payload - e.g.
    data['data']['policy']['internetFirewall']['policy']. Every one of the
    18 rules-type exports shares the same GraphQL-derived signature at that
    node: an 'enabled' flag, a 'rules' list, and a 'revision' dict (see each
    export_*_rules_to_json function's policy_query) - matching on that
    signature means one traversal works across every type without
    hardcoding each type's policy_key (internetFirewall, wanFirewall, ...),
    and without depending on which ordering key a type uses
    (rules_in_sections for most types, rules_in_policy for pa_rules).
    Returns None if no such node is found (defensive - a malformed or
    unrecognized export)."""
    if isinstance(data, dict):
        if isinstance(data.get('rules'), list) and isinstance(data.get('revision'), dict):
            return data
        for v in data.values():
            found = _find_policy_node(v)
            if found is not None:
                return found
    return None


def _strip_rule_wrapper_id(rule_wrapper):
    """rule_wrapper is the {"audit": ..., "rule": {...}, "properties": [...]}
    shape every rules[] entry (and sub_policies[].cleanup_rule) uses - pop
    the embedded rule's own 'id' (the brownfield-import key) in place, if
    present."""
    if isinstance(rule_wrapper, dict):
        inner = rule_wrapper.get('rule')
        if isinstance(inner, dict):
            inner.pop('id', None)


def strip_policy_rules_ids(data):
    """Pure transform: strip brownfield-import-key ids from a full `catocli
    export <rules_type>` JSON payload (as written by any of the 18 export
    handlers, or read back from its output file) - each rule's own
    `rule.id`, each `sections[]` entry's `section_id`, and each
    `sub_policies[]` entry's `sub_policy_id`/`scope_rule_id` (plus its
    nested `cleanup_rule`'s `rule.id`, for sub-policy-capable types: if_rules,
    wf_rules, lan_fw_rules). Never touches names, `rules_in_sections` /
    `rules_in_policy` (ordering is name-based - see CLAUDE.md), or anything
    else.

    Embedded entity references inside rule criteria (source.group[].id,
    destination.application[].id, etc.) need no handling here: every such
    {id, name} reference is ALREADY stripped of its id unconditionally, at
    export time, by strip_ids_recursive above (called by every
    export_*_rules_to_json function before this transform would ever run) -
    whenever a name sibling exists. The only ids strip_ids_recursive
    deliberately leaves in place are id-only reference types with no name
    sibling (e.g. a bare id + several other fields) - the documented
    manual-resolution cases - so there is nothing left to strip for those.

    Returns a new dict; does not mutate the input (so an archived raw copy
    made from the same in-memory object, if any, stays untouched)."""
    data = copy.deepcopy(data)
    policy_node = _find_policy_node(data)
    if policy_node is None:
        return data

    for rule_wrapper in policy_node.get('rules') or []:
        _strip_rule_wrapper_id(rule_wrapper)

    for section in policy_node.get('sections') or []:
        if isinstance(section, dict):
            section.pop('section_id', None)

    for sub_policy in policy_node.get('sub_policies') or []:
        if isinstance(sub_policy, dict):
            sub_policy.pop('sub_policy_id', None)
            sub_policy.pop('scope_rule_id', None)
            _strip_rule_wrapper_id(sub_policy.get('cleanup_rule'))

    return data


# Export type -> pure strip function, for every dependency type that ships
# a native --strip-ids flag in export_deps.py. Shared by export_all_to_json's
# --strip-ids post-processing pass below, so `catocli export <type>
# --strip-ids` and `catocli export all --strip-ids` always produce
# byte-identical output for these types - no second, drifting
# implementation. socket_sites and the 18 *_rules types are handled
# separately in _strip_exported_payload (different shapes; see there).
_DEPENDENCY_STRIP_FUNCS = {
    'groups': strip_groups_ids,
    'global_ip_ranges': strip_global_ip_ranges_ids,
    'custom_apps': strip_custom_apps_ids,
    'fqdn_containers': strip_fqdn_containers_ids,
    'ip_range_containers': strip_ip_range_containers_ids,
    'mailing_lists': strip_mailing_lists_ids,
    'subscription_groups': strip_subscription_groups_ids,
    'dhcp_relay_groups': strip_dhcp_relay_groups_ids,
    'static_hosts': strip_static_hosts_ids,
    'webhooks': strip_webhooks_ids,
}


def _strip_exported_payload(export_type, data):
    """Dispatch to the correct pure strip transform for `export all
    --strip-ids`'s post-processing pass, based on export_type:
      - one of the dependency types in _DEPENDENCY_STRIP_FUNCS: the same
        function `catocli export <type> --strip-ids` calls natively
        (export_deps.py) - data is the bare JSON list those exports write.
      - 'socket_sites': strip_socket_site_ids (export_sites.py) - data is
        the {"sites": [...]} dict that export writes.
      - any of the 18 `*_rules` types: strip_policy_rules_ids (above) -
        data is the full nested GraphQL-shaped payload those exports write.
      - anything else (a future export type with no strip support yet):
        returned unchanged - defensive passthrough, never an error.
    """
    strip_func = _DEPENDENCY_STRIP_FUNCS.get(export_type)
    if strip_func is not None:
        return strip_func(data)
    if export_type == 'socket_sites':
        return strip_socket_site_ids(data)
    if export_type.endswith('_rules'):
        return strip_policy_rules_ids(data)
    return data


def _strip_output_file_in_place(export_type, output_file):
    """Load output_file's JSON, apply _strip_exported_payload for
    export_type, and overwrite output_file with the stripped result.

    Used only by export_all_to_json's --strip-ids post-processing, and only
    AFTER the raw file has already been archived (see that function's
    docstring): one API call per type, archive the raw copy first, then
    strip the primary file in place - so the API is never called a second
    time to produce the stripped version, and --archive-directory always
    keeps the id-bearing raw original regardless of --strip-ids.

    Returns (ok: bool, error: str or None)."""
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            raw_content = json.load(f)
    except Exception as e:
        return False, f"could not read '{output_file}' for --strip-ids post-processing: {e}"

    try:
        stripped_content = _strip_exported_payload(export_type, raw_content)
    except Exception as e:
        return False, f"--strip-ids transform failed: {e}"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stripped_content, f, indent=2)
            f.write('\n')
    except Exception as e:
        return False, f"could not write stripped content back to '{output_file}': {e}"

    return True, None


# Ported from the reference-architecture repo's scripts/migrate_tenant.py
# (CHECKLIST_TEMPLATE) - see that script's module docstring for the
# original tenant-migration-export design this generalizes. Adapted here to
# cover every type `catocli export all --strip-ids` can produce, including
# the 18 *_rules policy types migrate_tenant.py never touched.
EXPORT_ALL_CHECKLIST_TEMPLATE = """\
# Tenant migration checklist

Generated {generated_at} by `{generated_by}`. This directory is a READ-ONLY
export capture -- nothing was applied or imported anywhere. Everything below
must be resolved by a human, in the TARGET tenant, before any of this is
applied there.

## Before doing anything else

- [ ] Run your config-data validator (e.g. the reference-architecture repo's
      `scripts/validate_config_data.py --config-data {output_dir}`) against
      this directory and fix any ERRORs it reports before copying anything
      into a target repo's `config_data/`. NOTE: because this export was
      deliberately stripped of source-tenant ids, the validator WILL report
      "missing id field" errors for every dependency/static-host object,
      every site, and every policy rule/section -- that's expected at this
      stage (the ids don't exist yet; the target tenant assigns its own on
      creation/apply). Focus on everything else it reports (duplicate
      names, dangling `rules_in_sections`/`rules_in_policy` references,
      cross-file ref warnings); re-run the validator for a genuinely clean
      result only after re-exporting from the TARGET tenant post-apply.

## Manual re-resolution required

- [ ] **Group members with id-only types.** `--strip-ids` keeps `{{type, name}}`
      for every group member it CAN resolve by name, but the following member
      types are only addressable by id in the source tenant today, so their
      `id` was stripped with no name-based fallback: `FLOATING_SUBNET`,
      `HOST`, `NETWORK_INTERFACE`, `SITE_NETWORK_SUBNET`. Inspect
      `groups.json` for members of these types and re-resolve each one's id
      in the TARGET tenant via `catocli entity entityLookup` (or the
      equivalent MCP/UI lookup) before applying.

- [ ] **Mailing-list admin ids.** The mailing-list admin reference REQUIRES an
      id -- `--strip-ids` on `mailing_lists.json` necessarily drops each
      admin's id and keeps only `{{name}}`. Re-resolve each admin's id in the
      TARGET tenant (e.g. `catocli entity entityLookup`) before this file can
      be applied there.

- [ ] **Wi-Fi PSKs.** The Cato API never returns Wi-Fi passkeys on export --
      `socket_sites.json`'s `wifi_ssids[]` entries with `security.mode ==
      "PSK"` have no passkey value, stripped or otherwise. Supply each one
      in the TARGET tenant's site/Wi-Fi configuration, keyed by site and SSID
      name.

- [ ] **Licenses.** `socket_sites.json` has had `license_id` and
      `license_bw` stripped from every site (they're source-tenant-specific
      and meaningless in the target). Re-assign a license to each site in
      the TARGET tenant as part of onboarding.

- [ ] **Physical socket re-registration.** Exporting/importing JSON does not
      move hardware. Every physical socket behind a migrated site must be
      physically re-registered against the TARGET account (new registration
      code) -- applying this config alone will not make a socket appear in
      the new tenant.

## Policy rule files

Every `*_rules`-type file in this export has had its brownfield-import-key
ids stripped (each rule's `id`, each section's `section_id`, and each
sub-policy's `sub_policy_id`/`scope_rule_id`) -- rule/section names and the
`rules_in_sections`/`rules_in_policy` ordering arrays are untouched (ordering
is name-based), so these files apply cleanly to a greenfield target policy
with no further action required here.

## Files in this export

{file_list}
"""


def _write_export_all_checklist(output_directory, filenames, generated_by):
    """Write CHECKLIST.md into output_directory (see EXPORT_ALL_CHECKLIST_TEMPLATE)
    and return its path. Only called when --strip-ids is set."""
    file_list = "\n".join(f"- `{name}`" for name in sorted(filenames)) or "(none - every requested type failed)"
    content = EXPORT_ALL_CHECKLIST_TEMPLATE.format(
        generated_at=datetime.now(timezone.utc).isoformat(),
        generated_by=generated_by,
        output_dir=output_directory,
        file_list=file_list,
    )
    path = os.path.join(output_directory, "CHECKLIST.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path


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
        # Sub-policy references are structural keys, including names containing backslashes.
        # Entity selector normalization must not remove those names.
        raw_rules = all_ifw_rules['data']['policy']['internetFirewall']['policy']['rules']
        for row, raw_row in zip(policy_node['rules'], raw_rules):
            if raw_row.get('subPolicy'):
                row['subPolicy'] = dict(raw_row['subPolicy'])

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
                # Empty section name is the canonical implicit-default-section
                # sentinel ("" = rule at the policy root, no explicit section).
                # Preserve it verbatim -- consumers (bulk modules, validator,
                # importers) key on "".
                if not section_name or section_name.strip() == "":
                    section_name = ""
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
                    # Main-policy rule: "" is the canonical implicit-default-
                    # section sentinel (rule at the policy root) -- preserve it.
                    if not section_name or section_name.strip() == "":
                        section_name = ""
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
    Export WAN Firewall rules to JSON format. Mirrors the Internet Firewall
    exporter (incl. sub-policy / cleanup-rule handling - see
    docs/ifw-sub-policy-json-design.md), except that WAN Firewall has no
    API-default section to exclude, so no section exclusion/re-homing applies.
    """
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { wanFirewall { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled activePeriod { effectiveFrom expiresAt useEffectiveFrom useExpiresAt } source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } connectionOrigin country { id name } device { id name } deviceOS deviceAttributes { category type model manufacturer os osVersion } destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframePolicySchedule: customTimeframe { from to } customRecurringPolicySchedule: customRecurring { from to days } } direction exceptions { name source { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } deviceOS destination { host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } country { id name } device { id name } deviceAttributes { category type model manufacturer os osVersion } application { application { id name } appCategory { id name } customApp { id name } customCategory { id name } sanctionedAppsCategory { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { standard { id name } custom { port portRangeCustomService: portRange { from to } protocol } } connectionOrigin direction } } properties ruleType subPolicy { id name } } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } subPolicies { policy { id name description enabled policyLevel } } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }",
            "variables": {
                "accountId": account_id
            },
            "operationName": "policy"
        }
        all_wf_rules = makeCall(args, configuration, policy_query)
            
        # Processing data to strip id attributes
        processed_data = strip_ids_recursive(all_wf_rules)
        policy_node = processed_data['data']['policy']['wanFirewall']['policy']

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
        # WAN Firewall has no API-default section: nothing is excluded or
        # re-homed, so the default-section machinery below stays inert.
        default_section_name = None
        top_section_name = None

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
                # Empty section name is the canonical implicit-default-section
                # sentinel ("" = rule at the policy root, no explicit section).
                # Preserve it verbatim -- consumers (bulk modules, validator,
                # importers) key on "".
                if not section_name or section_name.strip() == "":
                    section_name = ""
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
            sections_with_ids = policy_node['sections']
            processed_sections = []
            for index, section_data in enumerate(sections_with_ids):
                section_data['section'].pop('subPolicyId', None)
                processed_sections.append({
                    "section_index": index + 1,
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
                'deviceAttributes', 'connectionsOriginList', 'direction'
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
            # matching the cato_wf_sub_policy resource which embeds and manages
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
                    # Main-policy rule: "" is the canonical implicit-default-
                    # section sentinel (rule at the policy root) -- preserve it.
                    if not section_name or section_name.strip() == "":
                        section_name = ""
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
            # Empty section name is the canonical implicit-default-section
            # sentinel ("" = rule at the policy root) -- preserve it verbatim.
            if not section_name or section_name.strip() == "":
                section_name = ""
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

# Hand-crafted Application Control policy query (generated from introspection; omits
# access/metadata payloads). Flat policy: sections + rules, no sub-policies.
APC_POLICY_QUERY = 'query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { applicationControl { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled ruleType applicationRule { application { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } applicationType } applicationActivitySatisfy applicationActivity { activity { id name } field { id name } operator value valueSet { id name } } applicationContext { applicationTenant { operator value valueSet { id name } } } accessMethod { accessMethod operator value valueSet { id name } } source { country { id name } host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } device { id name } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframe { from to } customRecurring { from to days } } severity applicationCriteriaSatisfy applicationCriteria { attributes { complianceAttributes { iso27001 sox hippa soc1 soc2 soc3 isae3402 pciDss } securityAttributes { mfa encryptionAtRest auditTrail rbac rememberPassword sso trustedCertificate tlsEnforcement httpSecurityHeaders } } originCountry { id name } risk { risk riskOperator } aiRisk } actionConfig { userNotification { id name } } } dataRule { application { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } applicationType } applicationContext { applicationTenant { operator value valueSet { id name } } } applicationActivitySatisfy applicationActivity { activity { id name } field { id name } operator value valueSet { id name } } accessMethod { accessMethod operator value valueSet { id name } } source { country { id name } host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } device { id name } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframe { from to } customRecurring { from to days } } severity fileAttributeSatisfy fileAttribute { fileAttribute operator value contentTypeValues { id name } contentTypeGroupValues { id name } } dlpProfile { contentProfile { id name } edmProfile { id name } } applicationCriteriaSatisfy applicationCriteria { attributes { complianceAttributes { iso27001 sox hippa soc1 soc2 soc3 isae3402 pciDss } securityAttributes { mfa encryptionAtRest auditTrail rbac rememberPassword sso trustedCertificate tlsEnforcement httpSecurityHeaders } } originCountry { id name } risk { risk riskOperator } aiRisk } actionConfig { userNotification { id name } } } fileRule { application { application { id name } customApp { id name } appCategory { id name } customCategory { id name } sanctionedAppsCategory { id name } applicationType } applicationContext { applicationTenant { operator value valueSet { id name } } } applicationActivitySatisfy applicationActivity { activity { id name } field { id name } operator value valueSet { id name } } accessMethod { accessMethod operator value valueSet { id name } } source { country { id name } host { id name } site { id name } subnet ip ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } } device { id name } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } schedule { activeOn customTimeframe { from to } customRecurring { from to days } } severity fileAttributeSatisfy fileAttribute { fileAttribute operator value contentTypeValues { id name } contentTypeGroupValues { id name } } applicationCriteriaSatisfy applicationCriteria { attributes { complianceAttributes { iso27001 sox hippa soc1 soc2 soc3 isae3402 pciDss } securityAttributes { mfa encryptionAtRest auditTrail rbac rememberPassword sso trustedCertificate tlsEnforcement httpSecurityHeaders } } originCountry { id name } risk { risk riskOperator } aiRisk } actionConfig { userNotification { id name } } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } additionalAttributes { dataControlEnabled } } } } }'


def export_apc_rules_to_json(args, configuration):
    """Export Application Control rules to the bulk-module JSON shape.

    Flat structure: sections[], rules[] (wrapper {audit, rule, properties},
    ids retained for brownfield import), rules_in_sections[] ordering rows.
    SYSTEM and LOCKED rules (built-in, not manageable via the API) are
    excluded.
    Only the typed-rule variant matching ruleType is exported; fields with no
    terraform surface (applicationCriteria/Context) are dropped."""
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": APC_POLICY_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy']['applicationControl']['policy']
        policy_node.pop('additionalAttributes', None)

        filtered_rules = []
        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            if any(p in ("SYSTEM", "LOCKED") for p in properties):
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding {properties} rule: {rule_data['rule'].get('name')}")
                continue
            rule_data.pop('metadata', None)
            filtered_rules.append(rule_data)

        # Keep only the ACTIVE typed-rule variant (the API returns default
        # shells for all three); drop fields with no terraform surface.
        for rule_data in filtered_rules:
            rule_info = rule_data['rule']
            rule_type = rule_info.get('ruleType')
            keep = {'APPLICATION': 'applicationRule', 'DATA': 'dataRule', 'FILE': 'fileRule'}.get(rule_type)
            for variant in ('applicationRule', 'dataRule', 'fileRule'):
                if variant != keep:
                    rule_info.pop(variant, None)
            active = rule_info.get(keep) or {}
            # No terraform surface for these (provider injects empty inputs):
            for unsupported in ('applicationCriteria', 'applicationCriteriaSatisfy', 'applicationContext'):
                active.pop(unsupported, None)

        processed_sections = []
        for index, section_data in enumerate(policy_node.get('sections') or []):
            info = section_data.get('section') or {}
            processed_sections.append({
                "section_index": index + 1,
                "section_name": info.get('name'),
                "section_id": info.get('id', ''),
            })

        rules_in_sections = []
        section_counters = {}
        for rule_data in filtered_rules:
            rule_info = rule_data['rule']
            section_name = (rule_info.get('section') or {}).get('name') or ''
            section_counters.setdefault(section_name, 0)
            section_counters[section_name] += 1
            rules_in_sections.append({
                "index_in_section": section_counters[section_name],
                "section_name": section_name,
                "rule_name": rule_info.get('name'),
            })
            rule_info.pop('index', None)
            rule_info['section'] = {"name": section_name}

        policy_node['rules'] = filtered_rules
        policy_node['sections'] = processed_sections
        policy_node['rules_in_sections'] = rules_in_sections

        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_apc_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_apc_rules_and_sections_{account_id}.json"

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


# Hand-crafted App Tenant Restriction policy query (generated from introspection; omits
# access/metadata payloads). Flat policy: sections + rules, no sub-policies.
ATR_POLICY_QUERY = 'query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { appTenantRestriction { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled application { id name } headers { name value } source { ip host { id name } site { id name } subnet ipRange { from to } globalIpRange { id name } networkInterface { id name } siteNetworkSubnet { id name } floatingSubnet { id name } user { id name } usersGroup { id name } group { id name } systemGroup { id name } country { id name } } schedule { activeOn customTimeframe { from to } customRecurring { from to days } } action severity } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }'


def export_atr_rules_to_json(args, configuration):
    """Export App Tenant Restriction rules to the bulk-module JSON shape.

    Flat structure: sections[], rules[] (wrapper {audit, rule, properties},
    ids retained for brownfield import), rules_in_sections[] ordering rows.
    SYSTEM and LOCKED rules (built-in, not manageable via the API) are
    excluded."""
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": ATR_POLICY_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy']['appTenantRestriction']['policy']
        policy_node.pop('additionalAttributes', None)

        filtered_rules = []
        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            if any(p in ("SYSTEM", "LOCKED") for p in properties):
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding {properties} rule: {rule_data['rule'].get('name')}")
                continue
            rule_data.pop('metadata', None)
            filtered_rules.append(rule_data)

        processed_sections = []
        for index, section_data in enumerate(policy_node.get('sections') or []):
            info = section_data.get('section') or {}
            processed_sections.append({
                "section_index": index + 1,
                "section_name": info.get('name'),
                "section_id": info.get('id', ''),
            })

        rules_in_sections = []
        section_counters = {}
        for rule_data in filtered_rules:
            rule_info = rule_data['rule']
            section_name = (rule_info.get('section') or {}).get('name') or ''
            section_counters.setdefault(section_name, 0)
            section_counters[section_name] += 1
            rules_in_sections.append({
                "index_in_section": section_counters[section_name],
                "section_name": section_name,
                "rule_name": rule_info.get('name'),
            })
            rule_info.pop('index', None)
            rule_info['section'] = {"name": section_name}

        policy_node['rules'] = filtered_rules
        policy_node['sections'] = processed_sections
        policy_node['rules_in_sections'] = rules_in_sections

        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_atr_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_atr_rules_and_sections_{account_id}.json"

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


# Hand-crafted privateAccess policy query. Flat ordered rule list - sections
# exist in the API payload but are not yet supported by the terraform
# resources ("1st phase"); live policies return sections: [].
PA_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { privateAccess { policy { enabled rules { audit { updatedTime updatedBy } properties rule { id name description index section { id name subPolicyId } enabled source { user { id name } usersGroup { id name } systemGroup { id name } } platform country { id name } applications { application { id name } } connectionsOriginList action { action } tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } device { id name } userAttributes { riskScore { category operator } } schedule { activeOn customTimeframe { from to } customRecurring { from to days } } activePeriod { useEffectiveFrom effectiveFrom useExpiresAt expiresAt } } } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_pa_rules_to_json(args, configuration):
    """Export Private Access rules to the bulk-module JSON shape.

    Flat ordered rule list (no sections in the terraform surface yet, no
    sub-policies): rules[] wrappers ({audit, rule, properties}, ids retained
    for brownfield import) plus rules_in_policy[] ordering rows
    ({index_in_policy, rule_name})."""
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": PA_POLICY_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy']['privateAccess']['policy']

        filtered_rules = []
        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            if properties and properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule'].get('name')}")
                continue
            rule_data.pop('metadata', None)
            filtered_rules.append(rule_data)

        rules_in_policy = []
        for position, rule_data in enumerate(filtered_rules):
            rule_info = rule_data['rule']
            rules_in_policy.append({
                "index_in_policy": position + 1,
                "rule_name": rule_info.get('name'),
            })
            rule_info.pop('index', None)
            rule_info.pop('section', None)

        # Sections are not yet supported by the terraform private-access
        # resources; surface them untransformed for visibility (live: []).
        processed_sections = []
        for index, section_data in enumerate(policy_node.get('sections') or []):
            info = section_data.get('section') or {}
            processed_sections.append({
                "section_index": index + 1,
                "section_name": info.get('name'),
                "section_id": info.get('id', ''),
            })

        policy_node['rules'] = filtered_rules
        policy_node['sections'] = processed_sections
        policy_node['rules_in_policy'] = rules_in_policy

        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_pa_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_pa_rules_and_sections_{account_id}.json"

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


# Hand-crafted ztnaAlwaysOn policy query. Flat policy: sections + rules only
# (no sub-policies exist for this policy type). Omits access/metadata payloads.
AO_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { ztnaAlwaysOn { policy { enabled rules { audit { updatedTime updatedBy } properties rule { id name description index section { id name } enabled source { user { id name } usersGroup { id name } } platform devicePostureProfile { id name } action allowUserBypass bypassDuration { time unit } allowFailOpen antiTamperMode } } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_ao_rules_to_json(args, configuration):
    """Export ZTNA Always-On rules to the bulk-module JSON shape.

    Flat structure (no sub-policies): sections[], rules[] (wrapper
    {audit, rule, properties}, ids retained for brownfield import), and
    rules_in_sections[] ordering rows. Sectionless policies export rules with
    section name "" and an empty sections[]."""
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": AO_POLICY_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy']['ztnaAlwaysOn']['policy']

        # SYSTEM filter (defensive - none observed live for this policy type)
        filtered_rules = []
        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            if properties and properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM rule: {rule_data['rule'].get('name')}")
                continue
            filtered_rules.append(rule_data)

        processed_sections = []
        for index, section_data in enumerate(policy_node.get('sections') or []):
            info = section_data.get('section') or {}
            # subPolicyId is selected only so the {id,name} ref survives
            # strip_ids_recursive (always null - no sub-policies for this type)
            processed_sections.append({
                "section_index": index + 1,
                "section_name": info.get('name'),
                "section_id": info.get('id', ''),
            })

        rules_in_sections = []
        section_counters = {}
        for rule_data in filtered_rules:
            rule_info = rule_data['rule']
            section_name = (rule_info.get('section') or {}).get('name') or ''
            section_counters.setdefault(section_name, 0)
            section_counters[section_name] += 1
            rules_in_sections.append({
                "index_in_section": section_counters[section_name],
                "section_name": section_name,
                "rule_name": rule_info.get('name'),
            })
            rule_info.pop('index', None)
            rule_info['section'] = {"name": section_name}

        policy_node['rules'] = filtered_rules
        policy_node['sections'] = processed_sections
        policy_node['rules_in_sections'] = rules_in_sections

        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_ao_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_ao_rules_and_sections_{account_id}.json"

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


# Hand-crafted socketLan policy query (generated from introspection). The
# catocli-generated query selects `access` on nested firewall rules, which the
# backend returns as null against a non-nullable EntityAccess and the whole
# query 500s - so `access` is omitted everywhere, as are metadata payloads.
LANFW_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { socketLan { policy { id name description enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled firewall { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled source { vlan mac ipRange { from to } group { id name } subnet site { id name } networkInterface { id name } systemGroup { id name } host { id name } ip globalIpRange { id name } floatingSubnet { id name } siteNetworkSubnet { id name } } destination { vlan ipRange { from to } subnet site { id name } networkInterface { id name } systemGroup { id name } host { id name } ip globalIpRange { id name } group { id name } floatingSubnet { id name } siteNetworkSubnet { id name } } direction application { application { id name } customApp { id name } domain fqdn ip subnet ipRange { from to } globalIpRange { id name } } service { simple { name } standard { id name } custom { port portRange { from to } protocol } } action tracking { event { enabled } alert { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } } properties ruleType subPolicy { id name } } site { site { id name } group { id name } } source { vlan ipRange { from to } group { id name } subnet networkInterface { id name } systemGroup { id name } host { id name } ip globalIpRange { id name } floatingSubnet { id name } siteNetworkSubnet { id name } } destination { vlan ipRange { from to } subnet networkInterface { id name } systemGroup { id name } host { id name } ip globalIpRange { id name } group { id name } floatingSubnet { id name } siteNetworkSubnet { id name } } direction service { simple { name } custom { port portRange { from to } protocol } } nat { enabled natType } transport } properties ruleType subPolicy { id name } } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } subPolicies { policy { id name description enabled policyLevel audit { publishedTime publishedBy } } properties } } revisions { revision { id name description changes createdTime updatedTime } } } } }"


def export_lan_fw_rules_to_json(args, configuration):
    """Export LAN Firewall (socketLan) rules to the bulk-module JSON shape.

    Structure (see docs/lanfw-bulk-json-design.md in the reference-architecture
    repo): network_rules[] with nested firewall_rules[], sections[] (main and
    sub-policy-owned), sub_policies[] (scope rows lifted out of the rule list),
    and rules_in_sections[] ordering rows for sections <-> network rules. Child
    firewall ordering is the nested array order.
    """
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": LANFW_POLICY_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy']['socketLan']['policy']
        processed_data['data']['policy']['socketLan'].pop('revisions', None)

        for noise in ('id', 'name', 'description', 'access'):
            policy_node.pop(noise, None)

        sub_policies_meta = policy_node.pop('subPolicies', None) or []
        meta_by_name = {m['policy']['name']: m['policy'] for m in sub_policies_meta if m.get('policy')}
        sub_name_by_id = {p['id']: name for name, p in meta_by_name.items() if p.get('id')}

        # --- sections: main and sub-policy-owned, one flat array; numbering is
        # parent-scoped. The sub-policy link is explicit (section.subPolicyId).
        processed_sections = []
        main_counter = 0
        sub_section_counters = {}
        for section_data in policy_node.get('sections') or []:
            info = section_data.get('section') or {}
            sub_policy_id = info.get('subPolicyId')
            if sub_policy_id:
                spn = sub_name_by_id.get(sub_policy_id, '')
                sub_section_counters.setdefault(spn, 0)
                sub_section_counters[spn] += 1
                processed_sections.append({
                    "section_index": sub_section_counters[spn],
                    "section_name": info.get('name'),
                    "section_id": info.get('id'),
                    "sub_policy_name": spn,
                })
            else:
                main_counter += 1
                processed_sections.append({
                    "section_index": main_counter,
                    "section_name": info.get('name'),
                    "section_id": info.get('id'),
                })

        # --- rules: single pass in exact API order ---
        network_rules_out = []
        sub_policies_out = []
        rules_in_sections = []
        group_counters = {}

        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            rule_info = rule_data.get('rule') or {}
            if properties and properties[0] == "SYSTEM":
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding SYSTEM network rule: {rule_info.get('name')}")
                continue
            rule_type = rule_data.pop('ruleType', 'POLICY_RULE')
            sub_policy_ref = rule_data.pop('subPolicy', None)
            section_name = (rule_info.get('section') or {}).get('name') or ''

            if rule_type == 'SUB_POLICY_SCOPE':
                sub_policy_name = rule_info.get('name')
                meta = meta_by_name.get(sub_policy_name, {})
                group_key = ('', section_name)
                group_counters.setdefault(group_key, 0)
                group_counters[group_key] += 1
                rules_in_sections.append({
                    "index_in_section": group_counters[group_key],
                    "section_name": section_name,
                    "entry_type": "sub_policy",
                    "sub_policy_name": sub_policy_name,
                })
                scope = {
                    field: rule_info[field]
                    for field in ('site', 'source', 'destination', 'service',
                                  'nat', 'direction', 'transport')
                    if rule_info.get(field) is not None
                }
                sub_policies_out.append({
                    "sub_policy_name": sub_policy_name,
                    "sub_policy_id": meta.get('id', ''),
                    "scope_rule_id": rule_info.get('id', ''),
                    "description": meta.get('description', rule_info.get('description', '')),
                    # policy.enabled is informational (no enable input on
                    # addSubPolicy and no updateSubPolicy); scope_enabled is the
                    # scope rule's flag, which terraform manages.
                    "enabled": meta.get('enabled', True),
                    "scope_enabled": rule_info.get('enabled', True),
                    "scope": scope,
                })
                continue

            sub_policy_name = sub_policy_ref.get('name') if sub_policy_ref else None
            group_key = (sub_policy_name or '', section_name)
            group_counters.setdefault(group_key, 0)
            group_counters[group_key] += 1
            ris_entry = {
                "index_in_section": group_counters[group_key],
                "section_name": section_name,
                "rule_name": rule_info.get('name'),
            }
            if sub_policy_name:
                ris_entry["sub_policy_name"] = sub_policy_name
            rules_in_sections.append(ris_entry)

            # Child firewall rules: nesting IS the parent reference; order is
            # the array order (per-parent index). Strip per-child noise.
            firewall_rules_out = []
            for child in rule_info.pop('firewall', None) or []:
                child_props = child.get('properties') or []
                child_rule = child.get('rule') or {}
                if child_props and child_props[0] == "SYSTEM":
                    if hasattr(args, 'verbose') and args.verbose:
                        print(f"Excluding SYSTEM firewall rule: {child_rule.get('name')}")
                    continue
                child.pop('ruleType', None)
                child.pop('subPolicy', None)
                child_rule.pop('index', None)
                child_rule.pop('section', None)
                firewall_rules_out.append(child)

            rule_info.pop('index', None)
            rule_info['section'] = {"name": section_name}
            entry = {
                "audit": rule_data.get('audit'),
                "rule": rule_info,
                "properties": properties,
                "firewall_rules": firewall_rules_out,
            }
            if sub_policy_name:
                entry["sub_policy_name"] = sub_policy_name
            network_rules_out.append(entry)

        policy_node.pop('rules', None)
        policy_node['sections'] = processed_sections
        policy_node['network_rules'] = network_rules_out
        policy_node['sub_policies'] = sub_policies_out
        policy_node['rules_in_sections'] = rules_in_sections

        # Handle custom filename and timestamp
        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_lan_fw_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = "all_lan_fw_rules_and_sections_{account_id}.json"

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
            # Empty section name is the canonical implicit-default-section
            # sentinel ("" = rule at the policy root) -- preserve it verbatim.
            if not section_name or section_name.strip() == "":
                section_name = ""
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


def _export_flat_policy_to_json(args, configuration, policy_key, policy_query_str, file_prefix, label):
    """Shared exporter for flat sections+rules policy families.

    Flat structure: sections[], rules[] (wrapper {audit, rule, properties},
    ids retained for brownfield import), rules_in_sections[] ordering rows.
    SYSTEM and LOCKED rules (built-in, not manageable via the API) are
    excluded."""
    try:
        account_id = getAccountID(args, configuration)
        policy_query = {
            "query": policy_query_str,
            "variables": {"accountId": account_id},
            "operationName": "policy",
        }
        response = makeCall(args, configuration, policy_query)
        processed_data = strip_ids_recursive(response)
        policy_node = processed_data['data']['policy'][policy_key]['policy']
        policy_node.pop('additionalAttributes', None)

        filtered_rules = []
        for rule_data in policy_node.get('rules') or []:
            properties = rule_data.get('properties') or []
            if any(p in ("SYSTEM", "LOCKED") for p in properties):
                if hasattr(args, 'verbose') and args.verbose:
                    print(f"Excluding {properties} rule: {rule_data['rule'].get('name')}")
                continue
            rule_data.pop('metadata', None)
            filtered_rules.append(rule_data)

        processed_sections = []
        for index, section_data in enumerate(policy_node.get('sections') or []):
            info = section_data.get('section') or {}
            processed_sections.append({
                "section_index": index + 1,
                "section_name": info.get('name'),
                "section_id": info.get('id', ''),
            })

        rules_in_sections = []
        section_counters = {}
        for rule_data in filtered_rules:
            rule_info = rule_data['rule']
            section_name = (rule_info.get('section') or {}).get('name') or ''
            section_counters.setdefault(section_name, 0)
            section_counters[section_name] += 1
            rules_in_sections.append({
                "index_in_section": section_counters[section_name],
                "section_name": section_name,
                "rule_name": rule_info.get('name'),
            })
            rule_info.pop('index', None)
            rule_info['section'] = {"name": section_name}

        policy_node['rules'] = filtered_rules
        policy_node['sections'] = processed_sections
        policy_node['rules_in_sections'] = rules_in_sections

        if hasattr(args, 'json_filename') and args.json_filename:
            base_filename = args.json_filename
            if base_filename.endswith('.json'):
                base_filename = base_filename[:-5]
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"{base_filename}_{timestamp}.json"
            else:
                filename_template = f"{base_filename}.json"
        else:
            if hasattr(args, 'append_timestamp') and args.append_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename_template = f"all_{file_prefix}_rules_and_sections_{{account_id}}_{timestamp}.json"
            else:
                filename_template = f"all_{file_prefix}_rules_and_sections_{{account_id}}.json"

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


TS_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { terminalServer { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled allowedHostIP { id name } excludeTraffic { id name } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_ts_rules_to_json(args, configuration):
    """Export Terminal Server rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'terminalServer', TS_POLICY_QUERY, 'ts', 'Terminal Server')


AMFH_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { antiMalwareFileHash { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled action expirationDate fileName sha256 } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_amfh_rules_to_json(args, configuration):
    """Export Anti-Malware File Hash rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'antiMalwareFileHash', AMFH_POLICY_QUERY, 'amfh', 'Anti-Malware File Hash')


SSIA_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { sdpStaticIpAllocation { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled source { user { id name } } ip } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_ssia_rules_to_json(args, configuration):
    """Export SDP Static IP Allocation rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'sdpStaticIpAllocation', SSIA_POLICY_QUERY, 'ssia', 'SDP Static IP Allocation')


DIA_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { dynamicIpAllocation { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled country { id name } devicePostureProfile { id name } platform range { globalIpRange { id name } } source { user { id name } usersGroup { id name } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_dia_rules_to_json(args, configuration):
    """Export Dynamic IP Allocation rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'dynamicIpAllocation', DIA_POLICY_QUERY, 'dia', 'Dynamic IP Allocation')


CC_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { clientConnectivity { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled action confidenceLevel connectionOrigin country { id name } device { id name } platform source { user { id name } usersGroup { id name } } sourceRange { globalIpRange { id name } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_cc_rules_to_json(args, configuration):
    """Export Client Connectivity rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'clientConnectivity', CC_POLICY_QUERY, 'cc', 'Client Connectivity')


ST_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { splitTunnel { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled action coverage routingPriority country { id name } platform destination { application { id name } domain fqdn globalIpRange { id name } } dnsExclusion { domain } source { user { id name } usersGroup { id name } } sourceNetwork { sourceNetworkType } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_st_rules_to_json(args, configuration):
    """Export Split Tunnel rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'splitTunnel', ST_POLICY_QUERY, 'st', 'Split Tunnel')


RPF_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { remotePortFwd { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled externalIp { id name } externalPortRange { from to } internalIp internalPortRange { from to } forwardIcmp remoteIPs { globalIpRange { id name } ip ipRange { from to } subnet } restrictionType tracking { enabled frequency subscriptionGroup { id name } webhook { id name } mailingList { id name } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_rpf_rules_to_json(args, configuration):
    """Export Remote Port Forwarding rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'remotePortFwd', RPF_POLICY_QUERY, 'rpf', 'Remote Port Forwarding')


SWP_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { siteWebProxy { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled fqdn port allowedDestinationProtocol shouldAssociateWithAllSites associatedSite { id name } authenticationConfig { method kerberosConfig { isEnabled } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_swp_rules_to_json(args, configuration):
    """Export Site Web Proxy rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'siteWebProxy', SWP_POLICY_QUERY, 'swp', 'Site Web Proxy')


SB_POLICY_QUERY = "query policy ( $accountId:ID! ) { policy ( accountId:$accountId ) { socketBypass { policy { enabled rules { audit { updatedTime updatedBy } rule { id name description index section { id name subPolicyId } enabled action { port event { enabled } } site { site { id name } group { id name } } source { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } siteNetworkSubnet { id name } subnet vlan } destination { application { id name } customApp { id name } domain fqdn globalIpRange { id name } ip ipRange { from to } subnet } service { simple { name } custom { port portRange { from to } protocol } } exception { name site { site { id name } group { id name } } source { floatingSubnet { id name } globalIpRange { id name } group { id name } host { id name } ip ipRange { from to } networkInterface { id name } siteNetworkSubnet { id name } subnet vlan } destination { application { id name } customApp { id name } domain fqdn globalIpRange { id name } ip ipRange { from to } subnet } service { simple { name } custom { port portRange { from to } protocol } } } } properties } sections { audit { updatedTime updatedBy } section { id name subPolicyId } properties } audit { publishedTime publishedBy } revision { id name description changes createdTime updatedTime } } } } }"


def export_sb_rules_to_json(args, configuration):
    """Export Socket Bypass rules to the bulk-module JSON shape."""
    return _export_flat_policy_to_json(
        args, configuration, 'socketBypass', SB_POLICY_QUERY, 'sb', 'Socket Bypass')


def _is_access_denied_error(error_text):
    """Case-insensitive match for the Cato API's access-denied signature.

    Used by export_all_to_json to fatally abort the whole run the moment one
    type hits this, instead of grinding through every remaining type hitting
    the identical wall - observed live: an under-privileged API key printed
    the same "Access denied: ... does not have sufficient permissions"
    error for type after type until the run finally finished on its own."""
    if not error_text:
        return False
    text = str(error_text).lower()
    return "access denied" in text or "does not have sufficient permissions" in text


def _preflight_validate_export_all_credentials(args, configuration):
    """Pre-flight credential/permission check for `catocli export all`, run
    once before any type is exported.

    Reuses catocli configure's own live-API credential validator
    (test_credentials() in catocli/parsers/configure/configure.py - the same
    lightweight entityLookup call `catocli configure set` runs before saving
    a profile) against the endpoint/token/account_id this invocation would
    actually use, instead of duplicating that query here. Returns
    (ok: bool, message: str)."""
    from catocli.parsers.configure.configure import test_credentials

    try:
        account_id = getAccountID(args, configuration)
    except Exception as e:
        return False, str(e)

    endpoint = getattr(configuration, 'host', None)
    token = None
    if hasattr(configuration, 'api_key') and configuration.api_key:
        token = configuration.api_key.get('x-api-key')

    if not endpoint or not token:
        return False, "no endpoint/token configured for the active profile"

    return test_credentials(endpoint, token, account_id)


def _strip_account_suffix_from_filename(path, account_id):
    """Remove a literal '_<account_id>' suffix immediately before the file
    extension, e.g. 'all_ifw_rules_and_sections_15412.json' ->
    'all_ifw_rules_and_sections.json'. Matches the literal resolved account
    id (not a regex guess over digits), so it only strips the exact suffix
    this run's own account produced. A no-op when the basename doesn't end
    with that exact suffix - e.g. the dependency-object exports (groups,
    custom_apps, ...), whose default filenames are already account-agnostic
    by convention and carry no suffix to strip."""
    directory, basename = os.path.split(path)
    stem, ext = os.path.splitext(basename)
    suffix = f"_{account_id}"
    if account_id and stem.endswith(suffix):
        stem = stem[: -len(suffix)]
    new_basename = f"{stem}{ext}"
    return os.path.join(directory, new_basename) if directory else new_basename


def export_all_to_json(args, configuration):
    """Run every registered `catocli export <type>` subcommand in-process
    (calling the exact same handler functions the individual subcommands
    invoke - no subprocesses), writing each type's own default filename into
    one shared --output-directory.

    The type list is NOT a second hardcoded registry: export_rules_parse()
    (catocli/parsers/custom/export_rules/__init__.py) stashes the live
    'export' subparsers registry on this command via
    set_defaults(_export_subparsers=export_subparsers) after every export
    subcommand (sites, dependency objects, and all rules types) has been
    registered onto it, so args._export_subparsers.choices always reflects
    every export subcommand that exists at runtime - a future export type
    added anywhere under `catocli export` is picked up automatically.

    Before any type is exported, a pre-flight credential/permission check
    (_preflight_validate_export_all_credentials, reusing `catocli configure`'s
    own live-API validator) runs once; on failure, nothing is exported and
    the process exits 1 immediately.

    For each type, this builds that subcommand's own default Namespace via
    sub_parser.parse_args([]) - every export subcommand's options are
    optional (see export_rules_parse/export_sites_parse/export_deps_parse),
    so this reproduces exactly what running `catocli export <type>` with no
    extra flags would do, including its own --json-filename default - then
    overrides only the options common to every export subcommand
    (-accountID, --output-directory, -v/--verbose) with this run's values.

    --types restricts the run to a comma-separated subset of type names.
    One failing type does NOT abort the run by default (continue-on-error);
    pass --fail-fast to stop at the first failure instead. The one exception
    to continue-on-error is an access-denied failure (see
    _is_access_denied_error): permissions are granted per-API, so a key that
    lacks permission for one operation will almost always lack it for every
    remaining one too - continuing would just reprint the identical error for
    every remaining type (this is exactly what happened in the field: an
    under-privileged key ground through type after type printing the same
    "Access denied" error). An access-denied failure therefore aborts the
    run immediately regardless of --fail-fast.

    --no-account-suffix is off by default (preserving today's filenames).
    When set, each type's own produced file is renamed in place
    (os.rename, via _strip_account_suffix_from_filename) to drop its
    trailing '_<account_id>' before the extension, using the literal
    account id this run resolved (not a regex guess over digits) -
    e.g. 'all_ifw_rules_and_sections_15412.json' becomes
    'all_ifw_rules_and_sections.json'. This happens right after the single
    export call returns and before archiving, so --archive-directory
    naturally copies the already-renamed file. Dependency-object exports
    (groups, custom_apps, ...) are already account-agnostic by convention
    and are unaffected (no suffix to strip).

    --archive-directory is off unless explicitly set. When set, every
    successfully-exported file is additionally copied byte-for-byte (same
    basename as the primary --output-directory file, post rename if
    --no-account-suffix is also set) into that directory - mirroring what
    this reference-architecture repo's scripts/export_all_configs.py does
    for config_data_archive/, a redundant, directly-diffable raw capture.
    The copy is made from the path the single export call already
    produced; the export is never re-run and the API is never called a
    second time to get it. A type whose own export fails writes nothing to
    the archive. If the archive copy itself fails (disk/permissions), that
    type is marked failed in the summary, but this is NOT an access-denied
    condition, so it never aborts the run.

    --strip-ids is off by default. When set, this run produces the same
    tenant-migration outcome as the reference-architecture repo's
    (now-superseded) scripts/migrate_tenant.py: every type's PRIMARY output
    file (in --output-directory) becomes tenant-portable (ids stripped),
    while --archive-directory, if also given, still receives the RAW
    id-bearing file. The ordering is strict and never varies: each type's
    API is called exactly once (no second call to produce a stripped
    version); if --archive-directory is set, the raw file is archived
    FIRST; only then is the primary file stripped in place, via
    _strip_output_file_in_place/_strip_exported_payload - reusing the exact
    same pure strip_*_ids functions each type's own native --strip-ids flag
    calls (export_deps.py's dependency types, export_sites.py's
    strip_socket_site_ids, and strip_policy_rules_ids above for every
    `*_rules` type), so there is never a second, drifting implementation. A
    type whose own export succeeded but whose strip post-processing failed
    is marked failed in the summary (like an archive-copy failure) without
    aborting the run. When at least the pre-flight check passed, a
    CHECKLIST.md is additionally written into --output-directory (see
    EXPORT_ALL_CHECKLIST_TEMPLATE) listing every file this run produced plus
    the manual re-resolution steps a target tenant still needs (id-only
    group members, mailing-list admin ids, Wi-Fi PSKs, licenses, physical
    socket re-registration).

    A per-type progress line is printed as each type runs, followed by a
    summary; if any requested type failed (including the pre-flight check,
    an access-denied abort, an archive-copy failure, or a --strip-ids
    post-processing failure), sys.exit(1) is called after the summary is
    printed (matching this codebase's convention of custom commands calling
    sys.exit() directly - see import_rules_to_tf.py / import_sites_to_tf.py
    - since clidriver.main() does not otherwise inspect a handler's
    returned "success" flag)."""
    registry = getattr(args, '_export_subparsers', None)
    if registry is None or not hasattr(registry, 'choices'):
        print("ERROR: internal error: export type registry not available")
        return [{"success": False, "error": "internal error: export type registry not available"}]

    all_types = sorted(name for name in registry.choices.keys() if name != 'all')

    types_to_run = all_types
    if getattr(args, 'types', None):
        requested = [t.strip() for t in args.types.split(',') if t.strip()]
        unknown = [t for t in requested if t not in registry.choices or t == 'all']
        if unknown:
            error = (
                f"--types: unknown export type(s): {', '.join(unknown)}. "
                f"Valid types: {', '.join(all_types)}"
            )
            print(f"ERROR: {error}")
            return [{"success": False, "error": error}]
        types_to_run = requested

    print("Pre-flight: validating credentials and permissions before exporting any type...")
    preflight_ok, preflight_message = _preflight_validate_export_all_credentials(args, configuration)
    if not preflight_ok:
        print(f"ERROR: Pre-flight credential check failed: {preflight_message}")
        print(
            "Run `catocli configure show` to verify the active profile's credentials, and "
            "confirm the associated Admin or Service Principal has sufficient permissions, "
            "then re-run `catocli export all`."
        )
        preflight_result = [{
            "success": False,
            "error": f"pre-flight credential check failed: {preflight_message}",
        }]
        sys.exit(1)
        return preflight_result  # unreachable after sys.exit; kept for type consistency

    verbose = hasattr(args, 'verbose') and args.verbose
    fail_fast = hasattr(args, 'fail_fast') and args.fail_fast
    strip_ids_requested = hasattr(args, 'strip_ids') and args.strip_ids
    total = len(types_to_run)

    # --no-account-suffix: off by default. Resolve the literal account id
    # once (pure local resolution - no API call) so every type's produced
    # filename can have its exact '_<account_id>' suffix stripped below.
    no_account_suffix = hasattr(args, 'no_account_suffix') and args.no_account_suffix
    resolved_account_id = None
    if no_account_suffix:
        try:
            resolved_account_id = str(getAccountID(args, configuration))
        except Exception as e:
            print(f"WARNING: --no-account-suffix: could not resolve account id ({e}); filenames will keep their account suffix")
            no_account_suffix = False

    # --archive-directory: off unless explicitly set. When set, every
    # successfully-exported file is additionally copied byte-for-byte (same
    # basename) into this directory, mirroring what this reference-
    # architecture repo's scripts/export_all_configs.py does for
    # config_data_archive/ - a redundant, diffable raw capture. The file is
    # never re-read from the API to get there; we just copy the path the
    # single export call already produced (item["output_file"]).
    archive_directory = getattr(args, 'archive_directory', None)
    archive_enabled = bool(archive_directory)
    if archive_enabled:
        try:
            os.makedirs(archive_directory, exist_ok=True)
        except Exception as e:
            print(f"WARNING: could not create --archive-directory '{archive_directory}' ({e}); archiving disabled for this run")
            archive_enabled = False

    results = []
    succeeded = []
    succeeded_output_files = []
    failed = []
    aborted_access_denied = False
    attempted = 0

    print(f"Exporting {total} type(s) into {getattr(args, 'output_directory', None) or 'config_data'}/\n")

    for idx, export_type in enumerate(types_to_run, 1):
        attempted = idx
        sub_parser = registry.choices[export_type]
        sub_func = sub_parser.get_default('func')
        prefix = f"[{idx}/{total}] {export_type}"

        if sub_func is None:
            failed.append((export_type, "no handler registered for this export type"))
            print(f"{prefix}: FAILED (no handler registered)")
            if fail_fast:
                break
            continue

        # Reproduce `catocli export <type>` with no extra flags, then layer
        # this run's common overrides on top. Deliberately NOT overridden:
        # sub_args.strip_ids (for the types that have it) stays at its
        # parse_args([]) default of False - --strip-ids on `all` is handled
        # entirely as post-processing below (_strip_output_file_in_place),
        # never by asking the type's own handler to export pre-stripped, so
        # every type's API is called exactly once per run regardless of
        # --strip-ids.
        sub_args = sub_parser.parse_args([])
        if hasattr(sub_args, 'accountID'):
            sub_args.accountID = getattr(args, 'accountID', None)
        if hasattr(sub_args, 'output_directory'):
            sub_args.output_directory = getattr(args, 'output_directory', None)
        if hasattr(sub_args, 'verbose'):
            sub_args.verbose = verbose

        print(f"{prefix}: exporting...")
        try:
            sub_result = sub_func(sub_args, configuration)
        except Exception as e:
            error_text = str(e)
            failed.append((export_type, error_text))
            print(f"{prefix}: FAILED ({error_text})")
            if _is_access_denied_error(error_text):
                aborted_access_denied = True
                break
            if fail_fast:
                break
            continue

        # Every export handler returns a list with exactly one result dict.
        item = sub_result[0] if isinstance(sub_result, list) and sub_result else {
            "success": False, "error": "no result returned"
        }
        results.append({"type": export_type, "result": item})

        if item.get("success"):
            output_file = item.get("output_file")
            if not output_file:
                output_files = item.get("output_files")
                output_file = output_files[0] if output_files else None

            # --no-account-suffix: rename the already-produced file in
            # place, stripping its literal '_<account_id>' suffix, before
            # archiving - so the archive copy (below) naturally picks up
            # the renamed file.
            if no_account_suffix and output_file:
                suffix_stripped_path = _strip_account_suffix_from_filename(output_file, resolved_account_id)
                if suffix_stripped_path != output_file:
                    try:
                        os.replace(output_file, suffix_stripped_path)
                        output_file = suffix_stripped_path
                    except Exception as e:
                        print(
                            f"WARNING: --no-account-suffix: could not rename '{output_file}' -> "
                            f"'{suffix_stripped_path}' ({e}); keeping the account-suffixed filename"
                        )

            # Archive a byte-for-byte copy of the file the single export
            # call above already produced - never re-run the export / call
            # the API again to get it.
            archived = False
            archive_error = None
            archive_path = None
            if archive_enabled and output_file:
                archive_path = os.path.join(archive_directory, os.path.basename(output_file))
                try:
                    shutil.copyfile(output_file, archive_path)
                    archived = True
                except Exception as e:
                    archive_error = str(e)

            if archive_enabled and output_file and not archived:
                # The export itself succeeded, but the redundant archive
                # copy failed (disk/permissions - not an API error, so this
                # never reaches _is_access_denied_error and can never
                # trigger the abort-the-run path below). Mark this type
                # failed in the summary without aborting the run.
                failed.append((
                    export_type,
                    f"export succeeded but archive copy to '{archive_path}' failed: {archive_error}",
                ))
                print(f"{prefix}: exported OK -> {output_file}, but FAILED to archive ({archive_error})")
                if fail_fast:
                    break
            else:
                # --strip-ids post-processing: ONLY reached once the raw
                # file is already safely archived (or archiving wasn't
                # requested) - see this function's docstring for why the
                # ordering is strict. Strips the PRIMARY --output-directory
                # file in place; the already-archived copy (if any) stays
                # raw/id-bearing.
                strip_ok = True
                strip_error = None
                if strip_ids_requested and output_file:
                    strip_ok, strip_error = _strip_output_file_in_place(export_type, output_file)

                if not strip_ok:
                    failed.append((
                        export_type,
                        f"export succeeded but --strip-ids post-processing of '{output_file}' failed: {strip_error}",
                    ))
                    print(f"{prefix}: exported OK -> {output_file}, but FAILED to strip ids ({strip_error})")
                    if fail_fast:
                        break
                else:
                    succeeded.append(export_type)
                    if output_file:
                        succeeded_output_files.append(output_file)
                    suffix_bits = []
                    if archived:
                        suffix_bits.append("archived")
                    if strip_ids_requested:
                        suffix_bits.append("stripped")
                    suffix = f" (+ {', '.join(suffix_bits)})" if suffix_bits else ""
                    print(f"{prefix}: OK -> {output_file}{suffix}")
        else:
            error_msg = item.get("error", "unknown error")
            failed.append((export_type, error_msg))
            print(f"{prefix}: FAILED ({error_msg})")
            if _is_access_denied_error(error_msg):
                aborted_access_denied = True
                break
            if fail_fast:
                break

    if aborted_access_denied:
        skipped_types = types_to_run[attempted:]
        print(
            f"\nABORTING: the API key does not have sufficient permissions for this operation "
            f"(access denied on '{types_to_run[attempted - 1]}') - skipping the remaining "
            f"{len(skipped_types)} export type(s). Verify the associated Admin or Service "
            f"Principal permissions (see `catocli configure show`) and re-run."
        )
    else:
        skipped_types = []

    # --strip-ids: write the migration checklist once the run is otherwise
    # done, regardless of whether every type succeeded - it documents
    # exactly what this run DID produce (see succeeded_output_files) plus
    # the manual re-resolution steps that never change.
    checklist_path = None
    if strip_ids_requested:
        checklist_output_dir = getattr(args, 'output_directory', None) or 'config_data'
        try:
            os.makedirs(checklist_output_dir, exist_ok=True)
            checklist_path = _write_export_all_checklist(
                checklist_output_dir,
                [os.path.basename(p) for p in succeeded_output_files],
                generated_by="catocli export all --strip-ids",
            )
            print(f"Wrote migration checklist: {checklist_path}")
        except Exception as e:
            print(f"WARNING: could not write CHECKLIST.md to '{checklist_output_dir}': {e}")

    print(f"\nExport all: {len(succeeded)} succeeded, {len(failed)} failed (of {total} requested type(s))")
    if archive_directory:
        if archive_enabled:
            print(f"Archived successful exports to: {archive_directory}")
        else:
            print(f"Archive directory '{archive_directory}' was requested but disabled for this run (see WARNING above)")
    if failed:
        print("Failed types:")
        for export_type, error_msg in failed:
            print(f"  - {export_type}: {error_msg}")

    overall_success = len(failed) == 0 and not aborted_access_denied
    result = [{
        "success": overall_success,
        "exported": succeeded,
        "failed": [{"type": t, "error": e} for t, e in failed],
        "results": results,
        "aborted_access_denied": aborted_access_denied,
        "skipped": skipped_types,
        "archive_directory": archive_directory if archive_enabled else None,
        "checklist_path": checklist_path,
    }]

    if not overall_success:
        sys.exit(1)

    return result
