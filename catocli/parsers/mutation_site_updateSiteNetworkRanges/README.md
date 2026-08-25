
## CATO-CLI - mutation.site.updateSiteNetworkRanges:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteNetworkRanges) for documentation on this operation.

### Usage for mutation.site.updateSiteNetworkRanges:

```bash
catocli mutation site updateSiteNetworkRanges -h

catocli mutation site updateSiteNetworkRanges <json>

catocli mutation site updateSiteNetworkRanges --json-file mutation.site.updateSiteNetworkRanges.json

catocli mutation site updateSiteNetworkRanges '{"updateSiteNetworkRangesInput":{"networkRangeRefInput":{"networkRangeId":"id"},"siteRefInput":{"by":"ID","input":"string"},"updateSiteNetworkRangeInput":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"example_value","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1}}}'

catocli mutation site updateSiteNetworkRanges '{
    "updateSiteNetworkRangesInput": {
        "networkRangeRefInput": {
            "networkRangeId": "id"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "updateSiteNetworkRangeInput": {
            "azureFloatingIp": "example_value",
            "dhcpSettings": {
                "dhcpMicrosegmentation": true,
                "dhcpType": "DHCP_RELAY",
                "ipRange": "example_value",
                "relayGroupId": "id"
            },
            "gateway": "example_value",
            "internetOnly": true,
            "lanSocketInterfaceId": "id",
            "localIp": "example_value",
            "mdnsReflector": true,
            "name": "string",
            "rangeType": "Routed",
            "subnet": "example_value",
            "translatedSubnet": "example_value",
            "vlan": 1
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateSiteNetworkRanges ####

`accountId` [ID] - (required) N/A    
`updateSiteNetworkRangesInput` [UpdateSiteNetworkRangesInput] - (required) N/A    
