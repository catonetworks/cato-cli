
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_ztnaAppConnector_parse(mutation_subparsers):
    mutation_ztnaAppConnector_parser = mutation_subparsers.add_parser('ztnaAppConnector', 
            help='ztnaAppConnector() mutation operation', 
            usage=get_help("mutation_ztnaAppConnector"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_ztnaAppConnector_help(args, configuration=None):
        """Show help when mutation_ztnaAppConnector is called without subcommand"""
        print("\ncatocli mutation ztnaAppConnector <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  addZtnaAppConnector            addZtnaAppConnector operation\n  updateZtnaAppConnector         updateZtnaAppConnector operation\n  removeZtnaAppConnector         removeZtnaAppConnector operation\n  unassignSocketFromZtnaAppConnector unassignSocketFromZtnaAppConnector operation\n  upgradeZtnaAppConnector        upgradeZtnaAppConnector operation\n  addZtnaAppConnectorsConfiguration addZtnaAppConnectorsConfiguration operation\n  updateZtnaAppConnectorsConfiguration updateZtnaAppConnectorsConfiguration operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation ztnaAppConnector <subcommand> -h")
        return None

    mutation_ztnaAppConnector_subparsers = mutation_ztnaAppConnector_parser.add_subparsers()
    mutation_ztnaAppConnector_parser.set_defaults(func=_show_mutation_ztnaAppConnector_help)

    mutation_ztnaAppConnector_addZtnaAppConnector_parser = mutation_ztnaAppConnector_subparsers.add_parser('addZtnaAppConnector', 
            help='addZtnaAppConnector() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_addZtnaAppConnector"))

    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_addZtnaAppConnector_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.addZtnaAppConnector')

    mutation_ztnaAppConnector_updateZtnaAppConnector_parser = mutation_ztnaAppConnector_subparsers.add_parser('updateZtnaAppConnector', 
            help='updateZtnaAppConnector() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_updateZtnaAppConnector"))

    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_updateZtnaAppConnector_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.updateZtnaAppConnector')

    mutation_ztnaAppConnector_removeZtnaAppConnector_parser = mutation_ztnaAppConnector_subparsers.add_parser('removeZtnaAppConnector', 
            help='removeZtnaAppConnector() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_removeZtnaAppConnector"))

    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_removeZtnaAppConnector_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.removeZtnaAppConnector')

    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser = mutation_ztnaAppConnector_subparsers.add_parser('unassignSocketFromZtnaAppConnector', 
            help='unassignSocketFromZtnaAppConnector() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector"))

    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_unassignSocketFromZtnaAppConnector_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.unassignSocketFromZtnaAppConnector')

    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser = mutation_ztnaAppConnector_subparsers.add_parser('upgradeZtnaAppConnector', 
            help='upgradeZtnaAppConnector() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_upgradeZtnaAppConnector"))

    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_upgradeZtnaAppConnector_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.upgradeZtnaAppConnector')

    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser = mutation_ztnaAppConnector_subparsers.add_parser('addZtnaAppConnectorsConfiguration', 
            help='addZtnaAppConnectorsConfiguration() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration"))

    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_addZtnaAppConnectorsConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.addZtnaAppConnectorsConfiguration')

    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser = mutation_ztnaAppConnector_subparsers.add_parser('updateZtnaAppConnectorsConfiguration', 
            help='updateZtnaAppConnectorsConfiguration() ztnaAppConnector operation', 
            usage=get_help("mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration"))

    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_ztnaAppConnector_updateZtnaAppConnectorsConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.ztnaAppConnector.updateZtnaAppConnectorsConfiguration')
