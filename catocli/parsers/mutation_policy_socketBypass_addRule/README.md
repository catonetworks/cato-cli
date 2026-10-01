
## CATO-CLI - mutation.policy.socketBypass.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.addRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.addRule:

```bash
catocli mutation policy socketBypass addRule -h

catocli mutation policy socketBypass addRule <json>

catocli mutation policy socketBypass addRule --json-file mutation.policy.socketBypass.addRule.json

catocli mutation policy socketBypass addRule '{"socketBypassAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":{"event":{"enabled":true},"port":"AUTOMATIC"},"description":"string","destination":{"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"enabled":true,"exception":[{"destination":{"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"domain":["example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"vlan":[100]}}],"name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"vlan":[100]}}},"socketBypassPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy socketBypass addRule '{
    "socketBypassAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
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
    },
    "socketBypassPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.addRule ####

`accountId` [ID] - (required) N/A
`socketBypassAddRuleInput` [SocketBypassAddRuleInput] - (required) N/A
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A
