
## CATO-CLI - mutation.policy.socketBypass.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.addRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.addRule:

```bash
catocli mutation policy socketBypass addRule -h

catocli mutation policy socketBypass addRule <json>

catocli mutation policy socketBypass addRule --json-file mutation.policy.socketBypass.addRule.json

catocli mutation policy socketBypass addRule '{"socketBypassAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"socketBypassAddRuleDataInput":{"action":{"event":{"enabled":true},"port":"AUTOMATIC"},"description":"string","destination":{"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"enabled":true,"exception":{"destination":{"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"}},"site":{"group":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"vlan":["example1","example2"]}},"name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"}},"site":{"group":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"vlan":["example1","example2"]}}},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass addRule '{
    "socketBypassAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "socketBypassAddRuleDataInput": {
            "action": {
                "event": {
                    "enabled": true
                },
                "port": "AUTOMATIC"
            },
            "description": "string",
            "destination": {
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
            "enabled": true,
            "exception": {
                "destination": {
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
                    "vlan": [
                        "example1",
                        "example2"
                    ]
                }
            },
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
                "vlan": [
                    "example1",
                    "example2"
                ]
            }
        }
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.addRule ####

`accountId` [ID] - (required) N/A    
`socketBypassAddRuleInput` [SocketBypassAddRuleInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
