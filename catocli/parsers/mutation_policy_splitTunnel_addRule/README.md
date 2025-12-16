
## CATO-CLI - mutation.policy.splitTunnel.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.addRule) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.addRule:

```bash
catocli mutation policy splitTunnel addRule -h

catocli mutation policy splitTunnel addRule <json>

catocli mutation policy splitTunnel addRule --json-file mutation.policy.splitTunnel.addRule.json

catocli mutation policy splitTunnel addRule '{"splitTunnelAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"splitTunnelAddRuleDataInput":{"action":"EXCLUDE","country":{"by":"ID","input":"string"},"coverage":"ALL","description":"string","destination":{"application":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"}},"dnsExclusion":{"domain":["example1","example2"]},"enabled":true,"name":"string","platform":"WINDOWS","routingPriority":"LAN","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"sourceNetwork":{"sourceNetworkType":"ANY"}}},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel addRule '{
    "splitTunnelAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "splitTunnelAddRuleDataInput": {
            "action": "EXCLUDE",
            "country": {
                "by": "ID",
                "input": "string"
            },
            "coverage": "ALL",
            "description": "string",
            "destination": {
                "application": {
                    "by": "ID",
                    "input": "string"
                },
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "dnsExclusion": {
                "domain": [
                    "example1",
                    "example2"
                ]
            },
            "enabled": true,
            "name": "string",
            "platform": "WINDOWS",
            "routingPriority": "LAN",
            "source": {
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "usersGroup": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "sourceNetwork": {
                "sourceNetworkType": "ANY"
            }
        }
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.addRule ####

`accountId` [ID] - (required) N/A    
`splitTunnelAddRuleInput` [SplitTunnelAddRuleInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
