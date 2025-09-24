
## CATO-CLI - mutation.sites.removeIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.removeIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.sites.removeIpsecIkeV2SiteTunnels:

`catocli mutation sites removeIpsecIkeV2SiteTunnels -h`

`catocli mutation sites removeIpsecIkeV2SiteTunnels <json>`

`catocli mutation sites removeIpsecIkeV2SiteTunnels "$(cat < mutation.sites.removeIpsecIkeV2SiteTunnels.json)"`

`catocli mutation sites removeIpsecIkeV2SiteTunnels '{"removeIpsecIkeV2SiteTunnelsInput":{"tunnelId":"PRIMARY1"},"siteId":"id"}'`

`catocli mutation sites removeIpsecIkeV2SiteTunnels -p '{
    "removeIpsecIkeV2SiteTunnelsInput": {
        "tunnelId": "PRIMARY1"
    },
    "siteId": "id"
}'`


#### Operation Arguments for mutation.sites.removeIpsecIkeV2SiteTunnels ####

`accountId` [ID] - (required) N/A    
`removeIpsecIkeV2SiteTunnelsInput` [RemoveIpsecIkeV2SiteTunnelsInput] - (required) N/A    
`siteId` [ID] - (required) N/A    
