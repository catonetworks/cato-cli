
## CATO-CLI - mutation.policy.dynamicIpAllocation.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.discardPolicyRevision:

`catocli mutation policy dynamicIpAllocation discardPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision "$(cat < discardPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyDiscardRevisionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.discardPolicyRevision ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (optional) N/A 
