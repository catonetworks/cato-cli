
## CATO-CLI - mutation.policy.socketLan.firewall.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.firewall.addRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.firewall.addRule:

```bash
catocli mutation policy socketLan firewall addRule -h

catocli mutation policy socketLan firewall addRule <json>

catocli mutation policy socketLan firewall addRule --json-file mutation.policy.socketLan.firewall.addRule.json

catocli mutation policy socketLan firewall addRule '{"socketLanFirewallAddRuleInput":{"policySubRulePositionInput":{"position":"AFTER_SUB_RULE","ref":"id"},"socketLanFirewallAddRuleDataInput":{"action":"ALLOW","application":{"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"description":"string","destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"vlan":["example1","example2"]},"direction":"TO","enabled":true,"name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"},"standard":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"mac":["example1","example2"],"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"vlan":["example1","example2"]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketLan firewall addRule '{
    "socketLanFirewallAddRuleInput": {
        "policySubRulePositionInput": {
            "position": "AFTER_SUB_RULE",
            "ref": "id"
        },
        "socketLanFirewallAddRuleDataInput": {
            "action": "ALLOW",
            "application": {
                "application": {
                    "by": "ID",
                    "input": "string"
                },
                "customApp": {
                    "by": "ID",
                    "input": "string"
                },
                "domain": [
                    "example1",
                    "example2"
                ],
                "fqdn": [
                    "example1",
                    "example2"
                ],
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
                "vlan": [
                    "example1",
                    "example2"
                ]
            },
            "direction": "TO",
            "enabled": true,
            "name": "string",
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
                },
                "standard": {
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
                "mac": [
                    "example1",
                    "example2"
                ],
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
                "vlan": [
                    "example1",
                    "example2"
                ]
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
            }
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.firewall.addRule ####

`accountId` [ID] - (required) N/A    
`socketLanFirewallAddRuleInput` [SocketLanFirewallAddRuleInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
