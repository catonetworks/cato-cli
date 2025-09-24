
## CATO-CLI - query.site.cloudInterconnectPhysicalConnectionId:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.cloudInterconnectPhysicalConnectionId) for documentation on this operation.

### Usage for query.site.cloudInterconnectPhysicalConnectionId:

`catocli query site cloudInterconnectPhysicalConnectionId -h`

`catocli query site cloudInterconnectPhysicalConnectionId <json>`

`catocli query site cloudInterconnectPhysicalConnectionId "$(cat < query.site.cloudInterconnectPhysicalConnectionId.json)"`

`catocli query site cloudInterconnectPhysicalConnectionId '{"cloudInterconnectPhysicalConnectionIdInput":{"haRole":"PRIMARY","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli query site cloudInterconnectPhysicalConnectionId -p '{
    "cloudInterconnectPhysicalConnectionIdInput": {
        "haRole": "PRIMARY",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for query.site.cloudInterconnectPhysicalConnectionId ####

`accountId` [ID] - (required) N/A    
`cloudInterconnectPhysicalConnectionIdInput` [CloudInterconnectPhysicalConnectionIdInput] - (required) N/A    
