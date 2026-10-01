
## CATO-CLI - mutation.sites.updateBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateBgpPeer) for documentation on this operation.

### Usage for mutation.sites.updateBgpPeer:

```bash
catocli mutation sites updateBgpPeer -h

catocli mutation sites updateBgpPeer <json>

catocli mutation sites updateBgpPeer --json-file mutation.sites.updateBgpPeer.json

catocli mutation sites updateBgpPeer '{"updateBgpPeerInput":{"advertiseAllRoutes":true,"advertiseDefaultRoute":true,"advertiseSummaryRoutes":true,"bfdEnabled":true,"bfdSettings":{"multiplier":1,"receiveInterval":1,"transmitInterval":1},"catoAsn":64512,"defaultAction":"DROP","defaultActionExclusion":[{"bgpRouteExactAndInclusiveFilterRule":{"ge":1,"globalIpRange":[{"by":"ID","input":"string"}],"globalIpRangeException":[{"by":"ID","input":"string"}],"le":1,"networkSubnet":["192.0.2.0/24"],"networkSubnetException":["192.0.2.0/24"]},"bgpRouteExactFilterRule":{"globalIpRange":[{"by":"ID","input":"string"}],"networkSubnet":["192.0.2.0/24"]},"communityFilterRule":{"community":[{"from":64512,"to":64512}],"predicate":"EQUAL"}}],"defaultRouteCommunities":[{"from":64512,"to":64512}],"holdTime":1,"id":"id","keepaliveInterval":1,"md5AuthKey":"string","metric":1,"name":"string","peerAsn":65536,"peerIp":"192.0.2.1","performNat":true,"summaryRoute":[{"community":[{"from":64512,"to":64512}],"route":"192.0.2.0/24"}],"tracking":{"alertFrequency":"HOURLY","enabled":true,"subscriptionId":"id"}}}'

catocli mutation sites updateBgpPeer '{
    "updateBgpPeerInput": {
        "advertiseAllRoutes": true,
        "advertiseDefaultRoute": true,
        "advertiseSummaryRoutes": true,
        "bfdEnabled": true,
        "bfdSettings": {
            "multiplier": 1,
            "receiveInterval": 1,
            "transmitInterval": 1
        },
        "catoAsn": 64512,
        "defaultAction": "DROP",
        "defaultActionExclusion": [
            {
                "bgpRouteExactAndInclusiveFilterRule": {
                    "ge": 1,
                    "globalIpRange": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "globalIpRangeException": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "le": 1,
                    "networkSubnet": [
                        "192.0.2.0/24"
                    ],
                    "networkSubnetException": [
                        "192.0.2.0/24"
                    ]
                },
                "bgpRouteExactFilterRule": {
                    "globalIpRange": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "networkSubnet": [
                        "192.0.2.0/24"
                    ]
                },
                "communityFilterRule": {
                    "community": [
                        {
                            "from": 64512,
                            "to": 64512
                        }
                    ],
                    "predicate": "EQUAL"
                }
            }
        ],
        "defaultRouteCommunities": [
            {
                "from": 64512,
                "to": 64512
            }
        ],
        "holdTime": 1,
        "id": "id",
        "keepaliveInterval": 1,
        "md5AuthKey": "string",
        "metric": 1,
        "name": "string",
        "peerAsn": 65536,
        "peerIp": "192.0.2.1",
        "performNat": true,
        "summaryRoute": [
            {
                "community": [
                    {
                        "from": 64512,
                        "to": 64512
                    }
                ],
                "route": "192.0.2.0/24"
            }
        ],
        "tracking": {
            "alertFrequency": "HOURLY",
            "enabled": true,
            "subscriptionId": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateBgpPeer ####

`accountId` [ID] - (required) N/A
`updateBgpPeerInput` [UpdateBgpPeerInput] - (required) N/A
