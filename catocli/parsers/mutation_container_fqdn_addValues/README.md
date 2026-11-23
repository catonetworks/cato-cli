
## CATO-CLI - mutation.container.fqdn.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.addValues) for documentation on this operation.

### Usage for mutation.container.fqdn.addValues:

```bash
catocli mutation container fqdn addValues -h

catocli mutation container fqdn addValues <json>

catocli mutation container fqdn addValues --json-file mutation.container.fqdn.addValues.json

catocli mutation container fqdn addValues '{"fqdnContainerAddValuesInput":{"ref":{"by":"ID","input":"string"},"values":["host.example.com"]}}'

catocli mutation container fqdn addValues '{
    "fqdnContainerAddValuesInput": {
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

#### Operation Arguments for mutation.container.fqdn.addValues ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`fqdnContainerAddValuesInput` [FqdnContainerAddValuesInput] - (required) Container reference and values to add.
