
## CATO-CLI - mutation.site.addCloudInterconnectSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addCloudInterconnectSite) for documentation on this operation.

### Usage for mutation.site.addCloudInterconnectSite:

`catocli mutation site addCloudInterconnectSite -h`

`catocli mutation site addCloudInterconnectSite <json>`

`catocli mutation site addCloudInterconnectSite "$(cat < addCloudInterconnectSite.json)"`

`catocli mutation site addCloudInterconnectSite '{"addCloudInterconnectSiteInput": {"addSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}}}'`

#### Operation Arguments for mutation.site.addCloudInterconnectSite ####
`accountId` [ID] - (required) N/A 
`addCloudInterconnectSiteInput` [AddCloudInterconnectSiteInput] - (required) N/A 
