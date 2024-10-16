
from ..parserApiClient import createRequest, get_help

def query_xdr_parse(query_subparsers):
	query_xdr_parser = query_subparsers.add_parser('xdr', 
			help='xdr() query operation', 
			usage=get_help("query_xdr"))

	query_xdr_subparsers = query_xdr_parser.add_subparsers()

	query_xdr_stories_parser = query_xdr_subparsers.add_parser('stories', 
			help='stories() xdr operation', 
			usage=get_help("query_xdr_stories"))

	query_xdr_stories_parser.add_argument('json', help='Variables in JSON format.')
	query_xdr_stories_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_xdr_stories_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_xdr_stories_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_xdr_stories_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_xdr_stories_parser.set_defaults(func=createRequest,operation_name='query.xdr.stories')

	query_xdr_story_parser = query_xdr_subparsers.add_parser('story', 
			help='story() xdr operation', 
			usage=get_help("query_xdr_story"))

	query_xdr_story_parser.add_argument('json', help='Variables in JSON format.')
	query_xdr_story_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_xdr_story_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_xdr_story_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_xdr_story_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_xdr_story_parser.set_defaults(func=createRequest,operation_name='query.xdr.story')
