
from ..parserApiClient import createRequest, get_help

def mutation_container_parse(mutation_subparsers):
	mutation_container_parser = mutation_subparsers.add_parser('container', 
			help='container() mutation operation', 
			usage=get_help("mutation_container"))

	mutation_container_subparsers = mutation_container_parser.add_subparsers()

	mutation_container_delete_parser = mutation_container_subparsers.add_parser('delete', 
			help='delete() container operation', 
			usage=get_help("mutation_container_delete"))

	mutation_container_delete_parser.add_argument('json', help='Variables in JSON format.')
	mutation_container_delete_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_container_delete_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_container_delete_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_container_delete_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_container_delete_parser.set_defaults(func=createRequest,operation_name='mutation.container.delete')
