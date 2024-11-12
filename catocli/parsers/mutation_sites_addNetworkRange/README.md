
## CATO-CLI - mutation.sites.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-addNetworkRange) for documentation on this operation.

### Usage for mutation.sites.addNetworkRange:

`catocli mutation sites addNetworkRange -h`

`catocli mutation sites addNetworkRange <json>`

`catocli mutation sites addNetworkRange "$(cat < addNetworkRange.json)"`

`catocli mutation sites addNetworkRange '{"addNetworkRangeInput": {"azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "mdnsReflector": {"mdnsReflector": "Boolean"}, "name": {"name": "String"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}, "lanSocketInterfaceId": "ID"}'`

#### Operation Arguments for mutation.sites.addNetworkRange ####
`accountId` [ID] - (required) N/A 
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A 
`lanSocketInterfaceId` [ID] - (required) N/A 
