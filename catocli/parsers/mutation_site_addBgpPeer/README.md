
## CATO-CLI - mutation.site.addBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addBgpPeer) for documentation on this operation.

### Usage for mutation.site.addBgpPeer:

`catocli mutation site addBgpPeer -h`

`catocli mutation site addBgpPeer <json>`

`catocli mutation site addBgpPeer "$(cat < mutation.site.addBgpPeer.json)"`

`catocli mutation site addBgpPeer '{"addBgpPeerInput":{"advertiseAllRoutes":true,"advertiseDefaultRoute":true,"advertiseSummaryRoutes":true,"bfdEnabled":true,"bfdSettingsInput":{"multiplier":1,"receiveInterval":1,"transmitInterval":1},"bgpFilterRuleInput":{"bgpRouteExactAndInclusiveFilterRule":{"ge":1,"globalIpRange":{"by":"ID","input":"string"},"globalIpRangeException":{"by":"ID","input":"string"},"le":1,"networkSubnet":["example1","example2"],"networkSubnetException":["example1","example2"]},"bgpRouteExactFilterRule":{"globalIpRange":{"by":"ID","input":"string"},"networkSubnet":["example1","example2"]},"communityFilterRule":{"community":{"from":"example_value","to":"example_value"},"predicate":"EQUAL"}},"bgpSummaryRouteInput":{"community":{"from":"example_value","to":"example_value"},"route":"example_value"},"bgpTrackingInput":{"alertFrequency":"HOURLY","enabled":true,"subscriptionId":"id"},"catoAsn":"example_value","defaultAction":"DROP","holdTime":1,"keepaliveInterval":1,"md5AuthKey":"string","metric":1,"name":"string","peerAsn":"example_value","peerIp":"example_value","performNat":true,"siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site addBgpPeer -p '{
    "addBgpPeerInput": {
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
        "keepaliveInterval": 1,
        "md5AuthKey": "string",
        "metric": 1,
        "name": "string",
        "peerAsn": "example_value",
        "peerIp": "example_value",
        "performNat": true,
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.addBgpPeer ####

`accountId` [ID] - (required) N/A    
`addBgpPeerInput` [AddBgpPeerInput] - (required) N/A    
