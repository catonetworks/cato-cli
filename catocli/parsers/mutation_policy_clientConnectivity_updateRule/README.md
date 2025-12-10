
## CATO-CLI - mutation.policy.clientConnectivity.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.updateRule) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.updateRule:

```bash
catocli mutation policy clientConnectivity updateRule -h

catocli mutation policy clientConnectivity updateRule <json>

catocli mutation policy clientConnectivity updateRule --json-file mutation.policy.clientConnectivity.updateRule.json

catocli mutation policy clientConnectivity updateRule '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"clientConnectivityUpdateRuleInput":{"clientConnectivityUpdateRuleDataInput":{"action":"ALLOW","confidenceLevel":"HIGH","connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","device":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"sourceRange":{"globalIpRange":{"by":"ID","input":"string"}}},"id":"id"}}'

catocli mutation policy clientConnectivity updateRule '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "clientConnectivityUpdateRuleInput": {
        "clientConnectivityUpdateRuleDataInput": {
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
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.updateRule ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`clientConnectivityUpdateRuleInput` [ClientConnectivityUpdateRuleInput] - (required) N/A    
