
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_privateApplication_parse(mutation_subparsers):
    mutation_privateApplication_parser = mutation_subparsers.add_parser('privateApplication', 
            help='privateApplication() mutation operation', 
            usage=get_help("mutation_privateApplication"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_privateApplication_help(args, configuration=None):
        """Show help when mutation_privateApplication is called without subcommand"""
        print("\ncatocli mutation privateApplication <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createPrivateApplication       createPrivateApplication operation\n  updatePrivateApplication       updatePrivateApplication operation\n  deletePrivateApplication       deletePrivateApplication operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation privateApplication <subcommand> -h")
        return None

    mutation_privateApplication_subparsers = mutation_privateApplication_parser.add_subparsers()
    mutation_privateApplication_parser.set_defaults(func=_show_mutation_privateApplication_help)

    mutation_privateApplication_createPrivateApplication_parser = mutation_privateApplication_subparsers.add_parser('createPrivateApplication', 
            help='createPrivateApplication() privateApplication operation', 
            usage=get_help("mutation_privateApplication_createPrivateApplication"))

    mutation_privateApplication_createPrivateApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_privateApplication_createPrivateApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_privateApplication_createPrivateApplication_parser.set_defaults(func=createRequest,operation_name='mutation.privateApplication.createPrivateApplication')

    mutation_privateApplication_updatePrivateApplication_parser = mutation_privateApplication_subparsers.add_parser('updatePrivateApplication', 
            help='updatePrivateApplication() privateApplication operation', 
            usage=get_help("mutation_privateApplication_updatePrivateApplication"))

    mutation_privateApplication_updatePrivateApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_privateApplication_updatePrivateApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_privateApplication_updatePrivateApplication_parser.set_defaults(func=createRequest,operation_name='mutation.privateApplication.updatePrivateApplication')

    mutation_privateApplication_deletePrivateApplication_parser = mutation_privateApplication_subparsers.add_parser('deletePrivateApplication', 
            help='deletePrivateApplication() privateApplication operation', 
            usage=get_help("mutation_privateApplication_deletePrivateApplication"))

    mutation_privateApplication_deletePrivateApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_privateApplication_deletePrivateApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_privateApplication_deletePrivateApplication_parser.set_defaults(func=createRequest,operation_name='mutation.privateApplication.deletePrivateApplication')
