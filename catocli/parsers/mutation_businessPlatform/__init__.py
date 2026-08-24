
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_businessPlatform_parse(mutation_subparsers):
    mutation_businessPlatform_parser = mutation_subparsers.add_parser('businessPlatform', 
            help='businessPlatform() mutation operation', 
            usage=get_help("mutation_businessPlatform"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_businessPlatform_help(args, configuration=None):
        """Show help when mutation_businessPlatform is called without subcommand"""
        print("\ncatocli mutation businessPlatform <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createTrialAccount             createTrialAccount operation\n  linkToTrialAccount             linkToTrialAccount operation\n  updateSettings                 updateSettings operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation businessPlatform <subcommand> -h")
        return None

    mutation_businessPlatform_subparsers = mutation_businessPlatform_parser.add_subparsers()
    mutation_businessPlatform_parser.set_defaults(func=_show_mutation_businessPlatform_help)

    mutation_businessPlatform_createTrialAccount_parser = mutation_businessPlatform_subparsers.add_parser('createTrialAccount', 
            help='createTrialAccount() businessPlatform operation', 
            usage=get_help("mutation_businessPlatform_createTrialAccount"))

    mutation_businessPlatform_createTrialAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_businessPlatform_createTrialAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_businessPlatform_createTrialAccount_parser.set_defaults(func=createRequest,operation_name='mutation.businessPlatform.createTrialAccount')

    mutation_businessPlatform_linkToTrialAccount_parser = mutation_businessPlatform_subparsers.add_parser('linkToTrialAccount', 
            help='linkToTrialAccount() businessPlatform operation', 
            usage=get_help("mutation_businessPlatform_linkToTrialAccount"))

    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_businessPlatform_linkToTrialAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_businessPlatform_linkToTrialAccount_parser.set_defaults(func=createRequest,operation_name='mutation.businessPlatform.linkToTrialAccount')

    mutation_businessPlatform_updateSettings_parser = mutation_businessPlatform_subparsers.add_parser('updateSettings', 
            help='updateSettings() businessPlatform operation', 
            usage=get_help("mutation_businessPlatform_updateSettings"))

    mutation_businessPlatform_updateSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_businessPlatform_updateSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_businessPlatform_updateSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_businessPlatform_updateSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_businessPlatform_updateSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_businessPlatform_updateSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_businessPlatform_updateSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_businessPlatform_updateSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_businessPlatform_updateSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_businessPlatform_updateSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_businessPlatform_updateSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_businessPlatform_updateSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_businessPlatform_updateSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_businessPlatform_updateSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_businessPlatform_updateSettings_parser.set_defaults(func=createRequest,operation_name='mutation.businessPlatform.updateSettings')
