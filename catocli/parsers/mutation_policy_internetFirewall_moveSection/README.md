
## CATO-CLI - mutation.policy.internetFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveSection:

`catocli mutation policy internetFirewall moveSection -h`

`catocli mutation policy internetFirewall moveSection <json>`

`catocli mutation policy internetFirewall moveSection "$(cat < moveSection.json)"`

`catocli mutation policy internetFirewall moveSection '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveSection ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
