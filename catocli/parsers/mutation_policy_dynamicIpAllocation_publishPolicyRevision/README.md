
## CATO-CLI - mutation.policy.dynamicIpAllocation.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.publishPolicyRevision:

`catocli mutation policy dynamicIpAllocation publishPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision "$(cat < mutation.policy.dynamicIpAllocation.publishPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy dynamicIpAllocation publishPolicyRevision -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
