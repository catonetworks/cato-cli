
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

```bash
catocli mutation site addSocketSite -h

catocli mutation site addSocketSite <json>

catocli mutation site addSocketSite --json-file mutation.site.addSocketSite.json

catocli mutation site addSocketSite '{"addSocketSiteInput":{"connectionType":"SOCKET_X1500","description":"string","name":"string","nativeNetworkRange":"192.0.2.0/24","secondaryVSocket":{"aws":{"eniIpAddress":"192.0.2.1","eniIpSubnet":"192.0.2.0/24","routeTableId":"string"},"azure":{"floatingIp":"192.0.2.1","interfaceIp":"192.0.2.1"},"gcp":{"interfaceIp":"192.0.2.1","loadBalancerIp":"192.0.2.1"}},"siteLocation":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH","translatedSubnet":"192.0.2.0/24","vlan":100}}'

catocli mutation site addSocketSite '{
    "addSocketSiteInput": {
        "connectionType": "SOCKET_X1500",
        "description": "string",
        "name": "string",
        "nativeNetworkRange": "192.0.2.0/24",
        "secondaryVSocket": {
            "aws": {
                "eniIpAddress": "192.0.2.1",
                "eniIpSubnet": "192.0.2.0/24",
                "routeTableId": "string"
            },
            "azure": {
                "floatingIp": "192.0.2.1",
                "interfaceIp": "192.0.2.1"
            },
            "gcp": {
                "interfaceIp": "192.0.2.1",
                "loadBalancerIp": "192.0.2.1"
            }
        },
        "siteLocation": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "siteType": "BRANCH",
        "translatedSubnet": "192.0.2.0/24",
        "vlan": 100
    }
}'
```

#### Operation Arguments for mutation.site.addSocketSite ####

`accountId` [ID] - (required) N/A
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A
