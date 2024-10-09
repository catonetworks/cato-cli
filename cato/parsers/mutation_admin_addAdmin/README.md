
## CATO-CLI - mutation.admin.addAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-addAdmin) for documentation on this operation.

### Usage for mutation.admin.addAdmin:

`cato mutation admin addAdmin -h`

`cato mutation admin addAdmin <accountID> <json>`

`cato mutation admin addAdmin 12345 "$(cat < addAdmin.json)"`

`cato mutation admin addAdmin 12345 '{"AddAdminInput": {"UpdateAdminRoleInput": {"allowedAccounts": {"allowedAccounts": ["ID"]}, "allowedEntities": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "role": {"id": {"id": "ID"}, "name": {"name": "String"}}}, "email": {"email": "String"}, "firstName": {"firstName": "String"}, "lastName": {"lastName": "String"}, "mfaEnabled": {"mfaEnabled": "Boolean"}, "passwordNeverExpires": {"passwordNeverExpires": "Boolean"}}}'`

#### Operation Arguments for mutation.admin.addAdmin ####
`AddAdminInput` [AddAdminInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
