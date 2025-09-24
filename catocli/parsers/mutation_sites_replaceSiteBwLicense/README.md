
## CATO-CLI - mutation.sites.replaceSiteBwLicense:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.replaceSiteBwLicense) for documentation on this operation.

### Usage for mutation.sites.replaceSiteBwLicense:

`catocli mutation sites replaceSiteBwLicense -h`

`catocli mutation sites replaceSiteBwLicense <json>`

`catocli mutation sites replaceSiteBwLicense "$(cat < mutation.sites.replaceSiteBwLicense.json)"`

`catocli mutation sites replaceSiteBwLicense '{"replaceSiteBwLicenseInput":{"bw":1,"licenseIdToAdd":"id","licenseIdToRemove":"id","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites replaceSiteBwLicense -p '{
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


#### Operation Arguments for mutation.sites.replaceSiteBwLicense ####

`accountId` [ID] - (required) N/A    
`replaceSiteBwLicenseInput` [ReplaceSiteBwLicenseInput] - (required) N/A    
