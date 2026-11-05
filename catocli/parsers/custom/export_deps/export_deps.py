import os
import json
import base64
import csv
import io
import ipaddress
from datetime import datetime
from ..customLib import writeDataToFile, makeCall, getAccountID
from ..export_sites.export_sites import getEntityLookup
from ...utils.export_utils import (
    export_data_unified,
    parse_names_arg,
    filter_items_by_name,
    merge_items_into_file,
)

# Group member types that only expose a resolvable reference through their
# tenant-specific id (no name-only lookup exists in the target tenant for
# these). Surfaced in the --strip-ids help text so a migration operator knows
# which members will need manual id re-resolution after a --strip-ids export
# is applied into a different tenant.
ID_ONLY_MEMBER_TYPES = ("FLOATING_SUBNET", "HOST", "NETWORK_INTERFACE", "SITE_NETWORK_SUBNET")

GROUP_LIST_QUERY = (
    "query groupsGroupList ( $accountId:ID! $groupListInput:GroupListInput ) "
    "{ groups ( accountId:$accountId ) { groupList ( input:$groupListInput ) "
    "{ items { id name description } paging { total } } } }"
)

GROUP_MEMBERS_QUERY = (
    "query groupsGroupMembers ( $accountId:ID! $groupMembersListInput:GroupMembersListInput! $groupRefInput:GroupRefInput! ) "
    "{ groups ( accountId:$accountId ) { group ( input:$groupRefInput ) { members ( input:$groupMembersListInput ) "
    "{ items { id name type } paging { total } } } } }"
)

GLOBAL_IP_RANGE_LIST_QUERY = (
    "query objectGlobalIpRangeList ( $accountId:ID! ) "
    "{ object ( accountId:$accountId ) { globalIpRangeList { items { id name description ipRange } total } } }"
)

CUSTOM_APPLICATION_LIST_QUERY = (
    "query customAppDataCustomApplicationList ( $accountId:ID! $customApplicationListInput:CustomApplicationListInput! ) "
    "{ customAppData ( accountId:$accountId ) { customApplicationList ( input:$customApplicationListInput ) "
    "{ items { id name description category { id name } criteria { destination { destinationIp { ip ipRange { from to } subnet } "
    "domain fqdn } port portRange { from to } protocol } } paging { total } } } }"
)

MAILING_LIST_LIST_QUERY = (
    "query notificationMailingListList ( $accountId:ID! ) "
    "{ notification ( accountId:$accountId ) { mailingListList "
    "{ items { id name address admin { id name } } paging { total } } } }"
)

SUBSCRIPTION_GROUP_LIST_QUERY = (
    "query notificationSubscriptionGroupList ( $accountId:ID! ) "
    "{ notification ( accountId:$accountId ) { subscriptionGroupList "
    "{ items { id name mailingList { id name } integration { webhookList { id name } } } paging { total } } } }"
)

DHCP_RELAY_GROUP_LIST_QUERY = (
    "query networkConfigDhcpRelayGroupList ( $accountId:ID! $networkConfigDhcpRelayGroupListInput:NetworkConfigDhcpRelayGroupListInput! ) "
    "{ networkConfig ( accountId:$accountId ) { dhcp { relayGroupList ( input:$networkConfigDhcpRelayGroupListInput ) "
    "{ items { id name server } paging { total } } } } }"
)

CONTAINER_LIST_QUERY = (
    "query containerList ( $accountId:ID! $input:ContainerSearchInput! ) "
    "{ container ( accountId:$accountId ) { list ( input:$input ) { containers "
    "{ __typename id name description size syncData { fileType url timeInterval timeUnit } } } } }"
)

FQDN_CONTAINER_DOWNLOAD_FILE_QUERY = (
    "query containerFqdnDownloadFile ( $accountId:ID! $input:DownloadFqdnContainerFileInput! ) "
    "{ container ( accountId:$accountId ) { fqdn { downloadFile ( input:$input ) { id name encodedFile } } } }"
)

IP_RANGE_CONTAINER_DOWNLOAD_FILE_QUERY = (
    "query containerIpAddressRangeDownloadFile ( $accountId:ID! $input:DownloadIpAddressRangeContainerFileInput! ) "
    "{ container ( accountId:$accountId ) { ipAddressRange { downloadFile ( input:$input ) { id name encodedFile } } } }"
)

STATIC_HOST_LIST_QUERY = (
    "query siteStaticHostList ( $accountId:ID! $site:SiteRefInput! ) "
    "{ site ( accountId:$accountId ) { staticHostList ( site:$site ) { items { hostId name ip macAddress } } } }"
)

PAGE_LIMIT = 1000

# networkConfig.dhcp.relayGroupList enforces its own server-side paging cap
# (observed: "Paging limit must be between 1 and 100"), unlike the other
# paginated list queries in this file which accept up to PAGE_LIMIT (1000).
DHCP_RELAY_GROUP_PAGE_LIMIT = 100


def _build_filename_template(args, default_filename):
    """Mirror the other export commands' --json-filename / --append-timestamp
    handling, but default to a plain filename (no {account_id} placeholder) -
    these dependency exports are account-agnostic by convention (groups.json,
    global_ip_ranges.json, custom_applications.json), matching the terraform
    reference-architecture's config_data/ naming."""
    if hasattr(args, 'json_filename') and args.json_filename:
        base_filename = args.json_filename
        if base_filename.endswith('.json'):
            base_filename = base_filename[:-5]
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            return f"{base_filename}_{timestamp}.json"
        return f"{base_filename}.json"
    else:
        if hasattr(args, 'append_timestamp') and args.append_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            base = default_filename[:-5] if default_filename.endswith('.json') else default_filename
            return f"{base}_{timestamp}.json"
        return default_filename


def _finalize_export(output_items, args, account_id, default_filename, name_key='name'):
    """Shared tail logic for every export_deps.py JSON export function:

      1. Apply --names filtering (if provided) - warns on unmatched names,
         fails (returns success: False) only if NOTHING matched.
      2. Sort the (possibly filtered) list by name_key, case-insensitive -
         this repo's standard top-level sort convention.
      3. Either --merge-into an existing JSON file (upsert by name_key) or
         write a fresh file via the normal --json-filename/--output-directory
         handling.

    Returns the catocli result list.
    """
    names = parse_names_arg(getattr(args, 'names', None))
    if names:
        output_items, not_found = filter_items_by_name(output_items, names, name_key=name_key)
        if not_found:
            print(f"WARNING: --names: no match found for: {', '.join(not_found)}")
        if not output_items:
            return [{
                "success": False,
                "error": f"--names matched none of the requested name(s): {', '.join(names)}",
                "not_found": not_found,
            }]

    output_items.sort(key=lambda x: (x.get(name_key) or "").lower())

    merge_into = getattr(args, 'merge_into', None)
    if merge_into:
        merged_list, created, updated = merge_items_into_file(output_items, merge_into, name_key=name_key)
        print(f"Merged {len(output_items)} item(s) into {merge_into} ({created} new, {updated} updated, {len(merged_list)} total)")
        return [{
            "success": True,
            "output_file": merge_into,
            "account_id": account_id,
            "count": len(output_items),
            "merged_total": len(merged_list),
            "created": created,
            "updated": updated,
        }]

    filename_template = _build_filename_template(args, default_filename)
    output_file = writeDataToFile(
        data=output_items,
        args=args,
        account_id=account_id,
        default_filename_template=filename_template,
        default_directory="config_data",
    )
    return [{"success": True, "output_file": output_file, "account_id": account_id, "count": len(output_items)}]


def export_groups_to_json(args, configuration):
    """Export Groups to the bulk-module JSON shape.

    Flat array of {id, name, description, members: [{type, id, name}]},
    sorted by name (case-insensitive). With --strip-ids, top-level group ids
    and member ids are omitted (members keep only {type, name}) - note that
    groups containing member types resolvable only by id in the current
    tenant (FLOATING_SUBNET, HOST, NETWORK_INTERFACE, SITE_NETWORK_SUBNET)
    will need their ids manually re-resolved after import into a different
    tenant."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        # Paginate groupList
        all_groups = []
        from_offset = 0
        while True:
            query = {
                "query": GROUP_LIST_QUERY,
                "variables": {
                    "accountId": account_id,
                    "groupListInput": {"paging": {"limit": PAGE_LIMIT, "from": from_offset}},
                },
                "operationName": "groupsGroupList",
            }
            response = makeCall(args, configuration, query)
            result = response['data']['groups']['groupList']
            items = result.get('items') or []
            all_groups.extend(items)
            total = (result.get('paging') or {}).get('total', len(all_groups))
            if verbose:
                print(f"Retrieved {len(items)} groups (offset: {from_offset}, total: {total})")
            from_offset += PAGE_LIMIT
            if len(all_groups) >= total or not items:
                break

        # Fetch members for each group
        output_groups = []
        for group in all_groups:
            group_id = group.get('id')
            all_members = []
            member_offset = 0
            while True:
                members_query = {
                    "query": GROUP_MEMBERS_QUERY,
                    "variables": {
                        "accountId": account_id,
                        "groupRefInput": {"by": "ID", "input": group_id},
                        "groupMembersListInput": {
                            "filter": [],
                            "paging": {"limit": PAGE_LIMIT, "from": member_offset},
                        },
                    },
                    "operationName": "groupsGroupMembers",
                }
                members_response = makeCall(args, configuration, members_query)
                members_result = members_response['data']['groups']['group']['members']
                member_items = members_result.get('items') or []
                all_members.extend(member_items)
                member_total = (members_result.get('paging') or {}).get('total', len(all_members))
                member_offset += PAGE_LIMIT
                if len(all_members) >= member_total or not member_items:
                    break

            if verbose:
                print(f"Group '{group.get('name')}': {len(all_members)} members")

            members_out = []
            for m in all_members:
                if strip_ids:
                    members_out.append({"type": m.get('type'), "name": m.get('name')})
                else:
                    members_out.append({"type": m.get('type'), "id": m.get('id'), "name": m.get('name')})

            # Member order is not guaranteed stable by the API - sort
            # deterministically by (type, name) so re-exports don't produce
            # diff noise on an otherwise-unchanged group.
            members_out.sort(key=lambda m: ((m.get('type') or '').lower(), (m.get('name') or '').lower()))

            group_out = {
                "name": group.get('name'),
                "description": group.get('description') or "",
                "members": members_out,
            }
            if not strip_ids:
                group_out = {"id": group_id, **group_out}
            output_groups.append(group_out)

        return _finalize_export(output_groups, args, account_id, "groups.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_global_ip_ranges_to_json(args, configuration):
    """Export Global IP Ranges to the bulk-module JSON shape.

    Flat array of {id, name, description, ipRange}, sorted by name. With
    --strip-ids, top-level ids are omitted."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        query = {
            "query": GLOBAL_IP_RANGE_LIST_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "objectGlobalIpRangeList",
        }
        response = makeCall(args, configuration, query)
        result = response['data']['object']['globalIpRangeList']
        items = result.get('items') or []

        if verbose:
            print(f"Retrieved {len(items)} global IP ranges")

        output_ranges = []
        for item in items:
            range_out = {
                "name": item.get('name'),
                "description": item.get('description') or "",
                "ipRange": item.get('ipRange'),
            }
            if not strip_ids:
                range_out = {"id": item.get('id'), **range_out}
            output_ranges.append(range_out)

        return _finalize_export(output_ranges, args, account_id, "global_ip_ranges.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_mailing_lists_to_json(args, configuration):
    """Export Mailing Lists to the bulk-module JSON shape.

    Flat array of {id, name, address: [...], admin: [{id, name}]}, sorted by
    name (case-insensitive). Account-wide, single-call (notification.
    mailingListList is not paginated). With --strip-ids, the top-level id and
    each admin's id are omitted (admins keep {name} only) - note that admin
    references REQUIRE an id in the provider, so a --strip-ids export's
    admin entries will need their ids manually re-resolved against the
    target tenant before they can be used."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        query = {
            "query": MAILING_LIST_LIST_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "notificationMailingListList",
        }
        response = makeCall(args, configuration, query)
        result = response['data']['notification']['mailingListList']
        items = result.get('items') or []

        if verbose:
            print(f"Retrieved {len(items)} mailing lists")

        output_lists = []
        for item in items:
            admins_out = []
            for admin in item.get('admin') or []:
                if strip_ids:
                    admins_out.append({"name": admin.get('name')})
                else:
                    admins_out.append({"id": admin.get('id'), "name": admin.get('name')})
            # Deterministic order - API doesn't guarantee admin list order.
            admins_out.sort(key=lambda a: (a.get('name') or '').lower())

            addresses_out = sorted(item.get('address') or [], key=lambda a: (a or '').lower())

            list_out = {
                "name": item.get('name'),
                "address": addresses_out,
                "admin": admins_out,
            }
            if not strip_ids:
                list_out = {"id": item.get('id'), **list_out}
            output_lists.append(list_out)

        return _finalize_export(output_lists, args, account_id, "mailing_lists.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_subscription_groups_to_json(args, configuration):
    """Export Subscription Groups to the bulk-module JSON shape.

    Flat array of {id, name, mailing_list: [{id, name}], integration: [{id,
    name}]}, sorted by name (case-insensitive). Account-wide, single-call
    (notification.subscriptionGroupList is not paginated). "integration" is
    the group's webhook integrations (notification.subscriptionGroup.
    integration.webhookList), referenced by {id, name}. With --strip-ids,
    the top-level id and all nested mailing_list/integration ids are
    omitted (both keep {name} only)."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        query = {
            "query": SUBSCRIPTION_GROUP_LIST_QUERY,
            "variables": {"accountId": account_id},
            "operationName": "notificationSubscriptionGroupList",
        }
        response = makeCall(args, configuration, query)
        result = response['data']['notification']['subscriptionGroupList']
        items = result.get('items') or []

        if verbose:
            print(f"Retrieved {len(items)} subscription groups")

        output_groups = []
        for item in items:
            mailing_lists_out = []
            for ml in item.get('mailingList') or []:
                if strip_ids:
                    mailing_lists_out.append({"name": ml.get('name')})
                else:
                    mailing_lists_out.append({"id": ml.get('id'), "name": ml.get('name')})
            # Deterministic order - the API does not guarantee stable order
            # for either nested list, which otherwise produces diff noise
            # across repeated exports of an unchanged group.
            mailing_lists_out.sort(key=lambda m: (m.get('name') or '').lower())

            webhooks_out = []
            for wh in (item.get('integration') or {}).get('webhookList') or []:
                if strip_ids:
                    webhooks_out.append({"name": wh.get('name')})
                else:
                    webhooks_out.append({"id": wh.get('id'), "name": wh.get('name')})
            webhooks_out.sort(key=lambda w: (w.get('name') or '').lower())

            group_out = {
                "name": item.get('name'),
                "mailing_list": mailing_lists_out,
                "integration": webhooks_out,
            }
            if not strip_ids:
                group_out = {"id": item.get('id'), **group_out}
            output_groups.append(group_out)

        return _finalize_export(output_groups, args, account_id, "subscription_groups.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_dhcp_relay_groups_to_json(args, configuration):
    """Export DHCP Relay Groups to the bulk-module JSON shape.

    Flat array of {id, name, server: [...server addresses...]}, sorted by
    name (case-insensitive). Pages networkConfig.dhcp.relayGroupList in
    batches of 100 (this list's own server-side paging cap, unlike the other
    paginated exports in this file which accept up to 1000). With
    --strip-ids, the top-level id is omitted (the provider's
    cato_dhcp_relay_group resource treats id as opaque/read-only and
    resolves groups by name on import, so stripping it is safe)."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        all_groups = []
        from_offset = 0
        while True:
            query = {
                "query": DHCP_RELAY_GROUP_LIST_QUERY,
                "variables": {
                    "accountId": account_id,
                    "networkConfigDhcpRelayGroupListInput": {"paging": {"limit": DHCP_RELAY_GROUP_PAGE_LIMIT, "from": from_offset}},
                },
                "operationName": "networkConfigDhcpRelayGroupList",
            }
            response = makeCall(args, configuration, query)
            result = response['data']['networkConfig']['dhcp']['relayGroupList']
            items = result.get('items') or []
            all_groups.extend(items)
            total = (result.get('paging') or {}).get('total', len(all_groups))
            if verbose:
                print(f"Retrieved {len(items)} DHCP relay groups (offset: {from_offset}, total: {total})")
            from_offset += DHCP_RELAY_GROUP_PAGE_LIMIT
            if len(all_groups) >= total or not items:
                break

        output_groups = []
        for group in all_groups:
            group_out = {
                "name": group.get('name'),
                "server": group.get('server') or [],
            }
            if not strip_ids:
                group_out = {"id": group.get('id'), **group_out}
            output_groups.append(group_out)

        return _finalize_export(output_groups, args, account_id, "dhcp_relay_groups.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def _ip_sort_key(value):
    """Sort key for an IP range's "from" value: sorts as a real IP address
    when parseable (so 2.0.0.1 sorts before 10.0.0.1), falling back to a
    lexical sort for anything that doesn't parse as one."""
    try:
        return (0, ipaddress.ip_address(value))
    except Exception:
        return (1, str(value or ""))


def _decode_container_file_text(encoded_file):
    """Containers' downloadFile queries return the member list as a base64
    encodedFile string. Decode it to text, falling back to the raw string if
    it turns out not to be base64 (defensive - observed tenants always
    base64-encode, but this keeps the export from hard-failing if a future
    API revision changes that)."""
    if not encoded_file:
        return ""
    try:
        return base64.b64decode(encoded_file).decode('utf-8')
    except Exception:
        return encoded_file


def _parse_fqdn_file_values(file_text):
    """Parse a downloaded FQDN container file (one fqdn per line, optionally
    CSV with a header) into a flat list of fqdn strings."""
    values = []
    for row in csv.reader(io.StringIO(file_text)):
        if not row:
            continue
        candidate = row[0].strip()
        if not candidate:
            continue
        if candidate.lower() in ("fqdn", "value", "values", "domain"):
            # Skip an obvious header row
            continue
        values.append(candidate)
    return values


def _parse_ip_range_file_values(file_text):
    """Parse a downloaded IP range container file into a list of {from, to}
    dicts. Each row may be "from,to" or a single IP (from == to in that
    case)."""
    values = []
    for row in csv.reader(io.StringIO(file_text)):
        if not row:
            continue
        cells = [c.strip() for c in row if c.strip() != ""]
        if not cells:
            continue
        if cells[0].lower() in ("from", "ip", "ip_range", "range"):
            # Skip an obvious header row
            continue
        if len(cells) >= 2:
            values.append({"from": cells[0], "to": cells[1]})
        else:
            values.append({"from": cells[0], "to": cells[0]})
    return values


def export_fqdn_containers_to_json(args, configuration):
    """Export FQDN Containers to the bulk-module JSON shape.

    Flat array of {id, name, description, mode, values: [...fqdn strings...]}
    sorted by name (case-insensitive). "mode" is INLINE (member values
    maintained directly in Cato) or URL (synced from an external file);
    derived from whether the container's syncData is null. URL-mode
    containers additionally carry "file_type" and "sync_data" (url,
    time_interval, time_unit). Member values are always fetched via
    container.fqdn.downloadFile and parsed from the returned file content,
    regardless of mode. With --strip-ids, the top-level id is omitted."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        query = {
            "query": CONTAINER_LIST_QUERY,
            "variables": {"accountId": account_id, "input": {"refs": [], "types": ["FQDN"]}},
            "operationName": "containerList",
        }
        response = makeCall(args, configuration, query)
        containers = response['data']['container']['list']['containers'] or []

        if verbose:
            print(f"Retrieved {len(containers)} FQDN containers")

        output_containers = []
        for container in containers:
            if container.get('__typename') != 'FqdnContainer':
                continue
            container_id = container.get('id')

            download_query = {
                "query": FQDN_CONTAINER_DOWNLOAD_FILE_QUERY,
                "variables": {"accountId": account_id, "input": {"by": "ID", "input": container_id}},
                "operationName": "containerFqdnDownloadFile",
            }
            download_response = makeCall(args, configuration, download_query)
            encoded_file = download_response['data']['container']['fqdn']['downloadFile'].get('encodedFile')
            # Sort lexically - the downloaded file's line order isn't a
            # guaranteed stable API contract, so leaving it as-is produces
            # diff noise across otherwise-unchanged re-exports.
            values = sorted(_parse_fqdn_file_values(_decode_container_file_text(encoded_file)), key=lambda v: v.lower())

            if verbose:
                print(f"Container '{container.get('name')}': {len(values)} fqdn value(s)")

            sync_data = container.get('syncData')
            mode = "URL" if sync_data else "INLINE"

            container_out = {
                "name": container.get('name'),
                "description": container.get('description') or "",
                "mode": mode,
                "values": values,
            }
            if sync_data:
                container_out["file_type"] = sync_data.get('fileType')
                container_out["sync_data"] = {
                    "url": sync_data.get('url'),
                    "time_interval": sync_data.get('timeInterval'),
                    "time_unit": sync_data.get('timeUnit'),
                }
            if not strip_ids:
                container_out = {"id": container_id, **container_out}
            output_containers.append(container_out)

        return _finalize_export(output_containers, args, account_id, "fqdn_containers.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_ip_range_containers_to_json(args, configuration):
    """Export IP Range Containers to the bulk-module JSON shape.

    Flat array of {id, name, description, mode, values: [{from, to}, ...]}
    sorted by name (case-insensitive). "mode" is INLINE (member values
    maintained directly in Cato) or URL (synced from an external file);
    derived from whether the container's syncData is null. URL-mode
    containers additionally carry "file_type" and "sync_data" (url,
    time_interval, time_unit). Member values are always fetched via
    container.ipAddressRange.downloadFile and parsed from the returned file
    content, regardless of mode - a single-IP row is returned as
    {from: ip, to: ip}. With --strip-ids, the top-level id is omitted."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        query = {
            "query": CONTAINER_LIST_QUERY,
            "variables": {"accountId": account_id, "input": {"refs": [], "types": ["IP_RANGE"]}},
            "operationName": "containerList",
        }
        response = makeCall(args, configuration, query)
        containers = response['data']['container']['list']['containers'] or []

        if verbose:
            print(f"Retrieved {len(containers)} IP range containers")

        output_containers = []
        for container in containers:
            if container.get('__typename') != 'IpAddressRangeContainer':
                continue
            container_id = container.get('id')

            download_query = {
                "query": IP_RANGE_CONTAINER_DOWNLOAD_FILE_QUERY,
                "variables": {"accountId": account_id, "input": {"by": "ID", "input": container_id}},
                "operationName": "containerIpAddressRangeDownloadFile",
            }
            download_response = makeCall(args, configuration, download_query)
            encoded_file = download_response['data']['container']['ipAddressRange']['downloadFile'].get('encodedFile')
            # Sort by "from" - the downloaded file's row order isn't a
            # guaranteed stable API contract, so leaving it as-is produces
            # diff noise across otherwise-unchanged re-exports. Sort as IP
            # addresses when parseable (so 2.0.0.1 sorts before 10.0.0.1),
            # falling back to a lexical sort for anything that isn't.
            values = sorted(
                _parse_ip_range_file_values(_decode_container_file_text(encoded_file)),
                key=lambda v: _ip_sort_key(v.get('from')),
            )

            if verbose:
                print(f"Container '{container.get('name')}': {len(values)} ip range value(s)")

            sync_data = container.get('syncData')
            mode = "URL" if sync_data else "INLINE"

            container_out = {
                "name": container.get('name'),
                "description": container.get('description') or "",
                "mode": mode,
                "values": values,
            }
            if sync_data:
                container_out["file_type"] = sync_data.get('fileType')
                container_out["sync_data"] = {
                    "url": sync_data.get('url'),
                    "time_interval": sync_data.get('timeInterval'),
                    "time_unit": sync_data.get('timeUnit'),
                }
            if not strip_ids:
                container_out = {"id": container_id, **container_out}
            output_containers.append(container_out)

        return _finalize_export(output_containers, args, account_id, "ip_range_containers.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_static_hosts(args, configuration):
    """Export Static Hosts to JSON or CSV format (-f/--format, default json).

    Flat array of {id, site_id, site_name, name, ip, mac_address} sorted by
    (site_name, name) case-insensitive. Sites are enumerated via
    entityLookup(type: "site"); each site's hosts come from
    site.staticHostList(site: {by: ID, input: <site_id>}). The underlying
    API field is "hostId" (mapped to the output's "id") and "macAddress"
    (mapped to "mac_address"). With --strip-ids, only the top-level "id" is
    omitted - site_id/site_name are always kept since they identify where
    the host lives."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        if hasattr(args, 'generate_template') and args.generate_template:
            return [{"success": False, "error": "Template generation is not supported for 'export static_hosts'"}]

        sites = getEntityLookup(args, configuration, account_id, "site", None, None)
        if verbose:
            print(f"Retrieved {len(sites)} site(s) to check for static hosts")

        site_names = parse_names_arg(getattr(args, 'site_names', None))
        if site_names:
            wanted_site_names_lower = {n.lower() for n in site_names}
            matched_site_names_lower = {
                (s.get('entity', {}).get('name') or '').strip().lower() for s in sites
            } & wanted_site_names_lower
            not_found_sites = [n for n in site_names if n.lower() not in matched_site_names_lower]
            if not_found_sites:
                print(f"WARNING: --site-names: no site found for: {', '.join(not_found_sites)}")
            sites = [
                s for s in sites
                if (s.get('entity', {}).get('name') or '').strip().lower() in wanted_site_names_lower
            ]
            if not sites:
                return [{
                    "success": False,
                    "error": f"--site-names matched no sites among the requested name(s): {', '.join(site_names)}",
                    "not_found": not_found_sites,
                }]

        output_hosts = []
        for site_entity in sites:
            site_id = site_entity.get('entity', {}).get('id')
            site_name = site_entity.get('entity', {}).get('name')
            if not site_id:
                continue

            query = {
                "query": STATIC_HOST_LIST_QUERY,
                "variables": {"accountId": account_id, "site": {"by": "ID", "input": site_id}},
                "operationName": "siteStaticHostList",
            }
            try:
                response = makeCall(args, configuration, query)
            except Exception as e:
                if verbose:
                    print(f"Skipping site {site_name} ({site_id}): {e}")
                continue

            items = (((response.get('data') or {}).get('site') or {}).get('staticHostList') or {}).get('items') or []
            if verbose:
                print(f"Site '{site_name}' ({site_id}): {len(items)} static host(s)")

            for item in items:
                host_out = {
                    "site_id": site_id,
                    "site_name": site_name,
                    "name": item.get('name'),
                    "ip": item.get('ip'),
                    "mac_address": item.get('macAddress'),
                }
                if not strip_ids:
                    host_out = {"id": item.get('hostId'), **host_out}
                output_hosts.append(host_out)

        names = parse_names_arg(getattr(args, 'names', None))
        if names:
            output_hosts, not_found = filter_items_by_name(output_hosts, names, name_key='name')
            if not_found:
                print(f"WARNING: --names: no match found for: {', '.join(not_found)}")
            if not output_hosts:
                return [{
                    "success": False,
                    "error": f"--names matched none of the requested name(s): {', '.join(names)}",
                    "not_found": not_found,
                }]

        output_hosts.sort(key=lambda h: ((h.get('site_name') or "").lower(), (h.get('name') or "").lower()))

        merge_into = getattr(args, 'merge_into', None)
        if merge_into:
            if getattr(args, 'format', 'json') == 'csv':
                return [{"success": False, "error": "--merge-into is only supported with -f/--format json for static_hosts"}]
            # Keyed by (site_name, name) since host names alone can collide
            # across sites.
            merged_list, created, updated = merge_items_into_file(
                output_hosts, merge_into,
                name_key=lambda h: (h.get('site_name'), h.get('name')),
            )
            print(f"Merged {len(output_hosts)} item(s) into {merge_into} ({created} new, {updated} updated, {len(merged_list)} total)")
            return [{
                "success": True,
                "output_file": merge_into,
                "account_id": account_id,
                "count": len(output_hosts),
                "merged_total": len(merged_list),
                "created": created,
                "updated": updated,
            }]

        return export_data_unified(
            data=output_hosts,
            args=args,
            base_name="static_hosts",
            account_id=account_id,
            csv_fieldnames=["site_name", "site_id", "name", "ip", "mac_address", "id"],
            default_directory="config_data",
        )

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]


def export_custom_apps_to_json(args, configuration):
    """Export Custom Applications to the bulk-module JSON shape.

    Flat array of {id, name, description, category, criteria} passed through
    from customAppData.customApplicationList, sorted by name
    (case-insensitive). With --strip-ids, top-level ids are omitted."""
    try:
        account_id = getAccountID(args, configuration)
        verbose = hasattr(args, 'verbose') and args.verbose
        strip_ids = hasattr(args, 'strip_ids') and args.strip_ids

        all_apps = []
        from_offset = 0
        while True:
            query = {
                "query": CUSTOM_APPLICATION_LIST_QUERY,
                "variables": {
                    "accountId": account_id,
                    "customApplicationListInput": {"paging": {"limit": PAGE_LIMIT, "from": from_offset}},
                },
                "operationName": "customAppDataCustomApplicationList",
            }
            response = makeCall(args, configuration, query)
            result = response['data']['customAppData']['customApplicationList']
            items = result.get('items') or []
            all_apps.extend(items)
            total = (result.get('paging') or {}).get('total', len(all_apps))
            if verbose:
                print(f"Retrieved {len(items)} custom applications (offset: {from_offset}, total: {total})")
            from_offset += PAGE_LIMIT
            if len(all_apps) >= total or not items:
                break

        output_apps = []
        for app in all_apps:
            # Deterministic order - the API does not guarantee stable order
            # for the category list, which otherwise produces diff noise
            # across repeated exports of an unchanged app.
            categories_out = sorted(
                app.get('category') or [],
                key=lambda c: ((c.get('name') or '').lower(), str(c.get('id') or '')),
            )

            app_out = {
                "name": app.get('name'),
                "description": app.get('description') or "",
                "category": categories_out,
                "criteria": app.get('criteria') or [],
            }
            if not strip_ids:
                app_out = {"id": app.get('id'), **app_out}
            output_apps.append(app_out)

        return _finalize_export(output_apps, args, account_id, "custom_applications.json")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return [{"success": False, "error": str(e)}]
