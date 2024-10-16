
from ..parserApiClient import createRequest, get_help

def query_appStats_parse(query_subparsers):
	query_appStats_parser = query_subparsers.add_parser('appStats', 
			help='appStats() query operation', 
			usage=get_help("query_appStats"))

	query_appStats_parser.add_argument('json', help='Variables in JSON format.')
	query_appStats_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_appStats_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_appStats_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_appStats_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_appStats_parser.set_defaults(func=createRequest,operation_name='query.appStats')
