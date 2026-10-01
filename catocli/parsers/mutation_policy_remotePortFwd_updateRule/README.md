
## CATO-CLI - mutation.policy.remotePortFwd.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.updateRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updateRule:

```bash
catocli mutation policy remotePortFwd updateRule -h

catocli mutation policy remotePortFwd updateRule <json>

catocli mutation policy remotePortFwd updateRule --json-file mutation.policy.remotePortFwd.updateRule.json

catocli mutation policy remotePortFwd updateRule '{"remotePortFwdPolicyMutationInput":{"revision":{"id":"id"}},"remotePortFwdUpdateRuleInput":{"id":"id","rule":{"description":"string","enabled":true,"externalIp":{"by":"ID","input":"string"},"externalPortRange":{"from":443,"to":443},"forwardIcmp":true,"internalIp":"192.0.2.1","internalPortRange":{"from":443,"to":443},"name":"string","remoteIPs":{"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"restrictionType":"ALLOW_LIST","tracking":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]}}}}'

catocli mutation policy remotePortFwd updateRule '{
    "remotePortFwdPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "remotePortFwdUpdateRuleInput": {
        "id": "id",
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
    }
}'
```

#### Operation Arguments for mutation.policy.remotePortFwd.updateRule ####

`accountId` [ID] - (required) N/A
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A
`remotePortFwdUpdateRuleInput` [RemotePortFwdUpdateRuleInput] - (required) N/A
