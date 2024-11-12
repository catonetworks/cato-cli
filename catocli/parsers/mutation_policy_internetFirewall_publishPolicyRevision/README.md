
## CATO-CLI - mutation.policy.internetFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.publishPolicyRevision:

`catocli mutation policy internetFirewall publishPolicyRevision -h`

`catocli mutation policy internetFirewall publishPolicyRevision <json>`

`catocli mutation policy internetFirewall publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy internetFirewall publishPolicyRevision '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
