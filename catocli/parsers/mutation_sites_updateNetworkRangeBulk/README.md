
## CATO-CLI - mutation.sites.updateNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.sites.updateNetworkRangeBulk:

```bash
catocli mutation sites updateNetworkRangeBulk -h

catocli mutation sites updateNetworkRangeBulk <json>

catocli mutation sites updateNetworkRangeBulk --json-file mutation.sites.updateNetworkRangeBulk.json

catocli mutation sites updateNetworkRangeBulk '{"updateNetworkRangeBulkInput":{"siteRefInput":{"by":"ID","input":"string"},"updateSiteNetworkRangeV2Input":{"azureFloatingIp":"example_value","dhcpSettings":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"gateway":"example_value","gcpLoadBalancerIp":"example_value","id":"id","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","primaryManagementIp":"example_value","rangeType":"Routed","secondaryManagementIp":"example_value","subnet":"example_value","translatedSubnet":"example_value","vlan":1}}}'

catocli mutation sites updateNetworkRangeBulk '{
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

#### Operation Arguments for mutation.sites.updateNetworkRangeBulk ####

`accountId` [ID] - (required) N/A    
`updateNetworkRangeBulkInput` [UpdateNetworkRangeBulkInput] - (required) N/A    
