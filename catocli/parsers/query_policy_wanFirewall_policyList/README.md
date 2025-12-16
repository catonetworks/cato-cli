
## CATO-CLI - query.policy.wanFirewall.policyList:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.wanFirewall.policyList) for documentation on this operation.

### Usage for query.policy.wanFirewall.policyList:

```bash
catocli query policy wanFirewall policyList -h

catocli query policy wanFirewall policyList <json>

catocli query policy wanFirewall policyList --json-file query.policy.wanFirewall.policyList.json

catocli query policy wanFirewall policyList '{"wanFirewallPolicyListInput":{"pagingInput":{"from":1,"limit":1},"wanFirewallPolicyListFilterInput":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"policyLevel":{"eq":"MAIN","in":"MAIN","neq":"MAIN","nin":"MAIN"}},"wanFirewallPolicyListSortInput":{"name":{"direction":"ASC","priority":1},"policyLevel":{"direction":"ASC","priority":1}}}}'

catocli query policy wanFirewall policyList '{
    "wanFirewallPolicyListInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "wanFirewallPolicyListFilterInput": {
            "id": {
                "eq": "id",
                "in": [
                    "id1",
                    "id2"
                ],
                "neq": "id",
                "nin": [
                    "id1",
                    "id2"
                ]
            },
            "name": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "policyLevel": {
                "eq": "MAIN",
                "in": "MAIN",
                "neq": "MAIN",
                "nin": "MAIN"
            }
        },
        "wanFirewallPolicyListSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "policyLevel": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.policy.wanFirewall.policyList ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyListInput` [WanFirewallPolicyListInput] - (required) N/A    
