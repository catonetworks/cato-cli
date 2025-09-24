
## CATO-CLI - mutation.site.removeIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.removeIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.removeIpsecIkeV2SiteTunnels:

`catocli mutation site removeIpsecIkeV2SiteTunnels -h`

`catocli mutation site removeIpsecIkeV2SiteTunnels <json>`

`catocli mutation site removeIpsecIkeV2SiteTunnels "$(cat < mutation.site.removeIpsecIkeV2SiteTunnels.json)"`

`catocli mutation site removeIpsecIkeV2SiteTunnels '{"removeIpsecIkeV2SiteTunnelsInput":{"tunnelId":"PRIMARY1"},"siteId":"id"}'`

`catocli mutation site removeIpsecIkeV2SiteTunnels -p '{
    "removeIpsecIkeV2SiteTunnelsInput": {
        "tunnelId": "PRIMARY1"
    },
    "siteId": "id"
}'`


#### Operation Arguments for mutation.site.removeIpsecIkeV2SiteTunnels ####

`accountId` [ID] - (required) N/A    
`removeIpsecIkeV2SiteTunnelsInput` [RemoveIpsecIkeV2SiteTunnelsInput] - (required) N/A    
`siteId` [ID] - (required) N/A    
