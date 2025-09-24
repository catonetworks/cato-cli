
## CATO-CLI - mutation.sites.assignSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.assignSiteBwLicense) for documentation on this operation.

### Usage for mutation.sites.assignSiteBwLicense:

`catocli mutation sites assignSiteBwLicense -h`

`catocli mutation sites assignSiteBwLicense <json>`

`catocli mutation sites assignSiteBwLicense "$(cat < mutation.sites.assignSiteBwLicense.json)"`

`catocli mutation sites assignSiteBwLicense '{"assignSiteBwLicenseInput":{"bw":1,"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites assignSiteBwLicense -p '{
    "assignSiteBwLicenseInput": {
        "bw": 1,
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.assignSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`assignSiteBwLicenseInput` [AssignSiteBwLicenseInput] - (required) N/A    
