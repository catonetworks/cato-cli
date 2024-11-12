
## CATO-CLI - mutation.admin.updateAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateAdmin) for documentation on this operation.

### Usage for mutation.admin.updateAdmin:

`catocli mutation admin updateAdmin -h`

`catocli mutation admin updateAdmin <json>`

`catocli mutation admin updateAdmin "$(cat < updateAdmin.json)"`

`catocli mutation admin updateAdmin '{"adminID": "ID", "updateAdminInput": {"firstName": {"firstName": "String"}, "lastName": {"lastName": "String"}, "mfaEnabled": {"mfaEnabled": "Boolean"}, "passwordNeverExpires": {"passwordNeverExpires": "Boolean"}, "updateAdminRoleInput": {"allowedAccounts": {"allowedAccounts": ["ID"]}, "allowedEntities": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "role": {"id": {"id": "ID"}, "name": {"name": "String"}}}}}'`

#### Operation Arguments for mutation.admin.updateAdmin ####
`accountId` [ID] - (required) N/A 
`adminID` [ID] - (required) N/A 
`updateAdminInput` [UpdateAdminInput] - (required) N/A 
