
## CATO-CLI - mutation.container.fqdn.updateFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateFromFile) for documentation on this operation.

### Usage for mutation.container.fqdn.updateFromFile:

`catocli mutation container fqdn updateFromFile -h`

`catocli mutation container fqdn updateFromFile <json>`

`catocli mutation container fqdn updateFromFile "$(cat < updateFromFile.json)"`

`catocli mutation container fqdn updateFromFile '{"updateFqdnContainerFromFileInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "fileType": {"fileType": "enum(ContainerFileType)"}, "uploadFile": {"uploadFile": "Upload"}}}'`

#### Operation Arguments for mutation.container.fqdn.updateFromFile ####
`accountId` [ID] - (required) N/A 
`updateFqdnContainerFromFileInput` [UpdateFqdnContainerFromFileInput] - (required) N/A 
