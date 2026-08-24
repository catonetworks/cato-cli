
## CATO-CLI - mutation.sites.updateSocketInterfaces:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSocketInterfaces) for documentation on this operation.

### Usage for mutation.sites.updateSocketInterfaces:

```bash
catocli mutation sites updateSocketInterfaces -h

catocli mutation sites updateSocketInterfaces <json>

catocli mutation sites updateSocketInterfaces --json-file mutation.sites.updateSocketInterfaces.json

catocli mutation sites updateSocketInterfaces '{"updateSocketInterfacesInput":{"siteRefInput":{"by":"ID","input":"string"},"socketInterfaceConfigurationInput":{"altWan":{"privateGatewayIp":"example_value","privateInterfaceIp":"example_value","privateNetwork":"example_value","privateVlanTag":1,"publicGatewayIp":"example_value","publicInterfaceIp":"example_value","publicNetwork":"example_value","publicVlanTag":1},"bandwidth":{"downstreamBandwidth":1,"downstreamBandwidthMbpsPrecision":1.5,"upstreamBandwidth":1,"upstreamBandwidthMbpsPrecision":1.5},"destType":"CATO","lag":{"minLinks":1},"lan":{"localIp":"example_value","subnet":"example_value","translatedSubnet":"example_value"},"name":"string","offCloud":{"enabled":true,"publicIp":"example_value","publicStaticPort":1},"socketInterfaceId":"LAN1","vrrp":{"vrrpType":"VIA_SWITCH"},"wan":{"precedence":"ACTIVE","role":"wan_1"}}}}'

catocli mutation sites updateSocketInterfaces '{
    "updateSocketInterfacesInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "socketInterfaceConfigurationInput": {
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
            "socketInterfaceId": "LAN1",
            "vrrp": {
                "vrrpType": "VIA_SWITCH"
            },
            "wan": {
                "precedence": "ACTIVE",
                "role": "wan_1"
            }
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSocketInterfaces ####

`accountId` [ID] - (required) N/A    
`updateSocketInterfacesInput` [UpdateSocketInterfacesInput] - (required) N/A    
