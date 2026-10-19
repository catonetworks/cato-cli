
## CATO-CLI - mutation.rbac:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.rbac) for documentation on this operation.

### Usage for mutation.rbac:

```bash
catocli mutation rbac -h

catocli mutation rbac <json>

catocli mutation rbac --json-file mutation.rbac.json

catocli mutation rbac '{"roleManagementCreateRoleInput":{"description":"string","name":"string","permission":[{"action":"VIEW","resource":"string"}]},"roleManagementDeleteRoleInput":{"id":"id"},"roleManagementUpdateRoleInput":{"description":"string","id":"id","name":"string","permission":[{"action":"VIEW","resource":"string"}]}}'

catocli mutation rbac '{
    "roleManagementCreateRoleInput": {
        "description": "string",
        "name": "string",
        "permission": [
            {
                "action": "VIEW",
                "resource": "string"
            }
        ]
    },
    "roleManagementDeleteRoleInput": {
        "id": "id"
    },
    "roleManagementUpdateRoleInput": {
        "description": "string",
        "id": "id",
        "name": "string",
        "permission": [
            {
                "action": "VIEW",
                "resource": "string"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.rbac ####

`accountId` [ID] - (required) N/A
`roleManagementCreateRoleInput` [RoleManagementCreateRoleInput] - (required) N/A
`roleManagementDeleteRoleInput` [RoleManagementDeleteRoleInput] - (required) N/A
`roleManagementUpdateRoleInput` [RoleManagementUpdateRoleInput] - (required) N/A
