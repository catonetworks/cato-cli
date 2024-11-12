
## CATO-CLI - mutation.policy.wanFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.createPolicyRevision:

`catocli mutation policy wanFirewall createPolicyRevision -h`

`catocli mutation policy wanFirewall createPolicyRevision <json>`

`catocli mutation policy wanFirewall createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy wanFirewall createPolicyRevision '{"policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
