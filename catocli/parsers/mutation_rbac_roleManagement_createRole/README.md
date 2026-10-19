
## CATO-CLI - mutation.rbac.roleManagement.createRole:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.rbac.roleManagement.createRole) for documentation on this operation.

### Usage for mutation.rbac.roleManagement.createRole:

```bash
catocli mutation rbac roleManagement createRole -h

catocli mutation rbac roleManagement createRole <json>

catocli mutation rbac roleManagement createRole --json-file mutation.rbac.roleManagement.createRole.json

catocli mutation rbac roleManagement createRole '{"roleManagementCreateRoleInput":{"description":"string","name":"string","permission":[{"action":"VIEW","resource":"string"}]}}'

catocli mutation rbac roleManagement createRole '{
    "roleManagementCreateRoleInput": {
        "description": "string",
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

#### Operation Arguments for mutation.rbac.roleManagement.createRole ####

`accountId` [ID] - (required) N/A
`roleManagementCreateRoleInput` [RoleManagementCreateRoleInput] - (required) N/A
