
## CATO-CLI - mutation.policy.dynamicIpAllocation.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.updateSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updateSection:

`catocli mutation policy dynamicIpAllocation updateSection -h`

`catocli mutation policy dynamicIpAllocation updateSection <json>`

`catocli mutation policy dynamicIpAllocation updateSection "$(cat < mutation.policy.dynamicIpAllocation.updateSection.json)"`

`catocli mutation policy dynamicIpAllocation updateSection '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}}}'`

`catocli mutation policy dynamicIpAllocation updateSection -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.updateSection ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
