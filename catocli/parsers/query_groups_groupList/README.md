
## CATO-CLI - query.groups.groupList:
[Click here](https://api.catonetworks.com/documentation/#query-query.groups.groupList) for documentation on this operation.

### Usage for query.groups.groupList:

`catocli query groups groupList -h`

`catocli query groups groupList <json>`

`catocli query groups groupList "$(cat < query.groups.groupList.json)"`

`catocli query groups groupList '{"groupListInput":{"groupListFilterInput":{"audit":{"updatedBy":{"by":"ID","input":"string"},"updatedTime":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]}},"freeText":{"search":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"member":{"ref":{"by":"ID","input":"string","type":"SITE"}},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"groupListSortInput":{"audit":{"updatedBy":{"direction":"ASC","priority":1},"updatedTime":{"direction":"ASC","priority":1}},"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"groupMembersListInput":{"groupMembersListFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"groupMembersListSortInput":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'`

`catocli query groups groupList -p '{
    "groupListInput": {
        "groupListFilterInput": {
            "audit": {
                "updatedBy": {
                    "by": "ID",
                    "input": "string"
                },
                "updatedTime": {
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
            "member": {
                "ref": {
                    "by": "ID",
                    "input": "string",
                    "type": "SITE"
                }
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
                ],
                "regex": "string"
            }
        },
        "groupListSortInput": {
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
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "groupMembersListInput": {
        "groupMembersListFilterInput": {
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
                ],
                "regex": "string"
            },
            "type": {
                "eq": "SITE",
                "in": "SITE",
                "neq": "SITE",
                "nin": "SITE"
            }
        },
        "groupMembersListSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    }
}'`


#### Operation Arguments for query.groups.groupList ####

`accountId` [ID] - (required) N/A    
`groupListInput` [GroupListInput] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
