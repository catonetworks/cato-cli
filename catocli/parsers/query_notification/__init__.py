
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def query_notification_parse(query_subparsers):
    query_notification_parser = query_subparsers.add_parser('notification', 
            help='notification() query operation', 
            usage=get_help("query_notification"), formatter_class=CustomSubparserHelpFormatter)

    def _show_query_notification_help(args, configuration=None):
        """Show help when query_notification is called without subcommand"""
        print("\ncatocli query notification <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  mailingListList                mailingListList operation\n  mailingList                    mailingList operation\n  integration                    integration operation\n  subscriptionGroupList          subscriptionGroupList operation\n  subscriptionGroup              subscriptionGroup operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query notification <subcommand> -h")
        return None

    query_notification_subparsers = query_notification_parser.add_subparsers()
    query_notification_parser.set_defaults(func=_show_query_notification_help)

    query_notification_mailingListList_parser = query_notification_subparsers.add_parser('mailingListList', 
            help='mailingListList() notification operation', 
            usage=get_help("query_notification_mailingListList"))

    query_notification_mailingListList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_mailingListList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_mailingListList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_mailingListList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_mailingListList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_mailingListList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_mailingListList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_mailingListList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_mailingListList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_mailingListList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_mailingListList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_mailingListList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_mailingListList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_mailingListList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_mailingListList_parser.set_defaults(func=createRequest,operation_name='query.notification.mailingListList')

    query_notification_mailingList_parser = query_notification_subparsers.add_parser('mailingList', 
            help='mailingList() notification operation', 
            usage=get_help("query_notification_mailingList"))

    query_notification_mailingList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_mailingList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_mailingList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_mailingList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_mailingList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_mailingList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_mailingList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_mailingList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_mailingList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_mailingList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_mailingList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_mailingList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_mailingList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_mailingList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_mailingList_parser.set_defaults(func=createRequest,operation_name='query.notification.mailingList')

    query_notification_integration_parser = query_notification_subparsers.add_parser('integration', 
            help='integration() notification operation', 
            usage=get_help("query_notification_integration"))

    def _show_query_notification_integration_help(args, configuration=None):
        """Show help when query_notification_integration is called without subcommand"""
        print("\ncatocli query notification integration <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  webhookList                    webhookList operation\n  webhook                        webhook operation\n  referenceBodyTemplateList      referenceBodyTemplateList operation\n  referenceBodyTemplate          referenceBodyTemplate operation\n  webhookFields                  webhookFields operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli query notification integration <subcommand> -h")
        return None

    query_notification_integration_subparsers = query_notification_integration_parser.add_subparsers()
    query_notification_integration_parser.set_defaults(func=_show_query_notification_integration_help)

    query_notification_integration_webhookList_parser = query_notification_integration_subparsers.add_parser('webhookList', 
            help='webhookList() integration operation', 
            usage=get_help("query_notification_integration_webhookList"))

    query_notification_integration_webhookList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_integration_webhookList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_integration_webhookList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_integration_webhookList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_integration_webhookList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_integration_webhookList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_integration_webhookList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_integration_webhookList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_integration_webhookList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_integration_webhookList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_integration_webhookList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_integration_webhookList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_integration_webhookList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_integration_webhookList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_integration_webhookList_parser.set_defaults(func=createRequest,operation_name='query.notification.integration.webhookList')

    query_notification_integration_webhook_parser = query_notification_integration_subparsers.add_parser('webhook', 
            help='webhook() integration operation', 
            usage=get_help("query_notification_integration_webhook"))

    query_notification_integration_webhook_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_integration_webhook_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_integration_webhook_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_integration_webhook_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_integration_webhook_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_integration_webhook_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_integration_webhook_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_integration_webhook_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_integration_webhook_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_integration_webhook_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_integration_webhook_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_integration_webhook_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_integration_webhook_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_integration_webhook_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_integration_webhook_parser.set_defaults(func=createRequest,operation_name='query.notification.integration.webhook')

    query_notification_integration_referenceBodyTemplateList_parser = query_notification_integration_subparsers.add_parser('referenceBodyTemplateList', 
            help='referenceBodyTemplateList() integration operation', 
            usage=get_help("query_notification_integration_referenceBodyTemplateList"))

    query_notification_integration_referenceBodyTemplateList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_integration_referenceBodyTemplateList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_integration_referenceBodyTemplateList_parser.set_defaults(func=createRequest,operation_name='query.notification.integration.referenceBodyTemplateList')

    query_notification_integration_referenceBodyTemplate_parser = query_notification_integration_subparsers.add_parser('referenceBodyTemplate', 
            help='referenceBodyTemplate() integration operation', 
            usage=get_help("query_notification_integration_referenceBodyTemplate"))

    query_notification_integration_referenceBodyTemplate_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_integration_referenceBodyTemplate_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_integration_referenceBodyTemplate_parser.set_defaults(func=createRequest,operation_name='query.notification.integration.referenceBodyTemplate')

    query_notification_integration_webhookFields_parser = query_notification_integration_subparsers.add_parser('webhookFields', 
            help='webhookFields() integration operation', 
            usage=get_help("query_notification_integration_webhookFields"))

    query_notification_integration_webhookFields_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_integration_webhookFields_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_integration_webhookFields_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_integration_webhookFields_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_integration_webhookFields_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_integration_webhookFields_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_integration_webhookFields_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_integration_webhookFields_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_integration_webhookFields_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_integration_webhookFields_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_integration_webhookFields_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_integration_webhookFields_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_integration_webhookFields_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_integration_webhookFields_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_integration_webhookFields_parser.set_defaults(func=createRequest,operation_name='query.notification.integration.webhookFields')

    query_notification_subscriptionGroupList_parser = query_notification_subparsers.add_parser('subscriptionGroupList', 
            help='subscriptionGroupList() notification operation', 
            usage=get_help("query_notification_subscriptionGroupList"))

    query_notification_subscriptionGroupList_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_subscriptionGroupList_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_subscriptionGroupList_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_subscriptionGroupList_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_subscriptionGroupList_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_subscriptionGroupList_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_subscriptionGroupList_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_subscriptionGroupList_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_subscriptionGroupList_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_subscriptionGroupList_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_subscriptionGroupList_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_subscriptionGroupList_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_subscriptionGroupList_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_subscriptionGroupList_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_subscriptionGroupList_parser.set_defaults(func=createRequest,operation_name='query.notification.subscriptionGroupList')

    query_notification_subscriptionGroup_parser = query_notification_subparsers.add_parser('subscriptionGroup', 
            help='subscriptionGroup() notification operation', 
            usage=get_help("query_notification_subscriptionGroup"))

    query_notification_subscriptionGroup_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    query_notification_subscriptionGroup_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    query_notification_subscriptionGroup_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    query_notification_subscriptionGroup_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    query_notification_subscriptionGroup_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    query_notification_subscriptionGroup_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    query_notification_subscriptionGroup_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    query_notification_subscriptionGroup_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    query_notification_subscriptionGroup_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    query_notification_subscriptionGroup_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    query_notification_subscriptionGroup_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    query_notification_subscriptionGroup_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    query_notification_subscriptionGroup_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    query_notification_subscriptionGroup_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    query_notification_subscriptionGroup_parser.set_defaults(func=createRequest,operation_name='query.notification.subscriptionGroup')
