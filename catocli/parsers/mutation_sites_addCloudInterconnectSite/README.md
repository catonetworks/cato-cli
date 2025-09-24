
## CATO-CLI - mutation.sites.addCloudInterconnectSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addCloudInterconnectSite) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectSite:

`catocli mutation sites addCloudInterconnectSite -h`

`catocli mutation sites addCloudInterconnectSite <json>`

`catocli mutation sites addCloudInterconnectSite "$(cat < mutation.sites.addCloudInterconnectSite.json)"`

`catocli mutation sites addCloudInterconnectSite '{"addCloudInterconnectSiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"description":"string","name":"string","siteType":"BRANCH"}}'`

`catocli mutation sites addCloudInterconnectSite -p '{
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


#### Operation Arguments for mutation.sites.addCloudInterconnectSite ####

`accountId` [ID] - (required) N/A    
`addCloudInterconnectSiteInput` [AddCloudInterconnectSiteInput] - (required) N/A    
