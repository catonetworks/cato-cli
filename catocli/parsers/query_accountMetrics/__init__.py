
from ..parserApiClient import createRequest, get_help

def query_accountMetrics_parse(query_subparsers):
	query_accountMetrics_parser = query_subparsers.add_parser('accountMetrics', 
			help='accountMetrics() query operation', 
			usage=get_help("query_accountMetrics"))

	query_accountMetrics_parser.add_argument('json', help='Variables in JSON format.')
	query_accountMetrics_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_accountMetrics_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_accountMetrics_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_accountMetrics_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_accountMetrics_parser.set_defaults(func=createRequest,operation_name='query.accountMetrics')
