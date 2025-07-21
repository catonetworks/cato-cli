
from ..parserApiClient import createRequest, get_help

def query_catalogs_parse(query_subparsers):
	query_catalogs_parser = query_subparsers.add_parser('catalogs', 
			help='catalogs() query operation', 
			usage=get_help("query_catalogs"))

	query_catalogs_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	query_catalogs_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_catalogs_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	query_catalogs_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	query_catalogs_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	query_catalogs_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	query_catalogs_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	query_catalogs_parser.set_defaults(func=createRequest,operation_name='query.catalogs')
