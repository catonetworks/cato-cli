
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_rbac_parse(mutation_subparsers):
    mutation_rbac_parser = mutation_subparsers.add_parser('rbac', 
            help='rbac() mutation operation', 
            usage=get_help("mutation_rbac"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_rbac_help(args, configuration=None):
        """Show help when mutation_rbac is called without subcommand"""
        print("\ncatocli mutation rbac <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  roleManagement                 roleManagement operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation rbac <subcommand> -h")
        return None

    mutation_rbac_subparsers = mutation_rbac_parser.add_subparsers()
    mutation_rbac_parser.set_defaults(func=_show_mutation_rbac_help)

    mutation_rbac_roleManagement_parser = mutation_rbac_subparsers.add_parser('roleManagement', 
            help='roleManagement() rbac operation', 
            usage=get_help("mutation_rbac_roleManagement"))

    def _show_mutation_rbac_roleManagement_help(args, configuration=None):
        """Show help when mutation_rbac_roleManagement is called without subcommand"""
        print("\ncatocli mutation rbac roleManagement <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  createRole                     createRole operation\n  updateRole                     updateRole operation\n  deleteRole                     deleteRole operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation rbac roleManagement <subcommand> -h")
        return None

    mutation_rbac_roleManagement_subparsers = mutation_rbac_roleManagement_parser.add_subparsers()
    mutation_rbac_roleManagement_parser.set_defaults(func=_show_mutation_rbac_roleManagement_help)

    mutation_rbac_roleManagement_createRole_parser = mutation_rbac_roleManagement_subparsers.add_parser('createRole', 
            help='createRole() roleManagement operation', 
            usage=get_help("mutation_rbac_roleManagement_createRole"))

    mutation_rbac_roleManagement_createRole_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_rbac_roleManagement_createRole_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_rbac_roleManagement_createRole_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_rbac_roleManagement_createRole_parser.set_defaults(func=createRequest,operation_name='mutation.rbac.roleManagement.createRole')

    mutation_rbac_roleManagement_updateRole_parser = mutation_rbac_roleManagement_subparsers.add_parser('updateRole', 
            help='updateRole() roleManagement operation', 
            usage=get_help("mutation_rbac_roleManagement_updateRole"))

    mutation_rbac_roleManagement_updateRole_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_rbac_roleManagement_updateRole_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_rbac_roleManagement_updateRole_parser.set_defaults(func=createRequest,operation_name='mutation.rbac.roleManagement.updateRole')

    mutation_rbac_roleManagement_deleteRole_parser = mutation_rbac_roleManagement_subparsers.add_parser('deleteRole', 
            help='deleteRole() roleManagement operation', 
            usage=get_help("mutation_rbac_roleManagement_deleteRole"))

    mutation_rbac_roleManagement_deleteRole_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_rbac_roleManagement_deleteRole_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_rbac_roleManagement_deleteRole_parser.set_defaults(func=createRequest,operation_name='mutation.rbac.roleManagement.deleteRole')
