
## CATO-CLI - mutation.container.fqdn.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.removeValues) for documentation on this operation.

### Usage for mutation.container.fqdn.removeValues:

```bash
catocli mutation container fqdn removeValues -h

catocli mutation container fqdn removeValues <json>

catocli mutation container fqdn removeValues --json-file mutation.container.fqdn.removeValues.json

catocli mutation container fqdn removeValues '{"fqdnContainerRemoveValuesInput":{"ref":{"by":"ID","input":"string"},"values":["host.example.com"]}}'

catocli mutation container fqdn removeValues '{
    "fqdnContainerRemoveValuesInput": {
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

#### Operation Arguments for mutation.container.fqdn.removeValues ####

`accountId` [ID] - (required) N/A
`fqdnContainerRemoveValuesInput` [FqdnContainerRemoveValuesInput] - (required) N/A
