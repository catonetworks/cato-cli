
## CATO-CLI - mutation.site.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2Site:

`catocli mutation site addIpsecIkeV2Site -h`

`catocli mutation site addIpsecIkeV2Site <json>`

`catocli mutation site addIpsecIkeV2Site "$(cat < mutation.site.addIpsecIkeV2Site.json)"`

`catocli mutation site addIpsecIkeV2Site '{"addIpsecIkeV2SiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"description":"string","name":"string","nativeNetworkRange":"example_value","siteType":"BRANCH","vlan":"example_value"}}'`

`catocli mutation site addIpsecIkeV2Site -p '{
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


#### Operation Arguments for mutation.site.addIpsecIkeV2Site ####

`accountId` [ID] - (required) N/A    
`addIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A    
