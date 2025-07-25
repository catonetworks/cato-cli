
## CATO-CLI - mutation.container.fqdn.createFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-createFromFile) for documentation on this operation.

### Usage for mutation.container.fqdn.createFromFile:

`catocli mutation container fqdn createFromFile -h`

`catocli mutation container fqdn createFromFile <json>`

`catocli mutation container fqdn createFromFile "$(cat < createFromFile.json)"`

`catocli mutation container fqdn createFromFile '{"createFqdnContainerFromFileInput": {"description": {"description": "String"}, "fileType": {"fileType": "enum(ContainerFileType)"}, "name": {"name": "String"}, "uploadFile": {"uploadFile": "Upload"}}}'`

#### Operation Arguments for mutation.container.fqdn.createFromFile ####
`accountId` [ID] - (required) N/A 
`createFqdnContainerFromFileInput` [CreateFqdnContainerFromFileInput] - (required) N/A 
