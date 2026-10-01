
## CATO-CLI - mutation.sites.createNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.sites.createNetworkRangeBulk:

```bash
catocli mutation sites createNetworkRangeBulk -h

catocli mutation sites createNetworkRangeBulk <json>

catocli mutation sites createNetworkRangeBulk --json-file mutation.sites.createNetworkRangeBulk.json

catocli mutation sites createNetworkRangeBulk '{"createNetworkRangeBulkInput":{"networkRange":[{"azureFloatingIp":"192.0.2.1","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"192.0.2.10-192.0.2.20","relayGroupId":"id"},"gateway":"192.0.2.1","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"192.0.2.1","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24","vlan":1}],"site":{"by":"ID","input":"string"}}}'

catocli mutation sites createNetworkRangeBulk '{
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

#### Operation Arguments for mutation.sites.createNetworkRangeBulk ####

`accountId` [ID] - (required) N/A
`createNetworkRangeBulkInput` [CreateNetworkRangeBulkInput] - (required) N/A
