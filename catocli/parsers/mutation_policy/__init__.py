
from ..customParserApiClient import createRequest, get_help

def mutation_policy_parse(mutation_subparsers):
    mutation_policy_parser = mutation_subparsers.add_parser('policy', 
            help='policy() mutation operation', 
            usage=get_help("mutation_policy"))

    mutation_policy_subparsers = mutation_policy_parser.add_subparsers()

    mutation_policy_antiMalwareFileHash_parser = mutation_policy_subparsers.add_parser('antiMalwareFileHash', 
            help='antiMalwareFileHash() policy operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash"))

    mutation_policy_antiMalwareFileHash_subparsers = mutation_policy_antiMalwareFileHash_parser.add_subparsers()

    mutation_policy_antiMalwareFileHash_addRule_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('addRule', 
            help='addRule() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_addRule"))

    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.addRule')

    mutation_policy_antiMalwareFileHash_updateRule_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('updateRule', 
            help='updateRule() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_updateRule"))

    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.updateRule')

    mutation_policy_antiMalwareFileHash_removeRule_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('removeRule', 
            help='removeRule() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_removeRule"))

    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.removeRule')

    mutation_policy_antiMalwareFileHash_moveRule_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('moveRule', 
            help='moveRule() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_moveRule"))

    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.moveRule')

    mutation_policy_antiMalwareFileHash_addSection_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('addSection', 
            help='addSection() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_addSection"))

    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.addSection')

    mutation_policy_antiMalwareFileHash_updateSection_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('updateSection', 
            help='updateSection() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_updateSection"))

    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.updateSection')

    mutation_policy_antiMalwareFileHash_removeSection_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('removeSection', 
            help='removeSection() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_removeSection"))

    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.removeSection')

    mutation_policy_antiMalwareFileHash_moveSection_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('moveSection', 
            help='moveSection() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_moveSection"))

    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.moveSection')

    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_createPolicyRevision"))

    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.createPolicyRevision')

    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_publishPolicyRevision"))

    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.publishPolicyRevision')

    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_discardPolicyRevision"))

    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.discardPolicyRevision')

    mutation_policy_antiMalwareFileHash_updatePolicy_parser = mutation_policy_antiMalwareFileHash_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() antiMalwareFileHash operation', 
            usage=get_help("mutation_policy_antiMalwareFileHash_updatePolicy"))

    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_antiMalwareFileHash_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.antiMalwareFileHash.updatePolicy')

    mutation_policy_dynamicIpAllocation_parser = mutation_policy_subparsers.add_parser('dynamicIpAllocation', 
            help='dynamicIpAllocation() policy operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation"))

    mutation_policy_dynamicIpAllocation_subparsers = mutation_policy_dynamicIpAllocation_parser.add_subparsers()

    mutation_policy_dynamicIpAllocation_addRule_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('addRule', 
            help='addRule() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_addRule"))

    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.addRule')

    mutation_policy_dynamicIpAllocation_updateRule_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('updateRule', 
            help='updateRule() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_updateRule"))

    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.updateRule')

    mutation_policy_dynamicIpAllocation_removeRule_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('removeRule', 
            help='removeRule() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_removeRule"))

    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.removeRule')

    mutation_policy_dynamicIpAllocation_moveRule_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('moveRule', 
            help='moveRule() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_moveRule"))

    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.moveRule')

    mutation_policy_dynamicIpAllocation_addSection_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('addSection', 
            help='addSection() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_addSection"))

    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.addSection')

    mutation_policy_dynamicIpAllocation_updateSection_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('updateSection', 
            help='updateSection() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_updateSection"))

    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.updateSection')

    mutation_policy_dynamicIpAllocation_removeSection_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('removeSection', 
            help='removeSection() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_removeSection"))

    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.removeSection')

    mutation_policy_dynamicIpAllocation_moveSection_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('moveSection', 
            help='moveSection() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_moveSection"))

    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.moveSection')

    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_createPolicyRevision"))

    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.createPolicyRevision')

    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_publishPolicyRevision"))

    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.publishPolicyRevision')

    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_discardPolicyRevision"))

    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.discardPolicyRevision')

    mutation_policy_dynamicIpAllocation_updatePolicy_parser = mutation_policy_dynamicIpAllocation_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() dynamicIpAllocation operation', 
            usage=get_help("mutation_policy_dynamicIpAllocation_updatePolicy"))

    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_dynamicIpAllocation_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.dynamicIpAllocation.updatePolicy')

    mutation_policy_socketLan_parser = mutation_policy_subparsers.add_parser('socketLan', 
            help='socketLan() policy operation', 
            usage=get_help("mutation_policy_socketLan"))

    mutation_policy_socketLan_subparsers = mutation_policy_socketLan_parser.add_subparsers()

    mutation_policy_socketLan_addRule_parser = mutation_policy_socketLan_subparsers.add_parser('addRule', 
            help='addRule() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_addRule"))

    mutation_policy_socketLan_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.addRule')

    mutation_policy_socketLan_updateRule_parser = mutation_policy_socketLan_subparsers.add_parser('updateRule', 
            help='updateRule() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_updateRule"))

    mutation_policy_socketLan_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.updateRule')

    mutation_policy_socketLan_removeRule_parser = mutation_policy_socketLan_subparsers.add_parser('removeRule', 
            help='removeRule() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_removeRule"))

    mutation_policy_socketLan_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.removeRule')

    mutation_policy_socketLan_moveRule_parser = mutation_policy_socketLan_subparsers.add_parser('moveRule', 
            help='moveRule() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_moveRule"))

    mutation_policy_socketLan_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.moveRule')

    mutation_policy_socketLan_addSection_parser = mutation_policy_socketLan_subparsers.add_parser('addSection', 
            help='addSection() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_addSection"))

    mutation_policy_socketLan_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.addSection')

    mutation_policy_socketLan_updateSection_parser = mutation_policy_socketLan_subparsers.add_parser('updateSection', 
            help='updateSection() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_updateSection"))

    mutation_policy_socketLan_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.updateSection')

    mutation_policy_socketLan_removeSection_parser = mutation_policy_socketLan_subparsers.add_parser('removeSection', 
            help='removeSection() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_removeSection"))

    mutation_policy_socketLan_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.removeSection')

    mutation_policy_socketLan_moveSection_parser = mutation_policy_socketLan_subparsers.add_parser('moveSection', 
            help='moveSection() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_moveSection"))

    mutation_policy_socketLan_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.moveSection')

    mutation_policy_socketLan_createPolicyRevision_parser = mutation_policy_socketLan_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_createPolicyRevision"))

    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.createPolicyRevision')

    mutation_policy_socketLan_publishPolicyRevision_parser = mutation_policy_socketLan_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_publishPolicyRevision"))

    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.publishPolicyRevision')

    mutation_policy_socketLan_discardPolicyRevision_parser = mutation_policy_socketLan_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_discardPolicyRevision"))

    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.discardPolicyRevision')

    mutation_policy_socketLan_updatePolicy_parser = mutation_policy_socketLan_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() socketLan operation', 
            usage=get_help("mutation_policy_socketLan_updatePolicy"))

    mutation_policy_socketLan_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_socketLan_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_socketLan_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.socketLan.updatePolicy')

    mutation_policy_terminalServer_parser = mutation_policy_subparsers.add_parser('terminalServer', 
            help='terminalServer() policy operation', 
            usage=get_help("mutation_policy_terminalServer"))

    mutation_policy_terminalServer_subparsers = mutation_policy_terminalServer_parser.add_subparsers()

    mutation_policy_terminalServer_addRule_parser = mutation_policy_terminalServer_subparsers.add_parser('addRule', 
            help='addRule() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_addRule"))

    mutation_policy_terminalServer_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.addRule')

    mutation_policy_terminalServer_updateRule_parser = mutation_policy_terminalServer_subparsers.add_parser('updateRule', 
            help='updateRule() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_updateRule"))

    mutation_policy_terminalServer_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.updateRule')

    mutation_policy_terminalServer_removeRule_parser = mutation_policy_terminalServer_subparsers.add_parser('removeRule', 
            help='removeRule() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_removeRule"))

    mutation_policy_terminalServer_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.removeRule')

    mutation_policy_terminalServer_moveRule_parser = mutation_policy_terminalServer_subparsers.add_parser('moveRule', 
            help='moveRule() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_moveRule"))

    mutation_policy_terminalServer_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.moveRule')

    mutation_policy_terminalServer_addSection_parser = mutation_policy_terminalServer_subparsers.add_parser('addSection', 
            help='addSection() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_addSection"))

    mutation_policy_terminalServer_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.addSection')

    mutation_policy_terminalServer_updateSection_parser = mutation_policy_terminalServer_subparsers.add_parser('updateSection', 
            help='updateSection() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_updateSection"))

    mutation_policy_terminalServer_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.updateSection')

    mutation_policy_terminalServer_removeSection_parser = mutation_policy_terminalServer_subparsers.add_parser('removeSection', 
            help='removeSection() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_removeSection"))

    mutation_policy_terminalServer_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.removeSection')

    mutation_policy_terminalServer_moveSection_parser = mutation_policy_terminalServer_subparsers.add_parser('moveSection', 
            help='moveSection() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_moveSection"))

    mutation_policy_terminalServer_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.moveSection')

    mutation_policy_terminalServer_createPolicyRevision_parser = mutation_policy_terminalServer_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_createPolicyRevision"))

    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.createPolicyRevision')

    mutation_policy_terminalServer_publishPolicyRevision_parser = mutation_policy_terminalServer_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_publishPolicyRevision"))

    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.publishPolicyRevision')

    mutation_policy_terminalServer_discardPolicyRevision_parser = mutation_policy_terminalServer_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_discardPolicyRevision"))

    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.discardPolicyRevision')

    mutation_policy_terminalServer_updatePolicy_parser = mutation_policy_terminalServer_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() terminalServer operation', 
            usage=get_help("mutation_policy_terminalServer_updatePolicy"))

    mutation_policy_terminalServer_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_terminalServer_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_terminalServer_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.terminalServer.updatePolicy')

    mutation_policy_wanNetwork_parser = mutation_policy_subparsers.add_parser('wanNetwork', 
            help='wanNetwork() policy operation', 
            usage=get_help("mutation_policy_wanNetwork"))

    mutation_policy_wanNetwork_subparsers = mutation_policy_wanNetwork_parser.add_subparsers()

    mutation_policy_wanNetwork_addRule_parser = mutation_policy_wanNetwork_subparsers.add_parser('addRule', 
            help='addRule() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_addRule"))

    mutation_policy_wanNetwork_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.addRule')

    mutation_policy_wanNetwork_updateRule_parser = mutation_policy_wanNetwork_subparsers.add_parser('updateRule', 
            help='updateRule() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_updateRule"))

    mutation_policy_wanNetwork_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.updateRule')

    mutation_policy_wanNetwork_removeRule_parser = mutation_policy_wanNetwork_subparsers.add_parser('removeRule', 
            help='removeRule() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_removeRule"))

    mutation_policy_wanNetwork_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.removeRule')

    mutation_policy_wanNetwork_moveRule_parser = mutation_policy_wanNetwork_subparsers.add_parser('moveRule', 
            help='moveRule() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_moveRule"))

    mutation_policy_wanNetwork_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.moveRule')

    mutation_policy_wanNetwork_addSection_parser = mutation_policy_wanNetwork_subparsers.add_parser('addSection', 
            help='addSection() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_addSection"))

    mutation_policy_wanNetwork_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.addSection')

    mutation_policy_wanNetwork_updateSection_parser = mutation_policy_wanNetwork_subparsers.add_parser('updateSection', 
            help='updateSection() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_updateSection"))

    mutation_policy_wanNetwork_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.updateSection')

    mutation_policy_wanNetwork_removeSection_parser = mutation_policy_wanNetwork_subparsers.add_parser('removeSection', 
            help='removeSection() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_removeSection"))

    mutation_policy_wanNetwork_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.removeSection')

    mutation_policy_wanNetwork_moveSection_parser = mutation_policy_wanNetwork_subparsers.add_parser('moveSection', 
            help='moveSection() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_moveSection"))

    mutation_policy_wanNetwork_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.moveSection')

    mutation_policy_wanNetwork_createPolicyRevision_parser = mutation_policy_wanNetwork_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_createPolicyRevision"))

    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.createPolicyRevision')

    mutation_policy_wanNetwork_publishPolicyRevision_parser = mutation_policy_wanNetwork_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_publishPolicyRevision"))

    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.publishPolicyRevision')

    mutation_policy_wanNetwork_discardPolicyRevision_parser = mutation_policy_wanNetwork_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_discardPolicyRevision"))

    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.discardPolicyRevision')

    mutation_policy_wanNetwork_updatePolicy_parser = mutation_policy_wanNetwork_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() wanNetwork operation', 
            usage=get_help("mutation_policy_wanNetwork_updatePolicy"))

    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanNetwork_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanNetwork_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanNetwork.updatePolicy')

    mutation_policy_internetFirewall_parser = mutation_policy_subparsers.add_parser('internetFirewall', 
            help='internetFirewall() policy operation', 
            usage=get_help("mutation_policy_internetFirewall"))

    mutation_policy_internetFirewall_subparsers = mutation_policy_internetFirewall_parser.add_subparsers()

    mutation_policy_internetFirewall_addRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('addRule', 
            help='addRule() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_addRule"))

    mutation_policy_internetFirewall_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addRule')

    mutation_policy_internetFirewall_updateRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateRule', 
            help='updateRule() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_updateRule"))

    mutation_policy_internetFirewall_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateRule')

    mutation_policy_internetFirewall_removeRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeRule', 
            help='removeRule() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_removeRule"))

    mutation_policy_internetFirewall_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeRule')

    mutation_policy_internetFirewall_moveRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveRule', 
            help='moveRule() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_moveRule"))

    mutation_policy_internetFirewall_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveRule')

    mutation_policy_internetFirewall_addSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('addSection', 
            help='addSection() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_addSection"))

    mutation_policy_internetFirewall_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addSection')

    mutation_policy_internetFirewall_updateSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateSection', 
            help='updateSection() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_updateSection"))

    mutation_policy_internetFirewall_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateSection')

    mutation_policy_internetFirewall_removeSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeSection', 
            help='removeSection() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_removeSection"))

    mutation_policy_internetFirewall_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeSection')

    mutation_policy_internetFirewall_moveSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveSection', 
            help='moveSection() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_moveSection"))

    mutation_policy_internetFirewall_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveSection')

    mutation_policy_internetFirewall_createPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_createPolicyRevision"))

    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.createPolicyRevision')

    mutation_policy_internetFirewall_publishPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_publishPolicyRevision"))

    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.publishPolicyRevision')

    mutation_policy_internetFirewall_discardPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_discardPolicyRevision"))

    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.discardPolicyRevision')

    mutation_policy_internetFirewall_updatePolicy_parser = mutation_policy_internetFirewall_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() internetFirewall operation', 
            usage=get_help("mutation_policy_internetFirewall_updatePolicy"))

    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_internetFirewall_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_internetFirewall_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updatePolicy')

    mutation_policy_remotePortFwd_parser = mutation_policy_subparsers.add_parser('remotePortFwd', 
            help='remotePortFwd() policy operation', 
            usage=get_help("mutation_policy_remotePortFwd"))

    mutation_policy_remotePortFwd_subparsers = mutation_policy_remotePortFwd_parser.add_subparsers()

    mutation_policy_remotePortFwd_addRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('addRule', 
            help='addRule() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_addRule"))

    mutation_policy_remotePortFwd_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.addRule')

    mutation_policy_remotePortFwd_updateRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updateRule', 
            help='updateRule() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_updateRule"))

    mutation_policy_remotePortFwd_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updateRule')

    mutation_policy_remotePortFwd_removeRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('removeRule', 
            help='removeRule() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_removeRule"))

    mutation_policy_remotePortFwd_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.removeRule')

    mutation_policy_remotePortFwd_moveRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('moveRule', 
            help='moveRule() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_moveRule"))

    mutation_policy_remotePortFwd_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.moveRule')

    mutation_policy_remotePortFwd_addSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('addSection', 
            help='addSection() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_addSection"))

    mutation_policy_remotePortFwd_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.addSection')

    mutation_policy_remotePortFwd_updateSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updateSection', 
            help='updateSection() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_updateSection"))

    mutation_policy_remotePortFwd_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updateSection')

    mutation_policy_remotePortFwd_removeSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('removeSection', 
            help='removeSection() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_removeSection"))

    mutation_policy_remotePortFwd_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.removeSection')

    mutation_policy_remotePortFwd_moveSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('moveSection', 
            help='moveSection() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_moveSection"))

    mutation_policy_remotePortFwd_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.moveSection')

    mutation_policy_remotePortFwd_createPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_createPolicyRevision"))

    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.createPolicyRevision')

    mutation_policy_remotePortFwd_publishPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_publishPolicyRevision"))

    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.publishPolicyRevision')

    mutation_policy_remotePortFwd_discardPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_discardPolicyRevision"))

    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.discardPolicyRevision')

    mutation_policy_remotePortFwd_updatePolicy_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() remotePortFwd operation', 
            usage=get_help("mutation_policy_remotePortFwd_updatePolicy"))

    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_remotePortFwd_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updatePolicy')

    mutation_policy_wanFirewall_parser = mutation_policy_subparsers.add_parser('wanFirewall', 
            help='wanFirewall() policy operation', 
            usage=get_help("mutation_policy_wanFirewall"))

    mutation_policy_wanFirewall_subparsers = mutation_policy_wanFirewall_parser.add_subparsers()

    mutation_policy_wanFirewall_addRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('addRule', 
            help='addRule() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_addRule"))

    mutation_policy_wanFirewall_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.addRule')

    mutation_policy_wanFirewall_updateRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('updateRule', 
            help='updateRule() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_updateRule"))

    mutation_policy_wanFirewall_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updateRule')

    mutation_policy_wanFirewall_removeRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('removeRule', 
            help='removeRule() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_removeRule"))

    mutation_policy_wanFirewall_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.removeRule')

    mutation_policy_wanFirewall_moveRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('moveRule', 
            help='moveRule() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_moveRule"))

    mutation_policy_wanFirewall_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.moveRule')

    mutation_policy_wanFirewall_addSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('addSection', 
            help='addSection() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_addSection"))

    mutation_policy_wanFirewall_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.addSection')

    mutation_policy_wanFirewall_updateSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('updateSection', 
            help='updateSection() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_updateSection"))

    mutation_policy_wanFirewall_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updateSection')

    mutation_policy_wanFirewall_removeSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('removeSection', 
            help='removeSection() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_removeSection"))

    mutation_policy_wanFirewall_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.removeSection')

    mutation_policy_wanFirewall_moveSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('moveSection', 
            help='moveSection() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_moveSection"))

    mutation_policy_wanFirewall_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.moveSection')

    mutation_policy_wanFirewall_createPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_createPolicyRevision"))

    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.createPolicyRevision')

    mutation_policy_wanFirewall_publishPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_publishPolicyRevision"))

    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.publishPolicyRevision')

    mutation_policy_wanFirewall_discardPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_discardPolicyRevision"))

    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.discardPolicyRevision')

    mutation_policy_wanFirewall_updatePolicy_parser = mutation_policy_wanFirewall_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() wanFirewall operation', 
            usage=get_help("mutation_policy_wanFirewall_updatePolicy"))

    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_wanFirewall_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_wanFirewall_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updatePolicy')

    mutation_policy_appTenantRestriction_parser = mutation_policy_subparsers.add_parser('appTenantRestriction', 
            help='appTenantRestriction() policy operation', 
            usage=get_help("mutation_policy_appTenantRestriction"))

    mutation_policy_appTenantRestriction_subparsers = mutation_policy_appTenantRestriction_parser.add_subparsers()

    mutation_policy_appTenantRestriction_addRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('addRule', 
            help='addRule() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_addRule"))

    mutation_policy_appTenantRestriction_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.addRule')

    mutation_policy_appTenantRestriction_updateRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updateRule', 
            help='updateRule() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_updateRule"))

    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updateRule')

    mutation_policy_appTenantRestriction_removeRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('removeRule', 
            help='removeRule() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_removeRule"))

    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.removeRule')

    mutation_policy_appTenantRestriction_moveRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('moveRule', 
            help='moveRule() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_moveRule"))

    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.moveRule')

    mutation_policy_appTenantRestriction_addSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('addSection', 
            help='addSection() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_addSection"))

    mutation_policy_appTenantRestriction_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.addSection')

    mutation_policy_appTenantRestriction_updateSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updateSection', 
            help='updateSection() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_updateSection"))

    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updateSection')

    mutation_policy_appTenantRestriction_removeSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('removeSection', 
            help='removeSection() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_removeSection"))

    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.removeSection')

    mutation_policy_appTenantRestriction_moveSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('moveSection', 
            help='moveSection() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_moveSection"))

    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.moveSection')

    mutation_policy_appTenantRestriction_createPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_createPolicyRevision"))

    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.createPolicyRevision')

    mutation_policy_appTenantRestriction_publishPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_publishPolicyRevision"))

    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.publishPolicyRevision')

    mutation_policy_appTenantRestriction_discardPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_discardPolicyRevision"))

    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.discardPolicyRevision')

    mutation_policy_appTenantRestriction_updatePolicy_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() appTenantRestriction operation', 
            usage=get_help("mutation_policy_appTenantRestriction_updatePolicy"))

    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_appTenantRestriction_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updatePolicy')

    mutation_policy_applicationControl_parser = mutation_policy_subparsers.add_parser('applicationControl', 
            help='applicationControl() policy operation', 
            usage=get_help("mutation_policy_applicationControl"))

    mutation_policy_applicationControl_subparsers = mutation_policy_applicationControl_parser.add_subparsers()

    mutation_policy_applicationControl_addRule_parser = mutation_policy_applicationControl_subparsers.add_parser('addRule', 
            help='addRule() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_addRule"))

    mutation_policy_applicationControl_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.addRule')

    mutation_policy_applicationControl_updateRule_parser = mutation_policy_applicationControl_subparsers.add_parser('updateRule', 
            help='updateRule() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_updateRule"))

    mutation_policy_applicationControl_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.updateRule')

    mutation_policy_applicationControl_removeRule_parser = mutation_policy_applicationControl_subparsers.add_parser('removeRule', 
            help='removeRule() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_removeRule"))

    mutation_policy_applicationControl_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.removeRule')

    mutation_policy_applicationControl_moveRule_parser = mutation_policy_applicationControl_subparsers.add_parser('moveRule', 
            help='moveRule() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_moveRule"))

    mutation_policy_applicationControl_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.moveRule')

    mutation_policy_applicationControl_addSection_parser = mutation_policy_applicationControl_subparsers.add_parser('addSection', 
            help='addSection() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_addSection"))

    mutation_policy_applicationControl_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.addSection')

    mutation_policy_applicationControl_updateSection_parser = mutation_policy_applicationControl_subparsers.add_parser('updateSection', 
            help='updateSection() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_updateSection"))

    mutation_policy_applicationControl_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.updateSection')

    mutation_policy_applicationControl_removeSection_parser = mutation_policy_applicationControl_subparsers.add_parser('removeSection', 
            help='removeSection() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_removeSection"))

    mutation_policy_applicationControl_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.removeSection')

    mutation_policy_applicationControl_moveSection_parser = mutation_policy_applicationControl_subparsers.add_parser('moveSection', 
            help='moveSection() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_moveSection"))

    mutation_policy_applicationControl_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.moveSection')

    mutation_policy_applicationControl_createPolicyRevision_parser = mutation_policy_applicationControl_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_createPolicyRevision"))

    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.createPolicyRevision')

    mutation_policy_applicationControl_publishPolicyRevision_parser = mutation_policy_applicationControl_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_publishPolicyRevision"))

    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.publishPolicyRevision')

    mutation_policy_applicationControl_discardPolicyRevision_parser = mutation_policy_applicationControl_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_discardPolicyRevision"))

    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.discardPolicyRevision')

    mutation_policy_applicationControl_updatePolicy_parser = mutation_policy_applicationControl_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() applicationControl operation', 
            usage=get_help("mutation_policy_applicationControl_updatePolicy"))

    mutation_policy_applicationControl_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_applicationControl_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_applicationControl_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.applicationControl.updatePolicy')

    mutation_policy_tlsInspect_parser = mutation_policy_subparsers.add_parser('tlsInspect', 
            help='tlsInspect() policy operation', 
            usage=get_help("mutation_policy_tlsInspect"))

    mutation_policy_tlsInspect_subparsers = mutation_policy_tlsInspect_parser.add_subparsers()

    mutation_policy_tlsInspect_addRule_parser = mutation_policy_tlsInspect_subparsers.add_parser('addRule', 
            help='addRule() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_addRule"))

    mutation_policy_tlsInspect_addRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_addRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_addRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.addRule')

    mutation_policy_tlsInspect_updateRule_parser = mutation_policy_tlsInspect_subparsers.add_parser('updateRule', 
            help='updateRule() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_updateRule"))

    mutation_policy_tlsInspect_updateRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_updateRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.updateRule')

    mutation_policy_tlsInspect_removeRule_parser = mutation_policy_tlsInspect_subparsers.add_parser('removeRule', 
            help='removeRule() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_removeRule"))

    mutation_policy_tlsInspect_removeRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_removeRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.removeRule')

    mutation_policy_tlsInspect_moveRule_parser = mutation_policy_tlsInspect_subparsers.add_parser('moveRule', 
            help='moveRule() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_moveRule"))

    mutation_policy_tlsInspect_moveRule_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_moveRule_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.moveRule')

    mutation_policy_tlsInspect_addSection_parser = mutation_policy_tlsInspect_subparsers.add_parser('addSection', 
            help='addSection() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_addSection"))

    mutation_policy_tlsInspect_addSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_addSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_addSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.addSection')

    mutation_policy_tlsInspect_updateSection_parser = mutation_policy_tlsInspect_subparsers.add_parser('updateSection', 
            help='updateSection() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_updateSection"))

    mutation_policy_tlsInspect_updateSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_updateSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.updateSection')

    mutation_policy_tlsInspect_removeSection_parser = mutation_policy_tlsInspect_subparsers.add_parser('removeSection', 
            help='removeSection() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_removeSection"))

    mutation_policy_tlsInspect_removeSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_removeSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.removeSection')

    mutation_policy_tlsInspect_moveSection_parser = mutation_policy_tlsInspect_subparsers.add_parser('moveSection', 
            help='moveSection() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_moveSection"))

    mutation_policy_tlsInspect_moveSection_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_moveSection_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.moveSection')

    mutation_policy_tlsInspect_createPolicyRevision_parser = mutation_policy_tlsInspect_subparsers.add_parser('createPolicyRevision', 
            help='createPolicyRevision() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_createPolicyRevision"))

    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_createPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.createPolicyRevision')

    mutation_policy_tlsInspect_publishPolicyRevision_parser = mutation_policy_tlsInspect_subparsers.add_parser('publishPolicyRevision', 
            help='publishPolicyRevision() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_publishPolicyRevision"))

    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.publishPolicyRevision')

    mutation_policy_tlsInspect_discardPolicyRevision_parser = mutation_policy_tlsInspect_subparsers.add_parser('discardPolicyRevision', 
            help='discardPolicyRevision() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_discardPolicyRevision"))

    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.discardPolicyRevision')

    mutation_policy_tlsInspect_updatePolicy_parser = mutation_policy_tlsInspect_subparsers.add_parser('updatePolicy', 
            help='updatePolicy() tlsInspect operation', 
            usage=get_help("mutation_policy_tlsInspect_updatePolicy"))

    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('json', nargs='?', default='{}', help='Variables in JSON format (defaults to empty object if not provided).')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-accountID', help='The cato account ID to use for this operation. Overrides the account_id value in the profile setting.  This is use for reseller and MSP accounts to run queries against cato sub accounts from the parent account.')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', help='Print GraphQL query without sending API call')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', help='Verbose output')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', help='Pretty print')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-n', '--stream-events', dest='stream_events', help='Send events over network to host:port TCP')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-z', '--sentinel', dest='sentinel', help='Send events to Sentinel customerid:sharedkey')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('-H', '--header', action='append', dest='headers', help='Add custom headers in "Key: Value" format. Can be used multiple times.')
    mutation_policy_tlsInspect_updatePolicy_parser.add_argument('--headers-file', dest='headers_file', help='Load headers from a file. Each line should contain a header in "Key: Value" format.')
    mutation_policy_tlsInspect_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.tlsInspect.updatePolicy')
