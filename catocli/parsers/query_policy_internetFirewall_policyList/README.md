
## CATO-CLI - query.policy.internetFirewall.policyList:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.internetFirewall.policyList) for documentation on this operation.

### Usage for query.policy.internetFirewall.policyList:

```bash
catocli query policy internetFirewall policyList -h

catocli query policy internetFirewall policyList <json>

catocli query policy internetFirewall policyList --json-file query.policy.internetFirewall.policyList.json

catocli query policy internetFirewall policyList '{"internetFirewallPolicyListInput":{"internetFirewallPolicyListFilterInput":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"policyLevel":{"eq":"MAIN","in":"MAIN","neq":"MAIN","nin":"MAIN"}},"internetFirewallPolicyListSortInput":{"name":{"direction":"ASC","priority":1},"policyLevel":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'

catocli query policy internetFirewall policyList '{
    "internetFirewallPolicyListInput": {
        "internetFirewallPolicyListFilterInput": {
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
        "internetFirewallPolicyListSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "policyLevel": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    }
}'
```

#### Operation Arguments for query.policy.internetFirewall.policyList ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyListInput` [InternetFirewallPolicyListInput] - (required) N/A    
