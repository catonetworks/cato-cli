
## CATO-CLI - mutation.container.ipAddressRange.createFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.createFromFile) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.createFromFile:

`catocli mutation container ipAddressRange createFromFile -h`

`catocli mutation container ipAddressRange createFromFile <json>`

`catocli mutation container ipAddressRange createFromFile "$(cat < mutation.container.ipAddressRange.createFromFile.json)"`

`catocli mutation container ipAddressRange createFromFile '{"createIpAddressRangeContainerFromFileInput":{"description":"string","fileType":"STIX","name":"string","uploadFile":"example_value"}}'`

`catocli mutation container ipAddressRange createFromFile -p '{
    "createIpAddressRangeContainerFromFileInput": {
        "description": "string",
        "fileType": "STIX",
        "name": "string",
        "uploadFile": "example_value"
    }
}'`


#### Operation Arguments for mutation.container.ipAddressRange.createFromFile ####

`accountId` [ID] - (required) N/A    
`createIpAddressRangeContainerFromFileInput` [CreateIpAddressRangeContainerFromFileInput] - (required) N/A    
