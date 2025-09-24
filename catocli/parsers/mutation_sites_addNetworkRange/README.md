
## CATO-CLI - mutation.sites.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addNetworkRange) for documentation on this operation.

### Usage for mutation.sites.addNetworkRange:

`catocli mutation sites addNetworkRange -h`

`catocli mutation sites addNetworkRange <json>`

`catocli mutation sites addNetworkRange "$(cat < mutation.sites.addNetworkRange.json)"`

`catocli mutation sites addNetworkRange '{"addNetworkRangeInput":{"azureFloatingIp":"example_value","gateway":"example_value","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","networkDhcpSettingsInput":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1},"lanSocketInterfaceId":"id"}'`

`catocli mutation sites addNetworkRange -p '{
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


#### Operation Arguments for mutation.sites.addNetworkRange ####

`accountId` [ID] - (required) N/A    
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A    
`lanSocketInterfaceId` [ID] - (required) N/A    
