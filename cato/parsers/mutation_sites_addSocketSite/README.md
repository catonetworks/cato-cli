
## CATO-CLI - mutation.sites.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketSite) for documentation on this operation.

### Usage for mutation.sites.addSocketSite:

`cato mutation sites addSocketSite -h`

`cato mutation sites addSocketSite <accountID> <json>`

`cato mutation sites addSocketSite 12345 "$(cat < addSocketSite.json)"`

`cato mutation sites addSocketSite 12345 '{"AddSocketSiteInput": {"AddSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "connectionType": {"connectionType": "enum(SiteConnectionTypeEnum)"}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}}}'`

#### Operation Arguments for mutation.sites.addSocketSite ####
`AddSocketSiteInput` [AddSocketSiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
