
## CATO-CLI - mutation.policy.dynamicIpAllocation.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.moveSection:

`catocli mutation policy dynamicIpAllocation moveSection -h`

`catocli mutation policy dynamicIpAllocation moveSection <json>`

`catocli mutation policy dynamicIpAllocation moveSection "$(cat < moveSection.json)"`

`catocli mutation policy dynamicIpAllocation moveSection '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.moveSection ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
