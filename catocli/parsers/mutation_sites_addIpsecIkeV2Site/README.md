
## CATO-CLI - mutation.sites.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.sites.addIpsecIkeV2Site:

`catocli mutation sites addIpsecIkeV2Site -h`

`catocli mutation sites addIpsecIkeV2Site <json>`

`catocli mutation sites addIpsecIkeV2Site "$(cat < mutation.sites.addIpsecIkeV2Site.json)"`

`catocli mutation sites addIpsecIkeV2Site '{"addIpsecIkeV2SiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"description":"string","name":"string","nativeNetworkRange":"example_value","siteType":"BRANCH","vlan":"example_value"}}'`

`catocli mutation sites addIpsecIkeV2Site -p '{
    "addIpsecIkeV2SiteInput": {
        "addSiteLocationInput": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "description": "string",
        "name": "string",
        "nativeNetworkRange": "example_value",
        "siteType": "BRANCH",
        "vlan": "example_value"
    }
}'`


#### Operation Arguments for mutation.sites.addIpsecIkeV2Site ####

`accountId` [ID] - (required) N/A    
`addIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A    
