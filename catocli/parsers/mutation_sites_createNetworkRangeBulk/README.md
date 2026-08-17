
## CATO-CLI - mutation.sites.createNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.sites.createNetworkRangeBulk:

```bash
catocli mutation sites createNetworkRangeBulk -h

catocli mutation sites createNetworkRangeBulk <json>

catocli mutation sites createNetworkRangeBulk --json-file mutation.sites.createNetworkRangeBulk.json

catocli mutation sites createNetworkRangeBulk '{"createNetworkRangeBulkInput":{"createNetworkRangeInput":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","internetOnly":true,"lanSocketInterfaceId":"id","localIp":"example_value","mdnsReflector":true,"name":"string","rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation sites createNetworkRangeBulk '{
    "createNetworkRangeBulkInput": {
        "createNetworkRangeInput": {
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
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.createNetworkRangeBulk ####

`accountId` [ID] - (required) N/A    
`createNetworkRangeBulkInput` [CreateNetworkRangeBulkInput] - (required) N/A    
