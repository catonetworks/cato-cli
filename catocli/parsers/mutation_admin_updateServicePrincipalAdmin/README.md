
## CATO-CLI - mutation.admin.updateServicePrincipalAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.admin.updateServicePrincipalAdmin) for documentation on this operation.

### Usage for mutation.admin.updateServicePrincipalAdmin:

`catocli mutation admin updateServicePrincipalAdmin -h`

`catocli mutation admin updateServicePrincipalAdmin <json>`

`catocli mutation admin updateServicePrincipalAdmin "$(cat < mutation.admin.updateServicePrincipalAdmin.json)"`

`catocli mutation admin updateServicePrincipalAdmin '{"adminID":"id","updateServicePrincipalAdminInput":{"name":"string","updateAdminRoleInput":{"allowedAccounts":["id1","id2"],"allowedEntities":{"id":"id","name":"string","type":"account"},"role":{"id":"id","name":"string"}}}}'`

`catocli mutation admin updateServicePrincipalAdmin -p '{
    "adminID": "id",
    "updateServicePrincipalAdminInput": {
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


#### Operation Arguments for mutation.admin.updateServicePrincipalAdmin ####

`accountId` [ID] - (required) N/A    
`adminID` [ID] - (required) N/A    
`updateServicePrincipalAdminInput` [UpdateServicePrincipalAdminInput] - (required) N/A    
