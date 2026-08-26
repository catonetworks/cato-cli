
## CATO-CLI - mutation.policy.privateAccess.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.updateRule) for documentation on this operation.

### Usage for mutation.policy.privateAccess.updateRule:

```bash
catocli mutation policy privateAccess updateRule -h

catocli mutation policy privateAccess updateRule <json>

catocli mutation policy privateAccess updateRule --json-file mutation.policy.privateAccess.updateRule.json

catocli mutation policy privateAccess updateRule '{"privateAccessPolicyMutationInput":{"revision":{"id":"id"}},"privateAccessUpdateRuleInput":{"id":"id","rule":{"action":{"action":"ALLOW"},"activePeriod":{"effectiveFrom":"example_value","expiresAt":"example_value","useEffectiveFrom":true,"useExpiresAt":true},"applications":{"application":{"by":"ID","input":"string"}},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","device":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"source":{"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}},"userAttributes":{"riskScore":{"category":"ANY","operator":"GTE"}}}}}'

catocli mutation policy privateAccess updateRule '{
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "privateAccessUpdateRuleInput": {
        "id": "id",
        "rule": {
            "action": {
                "action": "ALLOW"
            },
            "activePeriod": {
                "effectiveFrom": "example_value",
                "expiresAt": "example_value",
                "useEffectiveFrom": true,
                "useExpiresAt": true
            },
            "applications": {
                "application": {
                    "by": "ID",
                    "input": "string"
                }
            },
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
            "schedule": {
                "activeOn": "ALWAYS",
                "customRecurring": {
                    "days": "SUNDAY",
                    "from": "example_value",
                    "to": "example_value"
                },
                "customTimeframe": {
                    "from": "example_value",
                    "to": "example_value"
                }
            },
            "source": {
                "systemGroup": {
                    "by": "ID",
                    "input": "string"
                },
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "usersGroup": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "tracking": {
                "alert": {
                    "enabled": true,
                    "frequency": "HOURLY",
                    "mailingList": {
                        "by": "ID",
                        "input": "string"
                    },
                    "subscriptionGroup": {
                        "by": "ID",
                        "input": "string"
                    },
                    "webhook": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "event": {
                    "enabled": true
                }
            },
            "userAttributes": {
                "riskScore": {
                    "category": "ANY",
                    "operator": "GTE"
                }
            }
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.updateRule ####

`accountId` [ID] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
`privateAccessUpdateRuleInput` [PrivateAccessUpdateRuleInput] - (required) N/A    
