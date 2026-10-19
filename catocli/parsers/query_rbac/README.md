
## CATO-CLI - query.rbac:
[Click here](https://api.catonetworks.com/documentation/#query-query.rbac) for documentation on this operation.

### Usage for query.rbac:

```bash
catocli query rbac -h

catocli query rbac <json>

catocli query rbac --json-file query.rbac.json

catocli query rbac '{"id":"id","roleManagementRoleListInput":{"filter":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"predefined":{"eq":true,"neq":true}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query rbac '{
    "id": "id",
    "roleManagementRoleListInput": {
        "filter": {
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
            "predefined": {
                "eq": true,
                "neq": true
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.rbac ####

`accountId` [ID] - (required) N/A
`id` [ID] - (required) N/A
`roleManagementRoleListInput` [RoleManagementRoleListInput] - (required) N/A
