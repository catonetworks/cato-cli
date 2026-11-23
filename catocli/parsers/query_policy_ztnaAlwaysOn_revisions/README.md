
## CATO-CLI - query.policy.ztnaAlwaysOn.revisions:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.ztnaAlwaysOn.revisions) for documentation on this operation.

### Usage for query.policy.ztnaAlwaysOn.revisions:

```bash
catocli query policy ztnaAlwaysOn revisions -h

catocli query policy ztnaAlwaysOn revisions <json>

catocli query policy ztnaAlwaysOn revisions --json-file query.policy.ztnaAlwaysOn.revisions.json

catocli query policy ztnaAlwaysOn revisions '{"policyRevisionsInput":{"filter":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"publishedBy":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"publishedTime":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"search":{"search":"string"},"state":{"eq":"ACTIVE","in":["ACTIVE"],"neq":"ACTIVE","nin":["ACTIVE"]}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"publishedTime":{"direction":"ASC","priority":1},"state":{"direction":"ASC","priority":1},"updatedTime":{"direction":"ASC","priority":1}}}}'

catocli query policy ztnaAlwaysOn revisions '{
    "policyRevisionsInput": {
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
            "publishedBy": {
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
            "publishedTime": {
                "between": [
                    "2026-01-02T15:04:05Z"
                ],
                "eq": "2026-01-02T15:04:05Z",
                "gt": "2026-01-02T15:04:05Z",
                "gte": "2026-01-02T15:04:05Z",
                "in": [
                    "2026-01-02T15:04:05Z"
                ],
                "lt": "2026-01-02T15:04:05Z",
                "lte": "2026-01-02T15:04:05Z",
                "neq": "2026-01-02T15:04:05Z",
                "nin": [
                    "2026-01-02T15:04:05Z"
                ]
            },
            "search": {
                "search": "string"
            },
            "state": {
                "eq": "ACTIVE",
                "in": [
                    "ACTIVE"
                ],
                "neq": "ACTIVE",
                "nin": [
                    "ACTIVE"
                ]
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
            "publishedTime": {
                "direction": "ASC",
                "priority": 1
            },
            "state": {
                "direction": "ASC",
                "priority": 1
            },
            "updatedTime": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.policy.ztnaAlwaysOn.revisions ####

`accountId` [ID] - (required) Account whose policies are accessed.
`policyRevisionsInput` [PolicyRevisionsInput] - (required) Parameters for this policy operation.
