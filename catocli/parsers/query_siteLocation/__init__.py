
from ..customParserApiClient import querySiteLocation, get_help

def query_siteLocation_parse(query_subparsers):
    query_siteLocation_parser = query_subparsers.add_parser('siteLocation', 
            help='siteLocation local cli query', 
            usage=get_help("query_siteLocation"))
    query_siteLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_siteLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_siteLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_siteLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_siteLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_siteLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_siteLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_siteLocation_parser.set_defaults(func=querySiteLocation,operation_name='query.siteLocation')
