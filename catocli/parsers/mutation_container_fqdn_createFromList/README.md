
## CATO-CLI - mutation.container.fqdn.createFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.createFromList) for documentation on this operation.

### Usage for mutation.container.fqdn.createFromList:

```bash
catocli mutation container fqdn createFromList -h

catocli mutation container fqdn createFromList <json>

catocli mutation container fqdn createFromList --json-file mutation.container.fqdn.createFromList.json

catocli mutation container fqdn createFromList '{"createFqdnContainerFromListInput":{"description":"string","name":"string","values":["host.example.com"]}}'

catocli mutation container fqdn createFromList '{
    "createFqdnContainerFromListInput": {
        "description": "string",
        "name": "string",
        "values": [
            "host.example.com"
        ]
    }
}'
```

#### Operation Arguments for mutation.container.fqdn.createFromList ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`createFqdnContainerFromListInput` [CreateFqdnContainerFromListInput] - (required) Container name, description and initial values.
