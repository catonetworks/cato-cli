
## CATO-CLI - mutation.policy.wanFirewall.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeSection:

`cato mutation policy wanFirewall removeSection -h`

`cato mutation policy wanFirewall removeSection <accountID> <json>`

`cato mutation policy wanFirewall removeSection 12345 "$(cat < removeSection.json)"`

`cato mutation policy wanFirewall removeSection 12345 '{"PolicyRemoveSectionInput": {"id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.removeSection ####
`PolicyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
