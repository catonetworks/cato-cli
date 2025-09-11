
from ..customParserApiClient import createRequest, get_help

def mutation_enterpriseDirectory_parse(mutation_subparsers):
    mutation_enterpriseDirectory_parser = mutation_subparsers.add_parser('enterpriseDirectory', 
            help='enterpriseDirectory() mutation operation', 
            usage=get_help("mutation_enterpriseDirectory"))

    mutation_enterpriseDirectory_subparsers = mutation_enterpriseDirectory_parser.add_subparsers()

    mutation_enterpriseDirectory_createLocation_parser = mutation_enterpriseDirectory_subparsers.add_parser('createLocation', 
            help='createLocation() enterpriseDirectory operation', 
            usage=get_help("mutation_enterpriseDirectory_createLocation"))

    mutation_enterpriseDirectory_createLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_enterpriseDirectory_createLocation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_enterpriseDirectory_createLocation_parser.set_defaults(func=createRequest,operation_name='mutation.enterpriseDirectory.createLocation')

    mutation_enterpriseDirectory_updateLocation_parser = mutation_enterpriseDirectory_subparsers.add_parser('updateLocation', 
            help='updateLocation() enterpriseDirectory operation', 
            usage=get_help("mutation_enterpriseDirectory_updateLocation"))

    mutation_enterpriseDirectory_updateLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_enterpriseDirectory_updateLocation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_enterpriseDirectory_updateLocation_parser.set_defaults(func=createRequest,operation_name='mutation.enterpriseDirectory.updateLocation')

    mutation_enterpriseDirectory_archiveLocation_parser = mutation_enterpriseDirectory_subparsers.add_parser('archiveLocation', 
            help='archiveLocation() enterpriseDirectory operation', 
            usage=get_help("mutation_enterpriseDirectory_archiveLocation"))

    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_enterpriseDirectory_archiveLocation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_enterpriseDirectory_archiveLocation_parser.set_defaults(func=createRequest,operation_name='mutation.enterpriseDirectory.archiveLocation')

    mutation_enterpriseDirectory_restoreLocation_parser = mutation_enterpriseDirectory_subparsers.add_parser('restoreLocation', 
            help='restoreLocation() enterpriseDirectory operation', 
            usage=get_help("mutation_enterpriseDirectory_restoreLocation"))

    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_enterpriseDirectory_restoreLocation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_enterpriseDirectory_restoreLocation_parser.set_defaults(func=createRequest,operation_name='mutation.enterpriseDirectory.restoreLocation')
