
## CATO-CLI - mutation.container.fqdn.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.removeValues) for documentation on this operation.

### Usage for mutation.container.fqdn.removeValues:

`catocli mutation container fqdn removeValues -h`

`catocli mutation container fqdn removeValues <json>`

`catocli mutation container fqdn removeValues "$(cat < mutation.container.fqdn.removeValues.json)"`

`catocli mutation container fqdn removeValues '{"fqdnContainerRemoveValuesInput":{"containerRefInput":{"by":"ID","input":"string"},"values":["example1","example2"]}}'`

`catocli mutation container fqdn removeValues -p '{
    "fqdnContainerRemoveValuesInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "values": [
            "example1",
            "example2"
        ]
    }
}'`


#### Operation Arguments for mutation.container.fqdn.removeValues ####

`accountId` [ID] - (required) N/A    
`fqdnContainerRemoveValuesInput` [FqdnContainerRemoveValuesInput] - (required) N/A    
