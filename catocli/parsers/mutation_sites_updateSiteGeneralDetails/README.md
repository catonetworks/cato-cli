
## CATO-CLI - mutation.sites.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateSiteGeneralDetails:

`catocli mutation sites updateSiteGeneralDetails -h`

`catocli mutation sites updateSiteGeneralDetails <json>`

`catocli mutation sites updateSiteGeneralDetails "$(cat < updateSiteGeneralDetails.json)"`

`catocli mutation sites updateSiteGeneralDetails '{"siteId": "ID", "updateSiteGeneralDetailsInput": {"description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}, "updateSiteLocationInput": {"address": {"address": "String"}, "cityName": {"cityName": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}}}'`

#### Operation Arguments for mutation.sites.updateSiteGeneralDetails ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
