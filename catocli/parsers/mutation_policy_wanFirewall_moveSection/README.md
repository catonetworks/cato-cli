
## CATO-CLI - mutation.policy.wanFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveSection:

`catocli mutation policy wanFirewall moveSection -h`

`catocli mutation policy wanFirewall moveSection <json>`

`catocli mutation policy wanFirewall moveSection "$(cat < moveSection.json)"`

`catocli mutation policy wanFirewall moveSection '{"policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveSection ####
`accountId` [ID] - (required) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
