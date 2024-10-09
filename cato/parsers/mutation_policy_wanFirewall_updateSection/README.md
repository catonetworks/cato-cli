
## CATO-CLI - mutation.policy.wanFirewall.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updateSection:

`cato mutation policy wanFirewall updateSection -h`

`cato mutation policy wanFirewall updateSection <accountID> <json>`

`cato mutation policy wanFirewall updateSection 12345 "$(cat < updateSection.json)"`

`cato mutation policy wanFirewall updateSection 12345 '{"PolicyUpdateSectionInput": {"PolicyUpdateSectionInfoInput": {"name": {"name": "String"}}, "id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.updateSection ####
`PolicyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
