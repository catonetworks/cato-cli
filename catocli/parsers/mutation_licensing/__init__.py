
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_licensing_parse(mutation_subparsers):
    mutation_licensing_parser = mutation_subparsers.add_parser('licensing', 
            help='licensing() mutation operation', 
            usage=get_help("mutation_licensing"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_licensing_help(args, configuration=None):
        """Show help when mutation_licensing is called without subcommand"""
        print("\ncatocli mutation licensing <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  addLicenseToManagedAccount     addLicenseToManagedAccount operation\n  updateLicenseForManagedAccount updateLicenseForManagedAccount operation\n  removeLicenseFromManagedAccount removeLicenseFromManagedAccount operation\n  updateCommercialLicense        updateCommercialLicense operation\n  enableServiceForManagedAccount enableServiceForManagedAccount operation\n  disableServiceForManagedAccount disableServiceForManagedAccount operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation licensing <subcommand> -h")
        return None

    mutation_licensing_subparsers = mutation_licensing_parser.add_subparsers()
    mutation_licensing_parser.set_defaults(func=_show_mutation_licensing_help)

    mutation_licensing_addLicenseToManagedAccount_parser = mutation_licensing_subparsers.add_parser('addLicenseToManagedAccount', 
            help='addLicenseToManagedAccount() licensing operation', 
            usage=get_help("mutation_licensing_addLicenseToManagedAccount"))

    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_addLicenseToManagedAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_addLicenseToManagedAccount_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.addLicenseToManagedAccount')

    mutation_licensing_updateLicenseForManagedAccount_parser = mutation_licensing_subparsers.add_parser('updateLicenseForManagedAccount', 
            help='updateLicenseForManagedAccount() licensing operation', 
            usage=get_help("mutation_licensing_updateLicenseForManagedAccount"))

    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_updateLicenseForManagedAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_updateLicenseForManagedAccount_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.updateLicenseForManagedAccount')

    mutation_licensing_removeLicenseFromManagedAccount_parser = mutation_licensing_subparsers.add_parser('removeLicenseFromManagedAccount', 
            help='removeLicenseFromManagedAccount() licensing operation', 
            usage=get_help("mutation_licensing_removeLicenseFromManagedAccount"))

    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_removeLicenseFromManagedAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_removeLicenseFromManagedAccount_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.removeLicenseFromManagedAccount')

    mutation_licensing_updateCommercialLicense_parser = mutation_licensing_subparsers.add_parser('updateCommercialLicense', 
            help='updateCommercialLicense() licensing operation', 
            usage=get_help("mutation_licensing_updateCommercialLicense"))

    mutation_licensing_updateCommercialLicense_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_updateCommercialLicense_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_updateCommercialLicense_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_updateCommercialLicense_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.updateCommercialLicense')

    mutation_licensing_enableServiceForManagedAccount_parser = mutation_licensing_subparsers.add_parser('enableServiceForManagedAccount', 
            help='enableServiceForManagedAccount() licensing operation', 
            usage=get_help("mutation_licensing_enableServiceForManagedAccount"))

    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_enableServiceForManagedAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_enableServiceForManagedAccount_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.enableServiceForManagedAccount')

    mutation_licensing_disableServiceForManagedAccount_parser = mutation_licensing_subparsers.add_parser('disableServiceForManagedAccount', 
            help='disableServiceForManagedAccount() licensing operation', 
            usage=get_help("mutation_licensing_disableServiceForManagedAccount"))

    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_licensing_disableServiceForManagedAccount_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_licensing_disableServiceForManagedAccount_parser.set_defaults(func=createRequest,operation_name='mutation.licensing.disableServiceForManagedAccount')
