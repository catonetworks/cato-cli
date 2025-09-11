
from ..customParserApiClient import createRequest, get_help

def query_socketPortMetricsTimeSeries_parse(query_subparsers):
    query_socketPortMetricsTimeSeries_parser = query_subparsers.add_parser('socketPortMetricsTimeSeries', 
            help='socketPortMetricsTimeSeries() query operation', 
            usage=get_help("query_socketPortMetricsTimeSeries"))

    query_socketPortMetricsTimeSeries_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_socketPortMetricsTimeSeries_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_socketPortMetricsTimeSeries_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_socketPortMetricsTimeSeries_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_socketPortMetricsTimeSeries_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_socketPortMetricsTimeSeries_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_socketPortMetricsTimeSeries_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_socketPortMetricsTimeSeries_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_socketPortMetricsTimeSeries_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')

    query_socketPortMetricsTimeSeries_parser.add_argument('-f', '--format', choices=['json', 'csv'], default='json', help='Output format (default: json)')
    query_socketPortMetricsTimeSeries_parser.add_argument('--csv-filename', dest='csv_filename', help='Override CSV file name (default: accountmetrics.csv)')
    query_socketPortMetricsTimeSeries_parser.add_argument('--append-timestamp', dest='append_timestamp', action='store_true', help='Append timestamp to the CSV file name')
    query_socketPortMetricsTimeSeries_parser.set_defaults(func=createRequest,operation_name='query.socketPortMetricsTimeSeries')
