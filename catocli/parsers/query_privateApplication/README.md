
## CATO-CLI - query.privateApplication:
[Click here](https://api.catonetworks.com/documentation/#query-query.privateApplication) for documentation on this operation.

### Usage for query.privateApplication:

```bash
catocli query privateApplication -h

catocli query privateApplication <json>

catocli query privateApplication --json-file query.privateApplication.json

catocli query privateApplication '{"privateApplicationListInput":{"filter":{"connectivityStatus":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"groupName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"published":{"eq":true,"neq":true},"searchGroupName":{"search":"string"},"searchName":{"search":"string"}},"paging":{"from":1,"limit":1},"sort":{"connectivityStatus":{"direction":"ASC","priority":1},"creationTime":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"published":{"direction":"ASC","priority":1}}},"privateApplicationRefInput":{"by":"ID","input":"string"}}'

catocli query privateApplication '{
    "privateApplicationListInput": {
        "filter": {
            "connectivityStatus": {
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
            "freeText": {
                "search": "string"
            },
            "groupName": {
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
            "published": {
                "eq": true,
                "neq": true
            },
            "searchGroupName": {
                "search": "string"
            },
            "searchName": {
                "search": "string"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "connectivityStatus": {
                "direction": "ASC",
                "priority": 1
            },
            "creationTime": {
                "direction": "ASC",
                "priority": 1
            },
            "id": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "published": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "privateApplicationRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.privateApplication ####

`accountId` [ID] - (required) N/A    
`privateApplicationListInput` [PrivateApplicationListInput] - (required) N/A    
`privateApplicationRefInput` [PrivateApplicationRefInput] - (required) N/A    
