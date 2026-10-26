
## CATO-CLI - query.user.usersGroupList:
[Click here](https://api.catonetworks.com/documentation/#query-query.user.usersGroupList) for documentation on this operation.

### Usage for query.user.usersGroupList:

```bash
catocli query user usersGroupList -h

catocli query user usersGroupList <json>

catocli query user usersGroupList --json-file query.user.usersGroupList.json

catocli query user usersGroupList '{"usersGroupListInput":{"filter":{"directoryId":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"importType":[{"eq":"MANUAL","in":["MANUAL"],"neq":"MANUAL","nin":["MANUAL"]}],"memberIds":["id1","id2"],"searchTerm":{"search":"string"}},"paging":{"from":1,"limit":1},"sort":{"creationDate":{"direction":"ASC","priority":1},"importType":{"direction":"ASC","priority":1},"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query user usersGroupList '{
    "usersGroupListInput": {
        "filter": {
            "directoryId": [
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
            "importType": [
                {
                    "eq": "MANUAL",
                    "in": [
                        "MANUAL"
                    ],
                    "neq": "MANUAL",
                    "nin": [
                        "MANUAL"
                    ]
                }
            ],
            "memberIds": [
                "id1",
                "id2"
            ],
            "searchTerm": {
                "search": "string"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "creationDate": {
                "direction": "ASC",
                "priority": 1
            },
            "importType": {
                "direction": "ASC",
                "priority": 1
            },
            "lastModified": {
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

#### Operation Arguments for query.user.usersGroupList ####

`accountId` [ID] - (required) Unique identifier of the Cato account.
`usersGroupListInput` [UsersGroupListInput] - (required) N/A
