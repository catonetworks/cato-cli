
## CATO-CLI - mutation.container.fqdn.updateFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.updateFromList) for documentation on this operation.

### Usage for mutation.container.fqdn.updateFromList:

```bash
catocli mutation container fqdn updateFromList -h

catocli mutation container fqdn updateFromList <json>

catocli mutation container fqdn updateFromList --json-file mutation.container.fqdn.updateFromList.json

catocli mutation container fqdn updateFromList '{"updateFqdnContainerFromListInput":{"description":"string","ref":{"by":"ID","input":"string"},"values":["host.example.com"]}}'

catocli mutation container fqdn updateFromList '{
    "updateFqdnContainerFromListInput": {
        "description": "string",
        "ref": {
            "by": "ID",
            "input": "string"
        },
        "values": [
            "host.example.com"
        ]
    }
}'
```

#### Operation Arguments for mutation.container.fqdn.updateFromList ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`updateFqdnContainerFromListInput` [UpdateFqdnContainerFromListInput] - (required) Container reference, values and description to update.
