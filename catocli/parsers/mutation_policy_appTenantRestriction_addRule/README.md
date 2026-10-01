
## CATO-CLI - mutation.policy.appTenantRestriction.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.addRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addRule:

```bash
catocli mutation policy appTenantRestriction addRule -h

catocli mutation policy appTenantRestriction addRule <json>

catocli mutation policy appTenantRestriction addRule --json-file mutation.policy.appTenantRestriction.addRule.json

catocli mutation policy appTenantRestriction addRule '{"appTenantRestrictionAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":"INJECT_HEADERS","application":{"by":"ID","input":"string"},"description":"string","enabled":true,"headers":[{"name":"X-Example","value":"example"}],"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"severity":"HIGH","source":{"country":[{"by":"ID","input":"string"}],"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}},"appTenantRestrictionPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy appTenantRestriction addRule '{
    "appTenantRestrictionAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "action": "INJECT_HEADERS",
            "application": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "enabled": true,
            "headers": [
                {
                    "name": "X-Example",
                    "value": "example"
                }
            ],
            "name": "string",
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
            "severity": "HIGH",
            "source": {
                "country": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "floatingSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "globalIpRange": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "group": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "host": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "ip": [
                    "192.0.2.1"
                ],
                "ipRange": [
                    {
                        "from": "192.0.2.1",
                        "to": "192.0.2.1"
                    }
                ],
                "networkInterface": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "site": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "siteNetworkSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ],
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
            }
        }
    },
    "appTenantRestrictionPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.appTenantRestriction.addRule ####

`accountId` [ID] - (required) N/A
`appTenantRestrictionAddRuleInput` [AppTenantRestrictionAddRuleInput] - (required) N/A
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A
