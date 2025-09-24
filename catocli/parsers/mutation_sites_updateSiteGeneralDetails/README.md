
## CATO-CLI - mutation.sites.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateSiteGeneralDetails:

`catocli mutation sites updateSiteGeneralDetails -h`

`catocli mutation sites updateSiteGeneralDetails <json>`

`catocli mutation sites updateSiteGeneralDetails "$(cat < mutation.sites.updateSiteGeneralDetails.json)"`

`catocli mutation sites updateSiteGeneralDetails '{"siteId":"id","updateSiteGeneralDetailsInput":{"description":"string","name":"string","siteType":"BRANCH","updateSiteLocationInput":{"address":"string","cityName":"string","countryCode":"string","stateCode":"string","timezone":"string"},"updateSitePreferredPopLocationInput":{"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}}}}'`

`catocli mutation sites updateSiteGeneralDetails -p '{
    "siteId": "id",
    "updateSiteGeneralDetailsInput": {
        "description": "string",
        "name": "string",
        "siteType": "BRANCH",
        "updateSiteLocationInput": {
            "address": "string",
            "cityName": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "updateSitePreferredPopLocationInput": {
            "preferredOnly": true,
            "primary": {
                "by": "ID",
                "input": "string"
            },
            "secondary": {
                "by": "ID",
                "input": "string"
            }
        }
    }
}'`


#### Operation Arguments for mutation.sites.updateSiteGeneralDetails ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A    
