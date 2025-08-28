
from ..customParserApiClient import createRequest, get_help

def query_appStats_parse(query_subparsers):
    query_appStats_parser = query_subparsers.add_parser('appStats', 
            help='appStats() query operation', 
            usage=get_help("query_appStats"))

    query_appStats_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_appStats_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_appStats_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_appStats_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_appStats_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_appStats_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_appStats_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_appStats_parser.set_defaults(func=createRequest,operation_name='query.appStats')
