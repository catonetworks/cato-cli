
## CATO-CLI - mutation.sites.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSocketSite) for documentation on this operation.

### Usage for mutation.sites.addSocketSite:

`catocli mutation sites addSocketSite -h`

`catocli mutation sites addSocketSite <json>`

`catocli mutation sites addSocketSite "$(cat < mutation.sites.addSocketSite.json)"`

`catocli mutation sites addSocketSite '{"addSocketSiteInput":{"addSiteLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"connectionType":"SOCKET_X1500","description":"string","name":"string","nativeNetworkRange":"example_value","siteType":"BRANCH","translatedSubnet":"example_value","vlan":"example_value"}}'`

`catocli mutation sites addSocketSite -p '{
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


#### Operation Arguments for mutation.sites.addSocketSite ####

`accountId` [ID] - (required) N/A    
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A    
