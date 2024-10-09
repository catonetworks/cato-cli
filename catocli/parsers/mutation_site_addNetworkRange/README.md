
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

`catocli mutation site addNetworkRange -h`

`catocli mutation site addNetworkRange <accountID> <json>`

`catocli mutation site addNetworkRange 12345 "$(cat < addNetworkRange.json)"`

`catocli mutation site addNetworkRange 12345 '{"AddNetworkRangeInput": {"NetworkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "mdnsReflector": {"mdnsReflector": "Boolean"}, "name": {"name": "String"}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}, "lanSocketInterfaceId": "ID"}'`

#### Operation Arguments for mutation.site.addNetworkRange ####
`AddNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`lanSocketInterfaceId` [ID] - (required) N/A 