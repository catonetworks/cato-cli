
## CATO-CLI - mutation.site.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAzureVSocket:

```bash
catocli mutation site addSecondaryAzureVSocket -h

catocli mutation site addSecondaryAzureVSocket <json>

catocli mutation site addSecondaryAzureVSocket --json-file mutation.site.addSecondaryAzureVSocket.json

catocli mutation site addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput":{"floatingIp":"192.0.2.1","interfaceIp":"192.0.2.1","site":{"by":"ID","input":"string"}}}'

catocli mutation site addSecondaryAzureVSocket '{
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

#### Operation Arguments for mutation.site.addSecondaryAzureVSocket ####

`accountId` [ID] - (required) N/A
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A
