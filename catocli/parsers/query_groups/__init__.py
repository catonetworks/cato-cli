
from ..customParserApiClient import createRequest, get_help

def query_groups_parse(query_subparsers):
    query_groups_parser = query_subparsers.add_parser('groups', 
            help='groups() query operation', 
            usage=get_help("query_groups"))

    query_groups_subparsers = query_groups_parser.add_subparsers()

    query_groups_group_parser = query_groups_subparsers.add_parser('group', 
            help='group() groups operation', 
            usage=get_help("query_groups_group"))

    query_groups_group_subparsers = query_groups_group_parser.add_subparsers()

    query_groups_group_members_parser = query_groups_group_subparsers.add_parser('members', 
            help='members() group operation', 
            usage=get_help("query_groups_group_members"))

    query_groups_group_members_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_groups_group_members_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_groups_group_members_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_groups_group_members_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_groups_group_members_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_groups_group_members_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_groups_group_members_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_groups_group_members_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_groups_group_members_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_groups_group_members_parser.set_defaults(func=createRequest,operation_name='query.groups.group.members')

    query_groups_whereUsed_parser = query_groups_subparsers.add_parser('whereUsed', 
            help='whereUsed() groups operation', 
            usage=get_help("query_groups_whereUsed"))

    query_groups_whereUsed_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_groups_whereUsed_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_groups_whereUsed_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_groups_whereUsed_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_groups_whereUsed_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_groups_whereUsed_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_groups_whereUsed_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_groups_whereUsed_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_groups_whereUsed_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_groups_whereUsed_parser.set_defaults(func=createRequest,operation_name='query.groups.whereUsed')

    query_groups_groupList_parser = query_groups_subparsers.add_parser('groupList', 
            help='groupList() groups operation', 
            usage=get_help("query_groups_groupList"))

    query_groups_groupList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_groups_groupList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_groups_groupList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_groups_groupList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_groups_groupList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_groups_groupList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_groups_groupList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_groups_groupList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_groups_groupList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_groups_groupList_parser.set_defaults(func=createRequest,operation_name='query.groups.groupList')
