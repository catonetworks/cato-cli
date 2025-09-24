
## CATO-CLI - mutation.policy.dynamicIpAllocation.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.addRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.addRule:

`catocli mutation policy dynamicIpAllocation addRule -h`

`catocli mutation policy dynamicIpAllocation addRule <json>`

`catocli mutation policy dynamicIpAllocation addRule "$(cat < mutation.policy.dynamicIpAllocation.addRule.json)"`

`catocli mutation policy dynamicIpAllocation addRule '{"dynamicIpAllocationAddRuleInput":{"dynamicIpAllocationAddRuleDataInput":{"country":{"by":"ID","input":"string"},"description":"string","enabled":true,"name":"string","platform":"WINDOWS","range":{"globalIpRange":{"by":"ID","input":"string"}},"source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy dynamicIpAllocation addRule -p '{
    "dynamicIpAllocationAddRuleInput": {
        "dynamicIpAllocationAddRuleDataInput": {
            "country": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "enabled": true,
            "name": "string",
            "platform": "WINDOWS",
            "range": {
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "source": {
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "usersGroup": {
                    "by": "ID",
                    "input": "string"
                }
            }
        },
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.addRule ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationAddRuleInput` [DynamicIpAllocationAddRuleInput] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
