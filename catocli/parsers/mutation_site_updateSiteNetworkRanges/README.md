
## CATO-CLI - mutation.site.updateSiteNetworkRanges:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteNetworkRanges) for documentation on this operation.

### Usage for mutation.site.updateSiteNetworkRanges:

```bash
catocli mutation site updateSiteNetworkRanges -h

catocli mutation site updateSiteNetworkRanges <json>

catocli mutation site updateSiteNetworkRanges --json-file mutation.site.updateSiteNetworkRanges.json

catocli mutation site updateSiteNetworkRanges '{"updateSiteNetworkRangesInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"networkRangeToAdd":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"networkRangeToRemove":[{"networkRangeId":"id"}],"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateSiteNetworkRanges '{
    "updateSiteNetworkRangesInput": {
        "networkRange": [
            {
                "azureFloatingIp": "192.0.2.1",
                "dhcpSettings": {
                    "dhcpMicrosegmentation": true,
                    "dhcpType": "DHCP_RELAY",
                    "ipRange": "192.0.2.10-192.0.2.20",
                    "relayGroupId": "id"
                },
                "gateway": "192.0.2.1",
                "internetOnly": true,
                "lanSocketInterfaceId": "id",
                "localIp": "192.0.2.1",
                "mdnsReflector": true,
                "name": "string",
                "rangeType": "Routed",
                "subnet": "192.0.2.0/24",
                "translatedSubnet": "192.0.2.0/24",
                "vlan": 1
            }
        ],
        "networkRangeToAdd": [
            {
                "azureFloatingIp": "192.0.2.1",
                "dhcpSettings": {
                    "dhcpMicrosegmentation": true,
                    "dhcpType": "DHCP_RELAY",
                    "ipRange": "192.0.2.10-192.0.2.20",
                    "relayGroupId": "id"
                },
                "gateway": "192.0.2.1",
                "internetOnly": true,
                "lanSocketInterfaceId": "id",
                "localIp": "192.0.2.1",
                "mdnsReflector": true,
                "name": "string",
                "rangeType": "Routed",
                "subnet": "192.0.2.0/24",
                "translatedSubnet": "192.0.2.0/24",
                "vlan": 1
            }
        ],
        "networkRangeToRemove": [
            {
                "networkRangeId": "id"
            }
        ],
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateSiteNetworkRanges ####

`accountId` [ID] - (required) N/A
`updateSiteNetworkRangesInput` [UpdateSiteNetworkRangesInput] - (required) N/A
