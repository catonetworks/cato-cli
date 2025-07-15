
from ..parserApiClient import createRawRequest, get_help

def raw_parse(raw_parser):
	raw_parser.add_argument('json', help='Query, Variables and opertaionName in JSON format.')
	raw_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print test request preview without sending api call')
	raw_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
	raw_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
	raw_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
	raw_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
	raw_parser.set_defaults(func=createRawRequest,operation_name='raw')
