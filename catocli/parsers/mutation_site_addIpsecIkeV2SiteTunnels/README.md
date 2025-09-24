
## CATO-CLI - mutation.site.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2SiteTunnels:

`catocli mutation site addIpsecIkeV2SiteTunnels -h`

`catocli mutation site addIpsecIkeV2SiteTunnels <json>`

`catocli mutation site addIpsecIkeV2SiteTunnels "$(cat < mutation.site.addIpsecIkeV2SiteTunnels.json)"`

`catocli mutation site addIpsecIkeV2SiteTunnels '{"addIpsecIkeV2SiteTunnelsInput":{"addIpsecIkeV2TunnelsInput":{"destinationType":"IPv4","popLocationId":"id","publicCatoIpId":"id","tunnels":{"lastMileBw":{"downstream":1,"downstreamMbpsPrecision":1.5,"upstream":1,"upstreamMbpsPrecision":1.5},"name":"string","privateCatoIp":"example_value","privateSiteIp":"example_value","psk":"string","publicSiteIp":"example_value","role":"WAN1"}}},"siteId":"id"}'`

`catocli mutation site addIpsecIkeV2SiteTunnels -p '{
    "addIpsecIkeV2SiteTunnelsInput": {
        "addIpsecIkeV2TunnelsInput": {
            "destinationType": "IPv4",
            "popLocationId": "id",
            "publicCatoIpId": "id",
            "tunnels": {
                "lastMileBw": {
                    "downstream": 1,
                    "downstreamMbpsPrecision": 1.5,
                    "upstream": 1,
                    "upstreamMbpsPrecision": 1.5
                },
                "name": "string",
                "privateCatoIp": "example_value",
                "privateSiteIp": "example_value",
                "psk": "string",
                "publicSiteIp": "example_value",
                "role": "WAN1"
            }
        }
    },
    "siteId": "id"
}'`


#### Operation Arguments for mutation.site.addIpsecIkeV2SiteTunnels ####

`accountId` [ID] - (required) N/A    
`addIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A    
`siteId` [ID] - (required) N/A    
