
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_user_parse(mutation_subparsers):
    mutation_user_parser = mutation_subparsers.add_parser('user', 
            help='user() mutation operation', 
            usage=get_help("mutation_user"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_user_help(args, configuration=None):
        """Show help when mutation_user is called without subcommand"""
        print("\ncatocli mutation user <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createUser                     createUser operation\n  updateUser                     updateUser operation\n  deleteUser                     deleteUser operation\n  revokeUserSession              revokeUserSession operation\n  enableUser                     enableUser operation\n  disableUser                    disableUser operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation user <subcommand> -h")
        return None

    mutation_user_subparsers = mutation_user_parser.add_subparsers()
    mutation_user_parser.set_defaults(func=_show_mutation_user_help)

    mutation_user_createUser_parser = mutation_user_subparsers.add_parser('createUser', 
            help='createUser() user operation', 
            usage=get_help("mutation_user_createUser"))

    mutation_user_createUser_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_createUser_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_createUser_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_createUser_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_createUser_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_createUser_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_createUser_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_createUser_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_createUser_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_createUser_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_createUser_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_createUser_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_createUser_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_createUser_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_createUser_parser.set_defaults(func=createRequest,operation_name='mutation.user.createUser')

    mutation_user_updateUser_parser = mutation_user_subparsers.add_parser('updateUser', 
            help='updateUser() user operation', 
            usage=get_help("mutation_user_updateUser"))

    mutation_user_updateUser_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_updateUser_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_updateUser_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_updateUser_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_updateUser_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_updateUser_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_updateUser_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_updateUser_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_updateUser_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_updateUser_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_updateUser_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_updateUser_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_updateUser_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_updateUser_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_updateUser_parser.set_defaults(func=createRequest,operation_name='mutation.user.updateUser')

    mutation_user_deleteUser_parser = mutation_user_subparsers.add_parser('deleteUser', 
            help='deleteUser() user operation', 
            usage=get_help("mutation_user_deleteUser"))

    mutation_user_deleteUser_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_deleteUser_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_deleteUser_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_deleteUser_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_deleteUser_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_deleteUser_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_deleteUser_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_deleteUser_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_deleteUser_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_deleteUser_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_deleteUser_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_deleteUser_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_deleteUser_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_deleteUser_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_deleteUser_parser.set_defaults(func=createRequest,operation_name='mutation.user.deleteUser')

    mutation_user_revokeUserSession_parser = mutation_user_subparsers.add_parser('revokeUserSession', 
            help='revokeUserSession() user operation', 
            usage=get_help("mutation_user_revokeUserSession"))

    mutation_user_revokeUserSession_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_revokeUserSession_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_revokeUserSession_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_revokeUserSession_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_revokeUserSession_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_revokeUserSession_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_revokeUserSession_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_revokeUserSession_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_revokeUserSession_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_revokeUserSession_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_revokeUserSession_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_revokeUserSession_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_revokeUserSession_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_revokeUserSession_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_revokeUserSession_parser.set_defaults(func=createRequest,operation_name='mutation.user.revokeUserSession')

    mutation_user_enableUser_parser = mutation_user_subparsers.add_parser('enableUser', 
            help='enableUser() user operation', 
            usage=get_help("mutation_user_enableUser"))

    mutation_user_enableUser_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_enableUser_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_enableUser_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_enableUser_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_enableUser_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_enableUser_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_enableUser_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_enableUser_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_enableUser_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_enableUser_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_enableUser_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_enableUser_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_enableUser_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_enableUser_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_enableUser_parser.set_defaults(func=createRequest,operation_name='mutation.user.enableUser')

    mutation_user_disableUser_parser = mutation_user_subparsers.add_parser('disableUser', 
            help='disableUser() user operation', 
            usage=get_help("mutation_user_disableUser"))

    mutation_user_disableUser_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_user_disableUser_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_user_disableUser_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_user_disableUser_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_user_disableUser_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_user_disableUser_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_user_disableUser_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_user_disableUser_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_user_disableUser_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_user_disableUser_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_user_disableUser_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_user_disableUser_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_user_disableUser_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_user_disableUser_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_user_disableUser_parser.set_defaults(func=createRequest,operation_name='mutation.user.disableUser')
