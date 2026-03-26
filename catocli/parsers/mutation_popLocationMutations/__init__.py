
from ..customParserApiClient import createRequest, get_help
from ...Utils.help_formatter import CustomSubparserHelpFormatter

def mutation_popLocationMutations_parse(mutation_subparsers):
    mutation_popLocationMutations_parser = mutation_subparsers.add_parser('popLocationMutations', 
            help='popLocationMutations() mutation operation', 
            usage=get_help("mutation_popLocationMutations"), formatter_class=CustomSubparserHelpFormatter)

    def _show_mutation_popLocationMutations_help(args, configuration=None):
        """Show help when mutation_popLocationMutations is called without subcommand"""
        print("\ncatocli mutation popLocationMutations <subcommand> [options]")
        print("\nAvailable subcommands:")
        print("  allocateIp                     allocateIp operation\n  releaseIp                      releaseIp operation\n  updateAllocatedIpDescription   updateAllocatedIpDescription operation")
        print("\nFor help on a specific subcommand:")
        print("  catocli mutation popLocationMutations <subcommand> -h")
        return None

    mutation_popLocationMutations_subparsers = mutation_popLocationMutations_parser.add_subparsers()
    mutation_popLocationMutations_parser.set_defaults(func=_show_mutation_popLocationMutations_help)

    mutation_popLocationMutations_allocateIp_parser = mutation_popLocationMutations_subparsers.add_parser('allocateIp', 
            help='allocateIp() popLocationMutations operation', 
            usage=get_help("mutation_popLocationMutations_allocateIp"))

    mutation_popLocationMutations_allocateIp_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_popLocationMutations_allocateIp_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_popLocationMutations_allocateIp_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_popLocationMutations_allocateIp_parser.set_defaults(func=createRequest,operation_name='mutation.popLocationMutations.allocateIp')

    mutation_popLocationMutations_releaseIp_parser = mutation_popLocationMutations_subparsers.add_parser('releaseIp', 
            help='releaseIp() popLocationMutations operation', 
            usage=get_help("mutation_popLocationMutations_releaseIp"))

    mutation_popLocationMutations_releaseIp_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_popLocationMutations_releaseIp_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_popLocationMutations_releaseIp_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_popLocationMutations_releaseIp_parser.set_defaults(func=createRequest,operation_name='mutation.popLocationMutations.releaseIp')

    mutation_popLocationMutations_updateAllocatedIpDescription_parser = mutation_popLocationMutations_subparsers.add_parser('updateAllocatedIpDescription', 
            help='updateAllocatedIpDescription() popLocationMutations operation', 
            usage=get_help("mutation_popLocationMutations_updateAllocatedIpDescription"))

    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--json-file', help='Path to a file containing JSON input variables.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--endpoint', dest='endpoint', help='Override the API endpoint from the profile. Requires --api-token and --accountID to be provided.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--api-token', dest='api_token', help='Override the API token from the profile. Requires --endpoint and --accountID to be provided.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--accountID', dest='accountID_override', help='Override the account ID from the profile. Can be used alone or with --endpoint and --api-token.')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.add_argument('--trace-id', dest='trace_id', action='store_true', help='Enable tracing and print the trace ID from the response')
    mutation_popLocationMutations_updateAllocatedIpDescription_parser.set_defaults(func=createRequest,operation_name='mutation.popLocationMutations.updateAllocatedIpDescription')
