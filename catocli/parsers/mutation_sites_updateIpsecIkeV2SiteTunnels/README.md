
## CATO-CLI - mutation.sites.updateIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.sites.updateIpsecIkeV2SiteTunnels:

`catocli mutation sites updateIpsecIkeV2SiteTunnels -h`

`catocli mutation sites updateIpsecIkeV2SiteTunnels <json>`

`catocli mutation sites updateIpsecIkeV2SiteTunnels "$(cat < updateIpsecIkeV2SiteTunnels.json)"`

`catocli mutation sites updateIpsecIkeV2SiteTunnels '{"siteId": "ID", "updateIpsecIkeV2SiteTunnelsInput": {"updateIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "popLocationId": {"popLocationId": "ID"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "tunnels": {"lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "psk": {"psk": "String"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}, "tunnelId": {"tunnelId": "enum(IPSecV2InterfaceId)"}}}}}'`

#### Operation Arguments for mutation.sites.updateIpsecIkeV2SiteTunnels ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateIpsecIkeV2SiteTunnelsInput` [UpdateIpsecIkeV2SiteTunnelsInput] - (required) N/A 
