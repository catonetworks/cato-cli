
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_site_parse(query_subparsers):
    query_site_parser = query_subparsers.add_parser('site', 
            help='site() query operation', 
            usage=get_help("query_site"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_site_help(args, configuration=None):
        """Show help when query_site is called without subcommand"""
        print("\ncatocli query site <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  secondaryAwsVSocket            secondaryAwsVSocket operation\n  secondaryAzureVSocket          secondaryAzureVSocket operation\n  knownHostList                  knownHostList operation\n  cloudInterconnectPhysicalConnection cloudInterconnectPhysicalConnection operation\n  cloudInterconnectPhysicalConnectionId cloudInterconnectPhysicalConnectionId operation\n  cloudInterconnectConnectionConnectivity cloudInterconnectConnectionConnectivity operation\n  retrieveUsedVlanIDs            retrieveUsedVlanIDs operation\n  availableVersionList           availableVersionList operation\n  wifiSsid                       wifiSsid operation\n  wifiSsidList                   wifiSsidList operation\n  ... and 18 more")
        print("\nFor help on a specific subcommand:")
        print("  catocli query site <subcommand> -h")
        return None

    query_site_subparsers = query_site_parser.add_subparsers()
    query_site_parser.set_defaults(func=_show_query_site_help)

    query_site_secondaryAwsVSocket_parser = query_site_subparsers.add_parser('secondaryAwsVSocket', 
            help='secondaryAwsVSocket() site operation', 
            usage=get_help("query_site_secondaryAwsVSocket"))

    query_site_secondaryAwsVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_secondaryAwsVSocket_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_secondaryAwsVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_secondaryAwsVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_secondaryAwsVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_secondaryAwsVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_secondaryAwsVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_secondaryAwsVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_secondaryAwsVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_secondaryAwsVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_secondaryAwsVSocket_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_secondaryAwsVSocket_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_secondaryAwsVSocket_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_secondaryAwsVSocket_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_secondaryAwsVSocket_parser.set_defaults(func=createRequest,operation_name='query.site.secondaryAwsVSocket')

    query_site_secondaryAzureVSocket_parser = query_site_subparsers.add_parser('secondaryAzureVSocket', 
            help='secondaryAzureVSocket() site operation', 
            usage=get_help("query_site_secondaryAzureVSocket"))

    query_site_secondaryAzureVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_secondaryAzureVSocket_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_secondaryAzureVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_secondaryAzureVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_secondaryAzureVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_secondaryAzureVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_secondaryAzureVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_secondaryAzureVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_secondaryAzureVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_secondaryAzureVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_secondaryAzureVSocket_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_secondaryAzureVSocket_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_secondaryAzureVSocket_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_secondaryAzureVSocket_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_secondaryAzureVSocket_parser.set_defaults(func=createRequest,operation_name='query.site.secondaryAzureVSocket')

    query_site_knownHostList_parser = query_site_subparsers.add_parser('knownHostList', 
            help='knownHostList() site operation', 
            usage=get_help("query_site_knownHostList"))

    query_site_knownHostList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_knownHostList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_knownHostList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_knownHostList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_knownHostList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_knownHostList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_knownHostList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_knownHostList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_knownHostList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_knownHostList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_knownHostList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_knownHostList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_knownHostList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_knownHostList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_knownHostList_parser.set_defaults(func=createRequest,operation_name='query.site.knownHostList')

    query_site_cloudInterconnectPhysicalConnection_parser = query_site_subparsers.add_parser('cloudInterconnectPhysicalConnection', 
            help='cloudInterconnectPhysicalConnection() site operation', 
            usage=get_help("query_site_cloudInterconnectPhysicalConnection"))

    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_cloudInterconnectPhysicalConnection_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_cloudInterconnectPhysicalConnection_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectPhysicalConnection')

    query_site_cloudInterconnectPhysicalConnectionId_parser = query_site_subparsers.add_parser('cloudInterconnectPhysicalConnectionId', 
            help='cloudInterconnectPhysicalConnectionId() site operation', 
            usage=get_help("query_site_cloudInterconnectPhysicalConnectionId"))

    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_cloudInterconnectPhysicalConnectionId_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_cloudInterconnectPhysicalConnectionId_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectPhysicalConnectionId')

    query_site_cloudInterconnectConnectionConnectivity_parser = query_site_subparsers.add_parser('cloudInterconnectConnectionConnectivity', 
            help='cloudInterconnectConnectionConnectivity() site operation', 
            usage=get_help("query_site_cloudInterconnectConnectionConnectivity"))

    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_cloudInterconnectConnectionConnectivity_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_cloudInterconnectConnectionConnectivity_parser.set_defaults(func=createRequest,operation_name='query.site.cloudInterconnectConnectionConnectivity')

    query_site_retrieveUsedVlanIDs_parser = query_site_subparsers.add_parser('retrieveUsedVlanIDs', 
            help='retrieveUsedVlanIDs() site operation', 
            usage=get_help("query_site_retrieveUsedVlanIDs"))

    query_site_retrieveUsedVlanIDs_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_retrieveUsedVlanIDs_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_retrieveUsedVlanIDs_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_retrieveUsedVlanIDs_parser.set_defaults(func=createRequest,operation_name='query.site.retrieveUsedVlanIDs')

    query_site_availableVersionList_parser = query_site_subparsers.add_parser('availableVersionList', 
            help='availableVersionList() site operation', 
            usage=get_help("query_site_availableVersionList"))

    query_site_availableVersionList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_availableVersionList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_availableVersionList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_availableVersionList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_availableVersionList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_availableVersionList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_availableVersionList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_availableVersionList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_availableVersionList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_availableVersionList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_availableVersionList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_availableVersionList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_availableVersionList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_availableVersionList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_availableVersionList_parser.set_defaults(func=createRequest,operation_name='query.site.availableVersionList')

    query_site_wifiSsid_parser = query_site_subparsers.add_parser('wifiSsid', 
            help='wifiSsid() site operation', 
            usage=get_help("query_site_wifiSsid"))

    query_site_wifiSsid_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_wifiSsid_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_wifiSsid_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_wifiSsid_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_wifiSsid_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_wifiSsid_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_wifiSsid_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_wifiSsid_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_wifiSsid_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_wifiSsid_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_wifiSsid_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_wifiSsid_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_wifiSsid_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_wifiSsid_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_wifiSsid_parser.set_defaults(func=createRequest,operation_name='query.site.wifiSsid')

    query_site_wifiSsidList_parser = query_site_subparsers.add_parser('wifiSsidList', 
            help='wifiSsidList() site operation', 
            usage=get_help("query_site_wifiSsidList"))

    query_site_wifiSsidList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_wifiSsidList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_wifiSsidList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_wifiSsidList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_wifiSsidList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_wifiSsidList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_wifiSsidList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_wifiSsidList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_wifiSsidList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_wifiSsidList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_wifiSsidList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_wifiSsidList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_wifiSsidList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_wifiSsidList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_wifiSsidList_parser.set_defaults(func=createRequest,operation_name='query.site.wifiSsidList')

    query_site_siteSocketConfiguration_parser = query_site_subparsers.add_parser('siteSocketConfiguration', 
            help='siteSocketConfiguration() site operation', 
            usage=get_help("query_site_siteSocketConfiguration"))

    query_site_siteSocketConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteSocketConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_siteSocketConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteSocketConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteSocketConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteSocketConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteSocketConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteSocketConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteSocketConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteSocketConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteSocketConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_siteSocketConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_siteSocketConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_siteSocketConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_siteSocketConfiguration_parser.set_defaults(func=createRequest,operation_name='query.site.siteSocketConfiguration')

    query_site_secondaryGcpVSocket_parser = query_site_subparsers.add_parser('secondaryGcpVSocket', 
            help='secondaryGcpVSocket() site operation', 
            usage=get_help("query_site_secondaryGcpVSocket"))

    query_site_secondaryGcpVSocket_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_secondaryGcpVSocket_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_secondaryGcpVSocket_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_secondaryGcpVSocket_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_secondaryGcpVSocket_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_secondaryGcpVSocket_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_secondaryGcpVSocket_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_secondaryGcpVSocket_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_secondaryGcpVSocket_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_secondaryGcpVSocket_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_secondaryGcpVSocket_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_secondaryGcpVSocket_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_secondaryGcpVSocket_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_secondaryGcpVSocket_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_secondaryGcpVSocket_parser.set_defaults(func=createRequest,operation_name='query.site.secondaryGcpVSocket')

    query_site_wifiRadioProfile_parser = query_site_subparsers.add_parser('wifiRadioProfile', 
            help='wifiRadioProfile() site operation', 
            usage=get_help("query_site_wifiRadioProfile"))

    query_site_wifiRadioProfile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_wifiRadioProfile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_wifiRadioProfile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_wifiRadioProfile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_wifiRadioProfile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_wifiRadioProfile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_wifiRadioProfile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_wifiRadioProfile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_wifiRadioProfile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_wifiRadioProfile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_wifiRadioProfile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_wifiRadioProfile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_wifiRadioProfile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_wifiRadioProfile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_wifiRadioProfile_parser.set_defaults(func=createRequest,operation_name='query.site.wifiRadioProfile')

    query_site_wifiRadioProfileBySite_parser = query_site_subparsers.add_parser('wifiRadioProfileBySite', 
            help='wifiRadioProfileBySite() site operation', 
            usage=get_help("query_site_wifiRadioProfileBySite"))

    query_site_wifiRadioProfileBySite_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_wifiRadioProfileBySite_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_wifiRadioProfileBySite_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_wifiRadioProfileBySite_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_wifiRadioProfileBySite_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_wifiRadioProfileBySite_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_wifiRadioProfileBySite_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_wifiRadioProfileBySite_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_wifiRadioProfileBySite_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_wifiRadioProfileBySite_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_wifiRadioProfileBySite_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_wifiRadioProfileBySite_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_wifiRadioProfileBySite_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_wifiRadioProfileBySite_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_wifiRadioProfileBySite_parser.set_defaults(func=createRequest,operation_name='query.site.wifiRadioProfileBySite')

    query_site_wifiRadioProfileList_parser = query_site_subparsers.add_parser('wifiRadioProfileList', 
            help='wifiRadioProfileList() site operation', 
            usage=get_help("query_site_wifiRadioProfileList"))

    query_site_wifiRadioProfileList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_wifiRadioProfileList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_wifiRadioProfileList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_wifiRadioProfileList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_wifiRadioProfileList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_wifiRadioProfileList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_wifiRadioProfileList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_wifiRadioProfileList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_wifiRadioProfileList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_wifiRadioProfileList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_wifiRadioProfileList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_wifiRadioProfileList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_wifiRadioProfileList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_wifiRadioProfileList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_wifiRadioProfileList_parser.set_defaults(func=createRequest,operation_name='query.site.wifiRadioProfileList')

    query_site_validateWifiRadioProfile_parser = query_site_subparsers.add_parser('validateWifiRadioProfile', 
            help='validateWifiRadioProfile() site operation', 
            usage=get_help("query_site_validateWifiRadioProfile"))

    query_site_validateWifiRadioProfile_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_validateWifiRadioProfile_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_validateWifiRadioProfile_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_validateWifiRadioProfile_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_validateWifiRadioProfile_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_validateWifiRadioProfile_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_validateWifiRadioProfile_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_validateWifiRadioProfile_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_validateWifiRadioProfile_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_validateWifiRadioProfile_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_validateWifiRadioProfile_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_validateWifiRadioProfile_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_validateWifiRadioProfile_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_validateWifiRadioProfile_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_validateWifiRadioProfile_parser.set_defaults(func=createRequest,operation_name='query.site.validateWifiRadioProfile')

    query_site_validateWifiRadioProfileByCountry_parser = query_site_subparsers.add_parser('validateWifiRadioProfileByCountry', 
            help='validateWifiRadioProfileByCountry() site operation', 
            usage=get_help("query_site_validateWifiRadioProfileByCountry"))

    query_site_validateWifiRadioProfileByCountry_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_validateWifiRadioProfileByCountry_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_validateWifiRadioProfileByCountry_parser.set_defaults(func=createRequest,operation_name='query.site.validateWifiRadioProfileByCountry')

    query_site_validWifiRadioSettings_parser = query_site_subparsers.add_parser('validWifiRadioSettings', 
            help='validWifiRadioSettings() site operation', 
            usage=get_help("query_site_validWifiRadioSettings"))

    query_site_validWifiRadioSettings_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_validWifiRadioSettings_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_validWifiRadioSettings_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_validWifiRadioSettings_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_validWifiRadioSettings_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_validWifiRadioSettings_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_validWifiRadioSettings_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_validWifiRadioSettings_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_validWifiRadioSettings_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_validWifiRadioSettings_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_validWifiRadioSettings_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_validWifiRadioSettings_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_validWifiRadioSettings_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_validWifiRadioSettings_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_validWifiRadioSettings_parser.set_defaults(func=createRequest,operation_name='query.site.validWifiRadioSettings')

    query_site_validWifiRadioSettingsByCountry_parser = query_site_subparsers.add_parser('validWifiRadioSettingsByCountry', 
            help='validWifiRadioSettingsByCountry() site operation', 
            usage=get_help("query_site_validWifiRadioSettingsByCountry"))

    query_site_validWifiRadioSettingsByCountry_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_validWifiRadioSettingsByCountry_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_validWifiRadioSettingsByCountry_parser.set_defaults(func=createRequest,operation_name='query.site.validWifiRadioSettingsByCountry')

    query_site_networkRange_parser = query_site_subparsers.add_parser('networkRange', 
            help='networkRange() site operation', 
            usage=get_help("query_site_networkRange"))

    query_site_networkRange_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_networkRange_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_networkRange_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_networkRange_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_networkRange_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_networkRange_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_networkRange_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_networkRange_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_networkRange_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_networkRange_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_networkRange_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_networkRange_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_networkRange_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_networkRange_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_networkRange_parser.set_defaults(func=createRequest,operation_name='query.site.networkRange')

    query_site_networkRangeList_parser = query_site_subparsers.add_parser('networkRangeList', 
            help='networkRangeList() site operation', 
            usage=get_help("query_site_networkRangeList"))

    query_site_networkRangeList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_networkRangeList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_networkRangeList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_networkRangeList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_networkRangeList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_networkRangeList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_networkRangeList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_networkRangeList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_networkRangeList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_networkRangeList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_networkRangeList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_networkRangeList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_networkRangeList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_networkRangeList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_networkRangeList_parser.set_defaults(func=createRequest,operation_name='query.site.networkRangeList')

    query_site_staticHost_parser = query_site_subparsers.add_parser('staticHost', 
            help='staticHost() site operation', 
            usage=get_help("query_site_staticHost"))

    query_site_staticHost_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_staticHost_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_staticHost_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_staticHost_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_staticHost_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_staticHost_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_staticHost_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_staticHost_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_staticHost_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_staticHost_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_staticHost_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_staticHost_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_staticHost_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_staticHost_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_staticHost_parser.set_defaults(func=createRequest,operation_name='query.site.staticHost')

    query_site_staticHostList_parser = query_site_subparsers.add_parser('staticHostList', 
            help='staticHostList() site operation', 
            usage=get_help("query_site_staticHostList"))

    query_site_staticHostList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_staticHostList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_staticHostList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_staticHostList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_staticHostList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_staticHostList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_staticHostList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_staticHostList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_staticHostList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_staticHostList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_staticHostList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_staticHostList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_staticHostList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_staticHostList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_staticHostList_parser.set_defaults(func=createRequest,operation_name='query.site.staticHostList')

    query_site_siteGeneralDetails_parser = query_site_subparsers.add_parser('siteGeneralDetails', 
            help='siteGeneralDetails() site operation', 
            usage=get_help("query_site_siteGeneralDetails"))

    query_site_siteGeneralDetails_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteGeneralDetails_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_siteGeneralDetails_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteGeneralDetails_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteGeneralDetails_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteGeneralDetails_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteGeneralDetails_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteGeneralDetails_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_siteGeneralDetails_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_siteGeneralDetails_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_siteGeneralDetails_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_siteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='query.site.siteGeneralDetails')

    query_site_bgpPeer_parser = query_site_subparsers.add_parser('bgpPeer', 
            help='bgpPeer() site operation', 
            usage=get_help("query_site_bgpPeer"))

    query_site_bgpPeer_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_bgpPeer_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_bgpPeer_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_bgpPeer_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_bgpPeer_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_bgpPeer_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_bgpPeer_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_bgpPeer_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_bgpPeer_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_bgpPeer_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_bgpPeer_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_bgpPeer_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_bgpPeer_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_bgpPeer_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_bgpPeer_parser.set_defaults(func=createRequest,operation_name='query.site.bgpPeer')

    query_site_bgpPeerList_parser = query_site_subparsers.add_parser('bgpPeerList', 
            help='bgpPeerList() site operation', 
            usage=get_help("query_site_bgpPeerList"))

    query_site_bgpPeerList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_bgpPeerList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_bgpPeerList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_bgpPeerList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_bgpPeerList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_bgpPeerList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_bgpPeerList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_bgpPeerList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_bgpPeerList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_bgpPeerList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_bgpPeerList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_bgpPeerList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_bgpPeerList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_bgpPeerList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_bgpPeerList_parser.set_defaults(func=createRequest,operation_name='query.site.bgpPeerList')

    query_site_siteBgpStatus_parser = query_site_subparsers.add_parser('siteBgpStatus', 
            help='siteBgpStatus() site operation', 
            usage=get_help("query_site_siteBgpStatus"))

    query_site_siteBgpStatus_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteBgpStatus_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_siteBgpStatus_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteBgpStatus_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteBgpStatus_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteBgpStatus_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteBgpStatus_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteBgpStatus_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteBgpStatus_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteBgpStatus_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteBgpStatus_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_siteBgpStatus_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_siteBgpStatus_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_siteBgpStatus_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_siteBgpStatus_parser.set_defaults(func=createRequest,operation_name='query.site.siteBgpStatus')

    query_site_siteBackhauling_parser = query_site_subparsers.add_parser('siteBackhauling', 
            help='siteBackhauling() site operation', 
            usage=get_help("query_site_siteBackhauling"))

    query_site_siteBackhauling_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_site_siteBackhauling_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_site_siteBackhauling_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_site_siteBackhauling_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_site_siteBackhauling_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_site_siteBackhauling_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_site_siteBackhauling_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_site_siteBackhauling_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_site_siteBackhauling_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_site_siteBackhauling_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_site_siteBackhauling_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_site_siteBackhauling_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_site_siteBackhauling_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_site_siteBackhauling_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_site_siteBackhauling_parser.set_defaults(func=createRequest,operation_name='query.site.siteBackhauling')
