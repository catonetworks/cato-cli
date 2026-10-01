
## CATO-CLI - mutation.policy.socketLan.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.addRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.addRule:

```bash
catocli mutation policy socketLan addRule -h

catocli mutation policy socketLan addRule <json>

catocli mutation policy socketLan addRule --json-file mutation.policy.socketLan.addRule.json

catocli mutation policy socketLan addRule '{"socketLanAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"description":"string","destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"vlan":[100]},"direction":"TO","enabled":true,"name":"string","nat":{"enabled":true,"natType":"DYNAMIC_PAT"},"service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"vlan":[100]},"transport":"WAN"}},"socketLanPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy socketLan addRule '{
    "socketLanAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
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
                "vlan": [
                    100
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
                "systemGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "vlan": [
                    100
                ]
            },
            "transport": "WAN"
        }
    },
    "socketLanPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.addRule ####

`accountId` [ID] - (required) N/A
`socketLanAddRuleInput` [SocketLanAddRuleInput] - (required) N/A
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A
