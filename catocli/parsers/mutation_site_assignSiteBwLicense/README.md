
## CATO-CLI - mutation.site.assignSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.assignSiteBwLicense) for documentation on this operation.

### Usage for mutation.site.assignSiteBwLicense:

`catocli mutation site assignSiteBwLicense -h`

`catocli mutation site assignSiteBwLicense <json>`

`catocli mutation site assignSiteBwLicense "$(cat < mutation.site.assignSiteBwLicense.json)"`

`catocli mutation site assignSiteBwLicense '{"assignSiteBwLicenseInput":{"bw":1,"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site assignSiteBwLicense -p '{
    "assignSiteBwLicenseInput": {
        "bw": 1,
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.assignSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`assignSiteBwLicenseInput` [AssignSiteBwLicenseInput] - (required) N/A    
