
from ..parserApiClient import createRequest, get_help

def query_hardware_parse(query_subparsers):
	query_hardware_parser = query_subparsers.add_parser('hardware', 
			help='hardware() query operation', 
			usage=get_help("query_hardware"))

	query_hardware_parser.add_argument('json', help='Variables in JSON format.')
	query_hardware_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_hardware_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_hardware_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_hardware_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_hardware_parser.set_defaults(func=createRequest,operation_name='query.hardware')
