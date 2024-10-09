
## CATO-CLI - query.admins:
[Click here](https://api.catonetworks.com/documentation/#query-admins) for documentation on this operation.

### Usage for query.admins:

`catocli query admins -h`

`catocli query admins <accountID> <json>`

`catocli query admins 12345 "$(cat < admins.json)"`

`catocli query admins 12345 '{"SortInput": {"field": {"field": "String"}, "order": {"order": "enum(DirectionInput)"}}, "adminIDs": ["ID"], "from": "Int", "limit": "Int", "search": "String"}'`

#### Operation Arguments for query.admins ####
`SortInput` [SortInput[]] - (optional) N/A 
`accountID` [ID] - (required) N/A 
`adminIDs` [ID[]] - (optional) N/A 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`search` [String] - (optional) N/A 
