
from ..parserApiClient import createRequest, get_help

def mutation_policy_parse(mutation_subparsers):
	mutation_policy_parser = mutation_subparsers.add_parser('policy', 
			help='policy() mutation operation', 
			usage=get_help("mutation_policy"))

	mutation_policy_subparsers = mutation_policy_parser.add_subparsers()

	mutation_policy_appTenantRestriction_parser = mutation_policy_subparsers.add_parser('appTenantRestriction', 
			help='appTenantRestriction() policy operation', 
			usage=get_help("mutation_policy_appTenantRestriction"))

	mutation_policy_appTenantRestriction_subparsers = mutation_policy_appTenantRestriction_parser.add_subparsers()

	mutation_policy_appTenantRestriction_addRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('addRule', 
			help='addRule() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_addRule"))

	mutation_policy_appTenantRestriction_addRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_addRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.addRule')

	mutation_policy_appTenantRestriction_addSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('addSection', 
			help='addSection() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_addSection"))

	mutation_policy_appTenantRestriction_addSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_addSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.addSection')

	mutation_policy_appTenantRestriction_createPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('createPolicyRevision', 
			help='createPolicyRevision() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_createPolicyRevision"))

	mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.createPolicyRevision')

	mutation_policy_appTenantRestriction_discardPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('discardPolicyRevision', 
			help='discardPolicyRevision() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_discardPolicyRevision"))

	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.discardPolicyRevision')

	mutation_policy_appTenantRestriction_moveRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('moveRule', 
			help='moveRule() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_moveRule"))

	mutation_policy_appTenantRestriction_moveRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.moveRule')

	mutation_policy_appTenantRestriction_moveSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('moveSection', 
			help='moveSection() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_moveSection"))

	mutation_policy_appTenantRestriction_moveSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.moveSection')

	mutation_policy_appTenantRestriction_publishPolicyRevision_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('publishPolicyRevision', 
			help='publishPolicyRevision() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_publishPolicyRevision"))

	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.publishPolicyRevision')

	mutation_policy_appTenantRestriction_removeRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('removeRule', 
			help='removeRule() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_removeRule"))

	mutation_policy_appTenantRestriction_removeRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.removeRule')

	mutation_policy_appTenantRestriction_removeSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('removeSection', 
			help='removeSection() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_removeSection"))

	mutation_policy_appTenantRestriction_removeSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.removeSection')

	mutation_policy_appTenantRestriction_updatePolicy_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updatePolicy', 
			help='updatePolicy() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_updatePolicy"))

	mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updatePolicy')

	mutation_policy_appTenantRestriction_updateRule_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updateRule', 
			help='updateRule() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_updateRule"))

	mutation_policy_appTenantRestriction_updateRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updateRule')

	mutation_policy_appTenantRestriction_updateSection_parser = mutation_policy_appTenantRestriction_subparsers.add_parser('updateSection', 
			help='updateSection() appTenantRestriction operation', 
			usage=get_help("mutation_policy_appTenantRestriction_updateSection"))

	mutation_policy_appTenantRestriction_updateSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_appTenantRestriction_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_appTenantRestriction_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.appTenantRestriction.updateSection')

	mutation_policy_internetFirewall_parser = mutation_policy_subparsers.add_parser('internetFirewall', 
			help='internetFirewall() policy operation', 
			usage=get_help("mutation_policy_internetFirewall"))

	mutation_policy_internetFirewall_subparsers = mutation_policy_internetFirewall_parser.add_subparsers()

	mutation_policy_internetFirewall_addRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('addRule', 
			help='addRule() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_addRule"))

	mutation_policy_internetFirewall_addRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addRule')

	mutation_policy_internetFirewall_addSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('addSection', 
			help='addSection() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_addSection"))

	mutation_policy_internetFirewall_addSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addSection')

	mutation_policy_internetFirewall_createPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('createPolicyRevision', 
			help='createPolicyRevision() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_createPolicyRevision"))

	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.createPolicyRevision')

	mutation_policy_internetFirewall_discardPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('discardPolicyRevision', 
			help='discardPolicyRevision() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_discardPolicyRevision"))

	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.discardPolicyRevision')

	mutation_policy_internetFirewall_moveRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveRule', 
			help='moveRule() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_moveRule"))

	mutation_policy_internetFirewall_moveRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveRule')

	mutation_policy_internetFirewall_moveSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveSection', 
			help='moveSection() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_moveSection"))

	mutation_policy_internetFirewall_moveSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveSection')

	mutation_policy_internetFirewall_publishPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('publishPolicyRevision', 
			help='publishPolicyRevision() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_publishPolicyRevision"))

	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.publishPolicyRevision')

	mutation_policy_internetFirewall_removeRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeRule', 
			help='removeRule() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_removeRule"))

	mutation_policy_internetFirewall_removeRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeRule')

	mutation_policy_internetFirewall_removeSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeSection', 
			help='removeSection() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_removeSection"))

	mutation_policy_internetFirewall_removeSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeSection')

	mutation_policy_internetFirewall_updatePolicy_parser = mutation_policy_internetFirewall_subparsers.add_parser('updatePolicy', 
			help='updatePolicy() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_updatePolicy"))

	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updatePolicy')

	mutation_policy_internetFirewall_updateRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateRule', 
			help='updateRule() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_updateRule"))

	mutation_policy_internetFirewall_updateRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateRule')

	mutation_policy_internetFirewall_updateSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateSection', 
			help='updateSection() internetFirewall operation', 
			usage=get_help("mutation_policy_internetFirewall_updateSection"))

	mutation_policy_internetFirewall_updateSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateSection')

	mutation_policy_remotePortFwd_parser = mutation_policy_subparsers.add_parser('remotePortFwd', 
			help='remotePortFwd() policy operation', 
			usage=get_help("mutation_policy_remotePortFwd"))

	mutation_policy_remotePortFwd_subparsers = mutation_policy_remotePortFwd_parser.add_subparsers()

	mutation_policy_remotePortFwd_addRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('addRule', 
			help='addRule() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_addRule"))

	mutation_policy_remotePortFwd_addRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_addRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.addRule')

	mutation_policy_remotePortFwd_addSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('addSection', 
			help='addSection() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_addSection"))

	mutation_policy_remotePortFwd_addSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_addSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.addSection')

	mutation_policy_remotePortFwd_createPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('createPolicyRevision', 
			help='createPolicyRevision() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_createPolicyRevision"))

	mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.createPolicyRevision')

	mutation_policy_remotePortFwd_discardPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('discardPolicyRevision', 
			help='discardPolicyRevision() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_discardPolicyRevision"))

	mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.discardPolicyRevision')

	mutation_policy_remotePortFwd_moveRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('moveRule', 
			help='moveRule() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_moveRule"))

	mutation_policy_remotePortFwd_moveRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_moveRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.moveRule')

	mutation_policy_remotePortFwd_moveSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('moveSection', 
			help='moveSection() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_moveSection"))

	mutation_policy_remotePortFwd_moveSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_moveSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.moveSection')

	mutation_policy_remotePortFwd_publishPolicyRevision_parser = mutation_policy_remotePortFwd_subparsers.add_parser('publishPolicyRevision', 
			help='publishPolicyRevision() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_publishPolicyRevision"))

	mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.publishPolicyRevision')

	mutation_policy_remotePortFwd_removeRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('removeRule', 
			help='removeRule() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_removeRule"))

	mutation_policy_remotePortFwd_removeRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_removeRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.removeRule')

	mutation_policy_remotePortFwd_removeSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('removeSection', 
			help='removeSection() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_removeSection"))

	mutation_policy_remotePortFwd_removeSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_removeSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.removeSection')

	mutation_policy_remotePortFwd_updatePolicy_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updatePolicy', 
			help='updatePolicy() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_updatePolicy"))

	mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updatePolicy')

	mutation_policy_remotePortFwd_updateRule_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updateRule', 
			help='updateRule() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_updateRule"))

	mutation_policy_remotePortFwd_updateRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_updateRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updateRule')

	mutation_policy_remotePortFwd_updateSection_parser = mutation_policy_remotePortFwd_subparsers.add_parser('updateSection', 
			help='updateSection() remotePortFwd operation', 
			usage=get_help("mutation_policy_remotePortFwd_updateSection"))

	mutation_policy_remotePortFwd_updateSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_remotePortFwd_updateSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_remotePortFwd_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_remotePortFwd_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_remotePortFwd_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_remotePortFwd_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.remotePortFwd.updateSection')

	mutation_policy_wanFirewall_parser = mutation_policy_subparsers.add_parser('wanFirewall', 
			help='wanFirewall() policy operation', 
			usage=get_help("mutation_policy_wanFirewall"))

	mutation_policy_wanFirewall_subparsers = mutation_policy_wanFirewall_parser.add_subparsers()

	mutation_policy_wanFirewall_addRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('addRule', 
			help='addRule() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_addRule"))

	mutation_policy_wanFirewall_addRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_addRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.addRule')

	mutation_policy_wanFirewall_addSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('addSection', 
			help='addSection() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_addSection"))

	mutation_policy_wanFirewall_addSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_addSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.addSection')

	mutation_policy_wanFirewall_createPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('createPolicyRevision', 
			help='createPolicyRevision() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_createPolicyRevision"))

	mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.createPolicyRevision')

	mutation_policy_wanFirewall_discardPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('discardPolicyRevision', 
			help='discardPolicyRevision() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_discardPolicyRevision"))

	mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.discardPolicyRevision')

	mutation_policy_wanFirewall_moveRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('moveRule', 
			help='moveRule() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_moveRule"))

	mutation_policy_wanFirewall_moveRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_moveRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.moveRule')

	mutation_policy_wanFirewall_moveSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('moveSection', 
			help='moveSection() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_moveSection"))

	mutation_policy_wanFirewall_moveSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_moveSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.moveSection')

	mutation_policy_wanFirewall_publishPolicyRevision_parser = mutation_policy_wanFirewall_subparsers.add_parser('publishPolicyRevision', 
			help='publishPolicyRevision() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_publishPolicyRevision"))

	mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.publishPolicyRevision')

	mutation_policy_wanFirewall_removeRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('removeRule', 
			help='removeRule() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_removeRule"))

	mutation_policy_wanFirewall_removeRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_removeRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.removeRule')

	mutation_policy_wanFirewall_removeSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('removeSection', 
			help='removeSection() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_removeSection"))

	mutation_policy_wanFirewall_removeSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_removeSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.removeSection')

	mutation_policy_wanFirewall_updatePolicy_parser = mutation_policy_wanFirewall_subparsers.add_parser('updatePolicy', 
			help='updatePolicy() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_updatePolicy"))

	mutation_policy_wanFirewall_updatePolicy_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updatePolicy')

	mutation_policy_wanFirewall_updateRule_parser = mutation_policy_wanFirewall_subparsers.add_parser('updateRule', 
			help='updateRule() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_updateRule"))

	mutation_policy_wanFirewall_updateRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_updateRule_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updateRule')

	mutation_policy_wanFirewall_updateSection_parser = mutation_policy_wanFirewall_subparsers.add_parser('updateSection', 
			help='updateSection() wanFirewall operation', 
			usage=get_help("mutation_policy_wanFirewall_updateSection"))

	mutation_policy_wanFirewall_updateSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_wanFirewall_updateSection_parser.add_argument('-accountID', help='Override the CATO_ACCOUNT_ID environment variable with this value.')
	mutation_policy_wanFirewall_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_wanFirewall_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_wanFirewall_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_wanFirewall_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.wanFirewall.updateSection')
