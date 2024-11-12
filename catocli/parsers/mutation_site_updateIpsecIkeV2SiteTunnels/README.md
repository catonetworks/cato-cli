
## CATO-CLI - mutation.site.updateIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.updateIpsecIkeV2SiteTunnels:

`catocli mutation site updateIpsecIkeV2SiteTunnels -h`

`catocli mutation site updateIpsecIkeV2SiteTunnels <json>`

`catocli mutation site updateIpsecIkeV2SiteTunnels "$(cat < updateIpsecIkeV2SiteTunnels.json)"`

`catocli mutation site updateIpsecIkeV2SiteTunnels '{"siteId": "ID", "updateIpsecIkeV2SiteTunnelsInput": {"updateIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "popLocationId": {"popLocationId": "ID"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "tunnels": {"lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "psk": {"psk": "String"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}, "tunnelId": {"tunnelId": "enum(IPSecV2InterfaceId)"}}}}}'`

#### Operation Arguments for mutation.site.updateIpsecIkeV2SiteTunnels ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateIpsecIkeV2SiteTunnelsInput` [UpdateIpsecIkeV2SiteTunnelsInput] - (required) N/A 
