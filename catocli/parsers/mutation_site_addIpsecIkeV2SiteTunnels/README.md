
## CATO-CLI - mutation.site.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2SiteTunnels:

`catocli mutation site addIpsecIkeV2SiteTunnels -h`

`catocli mutation site addIpsecIkeV2SiteTunnels <json>`

`catocli mutation site addIpsecIkeV2SiteTunnels "$(cat < addIpsecIkeV2SiteTunnels.json)"`

`catocli mutation site addIpsecIkeV2SiteTunnels '{"AddIpsecIkeV2SiteTunnelsInput": {"AddIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "popLocationId": {"popLocationId": "ID"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "tunnels": {"lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}}, "name": {"name": "String"}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "psk": {"psk": "String"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}, "role": {"role": "enum(IPSecV2TunnelRole)"}}}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.addIpsecIkeV2SiteTunnels ####
`AddIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
