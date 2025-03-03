
from ..parserApiClient import createRequest, get_help

def mutation_xdr_parse(mutation_subparsers):
	mutation_xdr_parser = mutation_subparsers.add_parser('xdr', 
			help='xdr() mutation operation', 
			usage=get_help("mutation_xdr"))

	mutation_xdr_subparsers = mutation_xdr_parser.add_subparsers()

	mutation_xdr_addStoryComment_parser = mutation_xdr_subparsers.add_parser('addStoryComment', 
			help='addStoryComment() xdr operation', 
			usage=get_help("mutation_xdr_addStoryComment"))

	mutation_xdr_addStoryComment_parser.add_argument('json', help='Variables in JSON format.')
	mutation_xdr_addStoryComment_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_xdr_addStoryComment_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_xdr_addStoryComment_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_xdr_addStoryComment_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_xdr_addStoryComment_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.addStoryComment')

	mutation_xdr_analystFeedback_parser = mutation_xdr_subparsers.add_parser('analystFeedback', 
			help='analystFeedback() xdr operation', 
			usage=get_help("mutation_xdr_analystFeedback"))

	mutation_xdr_analystFeedback_parser.add_argument('json', help='Variables in JSON format.')
	mutation_xdr_analystFeedback_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_xdr_analystFeedback_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_xdr_analystFeedback_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_xdr_analystFeedback_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_xdr_analystFeedback_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.analystFeedback')

	mutation_xdr_deleteStoryComment_parser = mutation_xdr_subparsers.add_parser('deleteStoryComment', 
			help='deleteStoryComment() xdr operation', 
			usage=get_help("mutation_xdr_deleteStoryComment"))

	mutation_xdr_deleteStoryComment_parser.add_argument('json', help='Variables in JSON format.')
	mutation_xdr_deleteStoryComment_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_xdr_deleteStoryComment_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_xdr_deleteStoryComment_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_xdr_deleteStoryComment_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_xdr_deleteStoryComment_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.deleteStoryComment')
