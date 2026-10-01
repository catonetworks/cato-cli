
## CATO-CLI - mutation.site.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2SiteTunnels:

```bash
catocli mutation site addIpsecIkeV2SiteTunnels -h

catocli mutation site addIpsecIkeV2SiteTunnels <json>

catocli mutation site addIpsecIkeV2SiteTunnels --json-file mutation.site.addIpsecIkeV2SiteTunnels.json

catocli mutation site addIpsecIkeV2SiteTunnels '{"addIpsecIkeV2SiteTunnelsInput":{"primary":{"destinationType":"IPv4","popLocationId":"id","publicCatoIpId":"id","tunnels":[{"lastMileBw":{"downstream":1,"downstreamMbpsPrecision":1.5,"upstream":1,"upstreamMbpsPrecision":1.5},"name":"string","privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","psk":"string","publicSiteIp":"192.0.2.1","role":"WAN1"}]},"secondary":{"destinationType":"IPv4","popLocationId":"id","publicCatoIpId":"id","tunnels":[{"lastMileBw":{"downstream":1,"downstreamMbpsPrecision":1.5,"upstream":1,"upstreamMbpsPrecision":1.5},"name":"string","privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","psk":"string","publicSiteIp":"192.0.2.1","role":"WAN1"}]}},"siteId":"id"}'

catocli mutation site addIpsecIkeV2SiteTunnels '{
    "addIpsecIkeV2SiteTunnelsInput": {
        "primary": {
            "destinationType": "IPv4",
            "popLocationId": "id",
            "publicCatoIpId": "id",
            "tunnels": [
                {
                    "lastMileBw": {
                        "downstream": 1,
                        "downstreamMbpsPrecision": 1.5,
                        "upstream": 1,
                        "upstreamMbpsPrecision": 1.5
                    },
                    "name": "string",
                    "privateCatoIp": "192.0.2.1",
                    "privateSiteIp": "192.0.2.1",
                    "psk": "string",
                    "publicSiteIp": "192.0.2.1",
                    "role": "WAN1"
                }
            ]
        },
        "secondary": {
            "destinationType": "IPv4",
            "popLocationId": "id",
            "publicCatoIpId": "id",
            "tunnels": [
                {
                    "lastMileBw": {
                        "downstream": 1,
                        "downstreamMbpsPrecision": 1.5,
                        "upstream": 1,
                        "upstreamMbpsPrecision": 1.5
                    },
                    "name": "string",
                    "privateCatoIp": "192.0.2.1",
                    "privateSiteIp": "192.0.2.1",
                    "psk": "string",
                    "publicSiteIp": "192.0.2.1",
                    "role": "WAN1"
                }
            ]
        }
    },
    "siteId": "id"
}'
```

#### Operation Arguments for mutation.site.addIpsecIkeV2SiteTunnels ####

`accountId` [ID] - (required) N/A
`addIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A
`siteId` [ID] - (required) N/A
