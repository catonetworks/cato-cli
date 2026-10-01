
## CATO-CLI - mutation.sites.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAzureVSocket:

```bash
catocli mutation sites addSecondaryAzureVSocket -h

catocli mutation sites addSecondaryAzureVSocket <json>

catocli mutation sites addSecondaryAzureVSocket --json-file mutation.sites.addSecondaryAzureVSocket.json

catocli mutation sites addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput":{"floatingIp":"192.0.2.1","interfaceIp":"192.0.2.1","site":{"by":"ID","input":"string"}}}'

catocli mutation sites addSecondaryAzureVSocket '{
    "addSecondaryAzureVSocketInput": {
        "floatingIp": "192.0.2.1",
        "interfaceIp": "192.0.2.1",
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.addSecondaryAzureVSocket ####

`accountId` [ID] - (required) N/A
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A
