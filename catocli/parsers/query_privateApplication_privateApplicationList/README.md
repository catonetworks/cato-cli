
## CATO-CLI - query.privateApplication.privateApplicationList:
[Click here](https://api.catonetworks.com/documentation/#query-query.privateApplication.privateApplicationList) for documentation on this operation.

### Usage for query.privateApplication.privateApplicationList:

```bash
catocli query privateApplication privateApplicationList -h

catocli query privateApplication privateApplicationList <json>

catocli query privateApplication privateApplicationList --json-file query.privateApplication.privateApplicationList.json

catocli query privateApplication privateApplicationList '{"privateApplicationListInput":{"filter":{"connectivityStatus":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"freeText":[{"search":"string"}],"groupName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"published":{"eq":true,"neq":true},"searchGroupName":{"search":"string"},"searchName":{"search":"string"}},"paging":{"from":1,"limit":1},"sort":{"connectivityStatus":{"direction":"ASC","priority":1},"creationTime":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"published":{"direction":"ASC","priority":1}}}}'

catocli query privateApplication privateApplicationList '{
    "privateApplicationListInput": {
        "filter": {
            "connectivityStatus": [
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
            "freeText": [
                {
                    "search": "string"
                }
            ],
            "groupName": [
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
            ],
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
    }
}'
```

#### Operation Arguments for query.privateApplication.privateApplicationList ####

`accountId` [ID] - (required) N/A
`privateApplicationListInput` [PrivateApplicationListInput] - (required) N/A
