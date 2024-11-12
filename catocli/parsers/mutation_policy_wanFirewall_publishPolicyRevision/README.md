
## CATO-CLI - mutation.policy.wanFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.publishPolicyRevision:

`catocli mutation policy wanFirewall publishPolicyRevision -h`

`catocli mutation policy wanFirewall publishPolicyRevision <json>`

`catocli mutation policy wanFirewall publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy wanFirewall publishPolicyRevision '{"policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
