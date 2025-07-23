
from ..parserApiClient import createRawRequest, get_help

def raw_parse(raw_parser):
	raw_parser.add_argument('json', nargs='?', default='{}', help='Query, Variables and opertaionName in JSON format (defaults to empty object if not provided).')
	raw_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
	raw_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	raw_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	raw_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	raw_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	raw_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint URL (e.g., https://api.catonetworks.com/api/v1/graphql2)')
	raw_parser.add_argument('--binary', action='store_true', help='Send multipart/form-data request for file uploads and binary content')
	raw_parser.add_argument('--file', action='append', nargs=2, metavar=('FIELD', 'PATH'), dest='files', help='Add file for multipart upload. Format: --file field_name file_path')
	raw_parser.set_defaults(func=createRawRequest,operation_name='raw')
