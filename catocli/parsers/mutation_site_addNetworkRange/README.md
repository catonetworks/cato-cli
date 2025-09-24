
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

`catocli mutation site addNetworkRange -h`

`catocli mutation site addNetworkRange <json>`

`catocli mutation site addNetworkRange "$(cat < mutation.site.addNetworkRange.json)"`

`catocli mutation site addNetworkRange '{"addNetworkRangeInput":{"azureFloatingIp":"example_value","gateway":"example_value","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","networkDhcpSettingsInput":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"lanSocketInterfaceId":"id"}'`

`catocli mutation site addNetworkRange -p '{
    "addNetworkRangeInput": {
        "azureFloatingIp": "example_value",
        "gateway": "example_value",
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
        "rangeType": "Routed",
        "subnet": "example_value",
        "translatedSubnet": "example_value",
        "vlan": 1
    },
    "lanSocketInterfaceId": "id"
}'`


#### Operation Arguments for mutation.site.addNetworkRange ####

`accountId` [ID] - (required) N/A    
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A    
`lanSocketInterfaceId` [ID] - (required) N/A    
