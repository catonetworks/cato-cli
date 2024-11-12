
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

`catocli mutation site updateSiteGeneralDetails -h`

`catocli mutation site updateSiteGeneralDetails <json>`

`catocli mutation site updateSiteGeneralDetails "$(cat < updateSiteGeneralDetails.json)"`

`catocli mutation site updateSiteGeneralDetails '{"siteId": "ID", "updateSiteGeneralDetailsInput": {"description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}, "updateSiteLocationInput": {"address": {"address": "String"}, "cityName": {"cityName": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}}}'`

#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
