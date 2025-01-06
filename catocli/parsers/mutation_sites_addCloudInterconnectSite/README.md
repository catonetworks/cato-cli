
## CATO-CLI - mutation.sites.addCloudInterconnectSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addCloudInterconnectSite) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectSite:

`catocli mutation sites addCloudInterconnectSite -h`

`catocli mutation sites addCloudInterconnectSite <json>`

`catocli mutation sites addCloudInterconnectSite "$(cat < addCloudInterconnectSite.json)"`

`catocli mutation sites addCloudInterconnectSite '{"addCloudInterconnectSiteInput": {"addSiteLocationInput": {"address": {"address": "String"}, "city": {"city": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}}}'`

#### Operation Arguments for mutation.sites.addCloudInterconnectSite ####
`accountId` [ID] - (required) N/A 
`addCloudInterconnectSiteInput` [AddCloudInterconnectSiteInput] - (required) N/A 
