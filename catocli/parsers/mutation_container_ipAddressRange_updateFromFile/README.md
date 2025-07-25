
## CATO-CLI - mutation.container.ipAddressRange.updateFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateFromFile) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromFile:

`catocli mutation container ipAddressRange updateFromFile -h`

`catocli mutation container ipAddressRange updateFromFile <json>`

`catocli mutation container ipAddressRange updateFromFile "$(cat < updateFromFile.json)"`

`catocli mutation container ipAddressRange updateFromFile '{"updateIpAddressRangeContainerFromFileInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "fileType": {"fileType": "enum(ContainerFileType)"}, "uploadFile": {"uploadFile": "Upload"}}}'`

#### Operation Arguments for mutation.container.ipAddressRange.updateFromFile ####
`accountId` [ID] - (required) N/A 
`updateIpAddressRangeContainerFromFileInput` [UpdateIpAddressRangeContainerFromFileInput] - (required) N/A 
