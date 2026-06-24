
from ..custom.auditFeedEnhanced import enhanced_audit_feed_handler
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_auditFeed_parse(query_subparsers):
    query_auditFeed_parser = query_subparsers.add_parser('auditFeed', 
            help='auditFeed() query operation', 
            usage=get_help("query_auditFeed"), formatter_class=CustomSubparserHelpFormatter)

    query_auditFeed_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_auditFeed_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_auditFeed_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_auditFeed_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_auditFeed_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_auditFeed_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_auditFeed_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_auditFeed_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_auditFeed_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_auditFeed_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_auditFeed_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_auditFeed_parser.add_argument('--print-events', dest='print_events', action='store_true', help='Print audit records to console')
    query_auditFeed_parser.add_argument('--prettify', dest='prettify', action='store_true', help='Prettify JSON output')
    query_auditFeed_parser.add_argument('--marker', dest='marker', help='Initial marker value (default: "", start of queue)')
    query_auditFeed_parser.add_argument('--marker-file', dest='marker_file', help='Config file location for marker persistence (default: ./audit-marker.txt)')
    query_auditFeed_parser.add_argument('--field-names', dest='field_names', help='Comma-separated list of audit fields to return')
    query_auditFeed_parser.add_argument('--filter-field', dest='filter_field', help='Audit field name to filter on, for example admin or change_type')
    query_auditFeed_parser.add_argument('--filter-operator', dest='filter_operator', default='is', help='Audit filter operator (default=is)')
    query_auditFeed_parser.add_argument('--filter-values', dest='filter_values', help='Comma-separated list of values for --filter-field')
    query_auditFeed_parser.add_argument('--fetch-limit', dest='fetch_limit', type=int, default=1, help='Stop execution if a fetch returns less than this number of audit records (default=1)')
    query_auditFeed_parser.add_argument('--runtime-limit', dest='runtime_limit', type=int, help='Stop execution if total runtime exceeds this many seconds (default=infinite)')
    query_auditFeed_parser.add_argument('--run', dest='run', action='store_true', help='Use run mode with continuous polling, marker persistence, and audit filtering')
    query_auditFeed_parser.add_argument('-vv', '--very-verbose', dest='very_verbose', action='store_true', help='Print detailed debug information')
    query_auditFeed_parser.add_argument('--append-new-line', '-anl', dest='append_new_line', action='store_true', help='Append a newline character (\\n) to each audit record when sent over network (-n) or to Sentinel (-z)')
    query_auditFeed_parser.set_defaults(func=auditFeed_dispatcher,operation_name='query.auditFeed')


def auditFeed_dispatcher(args, configuration):
    """Dispatcher that chooses between standard and enhanced auditFeed modes."""
    enhanced_features = [
        getattr(args, 'run', False),
        getattr(args, 'marker', None),
        getattr(args, 'marker_file', None),
        getattr(args, 'field_names', None),
        getattr(args, 'filter_field', None),
        getattr(args, 'filter_values', None),
        getattr(args, 'print_events', False),
        getattr(args, 'prettify', False),
        getattr(args, 'fetch_limit', 1) != 1,
        getattr(args, 'runtime_limit', None),
        getattr(args, 'very_verbose', False),
        getattr(args, 'append_new_line', False)
    ]

    if any(enhanced_features):
        return enhanced_audit_feed_handler(args, configuration)

    return createRequest(args, configuration)
