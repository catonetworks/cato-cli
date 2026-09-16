
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_posture_parse(mutation_subparsers):
    mutation_posture_parser = mutation_subparsers.add_parser('posture', 
            help='posture() mutation operation', 
            usage=get_help("mutation_posture"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_posture_help(args, configuration=None):
        """Show help when mutation_posture is called without subcommand"""
        print("\ncatocli mutation posture <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  addCheckComment                addCheckComment operation\n  updateCheckConfiguration       updateCheckConfiguration operation\n  reevaluateChecks               reevaluateChecks operation\n  muteCheck                      muteCheck operation\n  unmuteCheck                    unmuteCheck operation\n  muteFinding                    muteFinding operation\n  unmuteFinding                  unmuteFinding operation\n  dismissFinding                 dismissFinding operation\n  undismissFinding               undismissFinding operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation posture <subcommand> -h")
        return None

    mutation_posture_subparsers = mutation_posture_parser.add_subparsers()
    mutation_posture_parser.set_defaults(func=_show_mutation_posture_help)

    mutation_posture_addCheckComment_parser = mutation_posture_subparsers.add_parser('addCheckComment', 
            help='addCheckComment() posture operation', 
            usage=get_help("mutation_posture_addCheckComment"))

    mutation_posture_addCheckComment_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_addCheckComment_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_addCheckComment_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_addCheckComment_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_addCheckComment_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_addCheckComment_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_addCheckComment_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_addCheckComment_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_addCheckComment_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_addCheckComment_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_addCheckComment_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_addCheckComment_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_addCheckComment_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_addCheckComment_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_addCheckComment_parser.set_defaults(func=createRequest,operation_name='mutation.posture.addCheckComment')

    mutation_posture_updateCheckConfiguration_parser = mutation_posture_subparsers.add_parser('updateCheckConfiguration', 
            help='updateCheckConfiguration() posture operation', 
            usage=get_help("mutation_posture_updateCheckConfiguration"))

    mutation_posture_updateCheckConfiguration_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_updateCheckConfiguration_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_updateCheckConfiguration_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_updateCheckConfiguration_parser.set_defaults(func=createRequest,operation_name='mutation.posture.updateCheckConfiguration')

    mutation_posture_reevaluateChecks_parser = mutation_posture_subparsers.add_parser('reevaluateChecks', 
            help='reevaluateChecks() posture operation', 
            usage=get_help("mutation_posture_reevaluateChecks"))

    mutation_posture_reevaluateChecks_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_reevaluateChecks_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_reevaluateChecks_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_reevaluateChecks_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_reevaluateChecks_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_reevaluateChecks_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_reevaluateChecks_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_reevaluateChecks_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_reevaluateChecks_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_reevaluateChecks_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_reevaluateChecks_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_reevaluateChecks_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_reevaluateChecks_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_reevaluateChecks_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_reevaluateChecks_parser.set_defaults(func=createRequest,operation_name='mutation.posture.reevaluateChecks')

    mutation_posture_muteCheck_parser = mutation_posture_subparsers.add_parser('muteCheck', 
            help='muteCheck() posture operation', 
            usage=get_help("mutation_posture_muteCheck"))

    mutation_posture_muteCheck_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_muteCheck_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_muteCheck_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_muteCheck_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_muteCheck_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_muteCheck_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_muteCheck_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_muteCheck_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_muteCheck_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_muteCheck_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_muteCheck_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_muteCheck_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_muteCheck_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_muteCheck_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_muteCheck_parser.set_defaults(func=createRequest,operation_name='mutation.posture.muteCheck')

    mutation_posture_unmuteCheck_parser = mutation_posture_subparsers.add_parser('unmuteCheck', 
            help='unmuteCheck() posture operation', 
            usage=get_help("mutation_posture_unmuteCheck"))

    mutation_posture_unmuteCheck_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_unmuteCheck_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_unmuteCheck_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_unmuteCheck_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_unmuteCheck_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_unmuteCheck_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_unmuteCheck_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_unmuteCheck_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_unmuteCheck_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_unmuteCheck_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_unmuteCheck_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_unmuteCheck_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_unmuteCheck_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_unmuteCheck_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_unmuteCheck_parser.set_defaults(func=createRequest,operation_name='mutation.posture.unmuteCheck')

    mutation_posture_muteFinding_parser = mutation_posture_subparsers.add_parser('muteFinding', 
            help='muteFinding() posture operation', 
            usage=get_help("mutation_posture_muteFinding"))

    mutation_posture_muteFinding_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_muteFinding_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_muteFinding_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_muteFinding_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_muteFinding_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_muteFinding_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_muteFinding_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_muteFinding_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_muteFinding_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_muteFinding_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_muteFinding_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_muteFinding_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_muteFinding_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_muteFinding_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_muteFinding_parser.set_defaults(func=createRequest,operation_name='mutation.posture.muteFinding')

    mutation_posture_unmuteFinding_parser = mutation_posture_subparsers.add_parser('unmuteFinding', 
            help='unmuteFinding() posture operation', 
            usage=get_help("mutation_posture_unmuteFinding"))

    mutation_posture_unmuteFinding_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_unmuteFinding_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_unmuteFinding_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_unmuteFinding_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_unmuteFinding_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_unmuteFinding_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_unmuteFinding_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_unmuteFinding_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_unmuteFinding_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_unmuteFinding_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_unmuteFinding_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_unmuteFinding_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_unmuteFinding_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_unmuteFinding_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_unmuteFinding_parser.set_defaults(func=createRequest,operation_name='mutation.posture.unmuteFinding')

    mutation_posture_dismissFinding_parser = mutation_posture_subparsers.add_parser('dismissFinding', 
            help='dismissFinding() posture operation', 
            usage=get_help("mutation_posture_dismissFinding"))

    mutation_posture_dismissFinding_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_dismissFinding_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_dismissFinding_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_dismissFinding_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_dismissFinding_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_dismissFinding_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_dismissFinding_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_dismissFinding_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_dismissFinding_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_dismissFinding_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_dismissFinding_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_dismissFinding_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_dismissFinding_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_dismissFinding_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_dismissFinding_parser.set_defaults(func=createRequest,operation_name='mutation.posture.dismissFinding')

    mutation_posture_undismissFinding_parser = mutation_posture_subparsers.add_parser('undismissFinding', 
            help='undismissFinding() posture operation', 
            usage=get_help("mutation_posture_undismissFinding"))

    mutation_posture_undismissFinding_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_posture_undismissFinding_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_posture_undismissFinding_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_posture_undismissFinding_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_posture_undismissFinding_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_posture_undismissFinding_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_posture_undismissFinding_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_posture_undismissFinding_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_posture_undismissFinding_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_posture_undismissFinding_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_posture_undismissFinding_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_posture_undismissFinding_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_posture_undismissFinding_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_posture_undismissFinding_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_posture_undismissFinding_parser.set_defaults(func=createRequest,operation_name='mutation.posture.undismissFinding')
