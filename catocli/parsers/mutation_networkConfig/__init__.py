
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_networkConfig_parse(mutation_subparsers):
    mutation_networkConfig_parser = mutation_subparsers.add_parser('networkConfig', 
            help='networkConfig() mutation operation', 
            usage=get_help("mutation_networkConfig"), formatter_class=CustomSubparserHelpFormatter)

    mutation_networkConfig_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_networkConfig_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_networkConfig_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_networkConfig_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_networkConfig_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_networkConfig_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_networkConfig_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_networkConfig_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_networkConfig_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_networkConfig_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_networkConfig_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_networkConfig_parser.set_defaults(func=createRequest,operation_name='mutation.networkConfig')
