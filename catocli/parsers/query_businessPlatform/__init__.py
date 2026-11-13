
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_businessPlatform_parse(query_subparsers):
    query_businessPlatform_parser = query_subparsers.add_parser('businessPlatform', 
            help='businessPlatform() query operation', 
            usage=get_help("query_businessPlatform"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_businessPlatform_help(args, configuration=None):
        """Show help when query_businessPlatform is called without subcommand"""
        print("\ncatocli query businessPlatform <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  accountList                    accountList operation\n  countAccountByPlan             countAccountByPlan operation\n  settings                       settings operation\n  accountOverview                accountOverview operation\n  partnerList                    partnerList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query businessPlatform <subcommand> -h")
        return None

    query_businessPlatform_subparsers = query_businessPlatform_parser.add_subparsers()
    query_businessPlatform_parser.set_defaults(func=_show_query_businessPlatform_help)

    query_businessPlatform_accountList_parser = query_businessPlatform_subparsers.add_parser('accountList', 
            help='accountList() businessPlatform operation', 
            usage=get_help("query_businessPlatform_accountList"))

    query_businessPlatform_accountList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_businessPlatform_accountList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_businessPlatform_accountList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_businessPlatform_accountList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_businessPlatform_accountList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_businessPlatform_accountList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_businessPlatform_accountList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_businessPlatform_accountList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_businessPlatform_accountList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_businessPlatform_accountList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_businessPlatform_accountList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_businessPlatform_accountList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_businessPlatform_accountList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_businessPlatform_accountList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_businessPlatform_accountList_parser.set_defaults(func=createRequest,operation_name='query.businessPlatform.accountList')

    query_businessPlatform_countAccountByPlan_parser = query_businessPlatform_subparsers.add_parser('countAccountByPlan', 
            help='countAccountByPlan() businessPlatform operation', 
            usage=get_help("query_businessPlatform_countAccountByPlan"))

    query_businessPlatform_countAccountByPlan_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_businessPlatform_countAccountByPlan_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_businessPlatform_countAccountByPlan_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_businessPlatform_countAccountByPlan_parser.set_defaults(func=createRequest,operation_name='query.businessPlatform.countAccountByPlan')

    query_businessPlatform_settings_parser = query_businessPlatform_subparsers.add_parser('settings', 
            help='settings() businessPlatform operation', 
            usage=get_help("query_businessPlatform_settings"))

    query_businessPlatform_settings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_businessPlatform_settings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_businessPlatform_settings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_businessPlatform_settings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_businessPlatform_settings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_businessPlatform_settings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_businessPlatform_settings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_businessPlatform_settings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_businessPlatform_settings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_businessPlatform_settings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_businessPlatform_settings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_businessPlatform_settings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_businessPlatform_settings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_businessPlatform_settings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_businessPlatform_settings_parser.set_defaults(func=createRequest,operation_name='query.businessPlatform.settings')

    query_businessPlatform_accountOverview_parser = query_businessPlatform_subparsers.add_parser('accountOverview', 
            help='accountOverview() businessPlatform operation', 
            usage=get_help("query_businessPlatform_accountOverview"))

    query_businessPlatform_accountOverview_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_businessPlatform_accountOverview_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_businessPlatform_accountOverview_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_businessPlatform_accountOverview_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_businessPlatform_accountOverview_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_businessPlatform_accountOverview_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_businessPlatform_accountOverview_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_businessPlatform_accountOverview_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_businessPlatform_accountOverview_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_businessPlatform_accountOverview_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_businessPlatform_accountOverview_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_businessPlatform_accountOverview_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_businessPlatform_accountOverview_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_businessPlatform_accountOverview_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_businessPlatform_accountOverview_parser.set_defaults(func=createRequest,operation_name='query.businessPlatform.accountOverview')

    query_businessPlatform_partnerList_parser = query_businessPlatform_subparsers.add_parser('partnerList', 
            help='partnerList() businessPlatform operation', 
            usage=get_help("query_businessPlatform_partnerList"))

    query_businessPlatform_partnerList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_businessPlatform_partnerList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_businessPlatform_partnerList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_businessPlatform_partnerList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_businessPlatform_partnerList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_businessPlatform_partnerList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_businessPlatform_partnerList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_businessPlatform_partnerList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_businessPlatform_partnerList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_businessPlatform_partnerList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_businessPlatform_partnerList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_businessPlatform_partnerList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_businessPlatform_partnerList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_businessPlatform_partnerList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_businessPlatform_partnerList_parser.set_defaults(func=createRequest,operation_name='query.businessPlatform.partnerList')
