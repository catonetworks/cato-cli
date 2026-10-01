
## CATO-CLI - mutation.policy.socketBypass.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.updateRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.updateRule:

```bash
catocli mutation policy socketBypass updateRule -h

catocli mutation policy socketBypass updateRule <json>

catocli mutation policy socketBypass updateRule --json-file mutation.policy.socketBypass.updateRule.json

catocli mutation policy socketBypass updateRule '{"socketBypassPolicyMutationInput":{"revision":{"id":"id"}},"socketBypassUpdateRuleInput":{"id":"id","rule":{"action":{"event":{"enabled":true},"port":"AUTOMATIC"},"description":"string","destination":{"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"enabled":true,"exception":[{"destination":{"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"vlan":[100]}}],"name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"vlan":[100]}}}}'

catocli mutation policy socketBypass updateRule '{
    "socketBypassPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "socketBypassUpdateRuleInput": {
        "id": "id",
        "rule": {
            "action": {
                "event": {
                    "enabled": true
                },
                "port": "AUTOMATIC"
            },
            "description": "string",
            "destination": {
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
                "domain": [
                    "example.com"
                ],
                "fqdn": [
                    "host.example.com"
                ],
                "globalIpRange": [
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
                "subnet": [
                    "192.0.2.0/24"
                ]
            },
            "enabled": true,
            "exception": [
                {
                    "destination": {
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
                        "domain": [
                            "example.com"
                        ],
                        "fqdn": [
                            "host.example.com"
                        ],
                        "globalIpRange": [
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
                        "subnet": [
                            "192.0.2.0/24"
                        ]
                    },
                    "name": "string",
                    "service": {
                        "custom": [
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
                        "simple": [
                            {
                                "name": "HTTP"
                            }
                        ]
                    },
                    "site": {
                        "group": [
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
                        ]
                    },
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
                        "siteNetworkSubnet": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "subnet": [
                            "192.0.2.0/24"
                        ],
                        "vlan": [
                            100
                        ]
                    }
                }
            ],
            "name": "string",
            "service": {
                "custom": [
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
                "simple": [
                    {
                        "name": "HTTP"
                    }
                ]
            },
            "site": {
                "group": [
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
                ]
            },
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
                "siteNetworkSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ],
                "vlan": [
                    100
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
