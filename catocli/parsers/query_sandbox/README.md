
## CATO-CLI - query.sandbox:
[Click here](https://api.catonetworks.com/documentation/#query-sandbox) for documentation on this operation.

### Usage for query.sandbox:

`catocli query sandbox -h`

`catocli query sandbox <json>`

`catocli query sandbox "$(cat < sandbox.json)"`

`catocli query sandbox '{"sandboxReportsInput": {"pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}, "sandboxReportsFilterInput": {"fileHash": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "fileName": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "reportCreateDate": {"between": {"between": ["DateTime"]}, "eq": {"eq": "DateTime"}, "gt": {"gt": "DateTime"}, "gte": {"gte": "DateTime"}, "in": {"in": ["DateTime"]}, "lt": {"lt": "DateTime"}, "lte": {"lte": "DateTime"}, "neq": {"neq": "DateTime"}, "nin": {"nin": ["DateTime"]}}}, "sandboxReportsSortInput": {"fileName": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "reportCreateDate": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}}}'`

#### Operation Arguments for query.sandbox ####
`accountId` [ID] - (required) N/A 
`sandboxReportsInput` [SandboxReportsInput] - (required) N/A 
