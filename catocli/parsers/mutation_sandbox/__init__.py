
from ..parserApiClient import createRequest, get_help

def mutation_sandbox_parse(mutation_subparsers):
	mutation_sandbox_parser = mutation_subparsers.add_parser('sandbox', 
			help='sandbox() mutation operation', 
			usage=get_help("mutation_sandbox"))

	mutation_sandbox_subparsers = mutation_sandbox_parser.add_subparsers()

	mutation_sandbox_deleteReport_parser = mutation_sandbox_subparsers.add_parser('deleteReport', 
			help='deleteReport() sandbox operation', 
			usage=get_help("mutation_sandbox_deleteReport"))

	mutation_sandbox_deleteReport_parser.add_argument('json', help='Variables in JSON format.')
	mutation_sandbox_deleteReport_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sandbox_deleteReport_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_sandbox_deleteReport_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_sandbox_deleteReport_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_sandbox_deleteReport_parser.set_defaults(func=createRequest,operation_name='mutation.sandbox.deleteReport')

	mutation_sandbox_uploadFile_parser = mutation_sandbox_subparsers.add_parser('uploadFile', 
			help='uploadFile() sandbox operation', 
			usage=get_help("mutation_sandbox_uploadFile"))

	mutation_sandbox_uploadFile_parser.add_argument('json', help='Variables in JSON format.')
	mutation_sandbox_uploadFile_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_sandbox_uploadFile_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_sandbox_uploadFile_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_sandbox_uploadFile_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_sandbox_uploadFile_parser.set_defaults(func=createRequest,operation_name='mutation.sandbox.uploadFile')
