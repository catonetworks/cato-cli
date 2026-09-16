
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_networkConfig_parse(query_subparsers):
    query_networkConfig_parser = query_subparsers.add_parser('networkConfig', 
            help='networkConfig() query operation', 
            usage=get_help("query_networkConfig"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_networkConfig_help(args, configuration=None):
        """Show help when query_networkConfig is called without subcommand"""
        print("\ncatocli query networkConfig <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  dhcp                           dhcp operation\n  dns                            dns operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query networkConfig <subcommand> -h")
        return None

    query_networkConfig_subparsers = query_networkConfig_parser.add_subparsers()
    query_networkConfig_parser.set_defaults(func=_show_query_networkConfig_help)

    query_networkConfig_dhcp_parser = query_networkConfig_subparsers.add_parser('dhcp', 
            help='dhcp() networkConfig operation', 
            usage=get_help("query_networkConfig_dhcp"))

    def _show_query_networkConfig_dhcp_help(args, configuration=None):
        """Show help when query_networkConfig_dhcp is called without subcommand"""
        print("\ncatocli query networkConfig dhcp <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  settings                       settings operation\n  option                         option operation\n  optionList                     optionList operation\n  relayGroup                     relayGroup operation\n  relayGroupList                 relayGroupList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query networkConfig dhcp <subcommand> -h")
        return None

    query_networkConfig_dhcp_subparsers = query_networkConfig_dhcp_parser.add_subparsers()
    query_networkConfig_dhcp_parser.set_defaults(func=_show_query_networkConfig_dhcp_help)

    query_networkConfig_dhcp_settings_parser = query_networkConfig_dhcp_subparsers.add_parser('settings', 
            help='settings() dhcp operation', 
            usage=get_help("query_networkConfig_dhcp_settings"))

    query_networkConfig_dhcp_settings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dhcp_settings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dhcp_settings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dhcp_settings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dhcp_settings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dhcp_settings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dhcp_settings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dhcp_settings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dhcp_settings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dhcp_settings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dhcp_settings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dhcp_settings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dhcp_settings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dhcp_settings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dhcp_settings_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dhcp.settings')

    query_networkConfig_dhcp_option_parser = query_networkConfig_dhcp_subparsers.add_parser('option', 
            help='option() dhcp operation', 
            usage=get_help("query_networkConfig_dhcp_option"))

    query_networkConfig_dhcp_option_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dhcp_option_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dhcp_option_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dhcp_option_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dhcp_option_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dhcp_option_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dhcp_option_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dhcp_option_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dhcp_option_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dhcp_option_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dhcp_option_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dhcp_option_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dhcp_option_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dhcp_option_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dhcp_option_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dhcp.option')

    query_networkConfig_dhcp_optionList_parser = query_networkConfig_dhcp_subparsers.add_parser('optionList', 
            help='optionList() dhcp operation', 
            usage=get_help("query_networkConfig_dhcp_optionList"))

    query_networkConfig_dhcp_optionList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dhcp_optionList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dhcp_optionList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dhcp_optionList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dhcp_optionList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dhcp_optionList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dhcp_optionList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dhcp_optionList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dhcp_optionList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dhcp_optionList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dhcp_optionList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dhcp_optionList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dhcp_optionList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dhcp_optionList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dhcp_optionList_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dhcp.optionList')

    query_networkConfig_dhcp_relayGroup_parser = query_networkConfig_dhcp_subparsers.add_parser('relayGroup', 
            help='relayGroup() dhcp operation', 
            usage=get_help("query_networkConfig_dhcp_relayGroup"))

    query_networkConfig_dhcp_relayGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dhcp_relayGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dhcp_relayGroup_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dhcp.relayGroup')

    query_networkConfig_dhcp_relayGroupList_parser = query_networkConfig_dhcp_subparsers.add_parser('relayGroupList', 
            help='relayGroupList() dhcp operation', 
            usage=get_help("query_networkConfig_dhcp_relayGroupList"))

    query_networkConfig_dhcp_relayGroupList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dhcp_relayGroupList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dhcp_relayGroupList_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dhcp.relayGroupList')

    query_networkConfig_dns_parser = query_networkConfig_subparsers.add_parser('dns', 
            help='dns() networkConfig operation', 
            usage=get_help("query_networkConfig_dns"))

    def _show_query_networkConfig_dns_help(args, configuration=None):
        """Show help when query_networkConfig_dns is called without subcommand"""
        print("\ncatocli query networkConfig dns <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  settings                       settings operation\n  siteSettings                   siteSettings operation\n  forwardingRule                 forwardingRule operation\n  forwardingRuleList             forwardingRuleList operation\n  serverSet                      serverSet operation\n  serverSetList                  serverSetList operation\n  suffixSet                      suffixSet operation\n  suffixSetList                  suffixSetList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query networkConfig dns <subcommand> -h")
        return None

    query_networkConfig_dns_subparsers = query_networkConfig_dns_parser.add_subparsers()
    query_networkConfig_dns_parser.set_defaults(func=_show_query_networkConfig_dns_help)

    query_networkConfig_dns_settings_parser = query_networkConfig_dns_subparsers.add_parser('settings', 
            help='settings() dns operation', 
            usage=get_help("query_networkConfig_dns_settings"))

    query_networkConfig_dns_settings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_settings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_settings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_settings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_settings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_settings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_settings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_settings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_settings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_settings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_settings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_settings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_settings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_settings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_settings_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.settings')

    query_networkConfig_dns_siteSettings_parser = query_networkConfig_dns_subparsers.add_parser('siteSettings', 
            help='siteSettings() dns operation', 
            usage=get_help("query_networkConfig_dns_siteSettings"))

    query_networkConfig_dns_siteSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_siteSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_siteSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_siteSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_siteSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_siteSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_siteSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_siteSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_siteSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_siteSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_siteSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_siteSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_siteSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_siteSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_siteSettings_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.siteSettings')

    query_networkConfig_dns_forwardingRule_parser = query_networkConfig_dns_subparsers.add_parser('forwardingRule', 
            help='forwardingRule() dns operation', 
            usage=get_help("query_networkConfig_dns_forwardingRule"))

    query_networkConfig_dns_forwardingRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_forwardingRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_forwardingRule_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_forwardingRule_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.forwardingRule')

    query_networkConfig_dns_forwardingRuleList_parser = query_networkConfig_dns_subparsers.add_parser('forwardingRuleList', 
            help='forwardingRuleList() dns operation', 
            usage=get_help("query_networkConfig_dns_forwardingRuleList"))

    query_networkConfig_dns_forwardingRuleList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_forwardingRuleList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_forwardingRuleList_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.forwardingRuleList')

    query_networkConfig_dns_serverSet_parser = query_networkConfig_dns_subparsers.add_parser('serverSet', 
            help='serverSet() dns operation', 
            usage=get_help("query_networkConfig_dns_serverSet"))

    query_networkConfig_dns_serverSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_serverSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_serverSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_serverSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_serverSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_serverSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_serverSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_serverSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_serverSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_serverSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_serverSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_serverSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_serverSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_serverSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_serverSet_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.serverSet')

    query_networkConfig_dns_serverSetList_parser = query_networkConfig_dns_subparsers.add_parser('serverSetList', 
            help='serverSetList() dns operation', 
            usage=get_help("query_networkConfig_dns_serverSetList"))

    query_networkConfig_dns_serverSetList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_serverSetList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_serverSetList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_serverSetList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_serverSetList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_serverSetList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_serverSetList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_serverSetList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_serverSetList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_serverSetList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_serverSetList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_serverSetList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_serverSetList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_serverSetList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_serverSetList_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.serverSetList')

    query_networkConfig_dns_suffixSet_parser = query_networkConfig_dns_subparsers.add_parser('suffixSet', 
            help='suffixSet() dns operation', 
            usage=get_help("query_networkConfig_dns_suffixSet"))

    query_networkConfig_dns_suffixSet_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_suffixSet_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_suffixSet_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_suffixSet_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_suffixSet_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_suffixSet_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_suffixSet_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_suffixSet_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_suffixSet_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_suffixSet_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_suffixSet_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_suffixSet_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_suffixSet_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_suffixSet_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_suffixSet_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.suffixSet')

    query_networkConfig_dns_suffixSetList_parser = query_networkConfig_dns_subparsers.add_parser('suffixSetList', 
            help='suffixSetList() dns operation', 
            usage=get_help("query_networkConfig_dns_suffixSetList"))

    query_networkConfig_dns_suffixSetList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_networkConfig_dns_suffixSetList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_networkConfig_dns_suffixSetList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_networkConfig_dns_suffixSetList_parser.set_defaults(func=createRequest,operation_name='query.networkConfig.dns.suffixSetList')
