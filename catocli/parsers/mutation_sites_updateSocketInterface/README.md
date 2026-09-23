
## CATO-CLI - mutation.sites.updateSocketInterface:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSocketInterface) for documentation on this operation.

### Usage for mutation.sites.updateSocketInterface:

```bash
catocli mutation sites updateSocketInterface -h

catocli mutation sites updateSocketInterface <json>

catocli mutation sites updateSocketInterface --json-file mutation.sites.updateSocketInterface.json

catocli mutation sites updateSocketInterface '{"siteId":"id","socketInterfaceId":"LAN1","updateSocketInterfaceInput":{"altWan":{"privateGatewayIp":"example_value","privateInterfaceIp":"example_value","privateNetwork":"example_value","privateVlanTag":1,"publicGatewayIp":"example_value","publicInterfaceIp":"example_value","publicNetwork":"example_value","publicVlanTag":1},"bandwidth":{"downstreamBandwidth":1,"downstreamBandwidthMbpsPrecision":1.5,"upstreamBandwidth":1,"upstreamBandwidthMbpsPrecision":1.5},"destType":"CATO","lag":{"minLinks":1},"lan":{"localIp":"example_value","subnet":"example_value","translatedSubnet":"example_value"},"name":"string","offCloud":{"enabled":true,"publicIp":"example_value","publicStaticPort":1},"vrrp":{"vrrpType":"VIA_SWITCH"},"wan":{"precedence":"ACTIVE","role":"wan_1"}}}'

catocli mutation sites updateSocketInterface '{
    "siteId": "id",
    "socketInterfaceId": "LAN1",
    "updateSocketInterfaceInput": {
        "altWan": {
            "privateGatewayIp": "example_value",
            "privateInterfaceIp": "example_value",
            "privateNetwork": "example_value",
            "privateVlanTag": 1,
            "publicGatewayIp": "example_value",
            "publicInterfaceIp": "example_value",
            "publicNetwork": "example_value",
            "publicVlanTag": 1
        },
        "bandwidth": {
            "downstreamBandwidth": 1,
            "downstreamBandwidthMbpsPrecision": 1.5,
            "upstreamBandwidth": 1,
            "upstreamBandwidthMbpsPrecision": 1.5
        },
        "destType": "CATO",
        "lag": {
            "minLinks": 1
        },
        "lan": {
            "localIp": "example_value",
            "subnet": "example_value",
            "translatedSubnet": "example_value"
        },
        "name": "string",
        "offCloud": {
            "enabled": true,
            "publicIp": "example_value",
            "publicStaticPort": 1
        },
        "vrrp": {
            "vrrpType": "VIA_SWITCH"
        },
        "wan": {
            "precedence": "ACTIVE",
            "role": "wan_1"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSocketInterface ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`socketInterfaceId` [SocketInterfaceIDEnum] - (required) N/A Default Value: ['LAN1', 'LAN2', 'WAN1', 'WAN2', 'USB1', 'USB2', 'INT_1', 'INT_2', 'INT_3', 'INT_4', 'INT_5', 'INT_6', 'INT_7', 'INT_8', 'INT_9', 'INT_10', 'INT_11', 'INT_12', 'WLAN', 'LTE']   
`updateSocketInterfaceInput` [UpdateSocketInterfaceInput] - (required) N/A    
