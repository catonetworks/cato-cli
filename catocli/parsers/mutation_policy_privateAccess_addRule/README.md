
## CATO-CLI - mutation.policy.privateAccess.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.addRule) for documentation on this operation.

### Usage for mutation.policy.privateAccess.addRule:

```bash
catocli mutation policy privateAccess addRule -h

catocli mutation policy privateAccess addRule <json>

catocli mutation policy privateAccess addRule --json-file mutation.policy.privateAccess.addRule.json

catocli mutation policy privateAccess addRule '{"privateAccessAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":{"action":"ALLOW"},"activePeriod":{"effectiveFrom":"example_value","expiresAt":"example_value","useEffectiveFrom":true,"useExpiresAt":true},"applications":{"application":{"by":"ID","input":"string"}},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","device":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"source":{"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}},"userAttributes":{"riskScore":{"category":"ANY","operator":"GTE"}}}},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess addRule '{
    "privateAccessAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
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
    },
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.addRule ####

`accountId` [ID] - (required) N/A    
`privateAccessAddRuleInput` [PrivateAccessAddRuleInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
