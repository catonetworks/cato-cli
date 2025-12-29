
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_accountManagement_parse(mutation_subparsers):
    mutation_accountManagement_parser = mutation_subparsers.add_parser('accountManagement', 
            help='accountManagement() mutation operation', 
            usage=get_help("mutation_accountManagement"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_accountManagement_help(args, configuration=None):
        """Show help when mutation_accountManagement is called without subcommand"""
        print("\ncatocli mutation accountManagement <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  addAccount                     addAccount operation\n  updateAccount                  updateAccount operation\n  removeAccount                  removeAccount operation\n  disableAccount                 disableAccount operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation accountManagement <subcommand> -h")
        return None

    mutation_accountManagement_subparsers = mutation_accountManagement_parser.add_subparsers()
    mutation_accountManagement_parser.set_defaults(func=_show_mutation_accountManagement_help)

    mutation_accountManagement_addAccount_parser = mutation_accountManagement_subparsers.add_parser('addAccount', 
            help='addAccount() accountManagement operation', 
            usage=get_help("mutation_accountManagement_addAccount"))

    mutation_accountManagement_addAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_accountManagement_addAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_accountManagement_addAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_accountManagement_addAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_accountManagement_addAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_accountManagement_addAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_accountManagement_addAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_accountManagement_addAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_accountManagement_addAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_accountManagement_addAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_accountManagement_addAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_accountManagement_addAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_accountManagement_addAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_accountManagement_addAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_accountManagement_addAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.addAccount')

    mutation_accountManagement_updateAccount_parser = mutation_accountManagement_subparsers.add_parser('updateAccount', 
            help='updateAccount() accountManagement operation', 
            usage=get_help("mutation_accountManagement_updateAccount"))

    mutation_accountManagement_updateAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_accountManagement_updateAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_accountManagement_updateAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_accountManagement_updateAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_accountManagement_updateAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_accountManagement_updateAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_accountManagement_updateAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_accountManagement_updateAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_accountManagement_updateAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_accountManagement_updateAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_accountManagement_updateAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_accountManagement_updateAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_accountManagement_updateAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_accountManagement_updateAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_accountManagement_updateAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.updateAccount')

    mutation_accountManagement_removeAccount_parser = mutation_accountManagement_subparsers.add_parser('removeAccount', 
            help='removeAccount() accountManagement operation', 
            usage=get_help("mutation_accountManagement_removeAccount"))

    mutation_accountManagement_removeAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_accountManagement_removeAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_accountManagement_removeAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_accountManagement_removeAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_accountManagement_removeAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_accountManagement_removeAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_accountManagement_removeAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_accountManagement_removeAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_accountManagement_removeAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_accountManagement_removeAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_accountManagement_removeAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_accountManagement_removeAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_accountManagement_removeAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_accountManagement_removeAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_accountManagement_removeAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.removeAccount')

    mutation_accountManagement_disableAccount_parser = mutation_accountManagement_subparsers.add_parser('disableAccount', 
            help='disableAccount() accountManagement operation', 
            usage=get_help("mutation_accountManagement_disableAccount"))

    mutation_accountManagement_disableAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_accountManagement_disableAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_accountManagement_disableAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_accountManagement_disableAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_accountManagement_disableAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_accountManagement_disableAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_accountManagement_disableAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_accountManagement_disableAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_accountManagement_disableAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_accountManagement_disableAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_accountManagement_disableAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_accountManagement_disableAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_accountManagement_disableAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_accountManagement_disableAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_accountManagement_disableAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.disableAccount')
