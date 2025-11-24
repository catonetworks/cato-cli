
## CATO-CLI - query.catalogs.contentTypeGroupList:
[Click here](https://api.catonetworks.com/documentation/#query-query.catalogs.contentTypeGroupList) for documentation on this operation.

### Usage for query.catalogs.contentTypeGroupList:

```bash
catocli query catalogs contentTypeGroupList -h

catocli query catalogs contentTypeGroupList <json>

catocli query catalogs contentTypeGroupList --json-file query.catalogs.contentTypeGroupList.json

catocli query catalogs contentTypeGroupList '{"catalogApplicationContentTypeGroupListInput":{"catalogApplicationContentTypeGroupFilterInput":{"contentType":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"catalogApplicationContentTypeGroupSortInput":{"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'

catocli query catalogs contentTypeGroupList '{
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
    }
}'
```

#### Operation Arguments for query.catalogs.contentTypeGroupList ####

`accountId` [ID] - (required) N/A    
`catalogApplicationContentTypeGroupListInput` [CatalogApplicationContentTypeGroupListInput] - (required) N/A    
