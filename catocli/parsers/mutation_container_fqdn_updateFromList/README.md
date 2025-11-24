
## CATO-CLI - mutation.container.fqdn.updateFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.updateFromList) for documentation on this operation.

### Usage for mutation.container.fqdn.updateFromList:

```bash
catocli mutation container fqdn updateFromList -h

catocli mutation container fqdn updateFromList <json>

catocli mutation container fqdn updateFromList --json-file mutation.container.fqdn.updateFromList.json

catocli mutation container fqdn updateFromList '{"updateFqdnContainerFromListInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","values":["example1","example2"]}}'

catocli mutation container fqdn updateFromList '{
    "updateFqdnContainerFromListInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "description": "string",
        "values": [
            "example1",
            "example2"
        ]
    }
}'
```

#### Operation Arguments for mutation.container.fqdn.updateFromList ####

`accountId` [ID] - (required) N/A    
`updateFqdnContainerFromListInput` [UpdateFqdnContainerFromListInput] - (required) N/A    
