
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_notification_parse(mutation_subparsers):
    mutation_notification_parser = mutation_subparsers.add_parser('notification', 
            help='notification() mutation operation', 
            usage=get_help("mutation_notification"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_notification_help(args, configuration=None):
        """Show help when mutation_notification is called without subcommand"""
        print("\ncatocli mutation notification <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createMailingList              createMailingList operation\n  updateMailingList              updateMailingList operation\n  deleteMailingList              deleteMailingList operation\n  createSubscriptionGroup        createSubscriptionGroup operation\n  updateSubscriptionGroup        updateSubscriptionGroup operation\n  deleteSubscriptionGroup        deleteSubscriptionGroup operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation notification <subcommand> -h")
        return None

    mutation_notification_subparsers = mutation_notification_parser.add_subparsers()
    mutation_notification_parser.set_defaults(func=_show_mutation_notification_help)

    mutation_notification_createMailingList_parser = mutation_notification_subparsers.add_parser('createMailingList', 
            help='createMailingList() notification operation', 
            usage=get_help("mutation_notification_createMailingList"))

    mutation_notification_createMailingList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_createMailingList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_createMailingList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_createMailingList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_createMailingList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_createMailingList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_createMailingList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_createMailingList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_createMailingList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_createMailingList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_createMailingList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_createMailingList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_createMailingList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_createMailingList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_createMailingList_parser.set_defaults(func=createRequest,operation_name='mutation.notification.createMailingList')

    mutation_notification_updateMailingList_parser = mutation_notification_subparsers.add_parser('updateMailingList', 
            help='updateMailingList() notification operation', 
            usage=get_help("mutation_notification_updateMailingList"))

    mutation_notification_updateMailingList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_updateMailingList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_updateMailingList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_updateMailingList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_updateMailingList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_updateMailingList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_updateMailingList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_updateMailingList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_updateMailingList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_updateMailingList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_updateMailingList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_updateMailingList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_updateMailingList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_updateMailingList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_updateMailingList_parser.set_defaults(func=createRequest,operation_name='mutation.notification.updateMailingList')

    mutation_notification_deleteMailingList_parser = mutation_notification_subparsers.add_parser('deleteMailingList', 
            help='deleteMailingList() notification operation', 
            usage=get_help("mutation_notification_deleteMailingList"))

    mutation_notification_deleteMailingList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_deleteMailingList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_deleteMailingList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_deleteMailingList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_deleteMailingList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_deleteMailingList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_deleteMailingList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_deleteMailingList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_deleteMailingList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_deleteMailingList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_deleteMailingList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_deleteMailingList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_deleteMailingList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_deleteMailingList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_deleteMailingList_parser.set_defaults(func=createRequest,operation_name='mutation.notification.deleteMailingList')

    mutation_notification_createSubscriptionGroup_parser = mutation_notification_subparsers.add_parser('createSubscriptionGroup', 
            help='createSubscriptionGroup() notification operation', 
            usage=get_help("mutation_notification_createSubscriptionGroup"))

    mutation_notification_createSubscriptionGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_createSubscriptionGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_createSubscriptionGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_createSubscriptionGroup_parser.set_defaults(func=createRequest,operation_name='mutation.notification.createSubscriptionGroup')

    mutation_notification_updateSubscriptionGroup_parser = mutation_notification_subparsers.add_parser('updateSubscriptionGroup', 
            help='updateSubscriptionGroup() notification operation', 
            usage=get_help("mutation_notification_updateSubscriptionGroup"))

    mutation_notification_updateSubscriptionGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_updateSubscriptionGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_updateSubscriptionGroup_parser.set_defaults(func=createRequest,operation_name='mutation.notification.updateSubscriptionGroup')

    mutation_notification_deleteSubscriptionGroup_parser = mutation_notification_subparsers.add_parser('deleteSubscriptionGroup', 
            help='deleteSubscriptionGroup() notification operation', 
            usage=get_help("mutation_notification_deleteSubscriptionGroup"))

    mutation_notification_deleteSubscriptionGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_notification_deleteSubscriptionGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_notification_deleteSubscriptionGroup_parser.set_defaults(func=createRequest,operation_name='mutation.notification.deleteSubscriptionGroup')
