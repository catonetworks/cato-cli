
from ..customParserApiClient import createRequest, get_help

def query_policy_parse(query_subparsers):
    query_policy_parser = query_subparsers.add_parser('policy', 
            help='policy() query operation', 
            usage=get_help("query_policy"))

    query_policy_subparsers = query_policy_parser.add_subparsers()

    query_policy_antiMalwareFileHash_parser = query_policy_subparsers.add_parser('antiMalwareFileHash', 
            help='antiMalwareFileHash() policy operation', 
            usage=get_help("query_policy_antiMalwareFileHash"))

    query_policy_antiMalwareFileHash_subparsers = query_policy_antiMalwareFileHash_parser.add_subparsers()

    query_policy_antiMalwareFileHash_policy_parser = query_policy_antiMalwareFileHash_subparsers.add_parser('policy', 
            help='policy() antiMalwareFileHash operation', 
            usage=get_help("query_policy_antiMalwareFileHash_policy"))

    query_policy_antiMalwareFileHash_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_antiMalwareFileHash_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.antiMalwareFileHash.policy')

    query_policy_dynamicIpAllocation_parser = query_policy_subparsers.add_parser('dynamicIpAllocation', 
            help='dynamicIpAllocation() policy operation', 
            usage=get_help("query_policy_dynamicIpAllocation"))

    query_policy_dynamicIpAllocation_subparsers = query_policy_dynamicIpAllocation_parser.add_subparsers()

    query_policy_dynamicIpAllocation_policy_parser = query_policy_dynamicIpAllocation_subparsers.add_parser('policy', 
            help='policy() dynamicIpAllocation operation', 
            usage=get_help("query_policy_dynamicIpAllocation_policy"))

    query_policy_dynamicIpAllocation_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_dynamicIpAllocation_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.dynamicIpAllocation.policy')

    query_policy_socketLan_parser = query_policy_subparsers.add_parser('socketLan', 
            help='socketLan() policy operation', 
            usage=get_help("query_policy_socketLan"))

    query_policy_socketLan_subparsers = query_policy_socketLan_parser.add_subparsers()

    query_policy_socketLan_policy_parser = query_policy_socketLan_subparsers.add_parser('policy', 
            help='policy() socketLan operation', 
            usage=get_help("query_policy_socketLan_policy"))

    query_policy_socketLan_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_socketLan_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_socketLan_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_socketLan_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_socketLan_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_socketLan_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_socketLan_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_socketLan_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_socketLan_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_socketLan_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.socketLan.policy')

    query_policy_terminalServer_parser = query_policy_subparsers.add_parser('terminalServer', 
            help='terminalServer() policy operation', 
            usage=get_help("query_policy_terminalServer"))

    query_policy_terminalServer_subparsers = query_policy_terminalServer_parser.add_subparsers()

    query_policy_terminalServer_policy_parser = query_policy_terminalServer_subparsers.add_parser('policy', 
            help='policy() terminalServer operation', 
            usage=get_help("query_policy_terminalServer_policy"))

    query_policy_terminalServer_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_terminalServer_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_terminalServer_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_terminalServer_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_terminalServer_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_terminalServer_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_terminalServer_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_terminalServer_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_terminalServer_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_terminalServer_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.terminalServer.policy')

    query_policy_wanNetwork_parser = query_policy_subparsers.add_parser('wanNetwork', 
            help='wanNetwork() policy operation', 
            usage=get_help("query_policy_wanNetwork"))

    query_policy_wanNetwork_subparsers = query_policy_wanNetwork_parser.add_subparsers()

    query_policy_wanNetwork_policy_parser = query_policy_wanNetwork_subparsers.add_parser('policy', 
            help='policy() wanNetwork operation', 
            usage=get_help("query_policy_wanNetwork_policy"))

    query_policy_wanNetwork_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_wanNetwork_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_wanNetwork_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_wanNetwork_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_wanNetwork_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_wanNetwork_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_wanNetwork_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_wanNetwork_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_wanNetwork_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_wanNetwork_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.wanNetwork.policy')

    query_policy_internetFirewall_parser = query_policy_subparsers.add_parser('internetFirewall', 
            help='internetFirewall() policy operation', 
            usage=get_help("query_policy_internetFirewall"))

    query_policy_internetFirewall_subparsers = query_policy_internetFirewall_parser.add_subparsers()

    query_policy_internetFirewall_policy_parser = query_policy_internetFirewall_subparsers.add_parser('policy', 
            help='policy() internetFirewall operation', 
            usage=get_help("query_policy_internetFirewall_policy"))

    query_policy_internetFirewall_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_internetFirewall_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_internetFirewall_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_internetFirewall_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_internetFirewall_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_internetFirewall_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_internetFirewall_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_internetFirewall_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_internetFirewall_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_internetFirewall_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.internetFirewall.policy')

    query_policy_remotePortFwd_parser = query_policy_subparsers.add_parser('remotePortFwd', 
            help='remotePortFwd() policy operation', 
            usage=get_help("query_policy_remotePortFwd"))

    query_policy_remotePortFwd_subparsers = query_policy_remotePortFwd_parser.add_subparsers()

    query_policy_remotePortFwd_policy_parser = query_policy_remotePortFwd_subparsers.add_parser('policy', 
            help='policy() remotePortFwd operation', 
            usage=get_help("query_policy_remotePortFwd_policy"))

    query_policy_remotePortFwd_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_remotePortFwd_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_remotePortFwd_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_remotePortFwd_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_remotePortFwd_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_remotePortFwd_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_remotePortFwd_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_remotePortFwd_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_remotePortFwd_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_remotePortFwd_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.remotePortFwd.policy')

    query_policy_wanFirewall_parser = query_policy_subparsers.add_parser('wanFirewall', 
            help='wanFirewall() policy operation', 
            usage=get_help("query_policy_wanFirewall"))

    query_policy_wanFirewall_subparsers = query_policy_wanFirewall_parser.add_subparsers()

    query_policy_wanFirewall_policy_parser = query_policy_wanFirewall_subparsers.add_parser('policy', 
            help='policy() wanFirewall operation', 
            usage=get_help("query_policy_wanFirewall_policy"))

    query_policy_wanFirewall_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_wanFirewall_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_wanFirewall_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_wanFirewall_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_wanFirewall_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_wanFirewall_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_wanFirewall_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_wanFirewall_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_wanFirewall_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_wanFirewall_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.wanFirewall.policy')

    query_policy_appTenantRestriction_parser = query_policy_subparsers.add_parser('appTenantRestriction', 
            help='appTenantRestriction() policy operation', 
            usage=get_help("query_policy_appTenantRestriction"))

    query_policy_appTenantRestriction_subparsers = query_policy_appTenantRestriction_parser.add_subparsers()

    query_policy_appTenantRestriction_policy_parser = query_policy_appTenantRestriction_subparsers.add_parser('policy', 
            help='policy() appTenantRestriction operation', 
            usage=get_help("query_policy_appTenantRestriction_policy"))

    query_policy_appTenantRestriction_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_appTenantRestriction_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_appTenantRestriction_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_appTenantRestriction_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_appTenantRestriction_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_appTenantRestriction_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_appTenantRestriction_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_appTenantRestriction_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_appTenantRestriction_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.appTenantRestriction.policy')

    query_policy_applicationControl_parser = query_policy_subparsers.add_parser('applicationControl', 
            help='applicationControl() policy operation', 
            usage=get_help("query_policy_applicationControl"))

    query_policy_applicationControl_subparsers = query_policy_applicationControl_parser.add_subparsers()

    query_policy_applicationControl_policy_parser = query_policy_applicationControl_subparsers.add_parser('policy', 
            help='policy() applicationControl operation', 
            usage=get_help("query_policy_applicationControl_policy"))

    query_policy_applicationControl_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_applicationControl_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_applicationControl_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_applicationControl_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_applicationControl_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_applicationControl_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_applicationControl_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_applicationControl_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_applicationControl_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_applicationControl_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.applicationControl.policy')

    query_policy_tlsInspect_parser = query_policy_subparsers.add_parser('tlsInspect', 
            help='tlsInspect() policy operation', 
            usage=get_help("query_policy_tlsInspect"))

    query_policy_tlsInspect_subparsers = query_policy_tlsInspect_parser.add_subparsers()

    query_policy_tlsInspect_policy_parser = query_policy_tlsInspect_subparsers.add_parser('policy', 
            help='policy() tlsInspect operation', 
            usage=get_help("query_policy_tlsInspect_policy"))

    query_policy_tlsInspect_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_tlsInspect_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_tlsInspect_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_tlsInspect_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_tlsInspect_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_tlsInspect_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_tlsInspect_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_tlsInspect_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_tlsInspect_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_tlsInspect_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.tlsInspect.policy')
