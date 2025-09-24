
## CATO-CLI - mutation.container.fqdn.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.addValues) for documentation on this operation.

### Usage for mutation.container.fqdn.addValues:

`catocli mutation container fqdn addValues -h`

`catocli mutation container fqdn addValues <json>`

`catocli mutation container fqdn addValues "$(cat < mutation.container.fqdn.addValues.json)"`

`catocli mutation container fqdn addValues '{"fqdnContainerAddValuesInput":{"containerRefInput":{"by":"ID","input":"string"},"values":["example1","example2"]}}'`

`catocli mutation container fqdn addValues -p '{
    "fqdnContainerAddValuesInput": {
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


#### Operation Arguments for mutation.container.fqdn.addValues ####

`accountId` [ID] - (required) N/A    
`fqdnContainerAddValuesInput` [FqdnContainerAddValuesInput] - (required) N/A    
