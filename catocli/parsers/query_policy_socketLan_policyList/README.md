
## CATO-CLI - query.policy.socketLan.policyList:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.socketLan.policyList) for documentation on this operation.

### Usage for query.policy.socketLan.policyList:

```bash
catocli query policy socketLan policyList -h

catocli query policy socketLan policyList <json>

catocli query policy socketLan policyList --json-file query.policy.socketLan.policyList.json

catocli query policy socketLan policyList '{"socketLanPolicyListInput":{"filter":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"policyLevel":{"eq":"MAIN","in":"MAIN","neq":"MAIN","nin":"MAIN"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"policyLevel":{"direction":"ASC","priority":1}}}}'

catocli query policy socketLan policyList '{
    "socketLanPolicyListInput": {
        "filter": {
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
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
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

#### Operation Arguments for query.policy.socketLan.policyList ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyListInput` [SocketLanPolicyListInput] - (required) N/A    
