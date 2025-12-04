
## CATO-CLI - query.catalogs.catalogApplicationList:
[Click here](https://api.catonetworks.com/documentation/#query-query.catalogs.catalogApplicationList) for documentation on this operation.

### Usage for query.catalogs.catalogApplicationList:

```bash
catocli query catalogs catalogApplicationList -h

catocli query catalogs catalogApplicationList <json>

catocli query catalogs catalogApplicationList --json-file query.catalogs.catalogApplicationList.json

catocli query catalogs catalogApplicationList '{"catalogApplicationListInput":{"catalogApplicationFilterInput":{"activity":{"hasAny":{"by":"ID","input":"string"}},"capability":{"hasAny":"APP_CONTROL_INLINE"},"category":{"hasAny":{"by":"ID","input":"string"}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"recentlyAdded":{"eq":true,"neq":true},"risk":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"tenantActivity":{"eq":true,"neq":true},"type":{"eq":"APPLICATION","in":"APPLICATION","neq":"APPLICATION","nin":"APPLICATION"}},"catalogApplicationSortInput":{"category":{"name":{"direction":"ASC","priority":1}},"description":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"risk":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'

catocli query catalogs catalogApplicationList '{
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
            "tenantActivity": {
                "eq": true,
                "neq": true
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
}'
```

#### Operation Arguments for query.catalogs.catalogApplicationList ####

`accountId` [ID] - (required) N/A    
`catalogApplicationListInput` [CatalogApplicationListInput] - (required) N/A    
