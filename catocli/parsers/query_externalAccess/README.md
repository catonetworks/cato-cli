
## CATO-CLI - query.externalAccess:
[Click here](https://api.catonetworks.com/documentation/#query-query.externalAccess) for documentation on this operation.

### Usage for query.externalAccess:

```bash
catocli query externalAccess -h

catocli query externalAccess <json>

catocli query externalAccess --json-file query.externalAccess.json

catocli query externalAccess '{"incomingAccessRequestListInput":{"accessRequestSortInput":{"activeDate":{"direction":"ASC","priority":1},"expirationDate":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"requestedDate":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}},"incomingAccessRequestFilterInput":{"expirationDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"requestedDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"search":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"status":{"eq":"PENDING","in":"PENDING","neq":"PENDING","nin":"PENDING"}},"pagingInput":{"from":1,"limit":1}},"partnerAccessRequestListInput":{"pagingInput":{"from":1,"limit":1},"partnerAccessRequestFilterInput":{"expirationDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"requestedDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"search":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"status":{"eq":"PENDING","in":"PENDING","neq":"PENDING","nin":"PENDING"},"type":{"eq":"STANDARD","in":"STANDARD","neq":"STANDARD","nin":"STANDARD"}},"partnerAccessRequestSortInput":{"accountName":{"direction":"ASC","priority":1},"activeDate":{"direction":"ASC","priority":1},"expirationDate":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"requestedDate":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}}}'

catocli query externalAccess '{
    "incomingAccessRequestListInput": {
        "accessRequestSortInput": {
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
        },
        "incomingAccessRequestFilterInput": {
            "expirationDate": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ]
            },
            "requestedDate": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
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
                "in": "PENDING",
                "neq": "PENDING",
                "nin": "PENDING"
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "partnerAccessRequestListInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "partnerAccessRequestFilterInput": {
            "expirationDate": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ]
            },
            "requestedDate": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
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
                "in": "PENDING",
                "neq": "PENDING",
                "nin": "PENDING"
            },
            "type": {
                "eq": "STANDARD",
                "in": "STANDARD",
                "neq": "STANDARD",
                "nin": "STANDARD"
            }
        },
        "partnerAccessRequestSortInput": {
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
