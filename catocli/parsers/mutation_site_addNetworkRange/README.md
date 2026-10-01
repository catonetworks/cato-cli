
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

```bash
catocli mutation site addNetworkRange -h

catocli mutation site addNetworkRange <json>

catocli mutation site addNetworkRange --json-file mutation.site.addNetworkRange.json

catocli mutation site addNetworkRange '{"addNetworkRangeInput":{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1},"lanSocketInterfaceId":"id"}'

catocli mutation site addNetworkRange '{
    "addNetworkRangeInput": {
        "azureFloatingIp": "192.0.2.1",
        "dhcpSettings": {
            "dhcpMicrosegmentation": true,
            "dhcpType": "DHCP_RELAY",
            "ipRange": "192.0.2.10-192.0.2.20",
            "relayGroupId": "id"
        },
        "gateway": "192.0.2.1",
        "internetOnly": true,
        "localIp": "192.0.2.1",
        "mdnsReflector": true,
        "name": "string",
        "rangeType": "Routed",
        "subnet": "192.0.2.0/24",
        "translatedSubnet": "192.0.2.0/24",
        "vlan": 1
    },
    "lanSocketInterfaceId": "id"
}'
```

#### Operation Arguments for mutation.site.addNetworkRange ####

`accountId` [ID] - (required) N/A
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A
`lanSocketInterfaceId` [ID] - (required) N/A
