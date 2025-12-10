
## CATO-CLI - mutation.policy.ztnaAlwaysOn.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.addRule) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.addRule:

```bash
catocli mutation policy ztnaAlwaysOn addRule -h

catocli mutation policy ztnaAlwaysOn addRule <json>

catocli mutation policy ztnaAlwaysOn addRule --json-file mutation.policy.ztnaAlwaysOn.addRule.json

catocli mutation policy ztnaAlwaysOn addRule '{"ztnaAlwaysOnAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"ztnaAlwaysOnAddRuleDataInput":{"action":"ENFORCE","allowFailOpen":true,"allowUserBypass":true,"antiTamperMode":"OFF","bypassDuration":{"time":1,"unit":"MINUTES"},"description":"string","devicePostureProfile":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}}},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn addRule '{
    "ztnaAlwaysOnAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "ztnaAlwaysOnAddRuleDataInput": {
            "action": "ENFORCE",
            "allowFailOpen": true,
            "allowUserBypass": true,
            "antiTamperMode": "OFF",
            "bypassDuration": {
                "time": 1,
                "unit": "MINUTES"
            },
            "description": "string",
            "devicePostureProfile": {
                "by": "ID",
                "input": "string"
            },
            "enabled": true,
            "name": "string",
            "platform": "WINDOWS",
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
        }
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.addRule ####

`accountId` [ID] - (required) N/A    
`ztnaAlwaysOnAddRuleInput` [ZtnaAlwaysOnAddRuleInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
