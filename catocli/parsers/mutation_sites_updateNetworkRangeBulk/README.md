
## CATO-CLI - mutation.sites.updateNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.sites.updateNetworkRangeBulk:

```bash
catocli mutation sites updateNetworkRangeBulk -h

catocli mutation sites updateNetworkRangeBulk <json>

catocli mutation sites updateNetworkRangeBulk --json-file mutation.sites.updateNetworkRangeBulk.json

catocli mutation sites updateNetworkRangeBulk '{"updateNetworkRangeBulkInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","gcpLoadBalancerIp":"192.0.2.1","id":"id","internetOnly":true,"localIp":"192.0.2.1","mdnsReflector":true,"name":"string","primaryManagementIp":"192.0.2.1","rangeType":"Routed","secondaryManagementIp":"192.0.2.1","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateNetworkRangeBulk '{
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

#### Operation Arguments for mutation.sites.updateNetworkRangeBulk ####

`accountId` [ID] - (required) N/A
`updateNetworkRangeBulkInput` [UpdateNetworkRangeBulkInput] - (required) N/A
