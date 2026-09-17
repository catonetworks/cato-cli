
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

