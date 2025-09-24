
## CATO-CLI - mutation.admin.updateAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.admin.updateAdmin) for documentation on this operation.

### Usage for mutation.admin.updateAdmin:

`catocli mutation admin updateAdmin -h`

`catocli mutation admin updateAdmin <json>`

`catocli mutation admin updateAdmin "$(cat < mutation.admin.updateAdmin.json)"`

`catocli mutation admin updateAdmin '{"adminID":"id","updateAdminInput":{"firstName":"string","lastName":"string","passwordNeverExpires":true,"updateAdminRoleInput":{"allowedAccounts":["id1","id2"],"allowedEntities":{"id":"id","name":"string","type":"account"},"role":{"id":"id","name":"string"}}}}'`

`catocli mutation admin updateAdmin -p '{
    "adminID": "id",
    "updateAdminInput": {
        "firstName": "string",
        "lastName": "string",
        "passwordNeverExpires": true,
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


#### Operation Arguments for mutation.admin.updateAdmin ####

`accountId` [ID] - (required) N/A    
`adminID` [ID] - (required) N/A    
`updateAdminInput` [UpdateAdminInput] - (required) N/A    
