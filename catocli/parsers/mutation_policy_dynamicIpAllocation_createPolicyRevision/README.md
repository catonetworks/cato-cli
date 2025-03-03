
## CATO-CLI - mutation.policy.dynamicIpAllocation.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.createPolicyRevision:

`catocli mutation policy dynamicIpAllocation createPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation createPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation createPolicyRevision '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
