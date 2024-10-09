
## CATO-CLI - mutation.sites.updateHa:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateHa) for documentation on this operation.

### Usage for mutation.sites.updateHa:

`cato mutation sites updateHa -h`

`cato mutation sites updateHa <accountID> <json>`

`cato mutation sites updateHa 12345 "$(cat < updateHa.json)"`

`cato mutation sites updateHa 12345 '{"UpdateHaInput": {"primaryManagementIp": {"primaryManagementIp": "IPAddress"}, "secondaryManagementIp": {"secondaryManagementIp": "IPAddress"}, "vrid": {"vrid": "Int"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.sites.updateHa ####
`UpdateHaInput` [UpdateHaInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
