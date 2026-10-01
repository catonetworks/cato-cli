
## CATO-CLI - mutation.policy.wanNetwork.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.addRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.addRule:

```bash
catocli mutation policy wanNetwork addRule -h

catocli mutation policy wanNetwork addRule <json>

catocli mutation policy wanNetwork addRule --json-file mutation.policy.wanNetwork.addRule.json

catocli mutation policy wanNetwork addRule '{"wanNetworkAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"application":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"customService":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"customServiceIp":[{"ip":"192.0.2.1","ipRange":{"from":"192.0.2.1","to":"192.0.2.1"},"name":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"service":[{"by":"ID","input":"string"}]},"bandwidthPriority":{"by":"ID","input":"string"},"configuration":{"activeTcpAcceleration":true,"allocationIp":[{"by":"ID","input":"string"}],"backhaulingSite":[{"by":"ID","input":"string"}],"packetLossMitigation":true,"popLocation":[{"by":"ID","input":"string"}],"preserveSourcePort":true,"primaryTransport":{"primaryInterfaceRole":"AUTOMATIC","secondaryInterfaceRole":"AUTOMATIC","transportType":"AUTOMATIC"},"secondaryTransport":{"primaryInterfaceRole":"AUTOMATIC","secondaryInterfaceRole":"AUTOMATIC","transportType":"AUTOMATIC"}},"description":"string","destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"enabled":true,"exceptions":[{"application":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"customService":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"customServiceIp":[{"ip":"192.0.2.1","ipRange":{"from":"192.0.2.1","to":"192.0.2.1"},"name":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"service":[{"by":"ID","input":"string"}]},"destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"name":"string","source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}],"name":"string","routeType":"NONE","ruleType":"WAN","source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}},"wanNetworkPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy wanNetwork addRule '{
    "wanNetworkAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "application": {
                "appCategory": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "application": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "customApp": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "customCategory": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "customService": [
                    {
                        "port": [
                            443
                        ],
                        "portRange": {
                            "from": 443,
                            "to": 443
                        },
                        "protocol": "ANY"
                    }
                ],
                "customServiceIp": [
                    {
                        "ip": "192.0.2.1",
                        "ipRange": {
                            "from": "192.0.2.1",
                            "to": "192.0.2.1"
                        },
                        "name": "string"
                    }
                ],
                "domain": [
                    "example.com"
                ],
                "fqdn": [
                    "host.example.com"
                ],
                "service": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "bandwidthPriority": {
                "by": "ID",
                "input": "string"
            },
            "configuration": {
                "activeTcpAcceleration": true,
                "allocationIp": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "backhaulingSite": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "packetLossMitigation": true,
                "popLocation": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
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
            },
            "enabled": true,
            "exceptions": [
                {
                    "application": {
                        "appCategory": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "application": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "customApp": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "customCategory": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "customService": [
                            {
                                "port": [
                                    443
                                ],
                                "portRange": {
                                    "from": 443,
                                    "to": 443
                                },
                                "protocol": "ANY"
                            }
                        ],
                        "customServiceIp": [
                            {
                                "ip": "192.0.2.1",
                                "ipRange": {
                                    "from": "192.0.2.1",
                                    "to": "192.0.2.1"
                                },
                                "name": "string"
                            }
                        ],
                        "domain": [
                            "example.com"
                        ],
                        "fqdn": [
                            "host.example.com"
                        ],
                        "service": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    },
                    "destination": {
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
                    },
                    "name": "string",
                    "source": {
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
            ],
            "name": "string",
            "routeType": "NONE",
            "ruleType": "WAN",
            "source": {
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
    },
    "wanNetworkPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.wanNetwork.addRule ####

`accountId` [ID] - (required) N/A
`wanNetworkAddRuleInput` [WanNetworkAddRuleInput] - (required) N/A
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A
