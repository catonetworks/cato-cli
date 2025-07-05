
## CATO-CLI - mutation.policy.socketLan.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.moveSection:

`catocli mutation policy socketLan moveSection -h`

`catocli mutation policy socketLan moveSection <json>`

`catocli mutation policy socketLan moveSection "$(cat < moveSection.json)"`

`catocli mutation policy socketLan moveSection '{"policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "socketLanPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.socketLan.moveSection ####
`accountId` [ID] - (required) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (optional) N/A 
