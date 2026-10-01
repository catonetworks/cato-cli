
## CATO-CLI - mutation.site.updateBgpPeerBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateBgpPeerBulk) for documentation on this operation.

### Usage for mutation.site.updateBgpPeerBulk:

```bash
catocli mutation site updateBgpPeerBulk -h

catocli mutation site updateBgpPeerBulk <json>

catocli mutation site updateBgpPeerBulk --json-file mutation.site.updateBgpPeerBulk.json

catocli mutation site updateBgpPeerBulk '{"updateBgpPeerBulkInput":{"bgpPeer":[{"advertiseAllRoutes":true,"advertiseDefaultRoute":true,"advertiseSummaryRoutes":true,"bfdEnabled":true,"bfdSettings":{"multiplier":1,"receiveInterval":1,"transmitInterval":1},"catoAsn":64512,"defaultAction":"DROP","defaultActionExclusion":[{"bgpRouteExactAndInclusiveFilterRule":{"ge":1,"globalIpRange":[{"by":"ID","input":"string"}],"globalIpRangeException":[{"by":"ID","input":"string"}],"le":1,"networkSubnet":["192.0.2.0/24"],"networkSubnetException":["192.0.2.0/24"]},"bgpRouteExactFilterRule":{"globalIpRange":[{"by":"ID","input":"string"}],"networkSubnet":["192.0.2.0/24"]},"communityFilterRule":{"community":[{"from":64512,"to":64512}],"predicate":"EQUAL"}}],"defaultRouteCommunities":[{"from":64512,"to":64512}],"holdTime":1,"id":"id","keepaliveInterval":1,"md5AuthKey":"string","metric":1,"name":"string","peerAsn":65536,"peerIp":"192.0.2.1","performNat":true,"summaryRoute":[{"community":[{"from":64512,"to":64512}],"route":"192.0.2.0/24"}],"tracking":{"alertFrequency":"HOURLY","enabled":true,"subscriptionId":"id"}}],"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateBgpPeerBulk '{
    "updateBgpPeerBulkInput": {
        "bgpPeer": [
            {
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
        ],
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateBgpPeerBulk ####

`accountId` [ID] - (required) N/A
`updateBgpPeerBulkInput` [UpdateBgpPeerBulkInput] - (required) N/A
