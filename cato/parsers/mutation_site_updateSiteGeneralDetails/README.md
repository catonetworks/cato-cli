
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

`cato mutation site updateSiteGeneralDetails -h`

`cato mutation site updateSiteGeneralDetails <accountID> <json>`

`cato mutation site updateSiteGeneralDetails 12345 "$(cat < updateSiteGeneralDetails.json)"`

`cato mutation site updateSiteGeneralDetails 12345 '{"UpdateSiteGeneralDetailsInput": {"UpdateSiteLocationInput": {"address": {"address": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####
`UpdateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
