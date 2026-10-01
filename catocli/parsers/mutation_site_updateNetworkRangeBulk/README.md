
## CATO-CLI - mutation.site.updateNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.site.updateNetworkRangeBulk:

```bash
catocli mutation site updateNetworkRangeBulk -h

catocli mutation site updateNetworkRangeBulk <json>

catocli mutation site updateNetworkRangeBulk --json-file mutation.site.updateNetworkRangeBulk.json

catocli mutation site updateNetworkRangeBulk '{"updateNetworkRangeBulkInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","gcpLoadBalancerIp":"192.0.2.1","id":"id","internetOnly":true,"localIp":"192.0.2.1","mdnsReflector":true,"name":"string","primaryManagementIp":"192.0.2.1","rangeType":"Routed","secondaryManagementIp":"192.0.2.1","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateNetworkRangeBulk '{
    "updateNetworkRangeBulkInput": {
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
                "gcpLoadBalancerIp": "192.0.2.1",
                "id": "id",
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
        ],
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateNetworkRangeBulk ####

`accountId` [ID] - (required) N/A
`updateNetworkRangeBulkInput` [UpdateNetworkRangeBulkInput] - (required) N/A
