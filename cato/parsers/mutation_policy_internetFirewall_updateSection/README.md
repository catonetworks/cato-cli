
## CATO-CLI - mutation.policy.internetFirewall.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updateSection:

`cato mutation policy internetFirewall updateSection -h`

`cato mutation policy internetFirewall updateSection <accountID> <json>`

`cato mutation policy internetFirewall updateSection 12345 "$(cat < updateSection.json)"`

`cato mutation policy internetFirewall updateSection 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyUpdateSectionInput": {"PolicyUpdateSectionInfoInput": {"name": {"name": "String"}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.updateSection ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
