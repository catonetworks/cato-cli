
## CATO-CLI - mutation.policy.dynamicIpAllocation.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updateSection:

`catocli mutation policy dynamicIpAllocation updateSection -h`

`catocli mutation policy dynamicIpAllocation updateSection <json>`

`catocli mutation policy dynamicIpAllocation updateSection "$(cat < updateSection.json)"`

`catocli mutation policy dynamicIpAllocation updateSection '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyUpdateSectionInput": {"id": {"id": "ID"}, "policyUpdateSectionInfoInput": {"name": {"name": "String"}}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.updateSection ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A 
