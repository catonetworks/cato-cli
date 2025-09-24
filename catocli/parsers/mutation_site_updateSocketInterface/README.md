
## CATO-CLI - mutation.site.updateSocketInterface:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSocketInterface) for documentation on this operation.

### Usage for mutation.site.updateSocketInterface:

`catocli mutation site updateSocketInterface -h`

`catocli mutation site updateSocketInterface <json>`

`catocli mutation site updateSocketInterface "$(cat < mutation.site.updateSocketInterface.json)"`

`catocli mutation site updateSocketInterface '{"siteId":"id","socketInterfaceId":"LAN1","updateSocketInterfaceInput":{"destType":"CATO","name":"string","socketInterfaceAltWanInput":{"privateGatewayIp":"example_value","privateInterfaceIp":"example_value","privateNetwork":"example_value","privateVlanTag":1,"publicGatewayIp":"example_value","publicInterfaceIp":"example_value","publicNetwork":"example_value","publicVlanTag":1},"socketInterfaceBandwidthInput":{"downstreamBandwidth":1,"downstreamBandwidthMbpsPrecision":1.5,"upstreamBandwidth":1,"upstreamBandwidthMbpsPrecision":1.5},"socketInterfaceLagInput":{"minLinks":1},"socketInterfaceLanInput":{"localIp":"example_value","subnet":"example_value","translatedSubnet":"example_value"},"socketInterfaceOffCloudInput":{"enabled":true,"publicIp":"example_value","publicStaticPort":1},"socketInterfaceVrrpInput":{"vrrpType":"VIA_SWITCH"},"socketInterfaceWanInput":{"precedence":"ACTIVE","role":"wan_1"}}}'`

`catocli mutation site updateSocketInterface -p '{
    "siteId": "id",
    "socketInterfaceId": "LAN1",
    "updateSocketInterfaceInput": {
        "destType": "CATO",
        "name": "string",
        "socketInterfaceAltWanInput": {
            "privateGatewayIp": "example_value",
            "privateInterfaceIp": "example_value",
            "privateNetwork": "example_value",
            "privateVlanTag": 1,
            "publicGatewayIp": "example_value",
            "publicInterfaceIp": "example_value",
            "publicNetwork": "example_value",
            "publicVlanTag": 1
        },
        "socketInterfaceBandwidthInput": {
            "downstreamBandwidth": 1,
            "downstreamBandwidthMbpsPrecision": 1.5,
            "upstreamBandwidth": 1,
            "upstreamBandwidthMbpsPrecision": 1.5
        },
        "socketInterfaceLagInput": {
            "minLinks": 1
        },
        "socketInterfaceLanInput": {
            "localIp": "example_value",
            "subnet": "example_value",
            "translatedSubnet": "example_value"
        },
        "socketInterfaceOffCloudInput": {
            "enabled": true,
            "publicIp": "example_value",
            "publicStaticPort": 1
        },
        "socketInterfaceVrrpInput": {
            "vrrpType": "VIA_SWITCH"
        },
        "socketInterfaceWanInput": {
            "precedence": "ACTIVE",
            "role": "wan_1"
        }
    }
}'`


#### Operation Arguments for mutation.site.updateSocketInterface ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`socketInterfaceId` [SocketInterfaceIDEnum] - (required) N/A Default Value: ['LAN1', 'LAN2', 'WAN1', 'WAN2', 'USB1', 'USB2', 'INT_1', 'INT_2', 'INT_3', 'INT_4', 'INT_5', 'INT_6', 'INT_7', 'INT_8', 'INT_9', 'INT_10', 'INT_11', 'INT_12', 'WLAN', 'LTE']   
`updateSocketInterfaceInput` [UpdateSocketInterfaceInput] - (required) N/A    
