
## CATO-CLI - mutation.site.createBgpPeerBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createBgpPeerBulk) for documentation on this operation.

### Usage for mutation.site.createBgpPeerBulk:

```bash
catocli mutation site createBgpPeerBulk -h

catocli mutation site createBgpPeerBulk <json>

catocli mutation site createBgpPeerBulk --json-file mutation.site.createBgpPeerBulk.json

catocli mutation site createBgpPeerBulk '{"createBgpPeerBulkInput":{"bgpPeerConfigurationInput":{"advertiseAllRoutes":true,"advertiseDefaultRoute":true,"advertiseSummaryRoutes":true,"bfdEnabled":true,"bfdSettings":{"multiplier":1,"receiveInterval":1,"transmitInterval":1},"catoAsn":"example_value","defaultAction":"DROP","defaultActionExclusion":{"bgpRouteExactAndInclusiveFilterRule":{"ge":1,"globalIpRange":{"by":"ID","input":"string"},"globalIpRangeException":{"by":"ID","input":"string"},"le":1,"networkSubnet":["example1","example2"],"networkSubnetException":["example1","example2"]},"bgpRouteExactFilterRule":{"globalIpRange":{"by":"ID","input":"string"},"networkSubnet":["example1","example2"]},"communityFilterRule":{"community":{"from":"example_value","to":"example_value"},"predicate":"EQUAL"}},"defaultRouteCommunities":{"from":"example_value","to":"example_value"},"holdTime":1,"keepaliveInterval":1,"md5AuthKey":"string","metric":1,"name":"string","peerAsn":"example_value","peerIp":"example_value","performNat":true,"summaryRoute":{"community":{"from":"example_value","to":"example_value"},"route":"example_value"},"tracking":{"alertFrequency":"HOURLY","enabled":true,"subscriptionId":"id"}},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation site createBgpPeerBulk '{
    "createBgpPeerBulkInput": {
        "bgpPeerConfigurationInput": {
            "advertiseAllRoutes": true,
            "advertiseDefaultRoute": true,
            "advertiseSummaryRoutes": true,
            "bfdEnabled": true,
            "bfdSettings": {
                "multiplier": 1,
                "receiveInterval": 1,
                "transmitInterval": 1
            },
            "catoAsn": "example_value",
            "defaultAction": "DROP",
            "defaultActionExclusion": {
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
            "defaultRouteCommunities": {
                "from": "example_value",
                "to": "example_value"
            },
            "holdTime": 1,
            "keepaliveInterval": 1,
            "md5AuthKey": "string",
            "metric": 1,
            "name": "string",
            "peerAsn": "example_value",
            "peerIp": "example_value",
            "performNat": true,
            "summaryRoute": {
                "community": {
                    "from": "example_value",
                    "to": "example_value"
                },
                "route": "example_value"
            },
            "tracking": {
                "alertFrequency": "HOURLY",
                "enabled": true,
                "subscriptionId": "id"
            }
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.createBgpPeerBulk ####

`accountId` [ID] - (required) N/A    
`createBgpPeerBulkInput` [CreateBgpPeerBulkInput] - (required) N/A    
