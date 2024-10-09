
from ..parserApiClient import createRequest, get_help

def query_auditFeed_parse(query_subparsers):
	query_auditFeed_parser = query_subparsers.add_parser('auditFeed', 
			help='auditFeed() query operation', 
			usage=get_help("query_auditFeed"))

	query_auditFeed_parser.add_argument('accountID', help='The Account ID.')
	query_auditFeed_parser.add_argument('json', help='Variables in JSON format.')
	query_auditFeed_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_auditFeed_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_auditFeed_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_auditFeed_parser.set_defaults(func=createRequest,operation_name='query.auditFeed')
