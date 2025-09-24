
## CATO-CLI - query.site.siteBgpStatus:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.siteBgpStatus) for documentation on this operation.

### Usage for query.site.siteBgpStatus:

`catocli query site siteBgpStatus -h`

`catocli query site siteBgpStatus <json>`

`catocli query site siteBgpStatus "$(cat < query.site.siteBgpStatus.json)"`

`catocli query site siteBgpStatus '{"siteBgpStatusInput":{"siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli query site siteBgpStatus -p '{
    "siteBgpStatusInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for query.site.siteBgpStatus ####

`accountId` [ID] - (required) N/A    
`siteBgpStatusInput` [SiteBgpStatusInput] - (required) N/A    
