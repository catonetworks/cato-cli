
from ..parserApiClient import createRequest, get_help

def mutation_policy_parse(mutation_subparsers):
	mutation_policy_parser = mutation_subparsers.add_parser('policy', 
			help='policy() mutation operation', 
			usage=get_help("mutation_policy"))

	mutation_policy_subparsers = mutation_policy_parser.add_subparsers()

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
