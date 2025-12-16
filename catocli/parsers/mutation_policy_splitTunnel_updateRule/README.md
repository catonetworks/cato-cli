
## CATO-CLI - mutation.policy.splitTunnel.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.updateRule) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.updateRule:

```bash
catocli mutation policy splitTunnel updateRule -h

catocli mutation policy splitTunnel updateRule <json>

catocli mutation policy splitTunnel updateRule --json-file mutation.policy.splitTunnel.updateRule.json

catocli mutation policy splitTunnel updateRule '{"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"splitTunnelUpdateRuleInput":{"id":"id","splitTunnelUpdateRuleDataInput":{"action":"EXCLUDE","country":{"by":"ID","input":"string"},"coverage":"ALL","description":"string","destination":{"application":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"}},"dnsExclusion":{"domain":["example1","example2"]},"enabled":true,"name":"string","platform":"WINDOWS","routingPriority":"LAN","source":{"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"sourceNetwork":{"sourceNetworkType":"ANY"}}}}'

catocli mutation policy splitTunnel updateRule '{
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "splitTunnelUpdateRuleInput": {
        "id": "id",
        "splitTunnelUpdateRuleDataInput": {
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
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.updateRule ####

`accountId` [ID] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
`splitTunnelUpdateRuleInput` [SplitTunnelUpdateRuleInput] - (required) N/A    
