
## CATO-CLI - mutation.sites.addStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-addStaticHost) for documentation on this operation.

### Usage for mutation.sites.addStaticHost:

`cato mutation sites addStaticHost -h`

`cato mutation sites addStaticHost <accountID> <json>`

`cato mutation sites addStaticHost 12345 "$(cat < addStaticHost.json)"`

`cato mutation sites addStaticHost 12345 '{"AddStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.sites.addStaticHost ####
`AddStaticHostInput` [AddStaticHostInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
