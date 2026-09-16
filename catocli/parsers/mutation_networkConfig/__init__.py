
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_networkConfig_parse(mutation_subparsers):
    mutation_networkConfig_parser = mutation_subparsers.add_parser('networkConfig', 
            help='networkConfig() mutation operation', 
            usage=get_help("mutation_networkConfig"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_networkConfig_help(args, configuration=None):
        """Show help when mutation_networkConfig is called without subcommand"""
        print("\ncatocli mutation networkConfig <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  dhcp                           dhcp operation\n  dns                            dns operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation networkConfig <subcommand> -h")
        return None

    mutation_networkConfig_subparsers = mutation_networkConfig_parser.add_subparsers()
    mutation_networkConfig_parser.set_defaults(func=_show_mutation_networkConfig_help)

    mutation_networkConfig_dhcp_parser = mutation_networkConfig_subparsers.add_parser('dhcp', 
            help='dhcp() networkConfig operation', 
            usage=get_help("mutation_networkConfig_dhcp"))

    def _show_mutation_networkConfig_dhcp_help(args, configuration=None):
        """Show help when mutation_networkConfig_dhcp is called without subcommand"""
        print("\ncatocli mutation networkConfig dhcp <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  updateSettings                 updateSettings operation\n  createOption                   createOption operation\n  updateOption                   updateOption operation\n  deleteOption                   deleteOption operation\n  setOption                      setOption operation\n  createRelayGroup               createRelayGroup operation\n  updateRelayGroup               updateRelayGroup operation\n  deleteRelayGroup               deleteRelayGroup operation\n  setRelayGroup                  setRelayGroup operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation networkConfig dhcp <subcommand> -h")
        return None

    mutation_networkConfig_dhcp_subparsers = mutation_networkConfig_dhcp_parser.add_subparsers()
    mutation_networkConfig_dhcp_parser.set_defaults(func=_show_mutation_networkConfig_dhcp_help)

    mutation_networkConfig_dhcp_updateSettings_parser = mutation_networkConfig_dhcp_subparsers.add_parser('updateSettings', 
            help='updateSettings() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_updateSettings"))

    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_updateSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_updateSettings_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.updateSettings')

    mutation_networkConfig_dhcp_createOption_parser = mutation_networkConfig_dhcp_subparsers.add_parser('createOption', 
            help='createOption() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_createOption"))

    mutation_networkConfig_dhcp_createOption_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_createOption_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_createOption_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.createOption')

    mutation_networkConfig_dhcp_updateOption_parser = mutation_networkConfig_dhcp_subparsers.add_parser('updateOption', 
            help='updateOption() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_updateOption"))

    mutation_networkConfig_dhcp_updateOption_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_updateOption_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_updateOption_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.updateOption')

    mutation_networkConfig_dhcp_deleteOption_parser = mutation_networkConfig_dhcp_subparsers.add_parser('deleteOption', 
            help='deleteOption() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_deleteOption"))

    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_deleteOption_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_deleteOption_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.deleteOption')

    mutation_networkConfig_dhcp_setOption_parser = mutation_networkConfig_dhcp_subparsers.add_parser('setOption', 
            help='setOption() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_setOption"))

    mutation_networkConfig_dhcp_setOption_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_setOption_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_setOption_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.setOption')

    mutation_networkConfig_dhcp_createRelayGroup_parser = mutation_networkConfig_dhcp_subparsers.add_parser('createRelayGroup', 
            help='createRelayGroup() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_createRelayGroup"))

    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_createRelayGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_createRelayGroup_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.createRelayGroup')

    mutation_networkConfig_dhcp_updateRelayGroup_parser = mutation_networkConfig_dhcp_subparsers.add_parser('updateRelayGroup', 
            help='updateRelayGroup() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_updateRelayGroup"))

    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_updateRelayGroup_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.updateRelayGroup')

    mutation_networkConfig_dhcp_deleteRelayGroup_parser = mutation_networkConfig_dhcp_subparsers.add_parser('deleteRelayGroup', 
            help='deleteRelayGroup() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_deleteRelayGroup"))

    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_deleteRelayGroup_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.deleteRelayGroup')

    mutation_networkConfig_dhcp_setRelayGroup_parser = mutation_networkConfig_dhcp_subparsers.add_parser('setRelayGroup', 
            help='setRelayGroup() dhcp operation', 
            usage=get_help("mutation_networkConfig_dhcp_setRelayGroup"))

    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dhcp_setRelayGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dhcp_setRelayGroup_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dhcp.setRelayGroup')

    mutation_networkConfig_dns_parser = mutation_networkConfig_subparsers.add_parser('dns', 
            help='dns() networkConfig operation', 
            usage=get_help("mutation_networkConfig_dns"))

    def _show_mutation_networkConfig_dns_help(args, configuration=None):
        """Show help when mutation_networkConfig_dns is called without subcommand"""
        print("\ncatocli mutation networkConfig dns <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  updateSettings                 updateSettings operation\n  updateSiteSettings             updateSiteSettings operation\n  removeSiteSettings             removeSiteSettings operation\n  createForwardingRule           createForwardingRule operation\n  updateForwardingRule           updateForwardingRule operation\n  deleteForwardingRule           deleteForwardingRule operation\n  setForwardingRule              setForwardingRule operation\n  createServerSet                createServerSet operation\n  updateServerSet                updateServerSet operation\n  deleteServerSet                deleteServerSet operation\n  ... and 5 more")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation networkConfig dns <subcommand> -h")
        return None

    mutation_networkConfig_dns_subparsers = mutation_networkConfig_dns_parser.add_subparsers()
    mutation_networkConfig_dns_parser.set_defaults(func=_show_mutation_networkConfig_dns_help)

    mutation_networkConfig_dns_updateSettings_parser = mutation_networkConfig_dns_subparsers.add_parser('updateSettings', 
            help='updateSettings() dns operation', 
            usage=get_help("mutation_networkConfig_dns_updateSettings"))

    mutation_networkConfig_dns_updateSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_updateSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_updateSettings_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.updateSettings')

    mutation_networkConfig_dns_updateSiteSettings_parser = mutation_networkConfig_dns_subparsers.add_parser('updateSiteSettings', 
            help='updateSiteSettings() dns operation', 
            usage=get_help("mutation_networkConfig_dns_updateSiteSettings"))

    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_updateSiteSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_updateSiteSettings_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.updateSiteSettings')

    mutation_networkConfig_dns_removeSiteSettings_parser = mutation_networkConfig_dns_subparsers.add_parser('removeSiteSettings', 
            help='removeSiteSettings() dns operation', 
            usage=get_help("mutation_networkConfig_dns_removeSiteSettings"))

    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_removeSiteSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_removeSiteSettings_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.removeSiteSettings')

    mutation_networkConfig_dns_createForwardingRule_parser = mutation_networkConfig_dns_subparsers.add_parser('createForwardingRule', 
            help='createForwardingRule() dns operation', 
            usage=get_help("mutation_networkConfig_dns_createForwardingRule"))

    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_createForwardingRule_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_createForwardingRule_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.createForwardingRule')

    mutation_networkConfig_dns_updateForwardingRule_parser = mutation_networkConfig_dns_subparsers.add_parser('updateForwardingRule', 
            help='updateForwardingRule() dns operation', 
            usage=get_help("mutation_networkConfig_dns_updateForwardingRule"))

    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_updateForwardingRule_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_updateForwardingRule_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.updateForwardingRule')

    mutation_networkConfig_dns_deleteForwardingRule_parser = mutation_networkConfig_dns_subparsers.add_parser('deleteForwardingRule', 
            help='deleteForwardingRule() dns operation', 
            usage=get_help("mutation_networkConfig_dns_deleteForwardingRule"))

    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_deleteForwardingRule_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_deleteForwardingRule_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.deleteForwardingRule')

    mutation_networkConfig_dns_setForwardingRule_parser = mutation_networkConfig_dns_subparsers.add_parser('setForwardingRule', 
            help='setForwardingRule() dns operation', 
            usage=get_help("mutation_networkConfig_dns_setForwardingRule"))

    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_setForwardingRule_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_setForwardingRule_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.setForwardingRule')

    mutation_networkConfig_dns_createServerSet_parser = mutation_networkConfig_dns_subparsers.add_parser('createServerSet', 
            help='createServerSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_createServerSet"))

    mutation_networkConfig_dns_createServerSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_createServerSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_createServerSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.createServerSet')

    mutation_networkConfig_dns_updateServerSet_parser = mutation_networkConfig_dns_subparsers.add_parser('updateServerSet', 
            help='updateServerSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_updateServerSet"))

    mutation_networkConfig_dns_updateServerSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_updateServerSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_updateServerSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.updateServerSet')

    mutation_networkConfig_dns_deleteServerSet_parser = mutation_networkConfig_dns_subparsers.add_parser('deleteServerSet', 
            help='deleteServerSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_deleteServerSet"))

    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_deleteServerSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_deleteServerSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.deleteServerSet')

    mutation_networkConfig_dns_setServerSet_parser = mutation_networkConfig_dns_subparsers.add_parser('setServerSet', 
            help='setServerSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_setServerSet"))

    mutation_networkConfig_dns_setServerSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_setServerSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_setServerSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.setServerSet')

    mutation_networkConfig_dns_createSuffixSet_parser = mutation_networkConfig_dns_subparsers.add_parser('createSuffixSet', 
            help='createSuffixSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_createSuffixSet"))

    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_createSuffixSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_createSuffixSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.createSuffixSet')

    mutation_networkConfig_dns_updateSuffixSet_parser = mutation_networkConfig_dns_subparsers.add_parser('updateSuffixSet', 
            help='updateSuffixSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_updateSuffixSet"))

    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_updateSuffixSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_updateSuffixSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.updateSuffixSet')

    mutation_networkConfig_dns_deleteSuffixSet_parser = mutation_networkConfig_dns_subparsers.add_parser('deleteSuffixSet', 
            help='deleteSuffixSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_deleteSuffixSet"))

    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_deleteSuffixSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_deleteSuffixSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.deleteSuffixSet')

    mutation_networkConfig_dns_setSuffixSet_parser = mutation_networkConfig_dns_subparsers.add_parser('setSuffixSet', 
            help='setSuffixSet() dns operation', 
            usage=get_help("mutation_networkConfig_dns_setSuffixSet"))

    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_networkConfig_dns_setSuffixSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_dns_setSuffixSet_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig.dns.setSuffixSet')
