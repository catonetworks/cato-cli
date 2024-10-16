
from ..parserApiClient import createRequest, get_help

def query_entityLookup_parse(query_subparsers):
	query_entityLookup_parser = query_subparsers.add_parser('entityLookup', 
			help='entityLookup() query operation', 
			usage=get_help("query_entityLookup"))

	query_entityLookup_parser.add_argument('json', help='Variables in JSON format.')
	query_entityLookup_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_entityLookup_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_entityLookup_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_entityLookup_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_entityLookup_parser.set_defaults(func=createRequest,operation_name='query.entityLookup')
