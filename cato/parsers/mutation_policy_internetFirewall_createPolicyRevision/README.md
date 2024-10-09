
## CATO-CLI - mutation.policy.internetFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.createPolicyRevision:

`cato mutation policy internetFirewall createPolicyRevision -h`

`cato mutation policy internetFirewall createPolicyRevision <accountID> <json>`

`cato mutation policy internetFirewall createPolicyRevision 12345 "$(cat < createPolicyRevision.json)"`

`cato mutation policy internetFirewall createPolicyRevision 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.createPolicyRevision ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
