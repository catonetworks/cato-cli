
## CATO-CLI - mutation.policy.dynamicIpAllocation.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.createPolicyRevision:

`catocli mutation policy dynamicIpAllocation createPolicyRevision -h`

`catocli mutation policy dynamicIpAllocation createPolicyRevision <json>`

`catocli mutation policy dynamicIpAllocation createPolicyRevision "$(cat < mutation.policy.dynamicIpAllocation.createPolicyRevision.json)"`

`catocli mutation policy dynamicIpAllocation createPolicyRevision '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyCreateRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy dynamicIpAllocation createPolicyRevision -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
