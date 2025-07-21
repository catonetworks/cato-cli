
from ..parserApiClient import querySiteLocation, get_help

def query_siteLocation_parse(query_subparsers):
	query_siteLocation_parser = query_subparsers.add_parser('siteLocation', 
			help='siteLocation local cli query', 
			usage=get_help("query_siteLocation"))
	query_siteLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	query_siteLocation_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_siteLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	query_siteLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	query_siteLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	query_siteLocation_parser.set_defaults(func=querySiteLocation,operation_name='query.siteLocation')
