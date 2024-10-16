
## CATO-CLI - mutation.policy.wanFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveSection:

`catocli mutation policy wanFirewall moveSection -h`

`catocli mutation policy wanFirewall moveSection <json>`

`catocli mutation policy wanFirewall moveSection "$(cat < moveSection.json)"`

`catocli mutation policy wanFirewall moveSection '{"PolicyMoveSectionInput": {"PolicySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveSection ####
`PolicyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
