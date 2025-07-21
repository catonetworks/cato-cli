
## CATO-CLI - raw.graphql
[Click here](https://api.catonetworks.com/documentation/) for documentation on this operation.

### Usage for raw.graphql

`catocli raw -h`

`catocli raw <json>`

`catocli raw "$(cat < rawGraphqQL.json)"`

`catocli raw '{ "query": "query operationNameHere($yourArgument:String!) { field1 field2 }", "variables": { "yourArgument": "string", "accountID": "10949" }, "operationName": "operationNameHere" } '`

`catocli raw '{ "query": "mutation operationNameHere($yourArgument:String!) { field1 field2 }", "variables": { "yourArgument": "string", "accountID": "10949" }, "operationName": "operationNameHere" } '`

#### Override API endpoint

`catocli raw --endpoint https://custom-api.example.com/graphql '<json>'`
