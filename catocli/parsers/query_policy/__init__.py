
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_policy_parse(query_subparsers):
    query_policy_parser = query_subparsers.add_parser('policy', 
            help='policy() query operation', 
            usage=get_help("query_policy"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_policy_help(args, configuration=None):
        """Show help when query_policy is called without subcommand"""
        print("\ncatocli query policy <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  antiMalwareFileHash            antiMalwareFileHash operation\n  socketLan                      socketLan operation\n  wanNetwork                     wanNetwork operation\n  internetFirewall               internetFirewall operation\n  remotePortFwd                  remotePortFwd operation\n  wanFirewall                    wanFirewall operation\n  appTenantRestriction           appTenantRestriction operation\n  applicationControl             applicationControl operation\n  tlsInspect                     tlsInspect operation\n  clientConnectivity             clientConnectivity operation\n  ... and 4 more")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy <subcommand> -h")
        return None

    query_policy_subparsers = query_policy_parser.add_subparsers()
    query_policy_parser.set_defaults(func=_show_query_policy_help)

    query_policy_antiMalwareFileHash_parser = query_policy_subparsers.add_parser('antiMalwareFileHash', 
            help='antiMalwareFileHash() policy operation', 
            usage=get_help("query_policy_antiMalwareFileHash"))

    def _show_query_policy_antiMalwareFileHash_help(args, configuration=None):
        """Show help when query_policy_antiMalwareFileHash is called without subcommand"""
        print("\ncatocli query policy antiMalwareFileHash <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy antiMalwareFileHash <subcommand> -h")
        return None

    query_policy_antiMalwareFileHash_subparsers = query_policy_antiMalwareFileHash_parser.add_subparsers()
    query_policy_antiMalwareFileHash_parser.set_defaults(func=_show_query_policy_antiMalwareFileHash_help)

    query_policy_antiMalwareFileHash_policy_parser = query_policy_antiMalwareFileHash_subparsers.add_parser('policy', 
            help='policy() antiMalwareFileHash operation', 
            usage=get_help("query_policy_antiMalwareFileHash_policy"))

    query_policy_antiMalwareFileHash_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_antiMalwareFileHash_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_antiMalwareFileHash_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.antiMalwareFileHash.policy')

    query_policy_socketLan_parser = query_policy_subparsers.add_parser('socketLan', 
            help='socketLan() policy operation', 
            usage=get_help("query_policy_socketLan"))

    def _show_query_policy_socketLan_help(args, configuration=None):
        """Show help when query_policy_socketLan is called without subcommand"""
        print("\ncatocli query policy socketLan <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy socketLan <subcommand> -h")
        return None

    query_policy_socketLan_subparsers = query_policy_socketLan_parser.add_subparsers()
    query_policy_socketLan_parser.set_defaults(func=_show_query_policy_socketLan_help)

    query_policy_socketLan_policy_parser = query_policy_socketLan_subparsers.add_parser('policy', 
            help='policy() socketLan operation', 
            usage=get_help("query_policy_socketLan_policy"))

    query_policy_socketLan_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_socketLan_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_socketLan_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_socketLan_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_socketLan_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_socketLan_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_socketLan_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_socketLan_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_socketLan_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_socketLan_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_socketLan_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_socketLan_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_socketLan_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_socketLan_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_socketLan_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.socketLan.policy')

    query_policy_wanNetwork_parser = query_policy_subparsers.add_parser('wanNetwork', 
            help='wanNetwork() policy operation', 
            usage=get_help("query_policy_wanNetwork"))

    def _show_query_policy_wanNetwork_help(args, configuration=None):
        """Show help when query_policy_wanNetwork is called without subcommand"""
        print("\ncatocli query policy wanNetwork <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy wanNetwork <subcommand> -h")
        return None

    query_policy_wanNetwork_subparsers = query_policy_wanNetwork_parser.add_subparsers()
    query_policy_wanNetwork_parser.set_defaults(func=_show_query_policy_wanNetwork_help)

    query_policy_wanNetwork_policy_parser = query_policy_wanNetwork_subparsers.add_parser('policy', 
            help='policy() wanNetwork operation', 
            usage=get_help("query_policy_wanNetwork_policy"))

    query_policy_wanNetwork_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_wanNetwork_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_wanNetwork_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_wanNetwork_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_wanNetwork_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_wanNetwork_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_wanNetwork_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_wanNetwork_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_wanNetwork_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_wanNetwork_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_wanNetwork_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_wanNetwork_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_wanNetwork_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_wanNetwork_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_wanNetwork_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.wanNetwork.policy')

    query_policy_internetFirewall_parser = query_policy_subparsers.add_parser('internetFirewall', 
            help='internetFirewall() policy operation', 
            usage=get_help("query_policy_internetFirewall"))

    def _show_query_policy_internetFirewall_help(args, configuration=None):
        """Show help when query_policy_internetFirewall is called without subcommand"""
        print("\ncatocli query policy internetFirewall <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation\n  policyList                     policyList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy internetFirewall <subcommand> -h")
        return None

    query_policy_internetFirewall_subparsers = query_policy_internetFirewall_parser.add_subparsers()
    query_policy_internetFirewall_parser.set_defaults(func=_show_query_policy_internetFirewall_help)

    query_policy_internetFirewall_policy_parser = query_policy_internetFirewall_subparsers.add_parser('policy', 
            help='policy() internetFirewall operation', 
            usage=get_help("query_policy_internetFirewall_policy"))

    query_policy_internetFirewall_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_internetFirewall_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_internetFirewall_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_internetFirewall_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_internetFirewall_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_internetFirewall_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_internetFirewall_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_internetFirewall_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_internetFirewall_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_internetFirewall_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_internetFirewall_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_internetFirewall_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_internetFirewall_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_internetFirewall_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_internetFirewall_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.internetFirewall.policy')

    query_policy_internetFirewall_policyList_parser = query_policy_internetFirewall_subparsers.add_parser('policyList', 
            help='policyList() internetFirewall operation', 
            usage=get_help("query_policy_internetFirewall_policyList"))

    query_policy_internetFirewall_policyList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_internetFirewall_policyList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_internetFirewall_policyList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_internetFirewall_policyList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_internetFirewall_policyList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_internetFirewall_policyList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_internetFirewall_policyList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_internetFirewall_policyList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_internetFirewall_policyList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_internetFirewall_policyList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_internetFirewall_policyList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_internetFirewall_policyList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_internetFirewall_policyList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_internetFirewall_policyList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_internetFirewall_policyList_parser.set_defaults(func=createRequest,operation_name='query.policy.internetFirewall.policyList')

    query_policy_remotePortFwd_parser = query_policy_subparsers.add_parser('remotePortFwd', 
            help='remotePortFwd() policy operation', 
            usage=get_help("query_policy_remotePortFwd"))

    def _show_query_policy_remotePortFwd_help(args, configuration=None):
        """Show help when query_policy_remotePortFwd is called without subcommand"""
        print("\ncatocli query policy remotePortFwd <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy remotePortFwd <subcommand> -h")
        return None

    query_policy_remotePortFwd_subparsers = query_policy_remotePortFwd_parser.add_subparsers()
    query_policy_remotePortFwd_parser.set_defaults(func=_show_query_policy_remotePortFwd_help)

    query_policy_remotePortFwd_policy_parser = query_policy_remotePortFwd_subparsers.add_parser('policy', 
            help='policy() remotePortFwd operation', 
            usage=get_help("query_policy_remotePortFwd_policy"))

    query_policy_remotePortFwd_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_remotePortFwd_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_remotePortFwd_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_remotePortFwd_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_remotePortFwd_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_remotePortFwd_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_remotePortFwd_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_remotePortFwd_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_remotePortFwd_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_remotePortFwd_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_remotePortFwd_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_remotePortFwd_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_remotePortFwd_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_remotePortFwd_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_remotePortFwd_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.remotePortFwd.policy')

    query_policy_wanFirewall_parser = query_policy_subparsers.add_parser('wanFirewall', 
            help='wanFirewall() policy operation', 
            usage=get_help("query_policy_wanFirewall"))

    def _show_query_policy_wanFirewall_help(args, configuration=None):
        """Show help when query_policy_wanFirewall is called without subcommand"""
        print("\ncatocli query policy wanFirewall <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation\n  policyList                     policyList operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy wanFirewall <subcommand> -h")
        return None

    query_policy_wanFirewall_subparsers = query_policy_wanFirewall_parser.add_subparsers()
    query_policy_wanFirewall_parser.set_defaults(func=_show_query_policy_wanFirewall_help)

    query_policy_wanFirewall_policy_parser = query_policy_wanFirewall_subparsers.add_parser('policy', 
            help='policy() wanFirewall operation', 
            usage=get_help("query_policy_wanFirewall_policy"))

    query_policy_wanFirewall_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_wanFirewall_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_wanFirewall_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_wanFirewall_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_wanFirewall_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_wanFirewall_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_wanFirewall_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_wanFirewall_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_wanFirewall_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_wanFirewall_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_wanFirewall_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_wanFirewall_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_wanFirewall_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_wanFirewall_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_wanFirewall_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.wanFirewall.policy')

    query_policy_wanFirewall_policyList_parser = query_policy_wanFirewall_subparsers.add_parser('policyList', 
            help='policyList() wanFirewall operation', 
            usage=get_help("query_policy_wanFirewall_policyList"))

    query_policy_wanFirewall_policyList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_wanFirewall_policyList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_wanFirewall_policyList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_wanFirewall_policyList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_wanFirewall_policyList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_wanFirewall_policyList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_wanFirewall_policyList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_wanFirewall_policyList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_wanFirewall_policyList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_wanFirewall_policyList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_wanFirewall_policyList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_wanFirewall_policyList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_wanFirewall_policyList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_wanFirewall_policyList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_wanFirewall_policyList_parser.set_defaults(func=createRequest,operation_name='query.policy.wanFirewall.policyList')

    query_policy_appTenantRestriction_parser = query_policy_subparsers.add_parser('appTenantRestriction', 
            help='appTenantRestriction() policy operation', 
            usage=get_help("query_policy_appTenantRestriction"))

    def _show_query_policy_appTenantRestriction_help(args, configuration=None):
        """Show help when query_policy_appTenantRestriction is called without subcommand"""
        print("\ncatocli query policy appTenantRestriction <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy appTenantRestriction <subcommand> -h")
        return None

    query_policy_appTenantRestriction_subparsers = query_policy_appTenantRestriction_parser.add_subparsers()
    query_policy_appTenantRestriction_parser.set_defaults(func=_show_query_policy_appTenantRestriction_help)

    query_policy_appTenantRestriction_policy_parser = query_policy_appTenantRestriction_subparsers.add_parser('policy', 
            help='policy() appTenantRestriction operation', 
            usage=get_help("query_policy_appTenantRestriction_policy"))

    query_policy_appTenantRestriction_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_appTenantRestriction_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_appTenantRestriction_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_appTenantRestriction_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_appTenantRestriction_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_appTenantRestriction_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_appTenantRestriction_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_appTenantRestriction_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_appTenantRestriction_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_appTenantRestriction_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_appTenantRestriction_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.appTenantRestriction.policy')

    query_policy_applicationControl_parser = query_policy_subparsers.add_parser('applicationControl', 
            help='applicationControl() policy operation', 
            usage=get_help("query_policy_applicationControl"))

    def _show_query_policy_applicationControl_help(args, configuration=None):
        """Show help when query_policy_applicationControl is called without subcommand"""
        print("\ncatocli query policy applicationControl <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy applicationControl <subcommand> -h")
        return None

    query_policy_applicationControl_subparsers = query_policy_applicationControl_parser.add_subparsers()
    query_policy_applicationControl_parser.set_defaults(func=_show_query_policy_applicationControl_help)

    query_policy_applicationControl_policy_parser = query_policy_applicationControl_subparsers.add_parser('policy', 
            help='policy() applicationControl operation', 
            usage=get_help("query_policy_applicationControl_policy"))

    query_policy_applicationControl_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_applicationControl_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_applicationControl_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_applicationControl_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_applicationControl_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_applicationControl_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_applicationControl_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_applicationControl_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_applicationControl_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_applicationControl_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_applicationControl_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_applicationControl_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_applicationControl_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_applicationControl_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_applicationControl_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.applicationControl.policy')

    query_policy_tlsInspect_parser = query_policy_subparsers.add_parser('tlsInspect', 
            help='tlsInspect() policy operation', 
            usage=get_help("query_policy_tlsInspect"))

    def _show_query_policy_tlsInspect_help(args, configuration=None):
        """Show help when query_policy_tlsInspect is called without subcommand"""
        print("\ncatocli query policy tlsInspect <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy tlsInspect <subcommand> -h")
        return None

    query_policy_tlsInspect_subparsers = query_policy_tlsInspect_parser.add_subparsers()
    query_policy_tlsInspect_parser.set_defaults(func=_show_query_policy_tlsInspect_help)

    query_policy_tlsInspect_policy_parser = query_policy_tlsInspect_subparsers.add_parser('policy', 
            help='policy() tlsInspect operation', 
            usage=get_help("query_policy_tlsInspect_policy"))

    query_policy_tlsInspect_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_tlsInspect_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_tlsInspect_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_tlsInspect_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_tlsInspect_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_tlsInspect_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_tlsInspect_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_tlsInspect_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_tlsInspect_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_tlsInspect_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_tlsInspect_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_tlsInspect_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_tlsInspect_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_tlsInspect_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_tlsInspect_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.tlsInspect.policy')

    query_policy_clientConnectivity_parser = query_policy_subparsers.add_parser('clientConnectivity', 
            help='clientConnectivity() policy operation', 
            usage=get_help("query_policy_clientConnectivity"))

    def _show_query_policy_clientConnectivity_help(args, configuration=None):
        """Show help when query_policy_clientConnectivity is called without subcommand"""
        print("\ncatocli query policy clientConnectivity <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy clientConnectivity <subcommand> -h")
        return None

    query_policy_clientConnectivity_subparsers = query_policy_clientConnectivity_parser.add_subparsers()
    query_policy_clientConnectivity_parser.set_defaults(func=_show_query_policy_clientConnectivity_help)

    query_policy_clientConnectivity_policy_parser = query_policy_clientConnectivity_subparsers.add_parser('policy', 
            help='policy() clientConnectivity operation', 
            usage=get_help("query_policy_clientConnectivity_policy"))

    query_policy_clientConnectivity_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_clientConnectivity_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_clientConnectivity_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_clientConnectivity_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_clientConnectivity_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_clientConnectivity_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_clientConnectivity_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_clientConnectivity_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_clientConnectivity_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_clientConnectivity_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_clientConnectivity_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_clientConnectivity_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_clientConnectivity_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_clientConnectivity_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_clientConnectivity_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.clientConnectivity.policy')

    query_policy_dynamicIpAllocation_parser = query_policy_subparsers.add_parser('dynamicIpAllocation', 
            help='dynamicIpAllocation() policy operation', 
            usage=get_help("query_policy_dynamicIpAllocation"))

    def _show_query_policy_dynamicIpAllocation_help(args, configuration=None):
        """Show help when query_policy_dynamicIpAllocation is called without subcommand"""
        print("\ncatocli query policy dynamicIpAllocation <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy dynamicIpAllocation <subcommand> -h")
        return None

    query_policy_dynamicIpAllocation_subparsers = query_policy_dynamicIpAllocation_parser.add_subparsers()
    query_policy_dynamicIpAllocation_parser.set_defaults(func=_show_query_policy_dynamicIpAllocation_help)

    query_policy_dynamicIpAllocation_policy_parser = query_policy_dynamicIpAllocation_subparsers.add_parser('policy', 
            help='policy() dynamicIpAllocation operation', 
            usage=get_help("query_policy_dynamicIpAllocation_policy"))

    query_policy_dynamicIpAllocation_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_dynamicIpAllocation_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_dynamicIpAllocation_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.dynamicIpAllocation.policy')

    query_policy_splitTunnel_parser = query_policy_subparsers.add_parser('splitTunnel', 
            help='splitTunnel() policy operation', 
            usage=get_help("query_policy_splitTunnel"))

    def _show_query_policy_splitTunnel_help(args, configuration=None):
        """Show help when query_policy_splitTunnel is called without subcommand"""
        print("\ncatocli query policy splitTunnel <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy splitTunnel <subcommand> -h")
        return None

    query_policy_splitTunnel_subparsers = query_policy_splitTunnel_parser.add_subparsers()
    query_policy_splitTunnel_parser.set_defaults(func=_show_query_policy_splitTunnel_help)

    query_policy_splitTunnel_policy_parser = query_policy_splitTunnel_subparsers.add_parser('policy', 
            help='policy() splitTunnel operation', 
            usage=get_help("query_policy_splitTunnel_policy"))

    query_policy_splitTunnel_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_splitTunnel_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_splitTunnel_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_splitTunnel_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_splitTunnel_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_splitTunnel_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_splitTunnel_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_splitTunnel_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_splitTunnel_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_splitTunnel_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_splitTunnel_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_splitTunnel_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_splitTunnel_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_splitTunnel_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_splitTunnel_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.splitTunnel.policy')

    query_policy_terminalServer_parser = query_policy_subparsers.add_parser('terminalServer', 
            help='terminalServer() policy operation', 
            usage=get_help("query_policy_terminalServer"))

    def _show_query_policy_terminalServer_help(args, configuration=None):
        """Show help when query_policy_terminalServer is called without subcommand"""
        print("\ncatocli query policy terminalServer <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy terminalServer <subcommand> -h")
        return None

    query_policy_terminalServer_subparsers = query_policy_terminalServer_parser.add_subparsers()
    query_policy_terminalServer_parser.set_defaults(func=_show_query_policy_terminalServer_help)

    query_policy_terminalServer_policy_parser = query_policy_terminalServer_subparsers.add_parser('policy', 
            help='policy() terminalServer operation', 
            usage=get_help("query_policy_terminalServer_policy"))

    query_policy_terminalServer_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_terminalServer_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_terminalServer_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_terminalServer_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_terminalServer_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_terminalServer_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_terminalServer_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_terminalServer_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_terminalServer_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_terminalServer_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_terminalServer_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_terminalServer_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_terminalServer_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_terminalServer_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_terminalServer_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.terminalServer.policy')

    query_policy_ztnaAlwaysOn_parser = query_policy_subparsers.add_parser('ztnaAlwaysOn', 
            help='ztnaAlwaysOn() policy operation', 
            usage=get_help("query_policy_ztnaAlwaysOn"))

    def _show_query_policy_ztnaAlwaysOn_help(args, configuration=None):
        """Show help when query_policy_ztnaAlwaysOn is called without subcommand"""
        print("\ncatocli query policy ztnaAlwaysOn <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  policy                         policy operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query policy ztnaAlwaysOn <subcommand> -h")
        return None

    query_policy_ztnaAlwaysOn_subparsers = query_policy_ztnaAlwaysOn_parser.add_subparsers()
    query_policy_ztnaAlwaysOn_parser.set_defaults(func=_show_query_policy_ztnaAlwaysOn_help)

    query_policy_ztnaAlwaysOn_policy_parser = query_policy_ztnaAlwaysOn_subparsers.add_parser('policy', 
            help='policy() ztnaAlwaysOn operation', 
            usage=get_help("query_policy_ztnaAlwaysOn_policy"))

    query_policy_ztnaAlwaysOn_policy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_policy_ztnaAlwaysOn_policy_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_policy_ztnaAlwaysOn_policy_parser.set_defaults(func=createRequest,operation_name='query.policy.ztnaAlwaysOn.policy')
