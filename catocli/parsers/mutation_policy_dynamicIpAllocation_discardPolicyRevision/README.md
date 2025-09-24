
## CATO-CLI - mutation.policy.dynamicIpAllocation.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.discardPolicyRevision:

`catocli mutation policy dynamicIpAllocation discardPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision "$(cat < mutation.policy.dynamicIpAllocation.discardPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyDiscardRevisionInput":{"id":"id"}}'`

`catocli mutation policy dynamicIpAllocation discardPolicyRevision -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyDiscardRevisionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
