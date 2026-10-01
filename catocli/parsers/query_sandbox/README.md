
## CATO-CLI - query.sandbox:
[Click here](https://api.catonetworks.com/documentation/#query-query.sandbox) for documentation on this operation.

### Usage for query.sandbox:

```bash
catocli query sandbox -h

catocli query sandbox <json>

catocli query sandbox --json-file query.sandbox.json

catocli query sandbox '{"sandboxReportsInput":{"filter":{"fileHash":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"fileName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"reportCreateDate":[{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}]},"paging":{"from":1,"limit":1},"sort":{"fileName":{"direction":"ASC","priority":1},"reportCreateDate":{"direction":"ASC","priority":1}}}}'

catocli query sandbox '{
    "sandboxReportsInput": {
        "filter": {
            "fileHash": [
                {
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
                }
            ],
            "fileName": [
                {
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
                }
            ],
            "reportCreateDate": [
                {
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
                }
            ]
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "fileName": {
                "direction": "ASC",
                "priority": 1
            },
            "reportCreateDate": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.sandbox ####

`accountId` [ID] - (required) N/A
`sandboxReportsInput` [SandboxReportsInput] - (required) N/A
