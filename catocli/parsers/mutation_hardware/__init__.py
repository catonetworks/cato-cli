
from ..parserApiClient import createRequest, get_help

def mutation_hardware_parse(mutation_subparsers):
	mutation_hardware_parser = mutation_subparsers.add_parser('hardware', 
			help='hardware() mutation operation', 
			usage=get_help("mutation_hardware"))

	mutation_hardware_subparsers = mutation_hardware_parser.add_subparsers()

	mutation_hardware_updateHardwareShipping_parser = mutation_hardware_subparsers.add_parser('updateHardwareShipping', 
			help='updateHardwareShipping() hardware operation', 
			usage=get_help("mutation_hardware_updateHardwareShipping"))

	mutation_hardware_updateHardwareShipping_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
	mutation_hardware_updateHardwareShipping_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_hardware_updateHardwareShipping_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	mutation_hardware_updateHardwareShipping_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	mutation_hardware_updateHardwareShipping_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	mutation_hardware_updateHardwareShipping_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	mutation_hardware_updateHardwareShipping_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	mutation_hardware_updateHardwareShipping_parser.set_defaults(func=createRequest,operation_name='mutation.hardware.updateHardwareShipping')
