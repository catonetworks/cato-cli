
## CATO-CLI - mutation.sites.updateIpsecIkeV2SiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateIpsecIkeV2SiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateIpsecIkeV2SiteGeneralDetails:

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails -h`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails <json>`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails "$(cat < updateIpsecIkeV2SiteGeneralDetails.json)"`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails '{"UpdateIpsecIkeV2SiteGeneralDetailsInput": {"IpsecIkeV2MessageInput": {"cipher": {"cipher": "enum(IpSecCipher)"}, "dhGroup": {"dhGroup": "enum(IpSecDHGroup)"}, "integrity": {"integrity": "enum(IpSecHash)"}, "prf": {"prf": "enum(IpSecHash)"}}, "connectionMode": {"connectionMode": "enum(ConnectionMode)"}, "identificationType": {"identificationType": "enum(IdentificationType)"}, "networkRanges": {"networkRanges": ["IPSubnet"]}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.sites.updateIpsecIkeV2SiteGeneralDetails ####
`UpdateIpsecIkeV2SiteGeneralDetailsInput` [UpdateIpsecIkeV2SiteGeneralDetailsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
