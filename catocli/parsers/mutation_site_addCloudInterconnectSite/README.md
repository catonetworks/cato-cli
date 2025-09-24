
## CATO-CLI - mutation.site.addCloudInterconnectSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addCloudInterconnectSite) for documentation on this operation.

### Usage for mutation.site.addCloudInterconnectSite:

`catocli mutation site addCloudInterconnectSite -h`

`catocli mutation site addCloudInterconnectSite <json>`

`catocli mutation site addCloudInterconnectSite "$(cat < mutation.site.addCloudInterconnectSite.json)"`

`catocli mutation site addCloudInterconnectSite '{"addCloudInterconnectSiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"description":"string","name":"string","siteType":"BRANCH"}}'`

`catocli mutation site addCloudInterconnectSite -p '{
    "addCloudInterconnectSiteInput": {
        "addSiteLocationInput": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "description": "string",
        "name": "string",
        "siteType": "BRANCH"
    }
}'`


#### Operation Arguments for mutation.site.addCloudInterconnectSite ####

`accountId` [ID] - (required) N/A    
`addCloudInterconnectSiteInput` [AddCloudInterconnectSiteInput] - (required) N/A    
