
## CATO-CLI - mutation.container.fqdn.createFromFile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.createFromFile) for documentation on this operation.

### Usage for mutation.container.fqdn.createFromFile:

`catocli mutation container fqdn createFromFile -h`

`catocli mutation container fqdn createFromFile <json>`

`catocli mutation container fqdn createFromFile "$(cat < mutation.container.fqdn.createFromFile.json)"`

`catocli mutation container fqdn createFromFile '{"createFqdnContainerFromFileInput":{"description":"string","fileType":"STIX","name":"string","uploadFile":"example_value"}}'`

`catocli mutation container fqdn createFromFile -p '{
    "createFqdnContainerFromFileInput": {
        "description": "string",
        "fileType": "STIX",
        "name": "string",
        "uploadFile": "example_value"
    }
}'`


#### Operation Arguments for mutation.container.fqdn.createFromFile ####

`accountId` [ID] - (required) N/A    
`createFqdnContainerFromFileInput` [CreateFqdnContainerFromFileInput] - (required) N/A    
