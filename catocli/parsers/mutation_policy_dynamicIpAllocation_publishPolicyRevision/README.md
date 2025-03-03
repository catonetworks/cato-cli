
## CATO-CLI - mutation.policy.dynamicIpAllocation.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.publishPolicyRevision:

`catocli mutation policy dynamicIpAllocation publishPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
