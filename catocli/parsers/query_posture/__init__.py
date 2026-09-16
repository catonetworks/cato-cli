
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_posture_parse(query_subparsers):
    query_posture_parser = query_subparsers.add_parser('posture', 
            help='posture() query operation', 
            usage=get_help("query_posture"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_posture_help(args, configuration=None):
        """Show help when query_posture is called without subcommand"""
        print("\ncatocli query posture <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  dailySummaryList               dailySummaryList operation\n  accountSummaryList             accountSummaryList operation\n  checkSummary                   checkSummary operation\n  checkResultList                checkResultList operation\n  findingList                    findingList operation\n  findingSummary                 findingSummary operation\n  definitionList                 definitionList operation\n  complianceFrameworkList        complianceFrameworkList operation\n  categoryList                   categoryList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query posture <subcommand> -h")
        return None

    query_posture_subparsers = query_posture_parser.add_subparsers()
    query_posture_parser.set_defaults(func=_show_query_posture_help)

    query_posture_dailySummaryList_parser = query_posture_subparsers.add_parser('dailySummaryList', 
            help='dailySummaryList() posture operation', 
            usage=get_help("query_posture_dailySummaryList"))

    query_posture_dailySummaryList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_dailySummaryList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_dailySummaryList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_dailySummaryList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_dailySummaryList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_dailySummaryList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_dailySummaryList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_dailySummaryList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_dailySummaryList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_dailySummaryList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_dailySummaryList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_dailySummaryList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_dailySummaryList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_dailySummaryList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_dailySummaryList_parser.set_defaults(func=createRequest,operation_name='query.posture.dailySummaryList')

    query_posture_accountSummaryList_parser = query_posture_subparsers.add_parser('accountSummaryList', 
            help='accountSummaryList() posture operation', 
            usage=get_help("query_posture_accountSummaryList"))

    query_posture_accountSummaryList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_accountSummaryList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_accountSummaryList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_accountSummaryList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_accountSummaryList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_accountSummaryList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_accountSummaryList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_accountSummaryList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_accountSummaryList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_accountSummaryList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_accountSummaryList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_accountSummaryList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_accountSummaryList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_accountSummaryList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_accountSummaryList_parser.set_defaults(func=createRequest,operation_name='query.posture.accountSummaryList')

    query_posture_checkSummary_parser = query_posture_subparsers.add_parser('checkSummary', 
            help='checkSummary() posture operation', 
            usage=get_help("query_posture_checkSummary"))

    query_posture_checkSummary_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_checkSummary_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_checkSummary_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_checkSummary_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_checkSummary_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_checkSummary_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_checkSummary_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_checkSummary_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_checkSummary_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_checkSummary_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_checkSummary_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_checkSummary_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_checkSummary_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_checkSummary_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_checkSummary_parser.set_defaults(func=createRequest,operation_name='query.posture.checkSummary')

    query_posture_checkResultList_parser = query_posture_subparsers.add_parser('checkResultList', 
            help='checkResultList() posture operation', 
            usage=get_help("query_posture_checkResultList"))

    query_posture_checkResultList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_checkResultList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_checkResultList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_checkResultList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_checkResultList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_checkResultList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_checkResultList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_checkResultList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_checkResultList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_checkResultList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_checkResultList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_checkResultList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_checkResultList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_checkResultList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_checkResultList_parser.set_defaults(func=createRequest,operation_name='query.posture.checkResultList')

    query_posture_findingList_parser = query_posture_subparsers.add_parser('findingList', 
            help='findingList() posture operation', 
            usage=get_help("query_posture_findingList"))

    query_posture_findingList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_findingList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_findingList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_findingList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_findingList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_findingList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_findingList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_findingList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_findingList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_findingList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_findingList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_findingList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_findingList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_findingList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_findingList_parser.set_defaults(func=createRequest,operation_name='query.posture.findingList')

    query_posture_findingSummary_parser = query_posture_subparsers.add_parser('findingSummary', 
            help='findingSummary() posture operation', 
            usage=get_help("query_posture_findingSummary"))

    query_posture_findingSummary_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_findingSummary_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_findingSummary_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_findingSummary_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_findingSummary_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_findingSummary_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_findingSummary_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_findingSummary_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_findingSummary_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_findingSummary_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_findingSummary_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_findingSummary_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_findingSummary_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_findingSummary_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_findingSummary_parser.set_defaults(func=createRequest,operation_name='query.posture.findingSummary')

    query_posture_definitionList_parser = query_posture_subparsers.add_parser('definitionList', 
            help='definitionList() posture operation', 
            usage=get_help("query_posture_definitionList"))

    query_posture_definitionList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_definitionList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_definitionList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_definitionList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_definitionList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_definitionList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_definitionList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_definitionList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_definitionList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_definitionList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_definitionList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_definitionList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_definitionList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_definitionList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_definitionList_parser.set_defaults(func=createRequest,operation_name='query.posture.definitionList')

    query_posture_complianceFrameworkList_parser = query_posture_subparsers.add_parser('complianceFrameworkList', 
            help='complianceFrameworkList() posture operation', 
            usage=get_help("query_posture_complianceFrameworkList"))

    query_posture_complianceFrameworkList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_complianceFrameworkList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_complianceFrameworkList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_complianceFrameworkList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_complianceFrameworkList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_complianceFrameworkList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_complianceFrameworkList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_complianceFrameworkList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_complianceFrameworkList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_complianceFrameworkList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_complianceFrameworkList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_complianceFrameworkList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_complianceFrameworkList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_complianceFrameworkList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_complianceFrameworkList_parser.set_defaults(func=createRequest,operation_name='query.posture.complianceFrameworkList')

    query_posture_categoryList_parser = query_posture_subparsers.add_parser('categoryList', 
            help='categoryList() posture operation', 
            usage=get_help("query_posture_categoryList"))

    query_posture_categoryList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_posture_categoryList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_posture_categoryList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_posture_categoryList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_posture_categoryList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_posture_categoryList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_posture_categoryList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_posture_categoryList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_posture_categoryList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_posture_categoryList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_posture_categoryList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_posture_categoryList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_posture_categoryList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_posture_categoryList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_posture_categoryList_parser.set_defaults(func=createRequest,operation_name='query.posture.categoryList')
