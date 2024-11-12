
## CATO-CLI - mutation.sites.updateIpsecIkeV2SiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateIpsecIkeV2SiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateIpsecIkeV2SiteGeneralDetails:

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails -h`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails <json>`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails "$(cat < updateIpsecIkeV2SiteGeneralDetails.json)"`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails '{"siteId": "ID", "updateIpsecIkeV2SiteGeneralDetailsInput": {"connectionMode": {"connectionMode": "enum(ConnectionMode)"}, "identificationType": {"identificationType": "enum(IdentificationType)"}, "ipsecIkeV2MessageInput": {"cipher": {"cipher": "enum(IpSecCipher)"}, "dhGroup": {"dhGroup": "enum(IpSecDHGroup)"}, "integrity": {"integrity": "enum(IpSecHash)"}, "prf": {"prf": "enum(IpSecHash)"}}, "networkRanges": {"networkRanges": ["IPSubnet"]}}}'`

#### Operation Arguments for mutation.sites.updateIpsecIkeV2SiteGeneralDetails ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateIpsecIkeV2SiteGeneralDetailsInput` [UpdateIpsecIkeV2SiteGeneralDetailsInput] - (required) N/A 
