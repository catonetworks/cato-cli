
## CATO-CLI - query.rbac.roleManagement.roleList:
[Click here](https://api.catonetworks.com/documentation/#query-query.rbac.roleManagement.roleList) for documentation on this operation.

### Usage for query.rbac.roleManagement.roleList:

```bash
catocli query rbac roleManagement roleList -h

catocli query rbac roleManagement roleList <json>

catocli query rbac roleManagement roleList --json-file query.rbac.roleManagement.roleList.json

catocli query rbac roleManagement roleList '{"roleManagementRoleListInput":{"filter":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"predefined":{"eq":true,"neq":true}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query rbac roleManagement roleList '{
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

#### Operation Arguments for query.rbac.roleManagement.roleList ####

`accountId` [ID] - (required) N/A
`roleManagementRoleListInput` [RoleManagementRoleListInput] - (required) N/A
