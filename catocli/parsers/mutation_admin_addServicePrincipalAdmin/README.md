
## CATO-CLI - mutation.admin.addServicePrincipalAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.admin.addServicePrincipalAdmin) for documentation on this operation.

### Usage for mutation.admin.addServicePrincipalAdmin:

`catocli mutation admin addServicePrincipalAdmin -h`

`catocli mutation admin addServicePrincipalAdmin <json>`

`catocli mutation admin addServicePrincipalAdmin "$(cat < mutation.admin.addServicePrincipalAdmin.json)"`

`catocli mutation admin addServicePrincipalAdmin '{"addServicePrincipalAdminInput":{"email":"string","name":"string","updateAdminRoleInput":{"allowedAccounts":["id1","id2"],"allowedEntities":{"id":"id","name":"string","type":"account"},"role":{"id":"id","name":"string"}}}}'`

`catocli mutation admin addServicePrincipalAdmin -p '{
    "addServicePrincipalAdminInput": {
        "email": "string",
        "name": "string",
        "updateAdminRoleInput": {
            "allowedAccounts": [
                "id1",
                "id2"
            ],
            "allowedEntities": {
                "id": "id",
                "name": "string",
                "type": "account"
            },
            "role": {
                "id": "id",
                "name": "string"
            }
        }
    }
}'`


#### Operation Arguments for mutation.admin.addServicePrincipalAdmin ####

`accountId` [ID] - (required) N/A    
`addServicePrincipalAdminInput` [AddServicePrincipalAdminInput] - (required) N/A    
