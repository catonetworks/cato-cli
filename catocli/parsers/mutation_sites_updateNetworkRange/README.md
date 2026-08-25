
## CATO-CLI - mutation.sites.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateNetworkRange) for documentation on this operation.

### Usage for mutation.sites.updateNetworkRange:

```bash
catocli mutation sites updateNetworkRange -h

catocli mutation sites updateNetworkRange <json>

catocli mutation sites updateNetworkRange --json-file mutation.sites.updateNetworkRange.json

catocli mutation sites updateNetworkRange '{"networkRangeId":"id","updateNetworkRangeInput":{"azureFloatingIp":"example_value","gateway":"example_value","gcpLoadBalancerIp":"example_value","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","networkDhcpSettingsInput":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"primaryManagementIp":"example_value","rangeType":"Routed","secondaryManagementIp":"example_value","subnet":"example_value","translatedSubnet":"example_value","vlan":1}}'

catocli mutation sites updateNetworkRange '{
    "networkRangeId": "id",
    "updateNetworkRangeInput": {
        "azureFloatingIp": "example_value",
        "gateway": "example_value",
        "gcpLoadBalancerIp": "example_value",
        "internetOnly": true,
        "localIp": "example_value",
        "mdnsReflector": true,
        "name": "string",
        "networkDhcpSettingsInput": {
            "dhcpMicrosegmentation": true,
            "dhcpType": "DHCP_RELAY",
            "ipRange": "example_value",
            "relayGroupId": "id"
        },
        "primaryManagementIp": "example_value",
        "rangeType": "Routed",
        "secondaryManagementIp": "example_value",
        "subnet": "example_value",
        "translatedSubnet": "example_value",
        "vlan": 1
    }
}'
```

#### Operation Arguments for mutation.sites.updateNetworkRange ####

`accountId` [ID] - (required) N/A    
`networkRangeId` [ID] - (required) N/A    
`updateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A    
