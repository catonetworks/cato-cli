
## CATO-CLI - mutation.policy.socketLan.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.addSection:

`catocli mutation policy socketLan addSection -h`

`catocli mutation policy socketLan addSection <json>`

`catocli mutation policy socketLan addSection "$(cat < addSection.json)"`

`catocli mutation policy socketLan addSection '{"policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "socketLanPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.socketLan.addSection ####
`accountId` [ID] - (required) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (optional) N/A 
