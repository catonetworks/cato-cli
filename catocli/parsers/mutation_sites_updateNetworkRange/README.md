
## CATO-CLI - mutation.sites.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateNetworkRange) for documentation on this operation.

### Usage for mutation.sites.updateNetworkRange:

`catocli mutation sites updateNetworkRange -h`

`catocli mutation sites updateNetworkRange <accountID> <json>`

`catocli mutation sites updateNetworkRange 12345 "$(cat < updateNetworkRange.json)"`

`catocli mutation sites updateNetworkRange 12345 '{"UpdateNetworkRangeInput": {"NetworkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "mdnsReflector": {"mdnsReflector": "Boolean"}, "name": {"name": "String"}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}, "networkRangeId": "ID"}'`

#### Operation Arguments for mutation.sites.updateNetworkRange ####
`UpdateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`networkRangeId` [ID] - (required) N/A 
