
## CATO-CLI - mutation.policy.tlsInspect.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.addRule) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.addRule:

```bash
catocli mutation policy tlsInspect addRule -h

catocli mutation policy tlsInspect addRule <json>

catocli mutation policy tlsInspect addRule --json-file mutation.policy.tlsInspect.addRule.json

catocli mutation policy tlsInspect addRule '{"tlsInspectAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":"INSPECT","application":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"country":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"customService":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"customServiceIp":[{"ip":"192.0.2.1","ipRange":{"from":"192.0.2.1","to":"192.0.2.1"},"name":"string"}],"domain":["internal.example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"remoteAsn":[65536],"service":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"tlsInspectCategory":["POPULAR_CLOUD_APPS"]},"connectionOrigin":"ANY","country":[{"by":"ID","input":"string"}],"description":"string","devicePostureProfile":[{"by":"ID","input":"string"}],"enabled":true,"name":"string","platform":["WINDOWS"],"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"untrustedCertificateAction":"ALLOW"}},"tlsInspectPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy tlsInspect addRule '{
    "tlsInspectAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "action": "INSPECT",
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
                "country": [
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
                    "internal.example.com"
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
                "remoteAsn": [
                    65536
                ],
                "service": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ],
                "tlsInspectCategory": [
                    "POPULAR_CLOUD_APPS"
                ]
            },
            "connectionOrigin": "ANY",
            "country": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "description": "string",
            "devicePostureProfile": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "enabled": true,
            "name": "string",
            "platform": [
                "WINDOWS"
            ],
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
            },
            "untrustedCertificateAction": "ALLOW"
        }
    },
    "tlsInspectPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.tlsInspect.addRule ####

`accountId` [ID] - (required) N/A
`tlsInspectAddRuleInput` [TlsInspectAddRuleInput] - (required) N/A
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A
