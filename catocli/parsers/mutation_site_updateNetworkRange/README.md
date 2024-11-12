
## CATO-CLI - mutation.site.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateNetworkRange) for documentation on this operation.

### Usage for mutation.site.updateNetworkRange:

`catocli mutation site updateNetworkRange -h`

`catocli mutation site updateNetworkRange <json>`

`catocli mutation site updateNetworkRange "$(cat < updateNetworkRange.json)"`

`catocli mutation site updateNetworkRange '{"networkRangeId": "ID", "updateNetworkRangeInput": {"azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "mdnsReflector": {"mdnsReflector": "Boolean"}, "name": {"name": "String"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}}'`

#### Operation Arguments for mutation.site.updateNetworkRange ####
`accountId` [ID] - (required) N/A 
`networkRangeId` [ID] - (required) N/A 
`updateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A 
