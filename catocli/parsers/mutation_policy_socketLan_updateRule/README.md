
## CATO-CLI - mutation.policy.socketLan.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.updateRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.updateRule:

```bash
catocli mutation policy socketLan updateRule -h

catocli mutation policy socketLan updateRule <json>

catocli mutation policy socketLan updateRule --json-file mutation.policy.socketLan.updateRule.json

catocli mutation policy socketLan updateRule '{"socketLanPolicyMutationInput":{"revision":{"id":"id"}},"socketLanUpdateRuleInput":{"id":"id","rule":{"description":"string","destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"vlan":[100]},"direction":"TO","enabled":true,"name":"string","nat":{"enabled":true,"natType":"DYNAMIC_PAT"},"service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"simple":[{"name":"HTTP"}]},"site":{"group":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"vlan":[100]},"transport":"WAN"}}}'

catocli mutation policy socketLan updateRule '{
    "socketLanPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "socketLanUpdateRuleInput": {
        "id": "id",
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
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.updateRule ####

`accountId` [ID] - (required) N/A
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A
`socketLanUpdateRuleInput` [SocketLanUpdateRuleInput] - (required) N/A
