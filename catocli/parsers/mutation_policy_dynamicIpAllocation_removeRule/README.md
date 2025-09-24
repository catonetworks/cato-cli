
## CATO-CLI - mutation.policy.dynamicIpAllocation.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.removeRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.removeRule:

`catocli mutation policy dynamicIpAllocation removeRule -h`

`catocli mutation policy dynamicIpAllocation removeRule <json>`

`catocli mutation policy dynamicIpAllocation removeRule "$(cat < mutation.policy.dynamicIpAllocation.removeRule.json)"`

`catocli mutation policy dynamicIpAllocation removeRule '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"dynamicIpAllocationRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy dynamicIpAllocation removeRule -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "dynamicIpAllocationRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.removeRule ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`dynamicIpAllocationRemoveRuleInput` [DynamicIpAllocationRemoveRuleInput] - (required) N/A    
