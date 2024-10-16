
from ..parserApiClient import createRequest, get_help

def query_eventsTimeSeries_parse(query_subparsers):
	query_eventsTimeSeries_parser = query_subparsers.add_parser('eventsTimeSeries', 
			help='eventsTimeSeries() query operation', 
			usage=get_help("query_eventsTimeSeries"))

	query_eventsTimeSeries_parser.add_argument('json', help='Variables in JSON format.')
	query_eventsTimeSeries_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	query_eventsTimeSeries_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_eventsTimeSeries_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_eventsTimeSeries_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_eventsTimeSeries_parser.set_defaults(func=createRequest,operation_name='query.eventsTimeSeries')
