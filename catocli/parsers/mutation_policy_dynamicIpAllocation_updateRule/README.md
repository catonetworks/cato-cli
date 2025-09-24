
## CATO-CLI - mutation.policy.dynamicIpAllocation.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.updateRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updateRule:

`catocli mutation policy dynamicIpAllocation updateRule -h`

`catocli mutation policy dynamicIpAllocation updateRule <json>`

`catocli mutation policy dynamicIpAllocation updateRule "$(cat < mutation.policy.dynamicIpAllocation.updateRule.json)"`

`catocli mutation policy dynamicIpAllocation updateRule '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"dynamicIpAllocationUpdateRuleInput":{"dynamicIpAllocationUpdateRuleDataInput":{"country":{"by":"ID","input":"string"},"description":"string","enabled":true,"name":"string","platform":"WINDOWS","range":{"globalIpRange":{"by":"ID","input":"string"}},"source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"id":"id"}}'`

`catocli mutation policy dynamicIpAllocation updateRule -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "dynamicIpAllocationUpdateRuleInput": {
        "dynamicIpAllocationUpdateRuleDataInput": {
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
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.updateRule ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`dynamicIpAllocationUpdateRuleInput` [DynamicIpAllocationUpdateRuleInput] - (required) N/A    
