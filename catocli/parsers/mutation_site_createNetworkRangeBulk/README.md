
## CATO-CLI - mutation.site.createNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.site.createNetworkRangeBulk:

```bash
catocli mutation site createNetworkRangeBulk -h

catocli mutation site createNetworkRangeBulk <json>

catocli mutation site createNetworkRangeBulk --json-file mutation.site.createNetworkRangeBulk.json

catocli mutation site createNetworkRangeBulk '{"createNetworkRangeBulkInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"site":{"by":"ID","input":"string"}}}'

catocli mutation site createNetworkRangeBulk '{
    "createNetworkRangeBulkInput": {
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
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.createNetworkRangeBulk ####

`accountId` [ID] - (required) N/A
`createNetworkRangeBulkInput` [CreateNetworkRangeBulkInput] - (required) N/A
