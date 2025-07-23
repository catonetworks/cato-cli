
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

#### Binary content and file uploads

Use `--binary` flag for multipart/form-data requests with file uploads:

`catocli raw --binary --file privateKey /path/to/file.pem '{ "operationName": "accountUpdate", "variables": { "update": { "cloudAccessConfiguration": { "cloudApplications": { "items": [{ "privateKey": null }] } } } }, "query": "mutation accountUpdate($update: AccountInput!) { accountUpdate(update: $update) { id } }" }'`

`catocli raw --binary --file 1 /path/to/file.pem '{ "operationName": "accountUpdate", "variables": { "update": { "version": "1234" } }, "query": "mutation { accountUpdate { id } }" }'`

The `--binary` flag enables multipart/form-data mode which is required for file uploads. Files are specified using `--file field_name file_path` where:
- `field_name` is the GraphQL variable path where the file should be mapped
- `file_path` is the local path to the file to upload

Multiple files can be uploaded by using multiple `--file` arguments.
