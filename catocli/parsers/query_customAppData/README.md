
## CATO-CLI - query.customAppData:
[Click here](https://api.catonetworks.com/documentation/#query-query.customAppData) for documentation on this operation.

### Usage for query.customAppData:

```bash
catocli query customAppData -h

catocli query customAppData <json>

catocli query customAppData --json-file query.customAppData.json

catocli query customAppData '{"customApplicationListInput":{"customApplicationFilterInput":{"category":{"hasAny":{"by":"ID","input":"string"}},"freeText":{"search":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"customApplicationSortInput":{"category":{"name":{"direction":"ASC","priority":1}},"description":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"customApplicationRefInput":{"by":"ID","input":"string"}}'

catocli query customAppData '{
    "customApplicationListInput": {
        "customApplicationFilterInput": {
            "category": {
                "hasAny": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "freeText": {
                "search": "string"
            },
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
            }
        },
        "customApplicationSortInput": {
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
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "customApplicationRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.customAppData ####

`accountId` [ID] - (required) N/A    
`customApplicationListInput` [CustomApplicationListInput] - (required) N/A    
`customApplicationRefInput` [CustomApplicationRefInput] - (required) N/A    
