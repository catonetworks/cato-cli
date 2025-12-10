
## CATO-CLI - mutation.policy.clientConnectivity.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.addRule) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.addRule:

```bash
catocli mutation policy clientConnectivity addRule -h

catocli mutation policy clientConnectivity addRule <json>

catocli mutation policy clientConnectivity addRule --json-file mutation.policy.clientConnectivity.addRule.json

catocli mutation policy clientConnectivity addRule '{"clientConnectivityAddRuleInput":{"clientConnectivityAddRuleDataInput":{"action":"ALLOW","confidenceLevel":"HIGH","connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","device":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"sourceRange":{"globalIpRange":{"by":"ID","input":"string"}}},"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy clientConnectivity addRule '{
    "clientConnectivityAddRuleInput": {
        "clientConnectivityAddRuleDataInput": {
            "action": "ALLOW",
            "confidenceLevel": "HIGH",
            "connectionOrigin": "ANY",
            "country": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "device": {
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
            },
            "sourceRange": {
                "globalIpRange": {
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
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.addRule ####

`accountId` [ID] - (required) N/A    
`clientConnectivityAddRuleInput` [ClientConnectivityAddRuleInput] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
