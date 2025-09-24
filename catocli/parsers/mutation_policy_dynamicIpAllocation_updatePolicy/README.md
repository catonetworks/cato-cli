
## CATO-CLI - mutation.policy.dynamicIpAllocation.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updatePolicy:

`catocli mutation policy dynamicIpAllocation updatePolicy -h`

`catocli mutation policy dynamicIpAllocation updatePolicy <json>`

`catocli mutation policy dynamicIpAllocation updatePolicy "$(cat < mutation.policy.dynamicIpAllocation.updatePolicy.json)"`

`catocli mutation policy dynamicIpAllocation updatePolicy '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"dynamicIpAllocationPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy dynamicIpAllocation updatePolicy -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "dynamicIpAllocationPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.updatePolicy ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`dynamicIpAllocationPolicyUpdateInput` [DynamicIpAllocationPolicyUpdateInput] - (required) N/A    
