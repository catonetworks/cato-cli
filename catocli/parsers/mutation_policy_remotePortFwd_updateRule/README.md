
## CATO-CLI - mutation.policy.remotePortFwd.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.updateRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updateRule:

`catocli mutation policy remotePortFwd updateRule -h`

`catocli mutation policy remotePortFwd updateRule <json>`

`catocli mutation policy remotePortFwd updateRule "$(cat < mutation.policy.remotePortFwd.updateRule.json)"`

`catocli mutation policy remotePortFwd updateRule '{"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"remotePortFwdUpdateRuleInput":{"id":"id","remotePortFwdUpdateRuleDataInput":{"description":"string","enabled":true,"externalIp":{"by":"ID","input":"string"},"externalPortRange":{"from":"example_value","to":"example_value"},"forwardIcmp":true,"internalIp":"example_value","internalPortRange":{"from":"example_value","to":"example_value"},"name":"string","remoteIPs":{"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"restrictionType":"ALLOW_LIST","tracking":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}}}}}'`

`catocli mutation policy remotePortFwd updateRule -p '{
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "remotePortFwdUpdateRuleInput": {
        "id": "id",
        "remotePortFwdUpdateRuleDataInput": {
            "description": "string",
            "enabled": true,
            "externalIp": {
                "by": "ID",
                "input": "string"
            },
            "externalPortRange": {
                "from": "example_value",
                "to": "example_value"
            },
            "forwardIcmp": true,
            "internalIp": "example_value",
            "internalPortRange": {
                "from": "example_value",
                "to": "example_value"
            },
            "name": "string",
            "remoteIPs": {
                "globalIpRange": {
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
                "subnet": [
                    "example1",
                    "example2"
                ]
            },
            "restrictionType": "ALLOW_LIST",
            "tracking": {
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
            }
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.updateRule ####

`accountId` [ID] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
`remotePortFwdUpdateRuleInput` [RemotePortFwdUpdateRuleInput] - (required) N/A    
