
## CATO-CLI - mutation.policy.socketBypass.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.updateRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.updateRule:

```bash
catocli mutation policy socketBypass updateRule -h

catocli mutation policy socketBypass updateRule <json>

catocli mutation policy socketBypass updateRule --json-file mutation.policy.socketBypass.updateRule.json

catocli mutation policy socketBypass updateRule '{"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketBypassUpdateRuleInput":{"id":"id","socketBypassUpdateRuleDataInput":{"action":{"event":{"enabled":true},"port":"AUTOMATIC"},"description":"string","destination":{"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"enabled":true,"exception":{"destination":{"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"}},"site":{"group":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"vlan":["example1","example2"]}},"name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"simple":{"name":"HTTP"}},"site":{"group":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"vlan":["example1","example2"]}}}}'

catocli mutation policy socketBypass updateRule '{
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketBypassUpdateRuleInput": {
        "id": "id",
        "socketBypassUpdateRuleDataInput": {
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
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.updateRule ####

`accountId` [ID] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
`socketBypassUpdateRuleInput` [SocketBypassUpdateRuleInput] - (required) N/A    
