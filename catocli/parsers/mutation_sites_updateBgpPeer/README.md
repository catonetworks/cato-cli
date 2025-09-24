
## CATO-CLI - mutation.sites.updateBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateBgpPeer) for documentation on this operation.

### Usage for mutation.sites.updateBgpPeer:

`catocli mutation sites updateBgpPeer -h`

`catocli mutation sites updateBgpPeer <json>`

`catocli mutation sites updateBgpPeer "$(cat < mutation.sites.updateBgpPeer.json)"`

`catocli mutation sites updateBgpPeer '{"updateBgpPeerInput":{"advertiseAllRoutes":true,"advertiseDefaultRoute":true,"advertiseSummaryRoutes":true,"bfdEnabled":true,"bfdSettingsInput":{"multiplier":1,"receiveInterval":1,"transmitInterval":1},"bgpFilterRuleInput":{"bgpRouteExactAndInclusiveFilterRule":{"ge":1,"globalIpRange":{"by":"ID","input":"string"},"globalIpRangeException":{"by":"ID","input":"string"},"le":1,"networkSubnet":["example1","example2"],"networkSubnetException":["example1","example2"]},"bgpRouteExactFilterRule":{"globalIpRange":{"by":"ID","input":"string"},"networkSubnet":["example1","example2"]},"communityFilterRule":{"community":{"from":"example_value","to":"example_value"},"predicate":"EQUAL"}},"bgpSummaryRouteInput":{"community":{"from":"example_value","to":"example_value"},"route":"example_value"},"bgpTrackingInput":{"alertFrequency":"HOURLY","enabled":true,"subscriptionId":"id"},"catoAsn":"example_value","defaultAction":"DROP","holdTime":1,"id":"id","keepaliveInterval":1,"md5AuthKey":"string","metric":1,"name":"string","peerAsn":"example_value","peerIp":"example_value","performNat":true}}'`

`catocli mutation sites updateBgpPeer -p '{
    "updateBgpPeerInput": {
        "advertiseAllRoutes": true,
        "advertiseDefaultRoute": true,
        "advertiseSummaryRoutes": true,
        "bfdEnabled": true,
        "bfdSettingsInput": {
            "multiplier": 1,
            "receiveInterval": 1,
            "transmitInterval": 1
        },
        "bgpFilterRuleInput": {
            "bgpRouteExactAndInclusiveFilterRule": {
                "ge": 1,
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                },
                "globalIpRangeException": {
                    "by": "ID",
                    "input": "string"
                },
                "le": 1,
                "networkSubnet": [
                    "example1",
                    "example2"
                ],
                "networkSubnetException": [
                    "example1",
                    "example2"
                ]
            },
            "bgpRouteExactFilterRule": {
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                },
                "networkSubnet": [
                    "example1",
                    "example2"
                ]
            },
            "communityFilterRule": {
                "community": {
                    "from": "example_value",
                    "to": "example_value"
                },
                "predicate": "EQUAL"
            }
        },
        "bgpSummaryRouteInput": {
            "community": {
                "from": "example_value",
                "to": "example_value"
            },
            "route": "example_value"
        },
        "bgpTrackingInput": {
            "alertFrequency": "HOURLY",
            "enabled": true,
            "subscriptionId": "id"
        },
        "catoAsn": "example_value",
        "defaultAction": "DROP",
        "holdTime": 1,
        "id": "id",
        "keepaliveInterval": 1,
        "md5AuthKey": "string",
        "metric": 1,
        "name": "string",
        "peerAsn": "example_value",
        "peerIp": "example_value",
        "performNat": true
    }
}'`


#### Operation Arguments for mutation.sites.updateBgpPeer ####

`accountId` [ID] - (required) N/A    
`updateBgpPeerInput` [UpdateBgpPeerInput] - (required) N/A    
