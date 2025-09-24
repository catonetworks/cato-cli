
## CATO-CLI - mutation.sites.updateSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteBwLicense) for documentation on this operation.

### Usage for mutation.sites.updateSiteBwLicense:

`catocli mutation sites updateSiteBwLicense -h`

`catocli mutation sites updateSiteBwLicense <json>`

`catocli mutation sites updateSiteBwLicense "$(cat < mutation.sites.updateSiteBwLicense.json)"`

`catocli mutation sites updateSiteBwLicense '{"updateSiteBwLicenseInput":{"bw":1,"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites updateSiteBwLicense -p '{
    "updateSiteBwLicenseInput": {
        "bw": 1,
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.updateSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`updateSiteBwLicenseInput` [UpdateSiteBwLicenseInput] - (required) N/A    
