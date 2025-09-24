
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

`catocli mutation site addSocketSite -h`

`catocli mutation site addSocketSite <json>`

`catocli mutation site addSocketSite "$(cat < mutation.site.addSocketSite.json)"`

`catocli mutation site addSocketSite '{"addSocketSiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"connectionType":"SOCKET_X1500","description":"string","name":"string","nativeNetworkRange":"example_value","siteType":"BRANCH","translatedSubnet":"example_value","vlan":"example_value"}}'`

`catocli mutation site addSocketSite -p '{
    "addSocketSiteInput": {
        "addSiteLocationInput": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "connectionType": "SOCKET_X1500",
        "description": "string",
        "name": "string",
        "nativeNetworkRange": "example_value",
        "siteType": "BRANCH",
        "translatedSubnet": "example_value",
        "vlan": "example_value"
    }
}'`


#### Operation Arguments for mutation.site.addSocketSite ####

`accountId` [ID] - (required) N/A    
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A    
