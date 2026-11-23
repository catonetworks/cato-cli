
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_reporting_parse(mutation_subparsers):
    mutation_reporting_parser = mutation_subparsers.add_parser('reporting', 
            help='reporting() mutation operation', 
            usage=get_help("mutation_reporting"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_reporting_help(args, configuration=None):
        """Show help when mutation_reporting is called without subcommand"""
        print("\ncatocli mutation reporting <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createReportConfiguration      createReportConfiguration operation\n  updateReportConfiguration      updateReportConfiguration operation\n  deleteReportConfiguration      deleteReportConfiguration operation\n  generateReport                 generateReport operation\n  deleteReportRun                deleteReportRun operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation reporting <subcommand> -h")
        return None

    mutation_reporting_subparsers = mutation_reporting_parser.add_subparsers()
    mutation_reporting_parser.set_defaults(func=_show_mutation_reporting_help)

    mutation_reporting_createReportConfiguration_parser = mutation_reporting_subparsers.add_parser('createReportConfiguration', 
            help='createReportConfiguration() reporting operation', 
            usage=get_help("mutation_reporting_createReportConfiguration"))

    mutation_reporting_createReportConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_reporting_createReportConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_reporting_createReportConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_reporting_createReportConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_reporting_createReportConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_reporting_createReportConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_reporting_createReportConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_reporting_createReportConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_reporting_createReportConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_reporting_createReportConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_reporting_createReportConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_reporting_createReportConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_reporting_createReportConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_reporting_createReportConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_reporting_createReportConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.reporting.createReportConfiguration')

    mutation_reporting_updateReportConfiguration_parser = mutation_reporting_subparsers.add_parser('updateReportConfiguration', 
            help='updateReportConfiguration() reporting operation', 
            usage=get_help("mutation_reporting_updateReportConfiguration"))

    mutation_reporting_updateReportConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_reporting_updateReportConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_reporting_updateReportConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_reporting_updateReportConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.reporting.updateReportConfiguration')

    mutation_reporting_deleteReportConfiguration_parser = mutation_reporting_subparsers.add_parser('deleteReportConfiguration', 
            help='deleteReportConfiguration() reporting operation', 
            usage=get_help("mutation_reporting_deleteReportConfiguration"))

    mutation_reporting_deleteReportConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_reporting_deleteReportConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_reporting_deleteReportConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.reporting.deleteReportConfiguration')

    mutation_reporting_generateReport_parser = mutation_reporting_subparsers.add_parser('generateReport', 
            help='generateReport() reporting operation', 
            usage=get_help("mutation_reporting_generateReport"))

    mutation_reporting_generateReport_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_reporting_generateReport_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_reporting_generateReport_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_reporting_generateReport_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_reporting_generateReport_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_reporting_generateReport_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_reporting_generateReport_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_reporting_generateReport_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_reporting_generateReport_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_reporting_generateReport_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_reporting_generateReport_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_reporting_generateReport_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_reporting_generateReport_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_reporting_generateReport_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_reporting_generateReport_parser.set_defaults(func=createRequest,operation_name='mutation.reporting.generateReport')

    mutation_reporting_deleteReportRun_parser = mutation_reporting_subparsers.add_parser('deleteReportRun', 
            help='deleteReportRun() reporting operation', 
            usage=get_help("mutation_reporting_deleteReportRun"))

    mutation_reporting_deleteReportRun_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_reporting_deleteReportRun_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_reporting_deleteReportRun_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_reporting_deleteReportRun_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_reporting_deleteReportRun_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_reporting_deleteReportRun_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_reporting_deleteReportRun_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_reporting_deleteReportRun_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_reporting_deleteReportRun_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_reporting_deleteReportRun_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_reporting_deleteReportRun_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_reporting_deleteReportRun_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_reporting_deleteReportRun_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_reporting_deleteReportRun_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_reporting_deleteReportRun_parser.set_defaults(func=createRequest,operation_name='mutation.reporting.deleteReportRun')
