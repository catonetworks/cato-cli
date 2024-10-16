
## CATO-CLI - mutation.site.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2Site:

`catocli mutation site addIpsecIkeV2Site -h`

`catocli mutation site addIpsecIkeV2Site <json>`

`catocli mutation site addIpsecIkeV2Site "$(cat < addIpsecIkeV2Site.json)"`

`catocli mutation site addIpsecIkeV2Site '{"AddIpsecIkeV2SiteInput": {"AddSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}}}'`

#### Operation Arguments for mutation.site.addIpsecIkeV2Site ####
`AddIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
