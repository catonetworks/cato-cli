
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

`catocli mutation site updateSiteGeneralDetails -h`

`catocli mutation site updateSiteGeneralDetails <json>`

`catocli mutation site updateSiteGeneralDetails "$(cat < mutation.site.updateSiteGeneralDetails.json)"`

`catocli mutation site updateSiteGeneralDetails '{"siteId":"id","updateSiteGeneralDetailsInput":{"description":"string","name":"string","siteType":"BRANCH","updateSiteLocationInput":{"address":"string","cityName":"string","countryCode":"string","stateCode":"string","timezone":"string"},"updateSitePreferredPopLocationInput":{"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}}}}'`

`catocli mutation site updateSiteGeneralDetails -p '{
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


#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A    
