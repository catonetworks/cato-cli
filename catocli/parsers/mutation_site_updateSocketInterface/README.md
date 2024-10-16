
## CATO-CLI - mutation.site.updateSocketInterface:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSocketInterface) for documentation on this operation.

### Usage for mutation.site.updateSocketInterface:

`catocli mutation site updateSocketInterface -h`

`catocli mutation site updateSocketInterface <json>`

`catocli mutation site updateSocketInterface "$(cat < updateSocketInterface.json)"`

`catocli mutation site updateSocketInterface '{"UpdateSocketInterfaceInput": {"SocketInterfaceAltWanInput": {"privateGatewayIp": {"privateGatewayIp": "IPAddress"}, "privateInterfaceIp": {"privateInterfaceIp": "IPAddress"}, "privateNetwork": {"privateNetwork": "IPSubnet"}, "privateVlanTag": {"privateVlanTag": "Int"}, "publicGatewayIp": {"publicGatewayIp": "IPAddress"}, "publicInterfaceIp": {"publicInterfaceIp": "IPAddress"}, "publicNetwork": {"publicNetwork": "IPSubnet"}, "publicVlanTag": {"publicVlanTag": "Int"}}, "SocketInterfaceBandwidthInput": {"downstreamBandwidth": {"downstreamBandwidth": "Int"}, "upstreamBandwidth": {"upstreamBandwidth": "Int"}}, "SocketInterfaceLagInput": {"minLinks": {"minLinks": "Int"}}, "SocketInterfaceLanInput": {"localIp": {"localIp": "IPAddress"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}}, "SocketInterfaceOffCloudInput": {"enabled": {"enabled": "Boolean"}, "publicIp": {"publicIp": "IPAddress"}, "publicStaticPort": {"publicStaticPort": "Int"}}, "SocketInterfaceVrrpInput": {"vrrpType": {"vrrpType": "enum(VrrpType)"}}, "SocketInterfaceWanInput": {"precedence": {"precedence": "enum(SocketInterfacePrecedenceEnum)"}, "role": {"role": "enum(SocketInterfaceRole)"}}, "destType": {"destType": "enum(SocketInterfaceDestType)"}, "name": {"name": "String"}}, "siteId": "ID", "socketInterfaceId": "enum(SocketInterfaceIDEnum)"}'`

#### Operation Arguments for mutation.site.updateSocketInterface ####
`UpdateSocketInterfaceInput` [UpdateSocketInterfaceInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`socketInterfaceId` [SocketInterfaceIDEnum] - (required) N/A Default Value: ['LAN1', 'LAN2', 'WAN1', 'WAN2', 'USB1', 'USB2', 'INT_1', 'INT_2', 'INT_3', 'INT_4', 'INT_5', 'INT_6', 'INT_7', 'INT_8', 'INT_9', 'INT_10', 'INT_11', 'INT_12', 'WLAN', 'LTE']
