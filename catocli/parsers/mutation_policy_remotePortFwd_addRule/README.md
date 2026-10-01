
## CATO-CLI - mutation.policy.remotePortFwd.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.addRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.addRule:

```bash
catocli mutation policy remotePortFwd addRule -h

catocli mutation policy remotePortFwd addRule <json>

catocli mutation policy remotePortFwd addRule --json-file mutation.policy.remotePortFwd.addRule.json

catocli mutation policy remotePortFwd addRule '{"remotePortFwdAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"description":"string","enabled":true,"externalIp":{"by":"ID","input":"string"},"externalPortRange":{"from":443,"to":443},"forwardIcmp":true,"internalIp":"192.0.2.1","internalPortRange":{"from":443,"to":443},"name":"string","remoteIPs":{"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"restrictionType":"ALLOW_LIST","tracking":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]}}},"remotePortFwdPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy remotePortFwd addRule '{
    "remotePortFwdAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "description": "string",
            "enabled": true,
            "externalIp": {
                "by": "ID",
                "input": "string"
            },
            "externalPortRange": {
                "from": 443,
                "to": 443
            },
            "forwardIcmp": true,
            "internalIp": "192.0.2.1",
            "internalPortRange": {
                "from": 443,
                "to": 443
            },
            "name": "string",
            "remoteIPs": {
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
            "restrictionType": "ALLOW_LIST",
            "tracking": {
                "enabled": true,
                "frequency": "HOURLY",
                "mailingList": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subscriptionGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "webhook": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            }
        }
    },
    "remotePortFwdPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.remotePortFwd.addRule ####

`accountId` [ID] - (required) N/A
`remotePortFwdAddRuleInput` [RemotePortFwdAddRuleInput] - (required) N/A
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A
