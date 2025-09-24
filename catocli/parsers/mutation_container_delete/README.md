
## CATO-CLI - mutation.container.delete:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.delete) for documentation on this operation.

### Usage for mutation.container.delete:

`catocli mutation container delete -h`

`catocli mutation container delete <json>`

`catocli mutation container delete "$(cat < mutation.container.delete.json)"`

`catocli mutation container delete '{"deleteContainerInput":{"containerRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation container delete -p '{
    "deleteContainerInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.container.delete ####

`accountId` [ID] - (required) N/A    
`deleteContainerInput` [DeleteContainerInput] - (required) N/A    
