
from ..customParserApiClient import createRequest, get_help

def query_site_parse(query_subparsers):
    query_site_parser = query_subparsers.add_parser('site', 
            help='site() query operation', 
            usage=get_help("query_site"))

    query_site_subparsers = query_site_parser.add_subparsers()

    query_site_secondaryAwsVSocket_parser = query_site_subparsers.add_parser('secondaryAwsVSocket', 
            help='secondaryAwsVSocket() site operation', 
            usage=get_help("query_site_secondaryAwsVSocket"))

    query_site_secondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_secondaryAwsVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_secondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_secondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_secondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_secondaryAwsVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_secondaryAwsVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_secondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_secondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_secondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='query.site.secondaryAwsVSocket')

    query_site_secondaryAzureVSocket_parser = query_site_subparsers.add_parser('secondaryAzureVSocket', 
            help='secondaryAzureVSocket() site operation', 
            usage=get_help("query_site_secondaryAzureVSocket"))

    query_site_secondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_secondaryAzureVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_secondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_secondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_secondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_secondaryAzureVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_secondaryAzureVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_secondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_secondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_secondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='query.site.secondaryAzureVSocket')

    query_site_cloudInterconnectPhysicalConnection_parser = query_site_subparsers.add_parser('cloudInterconnectPhysicalConnection', 
            help='cloudInterconnectPhysicalConnection() site operation', 
            usage=get_help("query_site_cloudInterconnectPhysicalConnection"))

    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectPhysicalConnection')

    query_site_cloudInterconnectPhysicalConnectionId_parser = query_site_subparsers.add_parser('cloudInterconnectPhysicalConnectionId', 
            help='cloudInterconnectPhysicalConnectionId() site operation', 
            usage=get_help("query_site_cloudInterconnectPhysicalConnectionId"))

    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectPhysicalConnectionId')

    query_site_cloudInterconnectConnectionConnectivity_parser = query_site_subparsers.add_parser('cloudInterconnectConnectionConnectivity', 
            help='cloudInterconnectConnectionConnectivity() site operation', 
            usage=get_help("query_site_cloudInterconnectConnectionConnectivity"))

    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectConnectionConnectivity_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectConnectionConnectivity')

    query_site_bgpPeer_parser = query_site_subparsers.add_parser('bgpPeer', 
            help='bgpPeer() site operation', 
            usage=get_help("query_site_bgpPeer"))

    query_site_bgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_bgpPeer_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_bgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_bgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_bgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_bgpPeer_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_bgpPeer_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_bgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_bgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_bgpPeer_parser.set_defaults(func=createRequest,operation_name='query.site.bgpPeer')

    query_site_bgpPeerList_parser = query_site_subparsers.add_parser('bgpPeerList', 
            help='bgpPeerList() site operation', 
            usage=get_help("query_site_bgpPeerList"))

    query_site_bgpPeerList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_bgpPeerList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_bgpPeerList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_bgpPeerList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_bgpPeerList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_bgpPeerList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_bgpPeerList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_bgpPeerList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_bgpPeerList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_bgpPeerList_parser.set_defaults(func=createRequest,operation_name='query.site.bgpPeerList')

    query_site_siteBgpStatus_parser = query_site_subparsers.add_parser('siteBgpStatus', 
            help='siteBgpStatus() site operation', 
            usage=get_help("query_site_siteBgpStatus"))

    query_site_siteBgpStatus_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteBgpStatus_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteBgpStatus_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteBgpStatus_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteBgpStatus_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteBgpStatus_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteBgpStatus_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteBgpStatus_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteBgpStatus_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteBgpStatus_parser.set_defaults(func=createRequest,operation_name='query.site.siteBgpStatus')

    query_site_availableVersionList_parser = query_site_subparsers.add_parser('availableVersionList', 
            help='availableVersionList() site operation', 
            usage=get_help("query_site_availableVersionList"))

    query_site_availableVersionList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_availableVersionList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_availableVersionList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_availableVersionList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_availableVersionList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_availableVersionList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_availableVersionList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_availableVersionList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_availableVersionList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_availableVersionList_parser.set_defaults(func=createRequest,operation_name='query.site.availableVersionList')

    query_site_siteGeneralDetails_parser = query_site_subparsers.add_parser('siteGeneralDetails', 
            help='siteGeneralDetails() site operation', 
            usage=get_help("query_site_siteGeneralDetails"))

    query_site_siteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteGeneralDetails_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteGeneralDetails_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteGeneralDetails_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='query.site.siteGeneralDetails')
