
from ..customParserApiClient import createRequest, get_help

def mutation_xdr_parse(mutation_subparsers):
    mutation_xdr_parser = mutation_subparsers.add_parser('xdr', 
            help='xdr() mutation operation', 
            usage=get_help("mutation_xdr"))

    mutation_xdr_subparsers = mutation_xdr_parser.add_subparsers()

    mutation_xdr_analystFeedback_parser = mutation_xdr_subparsers.add_parser('analystFeedback', 
            help='analystFeedback() xdr operation', 
            usage=get_help("mutation_xdr_analystFeedback"))

    mutation_xdr_analystFeedback_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_xdr_analystFeedback_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_xdr_analystFeedback_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_xdr_analystFeedback_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_xdr_analystFeedback_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_xdr_analystFeedback_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_xdr_analystFeedback_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_xdr_analystFeedback_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_xdr_analystFeedback_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_xdr_analystFeedback_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.analystFeedback')

    mutation_xdr_addStoryComment_parser = mutation_xdr_subparsers.add_parser('addStoryComment', 
            help='addStoryComment() xdr operation', 
            usage=get_help("mutation_xdr_addStoryComment"))

    mutation_xdr_addStoryComment_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_xdr_addStoryComment_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_xdr_addStoryComment_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_xdr_addStoryComment_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_xdr_addStoryComment_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_xdr_addStoryComment_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_xdr_addStoryComment_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_xdr_addStoryComment_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_xdr_addStoryComment_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_xdr_addStoryComment_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.addStoryComment')

    mutation_xdr_deleteStoryComment_parser = mutation_xdr_subparsers.add_parser('deleteStoryComment', 
            help='deleteStoryComment() xdr operation', 
            usage=get_help("mutation_xdr_deleteStoryComment"))

    mutation_xdr_deleteStoryComment_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_xdr_deleteStoryComment_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_xdr_deleteStoryComment_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_xdr_deleteStoryComment_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_xdr_deleteStoryComment_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_xdr_deleteStoryComment_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_xdr_deleteStoryComment_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_xdr_deleteStoryComment_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_xdr_deleteStoryComment_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_xdr_deleteStoryComment_parser.set_defaults(func=createRequest,operation_name='mutation.xdr.deleteStoryComment')
