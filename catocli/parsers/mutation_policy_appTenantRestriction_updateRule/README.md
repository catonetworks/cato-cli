
## CATO-CLI - mutation.policy.appTenantRestriction.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.updateRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updateRule:

```bash
catocli mutation policy appTenantRestriction updateRule -h

catocli mutation policy appTenantRestriction updateRule <json>

catocli mutation policy appTenantRestriction updateRule --json-file mutation.policy.appTenantRestriction.updateRule.json

catocli mutation policy appTenantRestriction updateRule '{"appTenantRestrictionPolicyMutationInput":{"revision":{"id":"id"}},"appTenantRestrictionUpdateRuleInput":{"id":"id","rule":{"action":"INJECT_HEADERS","application":{"by":"ID","input":"string"},"description":"string","enabled":true,"headers":[{"name":"X-Example","value":"example"}],"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"severity":"HIGH","source":{"country":[{"by":"ID","input":"string"}],"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}}}'

catocli mutation policy appTenantRestriction updateRule '{
    "appTenantRestrictionPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "appTenantRestrictionUpdateRuleInput": {
        "id": "id",
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
    }
}'
```

#### Operation Arguments for mutation.policy.appTenantRestriction.updateRule ####

`accountId` [ID] - (required) N/A
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A
`appTenantRestrictionUpdateRuleInput` [AppTenantRestrictionUpdateRuleInput] - (required) N/A
