
## CATO-CLI - mutation.site.updateHa:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateHa) for documentation on this operation.

### Usage for mutation.site.updateHa:

`cato mutation site updateHa -h`

`cato mutation site updateHa <accountID> <json>`

`cato mutation site updateHa 12345 "$(cat < updateHa.json)"`

`cato mutation site updateHa 12345 '{"UpdateHaInput": {"primaryManagementIp": {"primaryManagementIp": "IPAddress"}, "secondaryManagementIp": {"secondaryManagementIp": "IPAddress"}, "vrid": {"vrid": "Int"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.updateHa ####
`UpdateHaInput` [UpdateHaInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
