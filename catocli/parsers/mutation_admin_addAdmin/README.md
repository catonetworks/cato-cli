
## CATO-CLI - mutation.admin.addAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.admin.addAdmin) for documentation on this operation.

### Usage for mutation.admin.addAdmin:

`catocli mutation admin addAdmin -h`

`catocli mutation admin addAdmin <json>`

`catocli mutation admin addAdmin "$(cat < mutation.admin.addAdmin.json)"`

`catocli mutation admin addAdmin '{"addAdminInput":{"adminType":"LOGIN","email":"string","firstName":"string","lastName":"string","passwordNeverExpires":true,"updateAdminRoleInput":{"allowedAccounts":["id1","id2"],"allowedEntities":{"id":"id","name":"string","type":"account"},"role":{"id":"id","name":"string"}}}}'`

`catocli mutation admin addAdmin -p '{
    "addAdminInput": {
        "adminType": "LOGIN",
        "email": "string",
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


#### Operation Arguments for mutation.admin.addAdmin ####

`accountId` [ID] - (required) N/A    
`addAdminInput` [AddAdminInput] - (required) N/A    
