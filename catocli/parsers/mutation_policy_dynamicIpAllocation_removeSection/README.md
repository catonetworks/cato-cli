
## CATO-CLI - mutation.policy.dynamicIpAllocation.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.removeSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.removeSection:

`catocli mutation policy dynamicIpAllocation removeSection -h`

`catocli mutation policy dynamicIpAllocation removeSection <json>`

`catocli mutation policy dynamicIpAllocation removeSection "$(cat < mutation.policy.dynamicIpAllocation.removeSection.json)"`

`catocli mutation policy dynamicIpAllocation removeSection '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'`

`catocli mutation policy dynamicIpAllocation removeSection -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.removeSection ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
