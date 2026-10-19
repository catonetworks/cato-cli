
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_user_parse(query_subparsers):
    query_user_parser = query_subparsers.add_parser('user', 
            help='user() query operation', 
            usage=get_help("query_user"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_user_help(args, configuration=None):
        """Show help when query_user is called without subcommand"""
        print("\ncatocli query user <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  userList                       userList operation\n  dynamicUserGroupsConfiguration dynamicUserGroupsConfiguration operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query user <subcommand> -h")
        return None

    query_user_subparsers = query_user_parser.add_subparsers()
    query_user_parser.set_defaults(func=_show_query_user_help)

    query_user_userList_parser = query_user_subparsers.add_parser('userList', 
            help='userList() user operation', 
            usage=get_help("query_user_userList"))

    query_user_userList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_user_userList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_user_userList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_user_userList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_user_userList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_user_userList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_user_userList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_user_userList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_user_userList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_user_userList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_user_userList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_user_userList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_user_userList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_user_userList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_user_userList_parser.set_defaults(func=createRequest,operation_name='query.user.userList')

    query_user_dynamicUserGroupsConfiguration_parser = query_user_subparsers.add_parser('dynamicUserGroupsConfiguration', 
            help='dynamicUserGroupsConfiguration() user operation', 
            usage=get_help("query_user_dynamicUserGroupsConfiguration"))

    query_user_dynamicUserGroupsConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_user_dynamicUserGroupsConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_user_dynamicUserGroupsConfiguration_parser.set_defaults(func=createRequest,operation_name='query.user.dynamicUserGroupsConfiguration')
