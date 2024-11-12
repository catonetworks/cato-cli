
## CATO-CLI - mutation.sites.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketSite) for documentation on this operation.

### Usage for mutation.sites.addSocketSite:

`catocli mutation sites addSocketSite -h`

`catocli mutation sites addSocketSite <json>`

`catocli mutation sites addSocketSite "$(cat < addSocketSite.json)"`

`catocli mutation sites addSocketSite '{"addSocketSiteInput": {"addSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "connectionType": {"connectionType": "enum(SiteConnectionTypeEnum)"}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}}}'`

#### Operation Arguments for mutation.sites.addSocketSite ####
`accountId` [ID] - (required) N/A 
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A 
