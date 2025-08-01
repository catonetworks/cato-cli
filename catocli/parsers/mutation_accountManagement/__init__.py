
from ..parserApiClient import createRequest, get_help

def mutation_accountManagement_parse(mutation_subparsers):
	mutation_accountManagement_parser = mutation_subparsers.add_parser('accountManagement', 
			help='accountManagement() mutation operation', 
			usage=get_help("mutation_accountManagement"))

	mutation_accountManagement_subparsers = mutation_accountManagement_parser.add_subparsers()

	mutation_accountManagement_addAccount_parser = mutation_accountManagement_subparsers.add_parser('addAccount', 
			help='addAccount() accountManagement operation', 
			usage=get_help("mutation_accountManagement_addAccount"))

	mutation_accountManagement_addAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_accountManagement_addAccount_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_accountManagement_addAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_accountManagement_addAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_accountManagement_addAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_accountManagement_addAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_accountManagement_addAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_accountManagement_addAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.addAccount')

	mutation_accountManagement_removeAccount_parser = mutation_accountManagement_subparsers.add_parser('removeAccount', 
			help='removeAccount() accountManagement operation', 
			usage=get_help("mutation_accountManagement_removeAccount"))

	mutation_accountManagement_removeAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_accountManagement_removeAccount_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_accountManagement_removeAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_accountManagement_removeAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_accountManagement_removeAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_accountManagement_removeAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_accountManagement_removeAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_accountManagement_removeAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.removeAccount')

	mutation_accountManagement_updateAccount_parser = mutation_accountManagement_subparsers.add_parser('updateAccount', 
			help='updateAccount() accountManagement operation', 
			usage=get_help("mutation_accountManagement_updateAccount"))

	mutation_accountManagement_updateAccount_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_accountManagement_updateAccount_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_accountManagement_updateAccount_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_accountManagement_updateAccount_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_accountManagement_updateAccount_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_accountManagement_updateAccount_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_accountManagement_updateAccount_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_accountManagement_updateAccount_parser.set_defaults(func=createRequest,operation_name='mutation.accountManagement.updateAccount')
