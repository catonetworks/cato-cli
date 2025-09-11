
from ..customParserApiClient import createRequest, get_help

def mutation_sandbox_parse(mutation_subparsers):
    mutation_sandbox_parser = mutation_subparsers.add_parser('sandbox', 
            help='sandbox() mutation operation', 
            usage=get_help("mutation_sandbox"))

    mutation_sandbox_subparsers = mutation_sandbox_parser.add_subparsers()

    mutation_sandbox_uploadFile_parser = mutation_sandbox_subparsers.add_parser('uploadFile', 
            help='uploadFile() sandbox operation', 
            usage=get_help("mutation_sandbox_uploadFile"))

    mutation_sandbox_uploadFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_sandbox_uploadFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_sandbox_uploadFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_sandbox_uploadFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_sandbox_uploadFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_sandbox_uploadFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_sandbox_uploadFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_sandbox_uploadFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_sandbox_uploadFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_sandbox_uploadFile_parser.set_defaults(func=createRequest,operation_name='mutation.sandbox.uploadFile')

    mutation_sandbox_deleteReport_parser = mutation_sandbox_subparsers.add_parser('deleteReport', 
            help='deleteReport() sandbox operation', 
            usage=get_help("mutation_sandbox_deleteReport"))

    mutation_sandbox_deleteReport_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_sandbox_deleteReport_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_sandbox_deleteReport_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_sandbox_deleteReport_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_sandbox_deleteReport_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_sandbox_deleteReport_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_sandbox_deleteReport_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_sandbox_deleteReport_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_sandbox_deleteReport_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_sandbox_deleteReport_parser.set_defaults(func=createRequest,operation_name='mutation.sandbox.deleteReport')
