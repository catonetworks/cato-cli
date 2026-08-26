
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

```bash
catocli mutation site addSocketSite -h

catocli mutation site addSocketSite <json>

catocli mutation site addSocketSite --json-file mutation.site.addSocketSite.json

catocli mutation site addSocketSite '{"addSocketSiteInput":{"connectionType":"SOCKET_X1500","description":"string","name":"string","nativeNetworkRange":"example_value","siteLocation":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH","translatedSubnet":"example_value","vlan":"example_value"}}'

catocli mutation site addSocketSite '{
    "addSocketSiteInput": {
        "connectionType": "SOCKET_X1500",
        "description": "string",
        "name": "string",
        "nativeNetworkRange": "example_value",
        "siteLocation": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "siteType": "BRANCH",
        "translatedSubnet": "example_value",
        "vlan": "example_value"
    }
}'
```

#### Operation Arguments for mutation.site.addSocketSite ####

`accountId` [ID] - (required) N/A    
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A    
