
## CATO-CLI - mutation.policy.wanNetwork.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.addSection:

`catocli mutation policy wanNetwork addSection -h`

`catocli mutation policy wanNetwork addSection <json>`

`catocli mutation policy wanNetwork addSection "$(cat < addSection.json)"`

`catocli mutation policy wanNetwork addSection '{"policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.addSection ####
`accountId` [ID] - (required) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
