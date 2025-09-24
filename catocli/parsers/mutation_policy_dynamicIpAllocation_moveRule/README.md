
## CATO-CLI - mutation.policy.dynamicIpAllocation.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.moveRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.moveRule:

`catocli mutation policy dynamicIpAllocation moveRule -h`

`catocli mutation policy dynamicIpAllocation moveRule <json>`

`catocli mutation policy dynamicIpAllocation moveRule "$(cat < mutation.policy.dynamicIpAllocation.moveRule.json)"`

`catocli mutation policy dynamicIpAllocation moveRule '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}}}'`

`catocli mutation policy dynamicIpAllocation moveRule -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.moveRule ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
