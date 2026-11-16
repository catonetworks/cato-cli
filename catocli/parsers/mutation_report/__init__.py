
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_report_parse(mutation_subparsers):
    mutation_report_parser = mutation_subparsers.add_parser('report', 
            help='report() mutation operation', 
            usage=get_help("mutation_report"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_report_help(args, configuration=None):
        """Show help when mutation_report is called without subcommand"""
        print("\ncatocli mutation report <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createConfiguration            createConfiguration operation\n  updateConfiguration            updateConfiguration operation\n  deleteConfiguration            deleteConfiguration operation\n  generateReport                 generateReport operation\n  deleteRun                      deleteRun operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation report <subcommand> -h")
        return None

    mutation_report_subparsers = mutation_report_parser.add_subparsers()
    mutation_report_parser.set_defaults(func=_show_mutation_report_help)

    mutation_report_createConfiguration_parser = mutation_report_subparsers.add_parser('createConfiguration', 
            help='createConfiguration() report operation', 
            usage=get_help("mutation_report_createConfiguration"))

    mutation_report_createConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_report_createConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_report_createConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_report_createConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_report_createConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_report_createConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_report_createConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_report_createConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_report_createConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_report_createConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_report_createConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_report_createConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_report_createConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_report_createConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_report_createConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.report.createConfiguration')

    mutation_report_updateConfiguration_parser = mutation_report_subparsers.add_parser('updateConfiguration', 
            help='updateConfiguration() report operation', 
            usage=get_help("mutation_report_updateConfiguration"))

    mutation_report_updateConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_report_updateConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_report_updateConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_report_updateConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_report_updateConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_report_updateConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_report_updateConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_report_updateConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_report_updateConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_report_updateConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_report_updateConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_report_updateConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_report_updateConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_report_updateConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_report_updateConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.report.updateConfiguration')

    mutation_report_deleteConfiguration_parser = mutation_report_subparsers.add_parser('deleteConfiguration', 
            help='deleteConfiguration() report operation', 
            usage=get_help("mutation_report_deleteConfiguration"))

    mutation_report_deleteConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_report_deleteConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_report_deleteConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_report_deleteConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_report_deleteConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_report_deleteConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_report_deleteConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_report_deleteConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_report_deleteConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_report_deleteConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_report_deleteConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_report_deleteConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_report_deleteConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_report_deleteConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_report_deleteConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.report.deleteConfiguration')

    mutation_report_generateReport_parser = mutation_report_subparsers.add_parser('generateReport', 
            help='generateReport() report operation', 
            usage=get_help("mutation_report_generateReport"))

    mutation_report_generateReport_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_report_generateReport_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_report_generateReport_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_report_generateReport_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_report_generateReport_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_report_generateReport_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_report_generateReport_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_report_generateReport_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_report_generateReport_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_report_generateReport_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_report_generateReport_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_report_generateReport_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_report_generateReport_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_report_generateReport_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_report_generateReport_parser.set_defaults(func=createRequest,operation_name='mutation.report.generateReport')

    mutation_report_deleteRun_parser = mutation_report_subparsers.add_parser('deleteRun', 
            help='deleteRun() report operation', 
            usage=get_help("mutation_report_deleteRun"))

    mutation_report_deleteRun_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_report_deleteRun_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_report_deleteRun_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_report_deleteRun_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_report_deleteRun_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_report_deleteRun_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_report_deleteRun_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_report_deleteRun_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_report_deleteRun_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_report_deleteRun_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_report_deleteRun_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_report_deleteRun_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_report_deleteRun_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_report_deleteRun_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_report_deleteRun_parser.set_defaults(func=createRequest,operation_name='mutation.report.deleteRun')
