
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_object_parse(mutation_subparsers):
    mutation_object_parser = mutation_subparsers.add_parser('object', 
            help='object() mutation operation', 
            usage=get_help("mutation_object"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_object_help(args, configuration=None):
        """Show help when mutation_object is called without subcommand"""
        print("\ncatocli mutation object <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createGlobalIpRangeBulk        createGlobalIpRangeBulk operation\n  updateGlobalIpRangeBulk        updateGlobalIpRangeBulk operation\n  deleteGlobalIpRangeBulk        deleteGlobalIpRangeBulk operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation object <subcommand> -h")
        return None

    mutation_object_subparsers = mutation_object_parser.add_subparsers()
    mutation_object_parser.set_defaults(func=_show_mutation_object_help)

    mutation_object_createGlobalIpRangeBulk_parser = mutation_object_subparsers.add_parser('createGlobalIpRangeBulk', 
            help='createGlobalIpRangeBulk() object operation', 
            usage=get_help("mutation_object_createGlobalIpRangeBulk"))

    mutation_object_createGlobalIpRangeBulk_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_object_createGlobalIpRangeBulk_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_object_createGlobalIpRangeBulk_parser.set_defaults(func=createRequest,operation_name='mutation.object.createGlobalIpRangeBulk')

    mutation_object_updateGlobalIpRangeBulk_parser = mutation_object_subparsers.add_parser('updateGlobalIpRangeBulk', 
            help='updateGlobalIpRangeBulk() object operation', 
            usage=get_help("mutation_object_updateGlobalIpRangeBulk"))

    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_object_updateGlobalIpRangeBulk_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_object_updateGlobalIpRangeBulk_parser.set_defaults(func=createRequest,operation_name='mutation.object.updateGlobalIpRangeBulk')

    mutation_object_deleteGlobalIpRangeBulk_parser = mutation_object_subparsers.add_parser('deleteGlobalIpRangeBulk', 
            help='deleteGlobalIpRangeBulk() object operation', 
            usage=get_help("mutation_object_deleteGlobalIpRangeBulk"))

    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_object_deleteGlobalIpRangeBulk_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_object_deleteGlobalIpRangeBulk_parser.set_defaults(func=createRequest,operation_name='mutation.object.deleteGlobalIpRangeBulk')
