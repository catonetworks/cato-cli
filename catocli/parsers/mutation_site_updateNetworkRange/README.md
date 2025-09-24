
## CATO-CLI - mutation.site.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateNetworkRange) for documentation on this operation.

### Usage for mutation.site.updateNetworkRange:

`catocli mutation site updateNetworkRange -h`

`catocli mutation site updateNetworkRange <json>`

`catocli mutation site updateNetworkRange "$(cat < mutation.site.updateNetworkRange.json)"`

`catocli mutation site updateNetworkRange '{"networkRangeId":"id","updateNetworkRangeInput":{"azureFloatingIp":"example_value","gateway":"example_value","internetOnly":true,"localIp":"example_value","mdnsReflector":true,"name":"string","networkDhcpSettingsInput":{"dhcpMicrosegmentation":true,"dhcpType":"DHCP_RELAY","ipRange":"example_value","relayGroupId":"id"},"rangeType":"Routed","subnet":"example_value","translatedSubnet":"example_value","vlan":1}}'`

`catocli mutation site updateNetworkRange -p '{
    "networkRangeId": "id",
    "updateNetworkRangeInput": {
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
    }
}'`


#### Operation Arguments for mutation.site.updateNetworkRange ####

`accountId` [ID] - (required) N/A    
`networkRangeId` [ID] - (required) N/A    
`updateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A    
