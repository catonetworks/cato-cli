
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_customAppData_parse(mutation_subparsers):
    mutation_customAppData_parser = mutation_subparsers.add_parser('customAppData', 
            help='customAppData() mutation operation', 
            usage=get_help("mutation_customAppData"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_customAppData_help(args, configuration=None):
        """Show help when mutation_customAppData is called without subcommand"""
        print("\ncatocli mutation customAppData <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  addCustomApplication           addCustomApplication operation\n  updateCustomApplication        updateCustomApplication operation\n  deleteCustomApplication        deleteCustomApplication operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation customAppData <subcommand> -h")
        return None

    mutation_customAppData_subparsers = mutation_customAppData_parser.add_subparsers()
    mutation_customAppData_parser.set_defaults(func=_show_mutation_customAppData_help)

    mutation_customAppData_addCustomApplication_parser = mutation_customAppData_subparsers.add_parser('addCustomApplication', 
            help='addCustomApplication() customAppData operation', 
            usage=get_help("mutation_customAppData_addCustomApplication"))

    mutation_customAppData_addCustomApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_customAppData_addCustomApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_customAppData_addCustomApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_customAppData_addCustomApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_customAppData_addCustomApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_customAppData_addCustomApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_customAppData_addCustomApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_customAppData_addCustomApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_customAppData_addCustomApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_customAppData_addCustomApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_customAppData_addCustomApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_customAppData_addCustomApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_customAppData_addCustomApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_customAppData_addCustomApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_customAppData_addCustomApplication_parser.set_defaults(func=createRequest,operation_name='mutation.customAppData.addCustomApplication')

    mutation_customAppData_updateCustomApplication_parser = mutation_customAppData_subparsers.add_parser('updateCustomApplication', 
            help='updateCustomApplication() customAppData operation', 
            usage=get_help("mutation_customAppData_updateCustomApplication"))

    mutation_customAppData_updateCustomApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_customAppData_updateCustomApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_customAppData_updateCustomApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_customAppData_updateCustomApplication_parser.set_defaults(func=createRequest,operation_name='mutation.customAppData.updateCustomApplication')

    mutation_customAppData_deleteCustomApplication_parser = mutation_customAppData_subparsers.add_parser('deleteCustomApplication', 
            help='deleteCustomApplication() customAppData operation', 
            usage=get_help("mutation_customAppData_deleteCustomApplication"))

    mutation_customAppData_deleteCustomApplication_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_customAppData_deleteCustomApplication_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_customAppData_deleteCustomApplication_parser.set_defaults(func=createRequest,operation_name='mutation.customAppData.deleteCustomApplication')
