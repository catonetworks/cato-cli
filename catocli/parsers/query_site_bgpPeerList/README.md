
## CATO-CLI - query.site.bgpPeerList:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.bgpPeerList) for documentation on this operation.

### Usage for query.site.bgpPeerList:

`catocli query site bgpPeerList -h`

`catocli query site bgpPeerList <json>`

`catocli query site bgpPeerList "$(cat < query.site.bgpPeerList.json)"`

`catocli query site bgpPeerList '{"bgpPeerListInput":{"siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli query site bgpPeerList -p '{
    "bgpPeerListInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for query.site.bgpPeerList ####

`accountId` [ID] - (required) N/A    
`bgpPeerListInput` [BgpPeerListInput] - (required) N/A    
