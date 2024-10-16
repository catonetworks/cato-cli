
from ..parserApiClient import createRequest, get_help

def query_admins_parse(query_subparsers):
	query_admins_parser = query_subparsers.add_parser('admins', 
			help='admins() query operation', 
			usage=get_help("query_admins"))

	query_admins_parser.add_argument('json', help='Variables in JSON format.')
	query_admins_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_admins_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_admins_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_admins_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_admins_parser.set_defaults(func=createRequest,operation_name='query.admins')
