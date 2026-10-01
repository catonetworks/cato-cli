
## CATO-CLI - mutation.site.updateSocketInterfaces:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSocketInterfaces) for documentation on this operation.

### Usage for mutation.site.updateSocketInterfaces:

```bash
catocli mutation site updateSocketInterfaces -h

catocli mutation site updateSocketInterfaces <json>

catocli mutation site updateSocketInterfaces --json-file mutation.site.updateSocketInterfaces.json

catocli mutation site updateSocketInterfaces '{"updateSocketInterfacesInput":{"site":{"by":"ID","input":"string"},"socketInterface":[{"altWan":{"privateGatewayIp":"192.0.2.1","privateInterfaceIp":"192.0.2.1","privateNetwork":"192.0.2.0/24","privateVlanTag":1,"publicGatewayIp":"192.0.2.1","publicInterfaceIp":"192.0.2.1","publicNetwork":"192.0.2.0/24","publicVlanTag":1},"bandwidth":{"downstreamBandwidth":1,"downstreamBandwidthMbpsPrecision":1.5,"upstreamBandwidth":1,"upstreamBandwidthMbpsPrecision":1.5},"destType":"CATO","lag":{"minLinks":1},"lan":{"localIp":"192.0.2.1","subnet":"192.0.2.0/24","translatedSubnet":"192.0.2.0/24"},"name":"string","offCloud":{"enabled":true,"publicIp":"192.0.2.1","publicStaticPort":1},"socketInterfaceId":"LAN1","vrrp":{"vrrpType":"VIA_SWITCH"},"wan":{"precedence":"ACTIVE","role":"wan_1"}}]}}'

catocli mutation site updateSocketInterfaces '{
    "updateSocketInterfacesInput": {
        "site": {
            "by": "ID",
            "input": "string"
        },
        "socketInterface": [
            {
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
                "socketInterfaceId": "LAN1",
                "vrrp": {
                    "vrrpType": "VIA_SWITCH"
                },
                "wan": {
                    "precedence": "ACTIVE",
                    "role": "wan_1"
                }
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.site.updateSocketInterfaces ####

`accountId` [ID] - (required) N/A
`updateSocketInterfacesInput` [UpdateSocketInterfacesInput] - (required) N/A
