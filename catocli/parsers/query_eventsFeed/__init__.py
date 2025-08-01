
from ..parserApiClient import createRequest, get_help

def query_eventsFeed_parse(query_subparsers):
	query_eventsFeed_parser = query_subparsers.add_parser('eventsFeed', 
			help='eventsFeed() query operation', 
			usage=get_help("query_eventsFeed"))

	query_eventsFeed_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	query_eventsFeed_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_eventsFeed_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	query_eventsFeed_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	query_eventsFeed_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	query_eventsFeed_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	query_eventsFeed_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	query_eventsFeed_parser.set_defaults(func=createRequest,operation_name='query.eventsFeed')
