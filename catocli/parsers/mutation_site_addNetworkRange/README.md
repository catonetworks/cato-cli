
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

`catocli mutation site addNetworkRange -h`

`catocli mutation site addNetworkRange <json>`

`catocli mutation site addNetworkRange "$(cat < addNetworkRange.json)"`

`catocli mutation site addNetworkRange '{"addNetworkRangeInput": {"azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "mdnsReflector": {"mdnsReflector": "Boolean"}, "name": {"name": "String"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}, "lanSocketInterfaceId": "ID"}'`

#### Operation Arguments for mutation.site.addNetworkRange ####
`accountId` [ID] - (required) N/A 
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A 
`lanSocketInterfaceId` [ID] - (required) N/A 
