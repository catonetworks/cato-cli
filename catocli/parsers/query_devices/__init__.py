
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_devices_parse(query_subparsers):
    query_devices_parser = query_subparsers.add_parser('devices', 
            help='devices() query operation', 
            usage=get_help("query_devices"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_devices_help(args, configuration=None):
        """Show help when query_devices is called without subcommand"""
        print("\ncatocli query devices <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  list                           list operation\n  attributesCatalog              attributesCatalog operation\n  csvExport                      csvExport operation\n  csvExportStatus                csvExportStatus operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query devices <subcommand> -h")
        return None

    query_devices_subparsers = query_devices_parser.add_subparsers()
    query_devices_parser.set_defaults(func=_show_query_devices_help)

    query_devices_list_parser = query_devices_subparsers.add_parser('list', 
            help='list() devices operation', 
            usage=get_help("query_devices_list"))

    query_devices_list_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_devices_list_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_devices_list_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_devices_list_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_devices_list_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_devices_list_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_devices_list_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_devices_list_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_devices_list_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_devices_list_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_devices_list_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_devices_list_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_devices_list_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_devices_list_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_devices_list_parser.set_defaults(func=createRequest,operation_name='query.devices.list')

    query_devices_attributesCatalog_parser = query_devices_subparsers.add_parser('attributesCatalog', 
            help='attributesCatalog() devices operation', 
            usage=get_help("query_devices_attributesCatalog"))

    query_devices_attributesCatalog_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_devices_attributesCatalog_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_devices_attributesCatalog_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_devices_attributesCatalog_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_devices_attributesCatalog_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_devices_attributesCatalog_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_devices_attributesCatalog_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_devices_attributesCatalog_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_devices_attributesCatalog_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_devices_attributesCatalog_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_devices_attributesCatalog_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_devices_attributesCatalog_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_devices_attributesCatalog_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_devices_attributesCatalog_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_devices_attributesCatalog_parser.set_defaults(func=createRequest,operation_name='query.devices.attributesCatalog')

    query_devices_csvExport_parser = query_devices_subparsers.add_parser('csvExport', 
            help='csvExport() devices operation', 
            usage=get_help("query_devices_csvExport"))

    query_devices_csvExport_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_devices_csvExport_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_devices_csvExport_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_devices_csvExport_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_devices_csvExport_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_devices_csvExport_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_devices_csvExport_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_devices_csvExport_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_devices_csvExport_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_devices_csvExport_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_devices_csvExport_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_devices_csvExport_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_devices_csvExport_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_devices_csvExport_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_devices_csvExport_parser.set_defaults(func=createRequest,operation_name='query.devices.csvExport')

    query_devices_csvExportStatus_parser = query_devices_subparsers.add_parser('csvExportStatus', 
            help='csvExportStatus() devices operation', 
            usage=get_help("query_devices_csvExportStatus"))

    query_devices_csvExportStatus_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_devices_csvExportStatus_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_devices_csvExportStatus_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_devices_csvExportStatus_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_devices_csvExportStatus_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_devices_csvExportStatus_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_devices_csvExportStatus_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_devices_csvExportStatus_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_devices_csvExportStatus_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_devices_csvExportStatus_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_devices_csvExportStatus_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_devices_csvExportStatus_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_devices_csvExportStatus_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_devices_csvExportStatus_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_devices_csvExportStatus_parser.set_defaults(func=createRequest,operation_name='query.devices.csvExportStatus')
