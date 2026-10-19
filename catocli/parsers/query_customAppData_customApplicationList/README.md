
## CATO-CLI - query.customAppData.customApplicationList:
[Click here](https://api.catonetworks.com/documentation/#query-query.customAppData.customApplicationList) for documentation on this operation.

### Usage for query.customAppData.customApplicationList:

```bash
catocli query customAppData customApplicationList -h

catocli query customAppData customApplicationList <json>

catocli query customAppData customApplicationList --json-file query.customAppData.customApplicationList.json

catocli query customAppData customApplicationList '{"customApplicationListInput":{"filter":[{"category":[{"hasAny":[{"by":"ID","input":"string"}]}],"freeText":{"search":"string"},"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]}],"paging":{"from":1,"limit":1},"sort":{"category":{"name":{"direction":"ASC","priority":1}},"description":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query customAppData customApplicationList '{
    "customApplicationListInput": {
        "filter": [
            {
                "category": [
                    {
                        "hasAny": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                ],
                "freeText": {
                    "search": "string"
                },
                "id": [
                    {
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
                    }
                ],
                "name": [
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
                ]
            }
        ],
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "category": {
                "name": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "description": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.customAppData.customApplicationList ####

`accountId` [ID] - (required) N/A
`customApplicationListInput` [CustomApplicationListInput] - (required) N/A
