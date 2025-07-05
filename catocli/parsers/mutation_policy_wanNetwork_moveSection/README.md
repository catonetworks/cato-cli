
## CATO-CLI - mutation.policy.wanNetwork.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.moveSection:

`catocli mutation policy wanNetwork moveSection -h`

`catocli mutation policy wanNetwork moveSection <json>`

`catocli mutation policy wanNetwork moveSection "$(cat < moveSection.json)"`

`catocli mutation policy wanNetwork moveSection '{"policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.moveSection ####
`accountId` [ID] - (required) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
