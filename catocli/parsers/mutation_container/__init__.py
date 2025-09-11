
from ..customParserApiClient import createRequest, get_help

def mutation_container_parse(mutation_subparsers):
    mutation_container_parser = mutation_subparsers.add_parser('container', 
            help='container() mutation operation', 
            usage=get_help("mutation_container"))

    mutation_container_subparsers = mutation_container_parser.add_subparsers()

    mutation_container_ipAddressRange_parser = mutation_container_subparsers.add_parser('ipAddressRange', 
            help='ipAddressRange() container operation', 
            usage=get_help("mutation_container_ipAddressRange"))

    mutation_container_ipAddressRange_subparsers = mutation_container_ipAddressRange_parser.add_subparsers()

    mutation_container_ipAddressRange_createFromFile_parser = mutation_container_ipAddressRange_subparsers.add_parser('createFromFile', 
            help='createFromFile() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_createFromFile"))

    mutation_container_ipAddressRange_createFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_createFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_createFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.createFromFile')

    mutation_container_ipAddressRange_updateFromFile_parser = mutation_container_ipAddressRange_subparsers.add_parser('updateFromFile', 
            help='updateFromFile() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_updateFromFile"))

    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_updateFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_updateFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.updateFromFile')

    mutation_container_ipAddressRange_addValues_parser = mutation_container_ipAddressRange_subparsers.add_parser('addValues', 
            help='addValues() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_addValues"))

    mutation_container_ipAddressRange_addValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_addValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_addValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_addValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.addValues')

    mutation_container_ipAddressRange_removeValues_parser = mutation_container_ipAddressRange_subparsers.add_parser('removeValues', 
            help='removeValues() ipAddressRange operation', 
            usage=get_help("mutation_container_ipAddressRange_removeValues"))

    mutation_container_ipAddressRange_removeValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_ipAddressRange_removeValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_ipAddressRange_removeValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.ipAddressRange.removeValues')

    mutation_container_fqdn_parser = mutation_container_subparsers.add_parser('fqdn', 
            help='fqdn() container operation', 
            usage=get_help("mutation_container_fqdn"))

    mutation_container_fqdn_subparsers = mutation_container_fqdn_parser.add_subparsers()

    mutation_container_fqdn_createFromFile_parser = mutation_container_fqdn_subparsers.add_parser('createFromFile', 
            help='createFromFile() fqdn operation', 
            usage=get_help("mutation_container_fqdn_createFromFile"))

    mutation_container_fqdn_createFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_createFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_createFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_createFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_createFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_createFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_createFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_createFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_createFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_createFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.createFromFile')

    mutation_container_fqdn_updateFromFile_parser = mutation_container_fqdn_subparsers.add_parser('updateFromFile', 
            help='updateFromFile() fqdn operation', 
            usage=get_help("mutation_container_fqdn_updateFromFile"))

    mutation_container_fqdn_updateFromFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_updateFromFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_updateFromFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_updateFromFile_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.updateFromFile')

    mutation_container_fqdn_addValues_parser = mutation_container_fqdn_subparsers.add_parser('addValues', 
            help='addValues() fqdn operation', 
            usage=get_help("mutation_container_fqdn_addValues"))

    mutation_container_fqdn_addValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_addValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_addValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_addValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_addValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_addValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_addValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_addValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_addValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_addValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.addValues')

    mutation_container_fqdn_removeValues_parser = mutation_container_fqdn_subparsers.add_parser('removeValues', 
            help='removeValues() fqdn operation', 
            usage=get_help("mutation_container_fqdn_removeValues"))

    mutation_container_fqdn_removeValues_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_fqdn_removeValues_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_fqdn_removeValues_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_fqdn_removeValues_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_fqdn_removeValues_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_fqdn_removeValues_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_fqdn_removeValues_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_fqdn_removeValues_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_fqdn_removeValues_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_fqdn_removeValues_parser.set_defaults(func=createRequest,operation_name='mutation.container.fqdn.removeValues')

    mutation_container_delete_parser = mutation_container_subparsers.add_parser('delete', 
            help='delete() container operation', 
            usage=get_help("mutation_container_delete"))

    mutation_container_delete_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_container_delete_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_container_delete_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_container_delete_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_container_delete_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_container_delete_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_container_delete_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_container_delete_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_container_delete_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_container_delete_parser.set_defaults(func=createRequest,operation_name='mutation.container.delete')
