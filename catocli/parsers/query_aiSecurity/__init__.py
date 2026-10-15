
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_aiSecurity_parse(query_subparsers):
    query_aiSecurity_parser = query_subparsers.add_parser('aiSecurity', 
            help='aiSecurity() query operation', 
            usage=get_help("query_aiSecurity"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_aiSecurity_help(args, configuration=None):
        """Show help when query_aiSecurity is called without subcommand"""
        print("\ncatocli query aiSecurity <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  apps                           apps operation\n  endUsers                       endUsers operation\n  agents                         agents operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query aiSecurity <subcommand> -h")
        return None

    query_aiSecurity_subparsers = query_aiSecurity_parser.add_subparsers()
    query_aiSecurity_parser.set_defaults(func=_show_query_aiSecurity_help)

    query_aiSecurity_apps_parser = query_aiSecurity_subparsers.add_parser('apps', 
            help='apps() aiSecurity operation', 
            usage=get_help("query_aiSecurity_apps"))

    def _show_query_aiSecurity_apps_help(args, configuration=None):
        """Show help when query_aiSecurity_apps is called without subcommand"""
        print("\ncatocli query aiSecurity apps <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  invocation                     invocation operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query aiSecurity apps <subcommand> -h")
        return None

    query_aiSecurity_apps_subparsers = query_aiSecurity_apps_parser.add_subparsers()
    query_aiSecurity_apps_parser.set_defaults(func=_show_query_aiSecurity_apps_help)

    query_aiSecurity_apps_invocation_parser = query_aiSecurity_apps_subparsers.add_parser('invocation', 
            help='invocation() apps operation', 
            usage=get_help("query_aiSecurity_apps_invocation"))

    query_aiSecurity_apps_invocation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_aiSecurity_apps_invocation_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_aiSecurity_apps_invocation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_aiSecurity_apps_invocation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_aiSecurity_apps_invocation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_aiSecurity_apps_invocation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_aiSecurity_apps_invocation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_aiSecurity_apps_invocation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_aiSecurity_apps_invocation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_aiSecurity_apps_invocation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_aiSecurity_apps_invocation_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_aiSecurity_apps_invocation_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_aiSecurity_apps_invocation_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_aiSecurity_apps_invocation_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_aiSecurity_apps_invocation_parser.set_defaults(func=createRequest,operation_name='query.aiSecurity.apps.invocation')

    query_aiSecurity_endUsers_parser = query_aiSecurity_subparsers.add_parser('endUsers', 
            help='endUsers() aiSecurity operation', 
            usage=get_help("query_aiSecurity_endUsers"))

    def _show_query_aiSecurity_endUsers_help(args, configuration=None):
        """Show help when query_aiSecurity_endUsers is called without subcommand"""
        print("\ncatocli query aiSecurity endUsers <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  sessionConversation            sessionConversation operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query aiSecurity endUsers <subcommand> -h")
        return None

    query_aiSecurity_endUsers_subparsers = query_aiSecurity_endUsers_parser.add_subparsers()
    query_aiSecurity_endUsers_parser.set_defaults(func=_show_query_aiSecurity_endUsers_help)

    query_aiSecurity_endUsers_sessionConversation_parser = query_aiSecurity_endUsers_subparsers.add_parser('sessionConversation', 
            help='sessionConversation() endUsers operation', 
            usage=get_help("query_aiSecurity_endUsers_sessionConversation"))

    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_aiSecurity_endUsers_sessionConversation_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_aiSecurity_endUsers_sessionConversation_parser.set_defaults(func=createRequest,operation_name='query.aiSecurity.endUsers.sessionConversation')

    query_aiSecurity_agents_parser = query_aiSecurity_subparsers.add_parser('agents', 
            help='agents() aiSecurity operation', 
            usage=get_help("query_aiSecurity_agents"))

    def _show_query_aiSecurity_agents_help(args, configuration=None):
        """Show help when query_aiSecurity_agents is called without subcommand"""
        print("\ncatocli query aiSecurity agents <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  session                        session operation\n  event                          event operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query aiSecurity agents <subcommand> -h")
        return None

    query_aiSecurity_agents_subparsers = query_aiSecurity_agents_parser.add_subparsers()
    query_aiSecurity_agents_parser.set_defaults(func=_show_query_aiSecurity_agents_help)

    query_aiSecurity_agents_session_parser = query_aiSecurity_agents_subparsers.add_parser('session', 
            help='session() agents operation', 
            usage=get_help("query_aiSecurity_agents_session"))

    query_aiSecurity_agents_session_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_aiSecurity_agents_session_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_aiSecurity_agents_session_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_aiSecurity_agents_session_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_aiSecurity_agents_session_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_aiSecurity_agents_session_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_aiSecurity_agents_session_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_aiSecurity_agents_session_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_aiSecurity_agents_session_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_aiSecurity_agents_session_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_aiSecurity_agents_session_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_aiSecurity_agents_session_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_aiSecurity_agents_session_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_aiSecurity_agents_session_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_aiSecurity_agents_session_parser.set_defaults(func=createRequest,operation_name='query.aiSecurity.agents.session')

    query_aiSecurity_agents_event_parser = query_aiSecurity_agents_subparsers.add_parser('event', 
            help='event() agents operation', 
            usage=get_help("query_aiSecurity_agents_event"))

    query_aiSecurity_agents_event_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_aiSecurity_agents_event_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_aiSecurity_agents_event_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_aiSecurity_agents_event_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_aiSecurity_agents_event_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_aiSecurity_agents_event_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_aiSecurity_agents_event_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_aiSecurity_agents_event_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_aiSecurity_agents_event_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_aiSecurity_agents_event_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_aiSecurity_agents_event_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_aiSecurity_agents_event_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_aiSecurity_agents_event_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_aiSecurity_agents_event_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_aiSecurity_agents_event_parser.set_defaults(func=createRequest,operation_name='query.aiSecurity.agents.event')
