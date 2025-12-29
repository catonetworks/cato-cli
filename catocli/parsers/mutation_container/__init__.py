
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_container_parse(mutation_subparsers):
    mutation_container_parser = mutation_subparsers.add_parser('container', 
            help='container() mutation operation', 
            usage=get_help("mutation_container"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_container_help(args, configuration=None):
        """Show help when mutation_container is called without subcommand"""
        print("\ncatocli mutation container <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  ipAddressRange                 ipAddressRange operation\n  fqdn                           fqdn operation\n  delete                         delete operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation container <subcommand> -h")
        return None

    mutation_container_subparsers = mutation_container_parser.add_subparsers()
    mutation_container_parser.set_defaults(func=_show_mutation_container_help)

    mutation_container_ipAddressRange_parser = mutation_container_subparsers.add_parser('ipAddressRange', 
            help='ipAddressRange() container operation', 
            usage=get_help("mutation_container_ipAddressRange"))

    def _show_mutation_container_ipAddressRange_help(args, configuration=None):
        """Show help when mutation_container_ipAddressRange is called without subcommand"""
        print("\ncatocli mutation container ipAddressRange <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createFromFile                 createFromFile operation\n  updateFromFile                 updateFromFile operation\n  addValues                      addValues operation\n  removeValues                   removeValues operation\n  createFromList                 createFromList operation\n  updateFromList                 updateFromList operation\n  createFromURL                  createFromURL operation\n  updateFromURL                  updateFromURL operation\n  syncFromURL                    syncFromURL operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation container ipAddressRange <subcommand> -h")
        return None

    mutation_container_ipAddressRange_subparsers = mutation_container_ipAddressRange_parser.add_subparsers()
    mutation_container_ipAddressRange_parser.set_defaults(func=_show_mutation_container_ipAddressRange_help)

    mutation_container_ipAddressRange_createFromFile_parser = mutation_container_ipAddressRange_subparsers.add_parser('createFromFile', 
            help='createFromFile() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_createFromFile"))

    mutation_container_ipAddressRange_createFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_createFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.createFromFile')

    mutation_container_ipAddressRange_updateFromFile_parser = mutation_container_ipAddressRange_subparsers.add_parser('updateFromFile', 
            help='updateFromFile() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_updateFromFile"))

    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_updateFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.updateFromFile')

    mutation_container_ipAddressRange_addValues_parser = mutation_container_ipAddressRange_subparsers.add_parser('addValues', 
            help='addValues() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_addValues"))

    mutation_container_ipAddressRange_addValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_addValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.addValues')

    mutation_container_ipAddressRange_removeValues_parser = mutation_container_ipAddressRange_subparsers.add_parser('removeValues', 
            help='removeValues() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_removeValues"))

    mutation_container_ipAddressRange_removeValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_removeValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.removeValues')

    mutation_container_ipAddressRange_createFromList_parser = mutation_container_ipAddressRange_subparsers.add_parser('createFromList', 
            help='createFromList() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_createFromList"))

    mutation_container_ipAddressRange_createFromList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_createFromList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_createFromList_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.createFromList')

    mutation_container_ipAddressRange_updateFromList_parser = mutation_container_ipAddressRange_subparsers.add_parser('updateFromList', 
            help='updateFromList() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_updateFromList"))

    mutation_container_ipAddressRange_updateFromList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_updateFromList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_updateFromList_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.updateFromList')

    mutation_container_ipAddressRange_createFromURL_parser = mutation_container_ipAddressRange_subparsers.add_parser('createFromURL', 
            help='createFromURL() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_createFromURL"))

    mutation_container_ipAddressRange_createFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_createFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_createFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.createFromURL')

    mutation_container_ipAddressRange_updateFromURL_parser = mutation_container_ipAddressRange_subparsers.add_parser('updateFromURL', 
            help='updateFromURL() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_updateFromURL"))

    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_updateFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_updateFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.updateFromURL')

    mutation_container_ipAddressRange_syncFromURL_parser = mutation_container_ipAddressRange_subparsers.add_parser('syncFromURL', 
            help='syncFromURL() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_syncFromURL"))

    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_ipAddressRange_syncFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_ipAddressRange_syncFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.syncFromURL')

    mutation_container_fqdn_parser = mutation_container_subparsers.add_parser('fqdn', 
            help='fqdn() container operation', 
            usage=get_help("mutation_container_fqdn"))

    def _show_mutation_container_fqdn_help(args, configuration=None):
        """Show help when mutation_container_fqdn is called without subcommand"""
        print("\ncatocli mutation container fqdn <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createFromFile                 createFromFile operation\n  updateFromFile                 updateFromFile operation\n  addValues                      addValues operation\n  removeValues                   removeValues operation\n  createFromList                 createFromList operation\n  updateFromList                 updateFromList operation\n  createFromURL                  createFromURL operation\n  updateFromURL                  updateFromURL operation\n  syncFromURL                    syncFromURL operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation container fqdn <subcommand> -h")
        return None

    mutation_container_fqdn_subparsers = mutation_container_fqdn_parser.add_subparsers()
    mutation_container_fqdn_parser.set_defaults(func=_show_mutation_container_fqdn_help)

    mutation_container_fqdn_createFromFile_parser = mutation_container_fqdn_subparsers.add_parser('createFromFile', 
            help='createFromFile() fqdn operation', 
            usage=get_help("mutation_container_fqdn_createFromFile"))

    mutation_container_fqdn_createFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_createFromFile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_createFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_createFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_createFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_createFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_createFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_createFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_createFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_createFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.createFromFile')

    mutation_container_fqdn_updateFromFile_parser = mutation_container_fqdn_subparsers.add_parser('updateFromFile', 
            help='updateFromFile() fqdn operation', 
            usage=get_help("mutation_container_fqdn_updateFromFile"))

    mutation_container_fqdn_updateFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_updateFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.updateFromFile')

    mutation_container_fqdn_addValues_parser = mutation_container_fqdn_subparsers.add_parser('addValues', 
            help='addValues() fqdn operation', 
            usage=get_help("mutation_container_fqdn_addValues"))

    mutation_container_fqdn_addValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_addValues_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_addValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_addValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_addValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_addValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_addValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_addValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_addValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_addValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_addValues_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_addValues_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_addValues_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_addValues_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_addValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.addValues')

    mutation_container_fqdn_removeValues_parser = mutation_container_fqdn_subparsers.add_parser('removeValues', 
            help='removeValues() fqdn operation', 
            usage=get_help("mutation_container_fqdn_removeValues"))

    mutation_container_fqdn_removeValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_removeValues_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_removeValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_removeValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_removeValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_removeValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_removeValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_removeValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_removeValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_removeValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_removeValues_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_removeValues_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_removeValues_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_removeValues_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_removeValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.removeValues')

    mutation_container_fqdn_createFromList_parser = mutation_container_fqdn_subparsers.add_parser('createFromList', 
            help='createFromList() fqdn operation', 
            usage=get_help("mutation_container_fqdn_createFromList"))

    mutation_container_fqdn_createFromList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_createFromList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_createFromList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_createFromList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_createFromList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_createFromList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_createFromList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_createFromList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_createFromList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_createFromList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_createFromList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_createFromList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_createFromList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_createFromList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_createFromList_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.createFromList')

    mutation_container_fqdn_updateFromList_parser = mutation_container_fqdn_subparsers.add_parser('updateFromList', 
            help='updateFromList() fqdn operation', 
            usage=get_help("mutation_container_fqdn_updateFromList"))

    mutation_container_fqdn_updateFromList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_updateFromList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_updateFromList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_updateFromList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_updateFromList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_updateFromList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_updateFromList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_updateFromList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_updateFromList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_updateFromList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_updateFromList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_updateFromList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_updateFromList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_updateFromList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_updateFromList_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.updateFromList')

    mutation_container_fqdn_createFromURL_parser = mutation_container_fqdn_subparsers.add_parser('createFromURL', 
            help='createFromURL() fqdn operation', 
            usage=get_help("mutation_container_fqdn_createFromURL"))

    mutation_container_fqdn_createFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_createFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_createFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_createFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_createFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_createFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_createFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_createFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_createFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_createFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_createFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_createFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_createFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_createFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_createFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.createFromURL')

    mutation_container_fqdn_updateFromURL_parser = mutation_container_fqdn_subparsers.add_parser('updateFromURL', 
            help='updateFromURL() fqdn operation', 
            usage=get_help("mutation_container_fqdn_updateFromURL"))

    mutation_container_fqdn_updateFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_updateFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_updateFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_updateFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.updateFromURL')

    mutation_container_fqdn_syncFromURL_parser = mutation_container_fqdn_subparsers.add_parser('syncFromURL', 
            help='syncFromURL() fqdn operation', 
            usage=get_help("mutation_container_fqdn_syncFromURL"))

    mutation_container_fqdn_syncFromURL_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_syncFromURL_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_fqdn_syncFromURL_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_fqdn_syncFromURL_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.syncFromURL')

    mutation_container_delete_parser = mutation_container_subparsers.add_parser('delete', 
            help='delete() container operation', 
            usage=get_help("mutation_container_delete"))

    mutation_container_delete_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_delete_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_container_delete_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_delete_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_delete_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_delete_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_delete_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_delete_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_delete_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_delete_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_delete_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_container_delete_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_container_delete_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_container_delete_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_container_delete_parser.set_defaults(func=createRequest,operation_name='mutation.container.delete')
