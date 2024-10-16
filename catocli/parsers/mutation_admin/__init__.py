
from ..parserApiClient import createRequest, get_help

def mutation_admin_parse(mutation_subparsers):
	mutation_admin_parser = mutation_subparsers.add_parser('admin', 
			help='admin() mutation operation', 
			usage=get_help("mutation_admin"))

	mutation_admin_subparsers = mutation_admin_parser.add_subparsers()

	mutation_admin_addAdmin_parser = mutation_admin_subparsers.add_parser('addAdmin', 
			help='addAdmin() admin operation', 
			usage=get_help("mutation_admin_addAdmin"))

	mutation_admin_addAdmin_parser.add_argument('json', help='Variables in JSON format.')
	mutation_admin_addAdmin_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_admin_addAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_admin_addAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_admin_addAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_admin_addAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.addAdmin')

	mutation_admin_removeAdmin_parser = mutation_admin_subparsers.add_parser('removeAdmin', 
			help='removeAdmin() admin operation', 
			usage=get_help("mutation_admin_removeAdmin"))

	mutation_admin_removeAdmin_parser.add_argument('json', help='Variables in JSON format.')
	mutation_admin_removeAdmin_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_admin_removeAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_admin_removeAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_admin_removeAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_admin_removeAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.removeAdmin')

	mutation_admin_updateAdmin_parser = mutation_admin_subparsers.add_parser('updateAdmin', 
			help='updateAdmin() admin operation', 
			usage=get_help("mutation_admin_updateAdmin"))

	mutation_admin_updateAdmin_parser.add_argument('json', help='Variables in JSON format.')
	mutation_admin_updateAdmin_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_admin_updateAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_admin_updateAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_admin_updateAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_admin_updateAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.updateAdmin')
