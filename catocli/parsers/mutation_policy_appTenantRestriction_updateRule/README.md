
## CATO-CLI - mutation.policy.appTenantRestriction.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.updateRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updateRule:

`catocli mutation policy appTenantRestriction updateRule -h`

`catocli mutation policy appTenantRestriction updateRule <json>`

`catocli mutation policy appTenantRestriction updateRule "$(cat < mutation.policy.appTenantRestriction.updateRule.json)"`

`catocli mutation policy appTenantRestriction updateRule '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"appTenantRestrictionUpdateRuleInput":{"appTenantRestrictionUpdateRuleDataInput":{"action":"INJECT_HEADERS","application":{"by":"ID","input":"string"},"description":"string","enabled":true,"headers":{"name":"example_value","value":"example_value"},"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"severity":"HIGH","source":{"country":{"by":"ID","input":"string"},"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"id":"id"}}'`

`catocli mutation policy appTenantRestriction updateRule -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "appTenantRestrictionUpdateRuleInput": {
        "appTenantRestrictionUpdateRuleDataInput": {
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
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.updateRule ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`appTenantRestrictionUpdateRuleInput` [AppTenantRestrictionUpdateRuleInput] - (required) N/A    
