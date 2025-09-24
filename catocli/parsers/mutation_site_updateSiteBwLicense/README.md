
## CATO-CLI - mutation.site.updateSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteBwLicense) for documentation on this operation.

### Usage for mutation.site.updateSiteBwLicense:

`catocli mutation site updateSiteBwLicense -h`

`catocli mutation site updateSiteBwLicense <json>`

`catocli mutation site updateSiteBwLicense "$(cat < mutation.site.updateSiteBwLicense.json)"`

`catocli mutation site updateSiteBwLicense '{"updateSiteBwLicenseInput":{"bw":1,"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site updateSiteBwLicense -p '{
    "updateSiteBwLicenseInput": {
        "bw": 1,
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.updateSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`updateSiteBwLicenseInput` [UpdateSiteBwLicenseInput] - (required) N/A    
