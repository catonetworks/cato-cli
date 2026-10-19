
## CATO-CLI - mutation.rbac.roleManagement.updateRole:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.rbac.roleManagement.updateRole) for documentation on this operation.

### Usage for mutation.rbac.roleManagement.updateRole:

```bash
catocli mutation rbac roleManagement updateRole -h

catocli mutation rbac roleManagement updateRole <json>

catocli mutation rbac roleManagement updateRole --json-file mutation.rbac.roleManagement.updateRole.json

catocli mutation rbac roleManagement updateRole '{"roleManagementUpdateRoleInput":{"description":"string","id":"id","name":"string","permission":[{"action":"VIEW","resource":"string"}]}}'

catocli mutation rbac roleManagement updateRole '{
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

#### Operation Arguments for mutation.rbac.roleManagement.updateRole ####

`accountId` [ID] - (required) N/A
`roleManagementUpdateRoleInput` [RoleManagementUpdateRoleInput] - (required) N/A
