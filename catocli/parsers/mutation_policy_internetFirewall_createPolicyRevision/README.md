
## CATO-CLI - mutation.policy.internetFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.createPolicyRevision:

`catocli mutation policy internetFirewall createPolicyRevision -h`

`catocli mutation policy internetFirewall createPolicyRevision <json>`

`catocli mutation policy internetFirewall createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy internetFirewall createPolicyRevision '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
