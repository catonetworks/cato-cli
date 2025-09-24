
## CATO-CLI - mutation.sites.removeSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.removeSiteBwLicense) for documentation on this operation.

### Usage for mutation.sites.removeSiteBwLicense:

`catocli mutation sites removeSiteBwLicense -h`

`catocli mutation sites removeSiteBwLicense <json>`

`catocli mutation sites removeSiteBwLicense "$(cat < mutation.sites.removeSiteBwLicense.json)"`

`catocli mutation sites removeSiteBwLicense '{"removeSiteBwLicenseInput":{"licenseId":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites removeSiteBwLicense -p '{
    "removeSiteBwLicenseInput": {
        "licenseId": "id",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.removeSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`removeSiteBwLicenseInput` [RemoveSiteBwLicenseInput] - (required) N/A    
