
## CATO-CLI - mutation.sites.updateSiteNetworkRanges:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteNetworkRanges) for documentation on this operation.

### Usage for mutation.sites.updateSiteNetworkRanges:

```bash
catocli mutation sites updateSiteNetworkRanges -h

catocli mutation sites updateSiteNetworkRanges <json>

catocli mutation sites updateSiteNetworkRanges --json-file mutation.sites.updateSiteNetworkRanges.json

catocli mutation sites updateSiteNetworkRanges '{"updateSiteNetworkRangesInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"networkRangeToAdd":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"networkRangeToRemove":[{"networkRangeId":"id"}],"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateSiteNetworkRanges '{
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

#### Operation Arguments for mutation.sites.updateSiteNetworkRanges ####

`accountId` [ID] - (required) N/A
`updateSiteNetworkRangesInput` [UpdateSiteNetworkRangesInput] - (required) N/A
