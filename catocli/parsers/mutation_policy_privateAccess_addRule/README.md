
## CATO-CLI - mutation.policy.privateAccess.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.addRule) for documentation on this operation.

### Usage for mutation.policy.privateAccess.addRule:

```bash
catocli mutation policy privateAccess addRule -h

catocli mutation policy privateAccess addRule <json>

catocli mutation policy privateAccess addRule --json-file mutation.policy.privateAccess.addRule.json

catocli mutation policy privateAccess addRule '{"privateAccessAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":{"action":"ALLOW"},"activePeriod":{"effectiveFrom":"2026-01-02T15:04:05Z","expiresAt":"2026-01-02T15:04:05Z","useEffectiveFrom":true,"useExpiresAt":true},"applications":{"application":[{"by":"ID","input":"string"}]},"connectionsOriginList":["SITE"],"country":[{"by":"ID","input":"string"}],"description":"string","device":[{"by":"ID","input":"string"}],"enabled":true,"name":"string","platform":["WINDOWS"],"schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"source":{"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}},"userAttributes":{"riskScore":{"category":"ANY","operator":"GTE"}}}},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

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
                "effectiveFrom": "2026-01-02T15:04:05Z",
                "expiresAt": "2026-01-02T15:04:05Z",
                "useEffectiveFrom": true,
                "useExpiresAt": true
            },
            "applications": {
                "application": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "connectionsOriginList": [
                "SITE"
            ],
            "country": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "description": "string",
            "device": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "enabled": true,
            "name": "string",
            "platform": [
                "WINDOWS"
            ],
            "schedule": {
                "activeOn": "ALWAYS",
                "customRecurring": {
                    "days": [
                        "SUNDAY"
                    ],
                    "from": "12:34:56",
                    "to": "12:34:56"
                },
                "customTimeframe": {
                    "from": "2026-01-02T15:04:05Z",
                    "to": "2026-01-02T15:04:05Z"
                }
            },
            "source": {
                "systemGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "user": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "usersGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "tracking": {
                "alert": {
                    "enabled": true,
                    "frequency": "HOURLY",
                    "mailingList": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "subscriptionGroup": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "webhook": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
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
