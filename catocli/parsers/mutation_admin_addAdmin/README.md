
## CATO-CLI - mutation.admin.addAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-addAdmin) for documentation on this operation.

### Usage for mutation.admin.addAdmin:

`catocli mutation admin addAdmin -h`

`catocli mutation admin addAdmin <json>`

`catocli mutation admin addAdmin "$(cat < addAdmin.json)"`

`catocli mutation admin addAdmin '{"AddAdminInput": {"UpdateAdminRoleInput": {"allowedAccounts": {"allowedAccounts": ["ID"]}, "allowedEntities": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "role": {"id": {"id": "ID"}, "name": {"name": "String"}}}, "email": {"email": "String"}, "firstName": {"firstName": "String"}, "lastName": {"lastName": "String"}, "mfaEnabled": {"mfaEnabled": "Boolean"}, "passwordNeverExpires": {"passwordNeverExpires": "Boolean"}}}'`

#### Operation Arguments for mutation.admin.addAdmin ####
`AddAdminInput` [AddAdminInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
