
## CATO-CLI - mutation.site.updateSocketInterface:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSocketInterface) for documentation on this operation.

### Usage for mutation.site.updateSocketInterface:

```bash
catocli mutation site updateSocketInterface -h

catocli mutation site updateSocketInterface <json>

catocli mutation site updateSocketInterface --json-file mutation.site.updateSocketInterface.json

catocli mutation site updateSocketInterface '{"siteId":"id","socketInterfaceId":"LAN1","updateSocketInterfaceInput":{"altWan":{"privateGatewayIp":"192.0.2.1","privateInterfaceIp":"192.0.2.1","privateNetwork":"192.0.2.0/24","privateVlanTag":1,"publicGatewayIp":"192.0.2.1","publicInterfaceIp":"192.0.2.1","publicNetwork":"192.0.2.0/24","publicVlanTag":1},"bandwidth":{"downstreamBandwidth":1,"downstreamBandwidthMbpsPrecision":1.5,"upstreamBandwidth":1,"upstreamBandwidthMbpsPrecision":1.5},"destType":"CATO","lag":{"minLinks":1},"lan":{"localIp":"192.0.2.1","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24"},"name":"string","offCloud":{"enabled":true,"publicIp":"192.0.2.1","publicStaticPort":1},"vrrp":{"vrrpType":"VIA_SWITCH"},"wan":{"precedence":"ACTIVE","role":"wan_1"}}}'

catocli mutation site updateSocketInterface '{
    "siteId": "id",
    "socketInterfaceId": "LAN1",
    "updateSocketInterfaceInput": {
        "altWan": {
            "privateGatewayIp": "192.0.2.1",
            "privateInterfaceIp": "192.0.2.1",
            "privateNetwork": "192.0.2.0/24",
            "privateVlanTag": 1,
            "publicGatewayIp": "192.0.2.1",
            "publicInterfaceIp": "192.0.2.1",
            "publicNetwork": "192.0.2.0/24",
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
            "localIp": "192.0.2.1",
            "subnet": "192.0.2.0/24",
            "translatedSubnet": "192.0.2.0/24"
        },
        "name": "string",
        "offCloud": {
            "enabled": true,
            "publicIp": "192.0.2.1",
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

#### Operation Arguments for mutation.site.updateSocketInterface ####

`accountId` [ID] - (required) N/A
`siteId` [ID] - (required) N/A
`socketInterfaceId` [SocketInterfaceIDEnum] - (required) N/A Default Value: ['LAN1', 'LAN2', 'WAN1', 'WAN2', 'USB1', 'USB2', 'INT_1', 'INT_2', 'INT_3', 'INT_4', 'INT_5', 'INT_6', 'INT_7', 'INT_8', 'INT_9', 'INT_10', 'INT_11', 'INT_12', 'WLAN', 'LTE', 'WBR1', 'WBR2', 'WBR3', 'WBR4']
`updateSocketInterfaceInput` [UpdateSocketInterfaceInput] - (required) N/A
