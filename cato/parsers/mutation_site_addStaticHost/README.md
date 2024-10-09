
## CATO-CLI - mutation.site.addStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-addStaticHost) for documentation on this operation.

### Usage for mutation.site.addStaticHost:

`cato mutation site addStaticHost -h`

`cato mutation site addStaticHost <accountID> <json>`

`cato mutation site addStaticHost 12345 "$(cat < addStaticHost.json)"`

`cato mutation site addStaticHost 12345 '{"AddStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.addStaticHost ####
`AddStaticHostInput` [AddStaticHostInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
