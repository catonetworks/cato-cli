
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

`catocli mutation site addSocketSite -h`

`catocli mutation site addSocketSite <accountID> <json>`

`catocli mutation site addSocketSite 12345 "$(cat < addSocketSite.json)"`

`catocli mutation site addSocketSite 12345 '{"AddSocketSiteInput": {"AddSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "connectionType": {"connectionType": "enum(SiteConnectionTypeEnum)"}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}}}'`

#### Operation Arguments for mutation.site.addSocketSite ####
`AddSocketSiteInput` [AddSocketSiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
