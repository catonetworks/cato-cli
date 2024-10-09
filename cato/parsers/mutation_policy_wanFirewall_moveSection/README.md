
## CATO-CLI - mutation.policy.wanFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveSection:

`cato mutation policy wanFirewall moveSection -h`

`cato mutation policy wanFirewall moveSection <accountID> <json>`

`cato mutation policy wanFirewall moveSection 12345 "$(cat < moveSection.json)"`

`cato mutation policy wanFirewall moveSection 12345 '{"PolicyMoveSectionInput": {"PolicySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveSection ####
`PolicyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
