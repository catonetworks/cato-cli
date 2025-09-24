
## CATO-CLI - mutation.site.replaceSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.replaceSiteBwLicense) for documentation on this operation.

### Usage for mutation.site.replaceSiteBwLicense:

`catocli mutation site replaceSiteBwLicense -h`

`catocli mutation site replaceSiteBwLicense <json>`

`catocli mutation site replaceSiteBwLicense "$(cat < mutation.site.replaceSiteBwLicense.json)"`

`catocli mutation site replaceSiteBwLicense '{"replaceSiteBwLicenseInput":{"bw":1,"licenseIdToAdd":"id","licenseIdToRemove":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site replaceSiteBwLicense -p '{
    "replaceSiteBwLicenseInput": {
        "bw": 1,
        "licenseIdToAdd": "id",
        "licenseIdToRemove": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.replaceSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`replaceSiteBwLicenseInput` [ReplaceSiteBwLicenseInput] - (required) N/A    
