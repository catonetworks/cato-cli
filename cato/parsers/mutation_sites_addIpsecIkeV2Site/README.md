
## CATO-CLI - mutation.sites.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.sites.addIpsecIkeV2Site:

`cato mutation sites addIpsecIkeV2Site -h`

`cato mutation sites addIpsecIkeV2Site <accountID> <json>`

`cato mutation sites addIpsecIkeV2Site 12345 "$(cat < addIpsecIkeV2Site.json)"`

`cato mutation sites addIpsecIkeV2Site 12345 '{"AddIpsecIkeV2SiteInput": {"AddSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "siteType": {"siteType": "enum(SiteType)"}}}'`

#### Operation Arguments for mutation.sites.addIpsecIkeV2Site ####
`AddIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
