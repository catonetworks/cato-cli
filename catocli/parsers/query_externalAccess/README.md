
## CATO-CLI - query.externalAccess:
[Click here](https://api.catonetworks.com/documentation/#query-query.externalAccess) for documentation on this operation.

### Usage for query.externalAccess:

```bash
catocli query externalAccess -h

catocli query externalAccess <json>

catocli query externalAccess --json-file query.externalAccess.json

catocli query externalAccess '{"incomingAccessRequestListInput":{"filter":{"expirationDate":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"requestedDate":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"search":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"status":{"eq":"PENDING","in":["PENDING"],"neq":"PENDING","nin":["PENDING"]}},"paging":{"from":1,"limit":1},"sort":{"activeDate":{"direction":"ASC","priority":1},"expirationDate":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"requestedDate":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}}},"partnerAccessRequestListInput":{"filter":{"expirationDate":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"requestedDate":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"search":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"status":{"eq":"PENDING","in":["PENDING"],"neq":"PENDING","nin":["PENDING"]},"type":{"eq":"STANDARD","in":["STANDARD"],"neq":"STANDARD","nin":["STANDARD"]}},"paging":{"from":1,"limit":1},"sort":{"accountName":{"direction":"ASC","priority":1},"activeDate":{"direction":"ASC","priority":1},"expirationDate":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"requestedDate":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}}}'

catocli query externalAccess '{
    "incomingAccessRequestListInput": {
        "filter": {
            "expirationDate": {
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
            "requestedDate": {
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
            "status": {
                "eq": "PENDING",
                "in": [
                    "PENDING"
                ],
                "neq": "PENDING",
                "nin": [
                    "PENDING"
                ]
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "activeDate": {
                "direction": "ASC",
                "priority": 1
            },
            "expirationDate": {
                "direction": "ASC",
                "priority": 1
            },
            "id": {
                "direction": "ASC",
                "priority": 1
            },
            "requestedDate": {
                "direction": "ASC",
                "priority": 1
            },
            "status": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "partnerAccessRequestListInput": {
        "filter": {
            "expirationDate": {
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
            "requestedDate": {
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
            "status": {
                "eq": "PENDING",
                "in": [
                    "PENDING"
                ],
                "neq": "PENDING",
                "nin": [
                    "PENDING"
                ]
            },
            "type": {
                "eq": "STANDARD",
                "in": [
                    "STANDARD"
                ],
                "neq": "STANDARD",
                "nin": [
                    "STANDARD"
                ]
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "accountName": {
                "direction": "ASC",
                "priority": 1
            },
            "activeDate": {
                "direction": "ASC",
                "priority": 1
            },
            "expirationDate": {
                "direction": "ASC",
                "priority": 1
            },
            "id": {
                "direction": "ASC",
                "priority": 1
            },
            "requestedDate": {
                "direction": "ASC",
                "priority": 1
            },
            "status": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.externalAccess ####

`accountId` [ID] - (required) N/A
`incomingAccessRequestListInput` [IncomingAccessRequestListInput] - (required) N/A
`partnerAccessRequestListInput` [PartnerAccessRequestListInput] - (required) N/A
