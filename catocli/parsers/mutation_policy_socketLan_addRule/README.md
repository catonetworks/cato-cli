
## CATO-CLI - mutation.policy.socketLan.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.addRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.addRule:

`catocli mutation policy socketLan addRule -h`

`catocli mutation policy socketLan addRule <json>`

`catocli mutation policy socketLan addRule "$(cat < mutation.policy.socketLan.addRule.json)"`

`catocli mutation policy socketLan addRule '{"socketLanAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"socketLanAddRuleDataInput":{"description":"string","destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"vlan":["example1","example2"]},"direction":"TO","enabled":true,"name":"string","nat":{"enabled":true,"natType":"DYNAMIC_PAT"},"service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"}},"site":{"group":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"vlan":["example1","example2"]},"transport":"WAN"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan addRule -p '{
    "socketLanAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "socketLanAddRuleDataInput": {
            "description": "string",
            "destination": {
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
                "vlan": [
                    "example1",
                    "example2"
                ]
            },
            "direction": "TO",
            "enabled": true,
            "name": "string",
            "nat": {
                "enabled": true,
                "natType": "DYNAMIC_PAT"
            },
            "service": {
                "custom": {
                    "port": [
                        "example1",
                        "example2"
                    ],
                    "portRange": {
                        "from": "example_value",
                        "to": "example_value"
                    },
                    "protocol": "ANY"
                },
                "simple": {
                    "name": "HTTP"
                }
            },
            "site": {
                "group": {
                    "by": "ID",
                    "input": "string"
                },
                "site": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "source": {
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
                "vlan": [
                    "example1",
                    "example2"
                ]
            },
            "transport": "WAN"
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.addRule ####

`accountId` [ID] - (required) N/A    
`socketLanAddRuleInput` [SocketLanAddRuleInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
