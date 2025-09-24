
## CATO-CLI - mutation.policy.remotePortFwd.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.addRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.addRule:

`catocli mutation policy remotePortFwd addRule -h`

`catocli mutation policy remotePortFwd addRule <json>`

`catocli mutation policy remotePortFwd addRule "$(cat < mutation.policy.remotePortFwd.addRule.json)"`

`catocli mutation policy remotePortFwd addRule '{"remotePortFwdAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"remotePortFwdAddRuleDataInput":{"description":"string","enabled":true,"externalIp":{"by":"ID","input":"string"},"externalPortRange":{"from":"example_value","to":"example_value"},"forwardIcmp":true,"internalIp":"example_value","internalPortRange":{"from":"example_value","to":"example_value"},"name":"string","remoteIPs":{"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"restrictionType":"ALLOW_LIST","tracking":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}}}},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd addRule -p '{
    "remotePortFwdAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "remotePortFwdAddRuleDataInput": {
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
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.addRule ####

`accountId` [ID] - (required) N/A    
`remotePortFwdAddRuleInput` [RemotePortFwdAddRuleInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
