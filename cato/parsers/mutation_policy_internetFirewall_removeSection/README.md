
## CATO-CLI - mutation.policy.internetFirewall.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeSection:

`cato mutation policy internetFirewall removeSection -h`

`cato mutation policy internetFirewall removeSection <accountID> <json>`

`cato mutation policy internetFirewall removeSection 12345 "$(cat < removeSection.json)"`

`cato mutation policy internetFirewall removeSection 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyRemoveSectionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.removeSection ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
