
## CATO-CLI - mutation.site.removeSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.removeSiteBwLicense) for documentation on this operation.

### Usage for mutation.site.removeSiteBwLicense:

`catocli mutation site removeSiteBwLicense -h`

`catocli mutation site removeSiteBwLicense <json>`

`catocli mutation site removeSiteBwLicense "$(cat < mutation.site.removeSiteBwLicense.json)"`

`catocli mutation site removeSiteBwLicense '{"removeSiteBwLicenseInput":{"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site removeSiteBwLicense -p '{
    "removeSiteBwLicenseInput": {
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.removeSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`removeSiteBwLicenseInput` [RemoveSiteBwLicenseInput] - (required) N/A    
