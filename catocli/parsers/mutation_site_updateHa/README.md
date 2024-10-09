
## CATO-CLI - mutation.site.updateHa:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateHa) for documentation on this operation.

### Usage for mutation.site.updateHa:

`catocli mutation site updateHa -h`

`catocli mutation site updateHa <accountID> <json>`

`catocli mutation site updateHa 12345 "$(cat < updateHa.json)"`

`catocli mutation site updateHa 12345 '{"UpdateHaInput": {"primaryManagementIp": {"primaryManagementIp": "IPAddress"}, "secondaryManagementIp": {"secondaryManagementIp": "IPAddress"}, "vrid": {"vrid": "Int"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.updateHa ####
`UpdateHaInput` [UpdateHaInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 