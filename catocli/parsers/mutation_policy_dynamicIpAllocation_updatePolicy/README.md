
## CATO-CLI - mutation.policy.dynamicIpAllocation.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updatePolicy:

`catocli mutation policy dynamicIpAllocation updatePolicy -h`

`catocli mutation policy dynamicIpAllocation updatePolicy <json>`

`catocli mutation policy dynamicIpAllocation updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy dynamicIpAllocation updatePolicy '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "dynamicIpAllocationPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.updatePolicy ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`dynamicIpAllocationPolicyUpdateInput` [DynamicIpAllocationPolicyUpdateInput] - (required) N/A 
