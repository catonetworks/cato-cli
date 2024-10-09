
## CATO-CLI - mutation.sites.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateSiteGeneralDetails:

`catocli mutation sites updateSiteGeneralDetails -h`

`catocli mutation sites updateSiteGeneralDetails <accountID> <json>`

`catocli mutation sites updateSiteGeneralDetails 12345 "$(cat < updateSiteGeneralDetails.json)"`

`catocli mutation sites updateSiteGeneralDetails 12345 '{"UpdateSiteGeneralDetailsInput": {"UpdateSiteLocationInput": {"address": {"address": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}, "description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.sites.updateSiteGeneralDetails ####
`UpdateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
