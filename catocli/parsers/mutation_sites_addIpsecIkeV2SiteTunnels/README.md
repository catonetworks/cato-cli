
## CATO-CLI - mutation.sites.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.sites.addIpsecIkeV2SiteTunnels:

`catocli mutation sites addIpsecIkeV2SiteTunnels -h`

`catocli mutation sites addIpsecIkeV2SiteTunnels <json>`

`catocli mutation sites addIpsecIkeV2SiteTunnels "$(cat < addIpsecIkeV2SiteTunnels.json)"`

`catocli mutation sites addIpsecIkeV2SiteTunnels '{"AddIpsecIkeV2SiteTunnelsInput": {"AddIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "popLocationId": {"popLocationId": "ID"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "tunnels": {"lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "psk": {"psk": "String"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}}}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.sites.addIpsecIkeV2SiteTunnels ####
`AddIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
