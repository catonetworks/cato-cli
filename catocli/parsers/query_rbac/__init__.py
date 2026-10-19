
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_rbac_parse(query_subparsers):
    query_rbac_parser = query_subparsers.add_parser('rbac', 
            help='rbac() query operation', 
            usage=get_help("query_rbac"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_rbac_help(args, configuration=None):
        """Show help when query_rbac is called without subcommand"""
        print("\ncatocli query rbac <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  roleManagement                 roleManagement operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query rbac <subcommand> -h")
        return None

    query_rbac_subparsers = query_rbac_parser.add_subparsers()
    query_rbac_parser.set_defaults(func=_show_query_rbac_help)

    query_rbac_roleManagement_parser = query_rbac_subparsers.add_parser('roleManagement', 
            help='roleManagement() rbac operation', 
            usage=get_help("query_rbac_roleManagement"))

    def _show_query_rbac_roleManagement_help(args, configuration=None):
        """Show help when query_rbac_roleManagement is called without subcommand"""
        print("\ncatocli query rbac roleManagement <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  permissionCatalog              permissionCatalog operation\n  role                           role operation\n  roleList                       roleList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query rbac roleManagement <subcommand> -h")
        return None

    query_rbac_roleManagement_subparsers = query_rbac_roleManagement_parser.add_subparsers()
    query_rbac_roleManagement_parser.set_defaults(func=_show_query_rbac_roleManagement_help)

    query_rbac_roleManagement_permissionCatalog_parser = query_rbac_roleManagement_subparsers.add_parser('permissionCatalog', 
            help='permissionCatalog() roleManagement operation', 
            usage=get_help("query_rbac_roleManagement_permissionCatalog"))

    query_rbac_roleManagement_permissionCatalog_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_rbac_roleManagement_permissionCatalog_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_rbac_roleManagement_permissionCatalog_parser.set_defaults(func=createRequest,operation_name='query.rbac.roleManagement.permissionCatalog')

    query_rbac_roleManagement_role_parser = query_rbac_roleManagement_subparsers.add_parser('role', 
            help='role() roleManagement operation', 
            usage=get_help("query_rbac_roleManagement_role"))

    query_rbac_roleManagement_role_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_rbac_roleManagement_role_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_rbac_roleManagement_role_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_rbac_roleManagement_role_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_rbac_roleManagement_role_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_rbac_roleManagement_role_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_rbac_roleManagement_role_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_rbac_roleManagement_role_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_rbac_roleManagement_role_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_rbac_roleManagement_role_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_rbac_roleManagement_role_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_rbac_roleManagement_role_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_rbac_roleManagement_role_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_rbac_roleManagement_role_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_rbac_roleManagement_role_parser.set_defaults(func=createRequest,operation_name='query.rbac.roleManagement.role')

    query_rbac_roleManagement_roleList_parser = query_rbac_roleManagement_subparsers.add_parser('roleList', 
            help='roleList() roleManagement operation', 
            usage=get_help("query_rbac_roleManagement_roleList"))

    query_rbac_roleManagement_roleList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_rbac_roleManagement_roleList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_rbac_roleManagement_roleList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_rbac_roleManagement_roleList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_rbac_roleManagement_roleList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_rbac_roleManagement_roleList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_rbac_roleManagement_roleList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_rbac_roleManagement_roleList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_rbac_roleManagement_roleList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_rbac_roleManagement_roleList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_rbac_roleManagement_roleList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_rbac_roleManagement_roleList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_rbac_roleManagement_roleList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_rbac_roleManagement_roleList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_rbac_roleManagement_roleList_parser.set_defaults(func=createRequest,operation_name='query.rbac.roleManagement.roleList')
