
## CATO-CLI - mutation.sites.updateSiteNetworkRanges:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteNetworkRanges) for documentation on this operation.

### Usage for mutation.sites.updateSiteNetworkRanges:

```bash
catocli mutation sites updateSiteNetworkRanges -h

catocli mutation sites updateSiteNetworkRanges <json>

catocli mutation sites updateSiteNetworkRanges --json-file mutation.sites.updateSiteNetworkRanges.json

catocli mutation sites updateSiteNetworkRanges '{"updateSiteNetworkRangesInput":{"networkRange":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"example_value","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"networkRangeToAdd":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"example_value","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"networkRangeToRemove":{"networkRangeId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateSiteNetworkRanges '{
    "updateSiteNetworkRangesInput": {
        "networkRange": {
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
        },
        "networkRangeToAdd": {
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
        },
        "networkRangeToRemove": {
            "networkRangeId": "id"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSiteNetworkRanges ####

`accountId` [ID] - (required) N/A    
`updateSiteNetworkRangesInput` [UpdateSiteNetworkRangesInput] - (required) N/A    
