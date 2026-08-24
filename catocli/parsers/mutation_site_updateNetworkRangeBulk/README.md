
## CATO-CLI - mutation.site.updateNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.site.updateNetworkRangeBulk:

```bash
catocli mutation site updateNetworkRangeBulk -h

catocli mutation site updateNetworkRangeBulk <json>

catocli mutation site updateNetworkRangeBulk --json-file mutation.site.updateNetworkRangeBulk.json

catocli mutation site updateNetworkRangeBulk '{"updateNetworkRangeBulkInput":{"siteRefInput":{"by":"ID","input":"string"},"updateSiteNetworkRangeV2Input":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","gcpLoadBalancerIp":"example_value","id":"id","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","primaryManagementIp":"example_value","rangeType":"Routed","secondaryManagementIp":"example_value","subnet":"example_value","translatedSubnet":"example_value","vlan":1}}}'

catocli mutation site updateNetworkRangeBulk '{
    "updateNetworkRangeBulkInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "updateSiteNetworkRangeV2Input": {
            "azureFloatingIp": "example_value",
            "dhcpSettings": {
                "dhcpMicrosegmentation": true,
                "dhcpType": "DHCP_RELAY",
                "ipRange": "example_value",
                "relayGroupId": "id"
            },
            "gateway": "example_value",
            "gcpLoadBalancerIp": "example_value",
            "id": "id",
            "internetOnly": true,
            "localIp": "example_value",
            "mdnsReflector": true,
            "name": "string",
            "primaryManagementIp": "example_value",
            "rangeType": "Routed",
            "secondaryManagementIp": "example_value",
            "subnet": "example_value",
            "translatedSubnet": "example_value",
            "vlan": 1
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateNetworkRangeBulk ####

`accountId` [ID] - (required) N/A    
`updateNetworkRangeBulkInput` [UpdateNetworkRangeBulkInput] - (required) N/A    
