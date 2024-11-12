
## CATO-CLI - mutation.policy.internetFirewall.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updateSection:

`catocli mutation policy internetFirewall updateSection -h`

`catocli mutation policy internetFirewall updateSection <json>`

`catocli mutation policy internetFirewall updateSection "$(cat < updateSection.json)"`

`catocli mutation policy internetFirewall updateSection '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyUpdateSectionInput": {"id": {"id": "ID"}, "policyUpdateSectionInfoInput": {"name": {"name": "String"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.updateSection ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A 
