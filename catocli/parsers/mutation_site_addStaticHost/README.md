
## CATO-CLI - mutation.site.addStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-addStaticHost) for documentation on this operation.

### Usage for mutation.site.addStaticHost:

`catocli mutation site addStaticHost -h`

`catocli mutation site addStaticHost <accountID> <json>`

`catocli mutation site addStaticHost 12345 "$(cat < addStaticHost.json)"`

`catocli mutation site addStaticHost 12345 '{"AddStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.addStaticHost ####
`AddStaticHostInput` [AddStaticHostInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 