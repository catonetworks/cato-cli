
from ...customParserApiClient import createRequest, get_help
from ..eventsFeedEnhanced import enhanced_events_feed_handler

def query_eventsFeed_parse(query_subparsers):
    query_eventsFeed_parser = query_subparsers.add_parser('eventsFeed', 
            help='Enhanced eventsFeed() query operation with advanced features', 
            usage=get_help("query_eventsFeed"))

    # Standard catocli arguments
    query_eventsFeed_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_eventsFeed_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_eventsFeed_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_eventsFeed_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_eventsFeed_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_eventsFeed_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_eventsFeed_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_eventsFeed_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_eventsFeed_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    
    # Enhanced eventsFeed arguments (from original cato-toolbox script)
    query_eventsFeed_parser.add_argument('--print-events', dest='print_events', action='store_true', help='Print event records to console')
    query_eventsFeed_parser.add_argument('--prettify', dest='prettify', action='store_true', help='Prettify JSON output')
    query_eventsFeed_parser.add_argument('--marker', dest='marker', help='Initial marker value (default: "", start of queue)')
    query_eventsFeed_parser.add_argument('--marker-file', dest='marker_file', help='Config file location for marker persistence (default: ./events-marker.txt)')
    query_eventsFeed_parser.add_argument('--event-types', dest='event_types', help='Comma-separated list of event types to filter on')
    query_eventsFeed_parser.add_argument('--event-sub-types', dest='event_sub_types', help='Comma-separated list of event sub types to filter on')
    query_eventsFeed_parser.add_argument('--fetch-limit', dest='fetch_limit', type=int, default=1, help='Stop execution if a fetch returns less than this number of events (default=1)')
    query_eventsFeed_parser.add_argument('--runtime-limit', dest='runtime_limit', type=int, help='Stop execution if total runtime exceeds this many seconds (default=infinite)')
    query_eventsFeed_parser.add_argument('--run', dest='run', action='store_true', help='Use run mode with continuous polling, marker persistence, and advanced filtering')
    query_eventsFeed_parser.add_argument('-vv', '--very-verbose', dest='very_verbose', action='store_true', help='Print detailed debug information')
    
    query_eventsFeed_parser.set_defaults(func=eventsFeed_dispatcher, operation_name='query.eventsFeed')


def eventsFeed_dispatcher(args, configuration):
    """Dispatcher that chooses between standard and enhanced eventsFeed modes"""
    # Check if run mode is requested or if any enhanced features are used
    enhanced_features = [
        getattr(args, 'run', False),
        getattr(args, 'marker', None),
        getattr(args, 'config_file', None),
        getattr(args, 'event_types', None),
        getattr(args, 'event_sub_types', None),
        getattr(args, 'print_events', False),
        getattr(args, 'prettify', False),
        getattr(args, 'fetch_limit', 1) != 1,
        getattr(args, 'runtime_limit', None),
        getattr(args, 'very_verbose', False)
    ]
    
    if any(enhanced_features):
        # Use enhanced handler
        return enhanced_events_feed_handler(args, configuration)
    else:
        # Use standard catocli handler  
        return createRequest(args, configuration)
