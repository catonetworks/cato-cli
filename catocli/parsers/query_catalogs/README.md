
## CATO-CLI - query.catalogs:
[Click here](https://api.catonetworks.com/documentation/#query-query.catalogs) for documentation on this operation.

### Usage for query.catalogs:

`catocli query catalogs -h`

`catocli query catalogs <json>`

`catocli query catalogs "$(cat < query.catalogs.json)"`

`catocli query catalogs '{"applicationRefInput":{"by":"ID","input":"string"},"catalogApplicationContentTypeGroupListInput":{"catalogApplicationContentTypeGroupFilterInput":{"contentType":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"catalogApplicationContentTypeGroupSortInput":{"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"catalogApplicationListInput":{"catalogApplicationFilterInput":{"activity":{"hasAny":{"by":"ID","input":"string"}},"capability":{"hasAny":"APP_CONTROL_INLINE"},"category":{"hasAny":{"by":"ID","input":"string"}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"recentlyAdded":{"eq":true,"neq":true},"risk":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"type":{"eq":"APPLICATION","in":"APPLICATION","neq":"APPLICATION","nin":"APPLICATION"}},"catalogApplicationSortInput":{"category":{"name":{"direction":"ASC","priority":1}},"description":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"risk":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'`

`catocli query catalogs -p '{
    "applicationRefInput": {
        "by": "ID",
        "input": "string"
    },
    "catalogApplicationContentTypeGroupListInput": {
        "catalogApplicationContentTypeGroupFilterInput": {
            "contentType": {
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
        "catalogApplicationContentTypeGroupSortInput": {
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
    "catalogApplicationListInput": {
        "catalogApplicationFilterInput": {
            "activity": {
                "hasAny": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "capability": {
                "hasAny": "APP_CONTROL_INLINE"
            },
            "category": {
                "hasAny": {
                    "by": "ID",
                    "input": "string"
                }
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
            },
            "recentlyAdded": {
                "eq": true,
                "neq": true
            },
            "risk": {
                "between": [
                    1,
                    2
                ],
                "eq": 1,
                "gt": 1,
                "gte": 1,
                "in": [
                    1,
                    2
                ],
                "lt": 1,
                "lte": 1,
                "neq": 1,
                "nin": [
                    1,
                    2
                ]
            },
            "type": {
                "eq": "APPLICATION",
                "in": "APPLICATION",
                "neq": "APPLICATION",
                "nin": "APPLICATION"
            }
        },
        "catalogApplicationSortInput": {
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
            },
            "risk": {
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


#### Operation Arguments for query.catalogs ####

`accountId` [ID] - (required) N/A    
`applicationRefInput` [ApplicationRefInput] - (required) N/A    
`catalogApplicationContentTypeGroupListInput` [CatalogApplicationContentTypeGroupListInput] - (required) N/A    
`catalogApplicationListInput` [CatalogApplicationListInput] - (required) N/A    
