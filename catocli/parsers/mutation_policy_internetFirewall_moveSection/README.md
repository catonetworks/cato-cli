
## CATO-CLI - mutation.policy.internetFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveSection:

`catocli mutation policy internetFirewall moveSection -h`

`catocli mutation policy internetFirewall moveSection <accountID> <json>`

`catocli mutation policy internetFirewall moveSection 12345 "$(cat < moveSection.json)"`

`catocli mutation policy internetFirewall moveSection 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyMoveSectionInput": {"PolicySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveSection ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`accountId` [ID] - (required) N/A 