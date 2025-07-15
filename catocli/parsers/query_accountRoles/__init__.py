
from ..parserApiClient import createRequest, get_help

def query_accountRoles_parse(query_subparsers):
	query_accountRoles_parser = query_subparsers.add_parser('accountRoles', 
			help='accountRoles() query operation', 
			usage=get_help("query_accountRoles"))

	query_accountRoles_parser.add_argument('json', help='Variables in JSON format.')
	query_accountRoles_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_accountRoles_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print test request preview without sending api call')
	query_accountRoles_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	query_accountRoles_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	query_accountRoles_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	query_accountRoles_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	query_accountRoles_parser.set_defaults(func=createRequest,operation_name='query.accountRoles')
