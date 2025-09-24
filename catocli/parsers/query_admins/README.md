
## CATO-CLI - query.admins:
[Click here](https://api.catonetworks.com/documentation/#query-query.admins) for documentation on this operation.

### Usage for query.admins:

`catocli query admins -h`

`catocli query admins <json>`

`catocli query admins "$(cat < query.admins.json)"`

`catocli query admins '{"adminIDs":["id1","id2"],"from":1,"limit":1,"search":"string","sortInput":{"field":"string","order":"asc"}}'`

`catocli query admins -p '{
    "adminIDs": [
        "id1",
        "id2"
    ],
    "from": 1,
    "limit": 1,
    "search": "string",
    "sortInput": {
        "field": "string",
        "order": "asc"
    }
}'`


#### Operation Arguments for query.admins ####

`accountID` [ID] - (required) N/A    
`adminIDs` [ID[]] - (required) N/A    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`search` [String] - (required) N/A    
`sortInput` [SortInput[]] - (required) N/A    
