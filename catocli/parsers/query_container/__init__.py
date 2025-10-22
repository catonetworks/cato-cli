
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_container_parse(query_subparsers):
    query_container_parser = query_subparsers.add_parser('container', 
            help='container() query operation', 
            usage=get_help("query_container"), formatter_class=CustomSubparserHelpFormatter)

    query_container_subparsers = query_container_parser.add_subparsers()

    query_container_list_parser = query_container_subparsers.add_parser('list', 
            help='list() container operation', 
            usage=get_help("query_container_list"))

    query_container_list_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_list_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_list_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_list_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_list_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_list_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_list_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_list_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_list_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_list_parser.set_defaults(func=createRequest,operation_name='query.container.list')

    query_container_ipAddressRange_parser = query_container_subparsers.add_parser('ipAddressRange', 
            help='ipAddressRange() container operation', 
            usage=get_help("query_container_ipAddressRange"))

    query_container_ipAddressRange_subparsers = query_container_ipAddressRange_parser.add_subparsers()

    query_container_ipAddressRange_search_parser = query_container_ipAddressRange_subparsers.add_parser('search', 
            help='search() ipAddressRange operation', 
            usage=get_help("query_container_ipAddressRange_search"))

    query_container_ipAddressRange_search_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_ipAddressRange_search_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_ipAddressRange_search_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_ipAddressRange_search_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_ipAddressRange_search_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_ipAddressRange_search_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_ipAddressRange_search_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_ipAddressRange_search_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_ipAddressRange_search_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_ipAddressRange_search_parser.set_defaults(func=createRequest,operation_name='query.container.ipAddressRange.search')

    query_container_ipAddressRange_searchIpAddressRange_parser = query_container_ipAddressRange_subparsers.add_parser('searchIpAddressRange', 
            help='searchIpAddressRange() ipAddressRange operation', 
            usage=get_help("query_container_ipAddressRange_searchIpAddressRange"))

    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_ipAddressRange_searchIpAddressRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_ipAddressRange_searchIpAddressRange_parser.set_defaults(func=createRequest,operation_name='query.container.ipAddressRange.searchIpAddressRange')

    query_container_ipAddressRange_downloadFile_parser = query_container_ipAddressRange_subparsers.add_parser('downloadFile', 
            help='downloadFile() ipAddressRange operation', 
            usage=get_help("query_container_ipAddressRange_downloadFile"))

    query_container_ipAddressRange_downloadFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_ipAddressRange_downloadFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_ipAddressRange_downloadFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_ipAddressRange_downloadFile_parser.set_defaults(func=createRequest,operation_name='query.container.ipAddressRange.downloadFile')

    query_container_fqdn_parser = query_container_subparsers.add_parser('fqdn', 
            help='fqdn() container operation', 
            usage=get_help("query_container_fqdn"))

    query_container_fqdn_subparsers = query_container_fqdn_parser.add_subparsers()

    query_container_fqdn_search_parser = query_container_fqdn_subparsers.add_parser('search', 
            help='search() fqdn operation', 
            usage=get_help("query_container_fqdn_search"))

    query_container_fqdn_search_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_fqdn_search_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_fqdn_search_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_fqdn_search_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_fqdn_search_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_fqdn_search_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_fqdn_search_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_fqdn_search_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_fqdn_search_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_fqdn_search_parser.set_defaults(func=createRequest,operation_name='query.container.fqdn.search')

    query_container_fqdn_searchFqdn_parser = query_container_fqdn_subparsers.add_parser('searchFqdn', 
            help='searchFqdn() fqdn operation', 
            usage=get_help("query_container_fqdn_searchFqdn"))

    query_container_fqdn_searchFqdn_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_fqdn_searchFqdn_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_fqdn_searchFqdn_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_fqdn_searchFqdn_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_fqdn_searchFqdn_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_fqdn_searchFqdn_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_fqdn_searchFqdn_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_fqdn_searchFqdn_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_fqdn_searchFqdn_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_fqdn_searchFqdn_parser.set_defaults(func=createRequest,operation_name='query.container.fqdn.searchFqdn')

    query_container_fqdn_downloadFile_parser = query_container_fqdn_subparsers.add_parser('downloadFile', 
            help='downloadFile() fqdn operation', 
            usage=get_help("query_container_fqdn_downloadFile"))

    query_container_fqdn_downloadFile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_container_fqdn_downloadFile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_container_fqdn_downloadFile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_container_fqdn_downloadFile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_container_fqdn_downloadFile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_container_fqdn_downloadFile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_container_fqdn_downloadFile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_container_fqdn_downloadFile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_container_fqdn_downloadFile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_container_fqdn_downloadFile_parser.set_defaults(func=createRequest,operation_name='query.container.fqdn.downloadFile')
