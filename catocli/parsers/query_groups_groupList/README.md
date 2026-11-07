
## CATO-CLI - query.groups.groupList:
[Click here](https://api.catonetworks.com/documentation/#query-query.groups.groupList) for documentation on this operation.

### Usage for query.groups.groupList:

```bash
catocli query groups groupList -h

catocli query groups groupList <json>

catocli query groups groupList --json-file query.groups.groupList.json

catocli query groups groupList '{"groupListInput":{"filter":[{"audit":[{"updatedBy":{"by":"ID","input":"string"},"updatedTime":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}}],"freeText":{"search":"string"},"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"member":[{"ref":{"by":"ID","input":"string","type":"SITE"}}],"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}]}],"paging":{"from":1,"limit":1},"sort":{"audit":{"updatedBy":{"direction":"ASC","priority":1},"updatedTime":{"direction":"ASC","priority":1}},"name":{"direction":"ASC","priority":1}}}}'

catocli query groups groupList '{
    "groupListInput": {
        "filter": [
            {
                "audit": [
                    {
                        "updatedBy": {
                            "by": "ID",
                            "input": "string"
                        },
                        "updatedTime": {
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
                "member": [
                    {
                        "ref": {
                            "by": "ID",
                            "input": "string",
                            "type": "SITE"
                        }
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
                        ],
                        "regex": "string"
                    }
                ]
            }
        ],
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "audit": {
                "updatedBy": {
                    "direction": "ASC",
                    "priority": 1
                },
                "updatedTime": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

## Advanced Usage
### Additional Examples
- List all groups
- List all groups (first page of 50)
- Search groups by name
- Search groups by name (free-text match)
- Use raw query to get group list

# List all groups

```bash
# List all groups (first page of 50)
catocli query groups groupList '{
    "groupListInput": {
        "paging": {
            "from": 0,
            "limit": 50
        }
    }
}'
```

# Search groups by name

```bash
# Search groups by name (free-text match)
catocli query groups groupList '{
    "groupListInput": {
        "filter": [
            {
                "freeText": {
                    "search": "my-group"
                }
            }
        ],
        "paging": {
            "from": 0,
            "limit": 50
        }
    }
}'
```

# Use raw query to get group list

```bash
# Use raw query to get group list
catocli raw '{
     "query": "query groupsGroupList ( $accountId:ID! ) { groups ( accountId:$accountId ) { groupList { items { audit { updatedBy { id name } updatedTime } description id membersCount membersCountPerType { membersCount type } name } paging { total } } } }",
     "variables": {
         "accountId": 15412
     },
     "operationName": "groupsGroupList"
}'
```

Note: the members of each group cannot be requested inside groupList; list a
specific group's members separately with `catocli query groups group members`.



#### Operation Arguments for query.groups.groupList ####

`accountId` [ID] - (required) N/A
`groupListInput` [GroupListInput] - (required) N/A
