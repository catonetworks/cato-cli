
## CATO-CLI - mutation.container.ipAddressRange.updateFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.updateFromFile) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromFile:

`catocli mutation container ipAddressRange updateFromFile -h`

`catocli mutation container ipAddressRange updateFromFile <json>`

`catocli mutation container ipAddressRange updateFromFile "$(cat < mutation.container.ipAddressRange.updateFromFile.json)"`

`catocli mutation container ipAddressRange updateFromFile '{"updateIpAddressRangeContainerFromFileInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","fileType":"STIX","uploadFile":"example_value"}}'`

`catocli mutation container ipAddressRange updateFromFile -p '{
    "updateIpAddressRangeContainerFromFileInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "description": "string",
        "fileType": "STIX",
        "uploadFile": "example_value"
    }
}'`


#### Operation Arguments for mutation.container.ipAddressRange.updateFromFile ####

`accountId` [ID] - (required) N/A    
`updateIpAddressRangeContainerFromFileInput` [UpdateIpAddressRangeContainerFromFileInput] - (required) N/A    
