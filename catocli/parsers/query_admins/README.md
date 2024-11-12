
## CATO-CLI - query.admins:
[Click here](https://api.catonetworks.com/documentation/#query-admins) for documentation on this operation.

### Usage for query.admins:

`catocli query admins -h`

`catocli query admins <json>`

`catocli query admins "$(cat < admins.json)"`

`catocli query admins '{"adminIDs": ["ID"], "from": "Int", "limit": "Int", "search": "String", "sortInput": {"field": {"field": "String"}, "order": {"order": "enum(DirectionInput)"}}}'`

#### Operation Arguments for query.admins ####
`accountID` [ID] - (required) N/A 
`adminIDs` [ID[]] - (optional) N/A 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`search` [String] - (optional) N/A 
`sortInput` [SortInput[]] - (optional) N/A 
