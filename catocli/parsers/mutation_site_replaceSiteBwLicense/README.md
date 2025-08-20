
## CATO-CLI - mutation.site.replaceSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-replaceSiteBwLicense) for documentation on this operation.

### Usage for mutation.site.replaceSiteBwLicense:

`catocli mutation site replaceSiteBwLicense -h`

`catocli mutation site replaceSiteBwLicense <json>`

`catocli mutation site replaceSiteBwLicense "$(cat < replaceSiteBwLicense.json)"`

`catocli mutation site replaceSiteBwLicense '{"replaceSiteBwLicenseInput": {"bw": {"bw": "Int"}, "licenseIdToAdd": {"licenseIdToAdd": "ID"}, "licenseIdToRemove": {"licenseIdToRemove": "ID"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.site.replaceSiteBwLicense ####
`accountId` [ID] - (required) N/A 
`replaceSiteBwLicenseInput` [ReplaceSiteBwLicenseInput] - (required) N/A 
