
## CATO-CLI - mutation.sites.updateIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.sites.updateIpsecIkeV2SiteTunnels:

`catocli mutation sites updateIpsecIkeV2SiteTunnels -h`

`catocli mutation sites updateIpsecIkeV2SiteTunnels <json>`

`catocli mutation sites updateIpsecIkeV2SiteTunnels "$(cat < mutation.sites.updateIpsecIkeV2SiteTunnels.json)"`

`catocli mutation sites updateIpsecIkeV2SiteTunnels '{"siteId":"id","updateIpsecIkeV2SiteTunnelsInput":{"updateIpsecIkeV2TunnelsInput":{"destinationType":"IPv4","popLocationId":"id","publicCatoIpId":"id","tunnels":{"lastMileBw":{"downstream":1,"downstreamMbpsPrecision":1.5,"upstream":1,"upstreamMbpsPrecision":1.5},"name":"string","privateCatoIp":"example_value","privateSiteIp":"example_value","psk":"string","publicSiteIp":"example_value","role":"WAN1","tunnelId":"PRIMARY1"}}}}'`

`catocli mutation sites updateIpsecIkeV2SiteTunnels -p '{
    "siteId": "id",
    "updateIpsecIkeV2SiteTunnelsInput": {
        "updateIpsecIkeV2TunnelsInput": {
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
                "role": "WAN1",
                "tunnelId": "PRIMARY1"
            }
        }
    }
}'`


#### Operation Arguments for mutation.sites.updateIpsecIkeV2SiteTunnels ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateIpsecIkeV2SiteTunnelsInput` [UpdateIpsecIkeV2SiteTunnelsInput] - (required) N/A    
