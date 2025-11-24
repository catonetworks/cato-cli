
from ...customParserApiClient import queryAppCategory, get_help

def query_appCategory_parse(query_subparsers):
    query_appCategory_parser = query_subparsers.add_parser('appCategory', 
            help='appCategory local cli query', 
            usage=get_help("query_appCategory"))
    query_appCategory_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_appCategory_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_appCategory_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_appCategory_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_appCategory_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_appCategory_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_appCategory_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_appCategory_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_appCategory_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_appCategory_parser.set_defaults(func=queryAppCategory, operation_name='query.appCategory')
