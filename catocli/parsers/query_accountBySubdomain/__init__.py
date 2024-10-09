
from ..parserApiClient import createRequest, get_help

def query_accountBySubdomain_parse(query_subparsers):
	query_accountBySubdomain_parser = query_subparsers.add_parser('accountBySubdomain', 
			help='accountBySubdomain() query operation', 
			usage=get_help("query_accountBySubdomain"))

	query_accountBySubdomain_parser.add_argument('accountID', help='The Account ID.')
	query_accountBySubdomain_parser.add_argument('json', help='Variables in JSON format.')
	query_accountBySubdomain_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_accountBySubdomain_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_accountBySubdomain_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_accountBySubdomain_parser.set_defaults(func=createRequest,operation_name='query.accountBySubdomain')