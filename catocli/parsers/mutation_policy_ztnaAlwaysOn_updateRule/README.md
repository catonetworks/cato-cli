
## CATO-CLI - mutation.policy.ztnaAlwaysOn.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.updateRule) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.updateRule:

```bash
catocli mutation policy ztnaAlwaysOn updateRule -h

catocli mutation policy ztnaAlwaysOn updateRule <json>

catocli mutation policy ztnaAlwaysOn updateRule --json-file mutation.policy.ztnaAlwaysOn.updateRule.json

catocli mutation policy ztnaAlwaysOn updateRule '{"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"ztnaAlwaysOnUpdateRuleInput":{"id":"id","ztnaAlwaysOnUpdateRuleDataInput":{"action":"ENFORCE","allowFailOpen":true,"allowUserBypass":true,"antiTamperMode":"OFF","bypassDuration":{"time":1,"unit":"MINUTES"},"description":"string","devicePostureProfile":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}}}}'

catocli mutation policy ztnaAlwaysOn updateRule '{
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "ztnaAlwaysOnUpdateRuleInput": {
        "id": "id",
        "ztnaAlwaysOnUpdateRuleDataInput": {
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
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.updateRule ####

`accountId` [ID] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
`ztnaAlwaysOnUpdateRuleInput` [ZtnaAlwaysOnUpdateRuleInput] - (required) N/A    
