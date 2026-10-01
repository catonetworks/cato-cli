
## CATO-CLI - mutation.site.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateNetworkRange) for documentation on this operation.

### Usage for mutation.site.updateNetworkRange:

```bash
catocli mutation site updateNetworkRange -h

catocli mutation site updateNetworkRange <json>

catocli mutation site updateNetworkRange --json-file mutation.site.updateNetworkRange.json

catocli mutation site updateNetworkRange '{"networkRangeId":"id","updateNetworkRangeInput":{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","gcpLoadBalancerIp":"192.0.2.1","internetOnly":true,"localIp":"192.0.2.1","mdnsReflector":true,"name":"string","primaryManagementIp":"192.0.2.1","rangeType":"Routed","secondaryManagementIp":"192.0.2.1","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}}'

catocli mutation site updateNetworkRange '{
    "networkRangeId": "id",
    "updateNetworkRangeInput": {
        "azureFloatingIp": "192.0.2.1",
        "dhcpSettings": {
            "dhcpMicrosegmentation": true,
            "dhcpType": "DHCP_RELAY",
            "ipRange": "192.0.2.10-192.0.2.20",
            "relayGroupId": "id"
        },
        "gateway": "192.0.2.1",
        "gcpLoadBalancerIp": "192.0.2.1",
        "internetOnly": true,
        "localIp": "192.0.2.1",
        "mdnsReflector": true,
        "name": "string",
        "primaryManagementIp": "192.0.2.1",
        "rangeType": "Routed",
        "secondaryManagementIp": "192.0.2.1",
        "subnet": "192.0.2.0/24",
        "translatedSubnet": "192.0.2.0/24",
        "vlan": 1
    }
}'
```

#### Operation Arguments for mutation.site.updateNetworkRange ####

`accountId` [ID] - (required) N/A
`networkRangeId` [ID] - (required) N/A
`updateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A
