import catocli.parsers.custom.export_deps.export_deps as export_deps
from ...utils.export_utils import add_common_export_arguments, add_name_filter_arguments

STRIP_IDS_HELP = (
    "Omit tenant-specific \"id\" keys from the output (top-level ids, and for "
    "'groups' also member ids, keeping member {type, name} only) so the file "
    "can be migrated into a different tenant. NOTE: groups containing member "
    "types that can only be resolved by id in the source tenant today "
    "(FLOATING_SUBNET, HOST, NETWORK_INTERFACE, SITE_NETWORK_SUBNET) will need "
    "those members' ids manually re-resolved against the target tenant after "
    "import."
)

MAILING_LIST_STRIP_IDS_HELP = (
    "Omit tenant-specific \"id\" keys from the output (top-level ids and each "
    "admin's id, keeping admin {name} only). NOTE: admin references REQUIRE "
    "an id in the provider - a --strip-ids export's admin entries will need "
    "their ids manually re-resolved against the target tenant before they "
    "can be used."
)

SUBSCRIPTION_GROUP_STRIP_IDS_HELP = (
    "Omit tenant-specific \"id\" keys from the output (top-level ids, and "
    "ids on nested mailing_list/integration entries, keeping {name} only) so "
    "the file can be migrated into a different tenant."
)

DHCP_RELAY_GROUP_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" from the output so the file "
    "can be migrated into a different tenant (the provider resolves relay "
    "groups by name on import, so the opaque id is not needed)."
)

CONTAINER_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" from the output so the file "
    "can be migrated into a different tenant."
)

STATIC_HOST_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" from the output (site_id/"
    "site_name are always kept since they identify where the host lives)."
)

WEBHOOK_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" from the output so the file "
    "can be migrated into a different tenant. NOTE: \"relatedWebhookId\" is "
    "NOT stripped - it is an id-only cross-reference to another webhook "
    "(chained webhooks) with no name-based fallback in the API, so it will "
    "need to be manually re-resolved against the target tenant if used."
)

ALLOCATED_IP_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" and the nested popLocation's "
    "\"id\" from the output (the synthesized \"name\" field - \"{popLocation "
    "name} - {ip}\" - is left untouched, since it is this object's "
    "cross-tenant remap join key)."
)

PRIVATE_APP_STRIP_IDS_HELP = (
    "Omit the tenant-specific top-level \"id\" and the nested "
    "publishedAppDomain's \"id\" from the output so the file can be "
    "migrated into a different tenant."
)

APP_CONNECTOR_STRIP_IDS_HELP = (
    "Omit each connector's tenant-specific top-level \"id\" and its nested "
    "preferredPopLocation primary/secondary \"id\"s from the output. "
    "\"groups\" (plain name strings) is unaffected - there is no id to strip."
)


def export_deps_parse(subparsers):
    """Create export parsers for the 1-dependencies object types: Groups,
    Global IP Ranges, and Custom Applications."""

    # Add groups command
    groups_parser = subparsers.add_parser(
        'groups',
        help='Export Groups to JSON format',
        usage='catocli export groups [-accountID <account_id>] [options]',
        description='''Export Groups to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, members: [{type, id, name}]}, sorted by
name (case-insensitive). Members are fetched per-group via
groups.group.members, paging both the group list and each group's member
list in batches of 1000.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export groups

  # Export with specific account ID
  catocli export groups -accountID 12345

  # Export with custom filename and timestamp
  catocli export groups --json-filename my_groups.json --append-timestamp

  # Export to custom directory
  catocli export groups --output-directory ./exports

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export groups --strip-ids

  # Export only specific named groups (escape a literal comma in a name with \\,)
  catocli export groups --names "Group A,Finance\\, HR Group"

  # Pull 2 named groups from a second tenant and merge them into this repo's groups.json
  CATO_PROFILE=tenantB catocli export groups --names "Group A,Group B" --merge-into ../config_data/groups.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    groups_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    groups_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: groups.json)')
    groups_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    groups_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    groups_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=STRIP_IDS_HELP)
    add_name_filter_arguments(groups_parser, names_help='Comma-separated list of exact group names to export, instead of exporting every group.')
    groups_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    groups_parser.set_defaults(func=export_deps.export_groups_to_json)

    # Add global_ip_ranges command
    global_ip_ranges_parser = subparsers.add_parser(
        'global_ip_ranges',
        help='Export Global IP Ranges to JSON format',
        usage='catocli export global_ip_ranges [-accountID <account_id>] [options]',
        description='''Export Global IP Ranges to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, ipRange}, sorted by name. Single-call
export (object.globalIpRangeList is not paginated).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export global_ip_ranges

  # Export with specific account ID
  catocli export global_ip_ranges -accountID 12345

  # Export with custom filename and timestamp
  catocli export global_ip_ranges --json-filename my_ranges.json --append-timestamp

  # Export to custom directory
  catocli export global_ip_ranges --output-directory ./exports

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export global_ip_ranges --strip-ids

  # Export only specific named ranges (escape a literal comma in a name with \\,)
  catocli export global_ip_ranges --names "Range A,Branch Offices\\, EU"

  # Pull 2 named ranges from a second tenant and merge them into this repo's global_ip_ranges.json
  CATO_PROFILE=tenantB catocli export global_ip_ranges --names "Range A,Range B" --merge-into ../config_data/global_ip_ranges.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    global_ip_ranges_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    global_ip_ranges_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: global_ip_ranges.json)')
    global_ip_ranges_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    global_ip_ranges_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    global_ip_ranges_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=STRIP_IDS_HELP)
    add_name_filter_arguments(global_ip_ranges_parser, names_help='Comma-separated list of exact range names to export, instead of exporting every range.')
    global_ip_ranges_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    global_ip_ranges_parser.set_defaults(func=export_deps.export_global_ip_ranges_to_json)

    # Add dhcp_relay_groups command
    dhcp_relay_groups_parser = subparsers.add_parser(
        'dhcp_relay_groups',
        help='Export DHCP Relay Groups to JSON format',
        usage='catocli export dhcp_relay_groups [-accountID <account_id>] [options]',
        description='''Export DHCP Relay Groups to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, server}, sorted by name. Pages networkConfig.dhcp.
relayGroupList in batches of 100 (the API's own paging cap for this list).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export dhcp_relay_groups

  # Export with specific account ID
  catocli export dhcp_relay_groups -accountID 12345

  # Export with custom filename and timestamp
  catocli export dhcp_relay_groups --json-filename my_relay_groups.json --append-timestamp

  # Export to custom directory
  catocli export dhcp_relay_groups --output-directory ./exports

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export dhcp_relay_groups --strip-ids

  # Export only specific named relay groups (escape a literal comma in a name with \\,)
  catocli export dhcp_relay_groups --names "Relay A,Branch Offices\\, EU"

  # Pull 2 named relay groups from a second tenant and merge them into this repo's dhcp_relay_groups.json
  CATO_PROFILE=tenantB catocli export dhcp_relay_groups --names "Relay A,Relay B" --merge-into ../config_data/dhcp_relay_groups.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    dhcp_relay_groups_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    dhcp_relay_groups_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: dhcp_relay_groups.json)')
    dhcp_relay_groups_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    dhcp_relay_groups_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    dhcp_relay_groups_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=DHCP_RELAY_GROUP_STRIP_IDS_HELP)
    add_name_filter_arguments(dhcp_relay_groups_parser, names_help='Comma-separated list of exact DHCP relay group names to export, instead of exporting every group.')
    dhcp_relay_groups_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    dhcp_relay_groups_parser.set_defaults(func=export_deps.export_dhcp_relay_groups_to_json)

    # Add custom_apps command
    custom_apps_parser = subparsers.add_parser(
        'custom_apps',
        help='Export Custom Applications to JSON format',
        usage='catocli export custom_apps [-accountID <account_id>] [options]',
        description='''Export Custom Applications to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, category, criteria} passed through
from customAppData.customApplicationList, sorted by name (case-insensitive).
Pages the custom application list in batches of 1000.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export custom_apps

  # Export with specific account ID
  catocli export custom_apps -accountID 12345

  # Export with custom filename and timestamp
  catocli export custom_apps --json-filename my_custom_apps.json --append-timestamp

  # Export to custom directory
  catocli export custom_apps --output-directory ./exports

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export custom_apps --strip-ids

  # Export only specific named custom apps (escape a literal comma in a name with \\,)
  catocli export custom_apps --names "CatoGPT,Finance\\, HR App"

  # Pull 2 named apps from a second tenant and merge them into this repo's custom_applications.json
  CATO_PROFILE=tenantB catocli export custom_apps --names "App A,App B" --merge-into ../config_data/custom_applications.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    custom_apps_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    custom_apps_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: custom_applications.json)')
    custom_apps_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    custom_apps_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    custom_apps_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=STRIP_IDS_HELP)
    add_name_filter_arguments(custom_apps_parser, names_help='Comma-separated list of exact custom application names to export, instead of exporting every app.')
    custom_apps_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    custom_apps_parser.set_defaults(func=export_deps.export_custom_apps_to_json)

    # Add mailing_lists command
    mailing_lists_parser = subparsers.add_parser(
        'mailing_lists',
        help='Export Mailing Lists to JSON format',
        usage='catocli export mailing_lists [-accountID <account_id>] [options]',
        description='''Export Mailing Lists to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, address: [...], admin: [{id, name}]}, sorted by
name (case-insensitive). Single-call export (notification.mailingListList
is not paginated).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export mailing_lists

  # Export with specific account ID
  catocli export mailing_lists -accountID 12345

  # Export with custom filename and timestamp
  catocli export mailing_lists --json-filename my_mailing_lists.json --append-timestamp

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export mailing_lists --strip-ids

  # Export only specific named mailing lists (escape a literal comma in a name with \\,)
  catocli export mailing_lists --names "All Admins,Finance\\, HR List"

  # Pull 2 named mailing lists from a second tenant and merge them into this repo's mailing_lists.json
  CATO_PROFILE=tenantB catocli export mailing_lists --names "List A,List B" --merge-into ../config_data/mailing_lists.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    mailing_lists_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    mailing_lists_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: mailing_lists.json)')
    mailing_lists_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    mailing_lists_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    mailing_lists_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=MAILING_LIST_STRIP_IDS_HELP)
    add_name_filter_arguments(mailing_lists_parser, names_help='Comma-separated list of exact mailing list names to export, instead of exporting every list.')
    mailing_lists_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    mailing_lists_parser.set_defaults(func=export_deps.export_mailing_lists_to_json)

    # Add subscription_groups command
    subscription_groups_parser = subparsers.add_parser(
        'subscription_groups',
        help='Export Subscription Groups to JSON format',
        usage='catocli export subscription_groups [-accountID <account_id>] [options]',
        description='''Export Subscription Groups to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, mailing_list: [{id, name}], integration: [{id,
name}]}, sorted by name (case-insensitive). "integration" is the group's
webhook integrations. Single-call export (notification.
subscriptionGroupList is not paginated).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export subscription_groups

  # Export with specific account ID
  catocli export subscription_groups -accountID 12345

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export subscription_groups --strip-ids

  # Export only specific named subscription groups (escape a literal comma in a name with \\,)
  catocli export subscription_groups --names "SOC,Finance\\, HR Group"

  # Pull 2 named groups from a second tenant and merge them into this repo's subscription_groups.json
  CATO_PROFILE=tenantB catocli export subscription_groups --names "SOC,NOC" --merge-into ../config_data/subscription_groups.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    subscription_groups_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    subscription_groups_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: subscription_groups.json)')
    subscription_groups_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    subscription_groups_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    subscription_groups_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=SUBSCRIPTION_GROUP_STRIP_IDS_HELP)
    add_name_filter_arguments(subscription_groups_parser, names_help='Comma-separated list of exact subscription group names to export, instead of exporting every group.')
    subscription_groups_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    subscription_groups_parser.set_defaults(func=export_deps.export_subscription_groups_to_json)

    # Add fqdn_containers command
    fqdn_containers_parser = subparsers.add_parser(
        'fqdn_containers',
        help='Export FQDN Containers to JSON format',
        usage='catocli export fqdn_containers [-accountID <account_id>] [options]',
        description='''Export FQDN Containers to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, mode, values: [...fqdn strings...]},
sorted by name (case-insensitive). "mode" is INLINE or URL, derived from
whether the container's syncData is null; URL-mode containers additionally
carry "file_type" and "sync_data". Member values are always fetched via
container.fqdn.downloadFile and parsed from the returned file content.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export fqdn_containers

  # Export with specific account ID
  catocli export fqdn_containers -accountID 12345

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export fqdn_containers --strip-ids

  # Export only specific named containers (escape a literal comma in a name with \\,)
  catocli export fqdn_containers --names "fqdn_container,Finance\\, HR Blocklist"

  # Pull 2 named containers from a second tenant and merge them into this repo's fqdn_containers.json
  CATO_PROFILE=tenantB catocli export fqdn_containers --names "Container A,Container B" --merge-into ../config_data/fqdn_containers.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    fqdn_containers_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    fqdn_containers_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: fqdn_containers.json)')
    fqdn_containers_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    fqdn_containers_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    fqdn_containers_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=CONTAINER_STRIP_IDS_HELP)
    add_name_filter_arguments(fqdn_containers_parser, names_help='Comma-separated list of exact FQDN container names to export, instead of exporting every container.')
    fqdn_containers_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    fqdn_containers_parser.set_defaults(func=export_deps.export_fqdn_containers_to_json)

    # Add ip_range_containers command
    ip_range_containers_parser = subparsers.add_parser(
        'ip_range_containers',
        help='Export IP Range Containers to JSON format',
        usage='catocli export ip_range_containers [-accountID <account_id>] [options]',
        description='''Export IP Range Containers to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, mode, values: [{from, to}, ...]},
sorted by name (case-insensitive). "mode" is INLINE or URL, derived from
whether the container's syncData is null; URL-mode containers additionally
carry "file_type" and "sync_data". Member values are always fetched via
container.ipAddressRange.downloadFile and parsed from the returned file
content (a single-IP row is returned as {from: ip, to: ip}).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export ip_range_containers

  # Export with specific account ID
  catocli export ip_range_containers -accountID 12345

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export ip_range_containers --strip-ids

  # Export only specific named containers (escape a literal comma in a name with \\,)
  catocli export ip_range_containers --names "ip_container,Finance\\, HR Ranges"

  # Pull 2 named containers from a second tenant and merge them into this repo's ip_range_containers.json
  CATO_PROFILE=tenantB catocli export ip_range_containers --names "Container A,Container B" --merge-into ../config_data/ip_range_containers.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    ip_range_containers_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    ip_range_containers_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: ip_range_containers.json)')
    ip_range_containers_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    ip_range_containers_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    ip_range_containers_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=CONTAINER_STRIP_IDS_HELP)
    add_name_filter_arguments(ip_range_containers_parser, names_help='Comma-separated list of exact IP range container names to export, instead of exporting every container.')
    ip_range_containers_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    ip_range_containers_parser.set_defaults(func=export_deps.export_ip_range_containers_to_json)

    # Add static_hosts command
    static_hosts_parser = subparsers.add_parser(
        'static_hosts',
        help='Export Static Hosts to JSON or CSV format',
        usage='catocli export static_hosts [-accountID <account_id>] [options]',
        description='''Export Static Hosts to JSON or CSV format for backup, analysis, or migration purposes.

Flat array/table of {id, site_id, site_name, name, ip, mac_address} sorted
by (site_name, name) case-insensitive. Sites are enumerated via
entityLookup(type: "site"); each site's hosts come from
site.staticHostList. Supports both JSON and CSV output (-f/--format).

Examples:
  # Basic export to JSON (uses CATO_ACCOUNT_ID environment variable)
  catocli export static_hosts

  # Export to CSV
  catocli export static_hosts -f csv

  # Export with specific account ID
  catocli export static_hosts -accountID 12345

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export static_hosts --strip-ids

  # Export only specific named hosts (escape a literal comma in a name with \\,)
  catocli export static_hosts --names "rasp01-app,Finance\\, HR Printer"

  # Export only hosts on specific named sites
  catocli export static_hosts --site-names "NA-US-RIC-BR,NA-US-SAN-BR"

  # Pull 2 named hosts from a second tenant and merge them into this repo's static_hosts.json (JSON only)
  CATO_PROFILE=tenantB catocli export static_hosts --names "Host A,Host B" --merge-into ../config_data/static_hosts.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    static_hosts_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    add_common_export_arguments(static_hosts_parser)
    for action in static_hosts_parser._actions:
        if action.dest == 'json_filename':
            action.help = 'Override JSON file name (default: static_hosts.json)'
        elif action.dest == 'csv_filename':
            action.help = 'Override CSV file name (default: static_hosts.csv)'
    static_hosts_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=STATIC_HOST_STRIP_IDS_HELP)
    add_name_filter_arguments(
        static_hosts_parser,
        names_help='Comma-separated list of exact host names to export, instead of exporting every host.',
        site_names_help='Comma-separated list of exact site names to filter hosts by.',
        include_site_names=True,
    )
    static_hosts_parser.add_argument(
        '--site-type', dest='site_type', choices=['physical', 'cloud', 'all'], default='physical',
        help="Which sites' hosts to export: physical = socket sites (connType in "
             "clisettings export_by_socket_type, matches the socket_sites export); "
             "cloud = non-physical (vSocket/SASE/cloud) sites; all = every site. "
             "Default physical, so static_hosts.json stays consistent with socket_sites.json.")
    static_hosts_parser.set_defaults(func=export_deps.export_static_hosts)

    # Add webhooks command
    webhooks_parser = subparsers.add_parser(
        'webhooks',
        help='Export Webhooks to JSON format',
        usage='catocli export webhooks [-accountID <account_id>] [options]',
        description='''Export Webhooks to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, enabled, url, requestMethod, relatedWebhookId},
sorted by name (case-insensitive). Single-call export (notification.
integration.webhookList is not paginated). This is the same underlying
object subscription_groups.json's "integration" field already references by
{id, name} - exported here as first-class objects with their own metadata.
Deliberately omits the webhook's "auth"/"header"/"body"/"responseMapping"
fields (not requested from the API at all) so no exported file can ever
capture live webhook credentials.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export webhooks

  # Export with specific account ID
  catocli export webhooks -accountID 12345

  # Export with custom filename and timestamp
  catocli export webhooks --json-filename my_webhooks.json --append-timestamp

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export webhooks --strip-ids

  # Export only specific named webhooks (escape a literal comma in a name with \\,)
  catocli export webhooks --names "SOC Alerts,Finance\\, HR Webhook"

  # Pull 2 named webhooks from a second tenant and merge them into this repo's webhooks.json
  CATO_PROFILE=tenantB catocli export webhooks --names "Webhook A,Webhook B" --merge-into ../config_data/webhooks.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    webhooks_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    webhooks_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: webhooks.json)')
    webhooks_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    webhooks_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    webhooks_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=WEBHOOK_STRIP_IDS_HELP)
    add_name_filter_arguments(webhooks_parser, names_help='Comma-separated list of exact webhook names to export, instead of exporting every webhook.')
    webhooks_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    webhooks_parser.set_defaults(func=export_deps.export_webhooks_to_json)

    # Add allocated_ips command
    allocated_ips_parser = subparsers.add_parser(
        'allocated_ips',
        help='Export PoP-allocated IP addresses to JSON format',
        usage='catocli export allocated_ips [-accountID <account_id>] [options]',
        description='''Export PoP-allocated IP addresses to JSON format for backup, analysis, or migration purposes.

Flat array of {id, ip, description, allocationType, popLocation: {id, name},
name}, sorted by name (case-insensitive). This object has no native "name"
field of its own, so "name" is SYNTHESIZED as "{popLocation name} - {ip}" -
matching the CMA's own entity display name, and used as the cross-tenant
remap join key. Account-wide, single-call export (popLocations.
allocatedIpList is not paginated).

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export allocated_ips

  # Export with specific account ID
  catocli export allocated_ips -accountID 12345

  # Export with custom filename and timestamp
  catocli export allocated_ips --json-filename my_allocated_ips.json --append-timestamp

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export allocated_ips --strip-ids

  # Export only specific named allocations (escape a literal comma in a name with \\,)
  catocli export allocated_ips --names "London - 1.2.3.4,Finance\\, HR - 5.6.7.8"

  # Pull 2 named allocations from a second tenant and merge them into this repo's allocated_ips.json
  CATO_PROFILE=tenantB catocli export allocated_ips --names "London - 1.2.3.4,Paris - 2.3.4.5" --merge-into ../config_data/allocated_ips.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    allocated_ips_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    allocated_ips_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: allocated_ips.json)')
    allocated_ips_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    allocated_ips_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    allocated_ips_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=ALLOCATED_IP_STRIP_IDS_HELP)
    add_name_filter_arguments(allocated_ips_parser, names_help='Comma-separated list of exact (synthesized) allocation names to export, instead of exporting every allocation.')
    allocated_ips_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    allocated_ips_parser.set_defaults(func=export_deps.export_allocated_ips_to_json)

    # Add private_apps command
    private_apps_parser = subparsers.add_parser(
        'private_apps',
        help='Export Private Applications (ZTNA) to JSON format',
        usage='catocli export private_apps [-accountID <account_id>] [options]',
        description='''Export Private Applications (ZTNA) to JSON format for backup, analysis, or migration purposes.

Flat array of {id, name, description, internalAppAddress, allowIcmpProtocol,
probingEnabled, published, creationTime, privateAppProbing: {type, interval,
faultThresholdDown}, protocolPorts: [{protocol, port, portRange: {from,
to}}], publishedAppDomain: {id, publishedAppDomain, catoIp,
connectorGroupName}}, sorted by name (case-insensitive). Pages
privateApplication.privateApplicationList in batches of 1000.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export private_apps

  # Export with specific account ID
  catocli export private_apps -accountID 12345

  # Export with custom filename and timestamp
  catocli export private_apps --json-filename my_private_apps.json --append-timestamp

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export private_apps --strip-ids

  # Export only specific named apps (escape a literal comma in a name with \\,)
  catocli export private_apps --names "App A,Finance\\, HR App"

  # Pull 2 named apps from a second tenant and merge them into this repo's private_applications.json
  CATO_PROFILE=tenantB catocli export private_apps --names "App A,App B" --merge-into ../config_data/private_applications.json''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    private_apps_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    private_apps_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: private_applications.json)')
    private_apps_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    private_apps_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    private_apps_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=PRIVATE_APP_STRIP_IDS_HELP)
    add_name_filter_arguments(private_apps_parser, names_help='Comma-separated list of exact private application names to export, instead of exporting every app.')
    private_apps_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    private_apps_parser.set_defaults(func=export_deps.export_private_apps_to_json)

    # Add app_connectors command
    app_connectors_parser = subparsers.add_parser(
        'app_connectors',
        help='Export ZTNA App Connectors (+ their groups) to JSON format',
        usage='catocli export app_connectors [-accountID <account_id>] [options]',
        description='''Export ZTNA App Connectors (+ their groups) to JSON format for backup, analysis, or migration purposes.

Output file is a dict (not a flat array, unlike every other `catocli export`
type): {"connectors": [...], "groups": [...]}. "connectors" is a flat array
of {id, name, description, groupName, type, serialNumber, socketId,
socketModel, location: {address, cityName, countryCode, stateCode,
timezone}, preferredPopLocation: {preferredOnly, automatic, primary: {id,
name}, secondary: {id, name}}, pooledBandwidthAllocation: {allocationId,
licenseId, bw}}, sorted by name (case-insensitive). "groups" is a flat,
sorted array of connector group NAME strings (no ids). Pages
ztnaAppConnector.ztnaAppConnectorList in batches of 1000. --names filters
connectors[] only.

Examples:
  # Basic export (uses CATO_ACCOUNT_ID environment variable)
  catocli export app_connectors

  # Export with specific account ID
  catocli export app_connectors -accountID 12345

  # Export with custom filename and timestamp
  catocli export app_connectors --json-filename my_app_connectors.json --append-timestamp

  # Export for migration into a different tenant (omit tenant-specific ids)
  catocli export app_connectors --strip-ids

  # Export only specific named connectors (escape a literal comma in a name with \\,)
  catocli export app_connectors --names "Connector A,Finance\\, HR Connector"''',
        formatter_class=__import__('argparse').RawDescriptionHelpFormatter
    )

    app_connectors_parser.add_argument('-accountID', help='Account ID to export data from (uses CATO_ACCOUNT_ID environment variable if not specified)', required=False)
    app_connectors_parser.add_argument('--json-filename', dest='json_filename', help='Override JSON file name (default: app_connectors.json)')
    app_connectors_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to file names')
    app_connectors_parser.add_argument('--output-directory', dest='output_directory', help='Output directory for exported files (default: config_data)')
    app_connectors_parser.add_argument('--strip-ids', dest='strip_ids', action='store_true', help=APP_CONNECTOR_STRIP_IDS_HELP)
    add_name_filter_arguments(app_connectors_parser, names_help='Comma-separated list of exact connector names to export (filters connectors[] only; groups[] is always exported in full), instead of exporting every connector.')
    app_connectors_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    app_connectors_parser.set_defaults(func=export_deps.export_app_connectors_to_json)

    return (groups_parser, global_ip_ranges_parser, dhcp_relay_groups_parser, custom_apps_parser,
            mailing_lists_parser, subscription_groups_parser, fqdn_containers_parser,
            ip_range_containers_parser, static_hosts_parser, webhooks_parser,
            allocated_ips_parser, private_apps_parser, app_connectors_parser)
