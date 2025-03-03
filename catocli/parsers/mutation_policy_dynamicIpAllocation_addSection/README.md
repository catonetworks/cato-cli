
## CATO-CLI - mutation.policy.dynamicIpAllocation.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.addSection:

`catocli mutation policy dynamicIpAllocation addSection -h`

`catocli mutation policy dynamicIpAllocation addSection <json>`

`catocli mutation policy dynamicIpAllocation addSection "$(cat < addSection.json)"`

`catocli mutation policy dynamicIpAllocation addSection '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.addSection ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
