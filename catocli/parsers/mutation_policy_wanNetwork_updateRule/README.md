
## CATO-CLI - mutation.policy.wanNetwork.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.updateRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.updateRule:

`catocli mutation policy wanNetwork updateRule -h`

`catocli mutation policy wanNetwork updateRule <json>`

`catocli mutation policy wanNetwork updateRule "$(cat < mutation.policy.wanNetwork.updateRule.json)"`

`catocli mutation policy wanNetwork updateRule '{"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanNetworkUpdateRuleInput":{"id":"id","wanNetworkUpdateRuleDataInput":{"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"customService":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"customServiceIp":{"ip":"example_value","ipRange":{"from":"example_value","to":"example_value"},"name":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"service":{"by":"ID","input":"string"}},"bandwidthPriority":{"by":"ID","input":"string"},"configuration":{"activeTcpAcceleration":true,"allocationIp":{"by":"ID","input":"string"},"backhaulingSite":{"by":"ID","input":"string"},"packetLossMitigation":true,"popLocation":{"by":"ID","input":"string"},"preserveSourcePort":true,"primaryTransport":{"primaryInterfaceRole":"AUTOMATIC","secondaryInterfaceRole":"AUTOMATIC","transportType":"AUTOMATIC"},"secondaryTransport":{"primaryInterfaceRole":"AUTOMATIC","secondaryInterfaceRole":"AUTOMATIC","transportType":"AUTOMATIC"}},"description":"string","destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"enabled":true,"exceptions":{"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"customService":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"customServiceIp":{"ip":"example_value","ipRange":{"from":"example_value","to":"example_value"},"name":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"service":{"by":"ID","input":"string"}},"destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"name":"string","source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"name":"string","routeType":"NONE","ruleType":"WAN","source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}}}}'`

`catocli mutation policy wanNetwork updateRule -p '{
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanNetworkUpdateRuleInput": {
        "id": "id",
        "wanNetworkUpdateRuleDataInput": {
            "application": {
                "appCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "application": {
                    "by": "ID",
                    "input": "string"
                },
                "customApp": {
                    "by": "ID",
                    "input": "string"
                },
                "customCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "customService": {
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
                "customServiceIp": {
                    "ip": "example_value",
                    "ipRange": {
                        "from": "example_value",
                        "to": "example_value"
                    },
                    "name": "string"
                },
                "domain": [
                    "example1",
                    "example2"
                ],
                "fqdn": [
                    "example1",
                    "example2"
                ],
                "service": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "bandwidthPriority": {
                "by": "ID",
                "input": "string"
            },
            "configuration": {
                "activeTcpAcceleration": true,
                "allocationIp": {
                    "by": "ID",
                    "input": "string"
                },
                "backhaulingSite": {
                    "by": "ID",
                    "input": "string"
                },
                "packetLossMitigation": true,
                "popLocation": {
                    "by": "ID",
                    "input": "string"
                },
                "preserveSourcePort": true,
                "primaryTransport": {
                    "primaryInterfaceRole": "AUTOMATIC",
                    "secondaryInterfaceRole": "AUTOMATIC",
                    "transportType": "AUTOMATIC"
                },
                "secondaryTransport": {
                    "primaryInterfaceRole": "AUTOMATIC",
                    "secondaryInterfaceRole": "AUTOMATIC",
                    "transportType": "AUTOMATIC"
                }
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
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "usersGroup": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "enabled": true,
            "exceptions": {
                "application": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customApp": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customService": {
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
                    "customServiceIp": {
                        "ip": "example_value",
                        "ipRange": {
                            "from": "example_value",
                            "to": "example_value"
                        },
                        "name": "string"
                    },
                    "domain": [
                        "example1",
                        "example2"
                    ],
                    "fqdn": [
                        "example1",
                        "example2"
                    ],
                    "service": {
                        "by": "ID",
                        "input": "string"
                    }
                },
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
                    "user": {
                        "by": "ID",
                        "input": "string"
                    },
                    "usersGroup": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "name": "string",
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
            "name": "string",
            "routeType": "NONE",
            "ruleType": "WAN",
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
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.updateRule ####

`accountId` [ID] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
`wanNetworkUpdateRuleInput` [WanNetworkUpdateRuleInput] - (required) N/A    
