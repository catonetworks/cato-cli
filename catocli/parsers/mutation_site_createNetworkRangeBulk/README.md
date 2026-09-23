
## CATO-CLI - mutation.site.createNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.site.createNetworkRangeBulk:

```bash
catocli mutation site createNetworkRangeBulk -h

catocli mutation site createNetworkRangeBulk <json>

catocli mutation site createNetworkRangeBulk --json-file mutation.site.createNetworkRangeBulk.json

catocli mutation site createNetworkRangeBulk '{"createNetworkRangeBulkInput":{"networkRange":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"example_value","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"site":{"by":"ID","input":"string"}}}'

catocli mutation site createNetworkRangeBulk '{
    "createNetworkRangeBulkInput": {
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
