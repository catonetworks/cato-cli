
## CATO-CLI - mutation.container.fqdn.updateFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.updateFromFile) for documentation on this operation.

### Usage for mutation.container.fqdn.updateFromFile:

`catocli mutation container fqdn updateFromFile -h`

`catocli mutation container fqdn updateFromFile <json>`

`catocli mutation container fqdn updateFromFile "$(cat < mutation.container.fqdn.updateFromFile.json)"`

`catocli mutation container fqdn updateFromFile '{"updateFqdnContainerFromFileInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","fileType":"STIX","uploadFile":"example_value"}}'`

`catocli mutation container fqdn updateFromFile -p '{
    "updateFqdnContainerFromFileInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "description": "string",
        "fileType": "STIX",
        "uploadFile": "example_value"
    }
}'`


#### Operation Arguments for mutation.container.fqdn.updateFromFile ####

`accountId` [ID] - (required) N/A    
`updateFqdnContainerFromFileInput` [UpdateFqdnContainerFromFileInput] - (required) N/A    
