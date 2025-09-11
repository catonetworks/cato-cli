
from ..customParserApiClient import createRequest, get_help

def mutation_groups_parse(mutation_subparsers):
    mutation_groups_parser = mutation_subparsers.add_parser('groups', 
            help='groups() mutation operation', 
            usage=get_help("mutation_groups"))

    mutation_groups_subparsers = mutation_groups_parser.add_subparsers()

    mutation_groups_createGroup_parser = mutation_groups_subparsers.add_parser('createGroup', 
            help='createGroup() groups operation', 
            usage=get_help("mutation_groups_createGroup"))

    mutation_groups_createGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_groups_createGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_groups_createGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_groups_createGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_groups_createGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_groups_createGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_groups_createGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_groups_createGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_groups_createGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_groups_createGroup_parser.set_defaults(func=createRequest,operation_name='mutation.groups.createGroup')

    mutation_groups_updateGroup_parser = mutation_groups_subparsers.add_parser('updateGroup', 
            help='updateGroup() groups operation', 
            usage=get_help("mutation_groups_updateGroup"))

    mutation_groups_updateGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_groups_updateGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_groups_updateGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_groups_updateGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_groups_updateGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_groups_updateGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_groups_updateGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_groups_updateGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_groups_updateGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_groups_updateGroup_parser.set_defaults(func=createRequest,operation_name='mutation.groups.updateGroup')

    mutation_groups_deleteGroup_parser = mutation_groups_subparsers.add_parser('deleteGroup', 
            help='deleteGroup() groups operation', 
            usage=get_help("mutation_groups_deleteGroup"))

    mutation_groups_deleteGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_groups_deleteGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_groups_deleteGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_groups_deleteGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_groups_deleteGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_groups_deleteGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_groups_deleteGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_groups_deleteGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_groups_deleteGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_groups_deleteGroup_parser.set_defaults(func=createRequest,operation_name='mutation.groups.deleteGroup')
