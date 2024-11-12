
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

`catocli mutation site addSocketSite -h`

`catocli mutation site addSocketSite <json>`

`catocli mutation site addSocketSite "$(cat < addSocketSite.json)"`

`catocli mutation site addSocketSite '{"addSocketSiteInput": {"addSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "connectionType": {"connectionType": "enum(SiteConnectionTypeEnum)"}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}}}'`

#### Operation Arguments for mutation.site.addSocketSite ####
`accountId` [ID] - (required) N/A 
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A 
