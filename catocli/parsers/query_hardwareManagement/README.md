
## CATO-CLI - query.hardwareManagement:
[Click here](https://api.catonetworks.com/documentation/#query-hardwareManagement) for documentation on this operation.

### Usage for query.hardwareManagement:

`catocli query hardwareManagement -h`

`catocli query hardwareManagement <json>`

`catocli query hardwareManagement "$(cat < hardwareManagement.json)"`

`catocli query hardwareManagement '{"socketInventoryInput": {"pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}, "socketInventoryFilterInput": {"freeText": {"search": {"search": "String"}}}, "socketInventoryOrderInput": {"deliverySiteName": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "description": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "installedSite": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "serialNumber": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "shippingCompany": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "shippingDate": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "socketType": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "status": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}}}'`

#### Operation Arguments for query.hardwareManagement ####
`accountId` [ID] - (required) N/A 
`socketInventoryInput` [SocketInventoryInput] - (optional) N/A 
