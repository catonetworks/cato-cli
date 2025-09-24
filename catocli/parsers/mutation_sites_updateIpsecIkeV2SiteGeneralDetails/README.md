
## CATO-CLI - mutation.sites.updateIpsecIkeV2SiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateIpsecIkeV2SiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateIpsecIkeV2SiteGeneralDetails:

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails -h`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails <json>`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails "$(cat < mutation.sites.updateIpsecIkeV2SiteGeneralDetails.json)"`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails '{"siteId":"id","updateIpsecIkeV2SiteGeneralDetailsInput":{"connectionMode":"RESPONDER_ONLY","identificationType":"IPV4","ipsecIkeV2MessageInput":{"cipher":"NONE","dhGroup":"NONE","integrity":"NONE","prf":"NONE"},"networkRanges":["example1","example2"]}}'`

`catocli mutation sites updateIpsecIkeV2SiteGeneralDetails -p '{
    "siteId": "id",
    "updateIpsecIkeV2SiteGeneralDetailsInput": {
        "connectionMode": "RESPONDER_ONLY",
        "identificationType": "IPV4",
        "ipsecIkeV2MessageInput": {
            "cipher": "NONE",
            "dhGroup": "NONE",
            "integrity": "NONE",
            "prf": "NONE"
        },
        "networkRanges": [
            "example1",
            "example2"
        ]
    }
}'`


#### Operation Arguments for mutation.sites.updateIpsecIkeV2SiteGeneralDetails ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateIpsecIkeV2SiteGeneralDetailsInput` [UpdateIpsecIkeV2SiteGeneralDetailsInput] - (required) N/A    
