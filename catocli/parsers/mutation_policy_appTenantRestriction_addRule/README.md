
## CATO-CLI - mutation.policy.appTenantRestriction.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.addRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addRule:

`catocli mutation policy appTenantRestriction addRule -h`

`catocli mutation policy appTenantRestriction addRule <json>`

`catocli mutation policy appTenantRestriction addRule "$(cat < mutation.policy.appTenantRestriction.addRule.json)"`

`catocli mutation policy appTenantRestriction addRule '{"appTenantRestrictionAddRuleInput":{"appTenantRestrictionAddRuleDataInput":{"action":"INJECT_HEADERS","application":{"by":"ID","input":"string"},"description":"string","enabled":true,"headers":{"name":"example_value","value":"example_value"},"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"severity":"HIGH","source":{"country":{"by":"ID","input":"string"},"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy appTenantRestriction addRule -p '{
    "appTenantRestrictionAddRuleInput": {
        "appTenantRestrictionAddRuleDataInput": {
            "action": "INJECT_HEADERS",
            "application": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "enabled": true,
            "headers": {
                "name": "example_value",
                "value": "example_value"
            },
            "name": "string",
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
            "severity": "HIGH",
            "source": {
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "floatingSubnet": {
                    "by": "ID",
                    "input": "string"
                },
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                },
                "group": {
                    "by": "ID",
                    "input": "string"
                },
                "host": {
                    "by": "ID",
                    "input": "string"
                },
                "ip": [
                    "example1",
                    "example2"
                ],
                "ipRange": {
                    "from": "example_value",
                    "to": "example_value"
                },
                "networkInterface": {
                    "by": "ID",
                    "input": "string"
                },
                "site": {
                    "by": "ID",
                    "input": "string"
                },
                "siteNetworkSubnet": {
                    "by": "ID",
                    "input": "string"
                },
                "subnet": [
                    "example1",
                    "example2"
                ],
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
            }
        },
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.addRule ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionAddRuleInput` [AppTenantRestrictionAddRuleInput] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
