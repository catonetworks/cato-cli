
from ..customParserApiClient import createRequest, get_help

def mutation_admin_parse(mutation_subparsers):
    mutation_admin_parser = mutation_subparsers.add_parser('admin', 
            help='admin() mutation operation', 
            usage=get_help("mutation_admin"))

    mutation_admin_subparsers = mutation_admin_parser.add_subparsers()

    mutation_admin_addAdmin_parser = mutation_admin_subparsers.add_parser('addAdmin', 
            help='addAdmin() admin operation', 
            usage=get_help("mutation_admin_addAdmin"))

    mutation_admin_addAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_addAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_addAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_addAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_addAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_addAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_addAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_addAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_addAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_addAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.addAdmin')

    mutation_admin_addServicePrincipalAdmin_parser = mutation_admin_subparsers.add_parser('addServicePrincipalAdmin', 
            help='addServicePrincipalAdmin() admin operation', 
            usage=get_help("mutation_admin_addServicePrincipalAdmin"))

    mutation_admin_addServicePrincipalAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_addServicePrincipalAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_addServicePrincipalAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.addServicePrincipalAdmin')

    mutation_admin_removeAdmin_parser = mutation_admin_subparsers.add_parser('removeAdmin', 
            help='removeAdmin() admin operation', 
            usage=get_help("mutation_admin_removeAdmin"))

    mutation_admin_removeAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_removeAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_removeAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_removeAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_removeAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_removeAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_removeAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_removeAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_removeAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_removeAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.removeAdmin')

    mutation_admin_removeServicePrincipalAdmin_parser = mutation_admin_subparsers.add_parser('removeServicePrincipalAdmin', 
            help='removeServicePrincipalAdmin() admin operation', 
            usage=get_help("mutation_admin_removeServicePrincipalAdmin"))

    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_removeServicePrincipalAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_removeServicePrincipalAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.removeServicePrincipalAdmin')

    mutation_admin_updateAdmin_parser = mutation_admin_subparsers.add_parser('updateAdmin', 
            help='updateAdmin() admin operation', 
            usage=get_help("mutation_admin_updateAdmin"))

    mutation_admin_updateAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_updateAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_updateAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_updateAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_updateAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_updateAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_updateAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_updateAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_updateAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_updateAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.updateAdmin')

    mutation_admin_updateServicePrincipalAdmin_parser = mutation_admin_subparsers.add_parser('updateServicePrincipalAdmin', 
            help='updateServicePrincipalAdmin() admin operation', 
            usage=get_help("mutation_admin_updateServicePrincipalAdmin"))

    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_admin_updateServicePrincipalAdmin_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_admin_updateServicePrincipalAdmin_parser.set_defaults(func=createRequest,operation_name='mutation.admin.updateServicePrincipalAdmin')
