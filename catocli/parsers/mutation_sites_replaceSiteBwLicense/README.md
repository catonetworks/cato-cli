
## CATO-CLI - mutation.sites.replaceSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-replaceSiteBwLicense) for documentation on this operation.

### Usage for mutation.sites.replaceSiteBwLicense:

`catocli mutation sites replaceSiteBwLicense -h`

`catocli mutation sites replaceSiteBwLicense <json>`

`catocli mutation sites replaceSiteBwLicense "$(cat < replaceSiteBwLicense.json)"`

`catocli mutation sites replaceSiteBwLicense '{"replaceSiteBwLicenseInput": {"bw": {"bw": "Int"}, "licenseIdToAdd": {"licenseIdToAdd": "ID"}, "licenseIdToRemove": {"licenseIdToRemove": "ID"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.sites.replaceSiteBwLicense ####
`accountId` [ID] - (required) N/A 
`replaceSiteBwLicenseInput` [ReplaceSiteBwLicenseInput] - (required) N/A 
