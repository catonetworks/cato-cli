
## CATO-CLI - mutation.sites.addSecondaryGcpVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSecondaryGcpVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryGcpVSocket:

```bash
catocli mutation sites addSecondaryGcpVSocket -h

catocli mutation sites addSecondaryGcpVSocket <json>

catocli mutation sites addSecondaryGcpVSocket --json-file mutation.sites.addSecondaryGcpVSocket.json

catocli mutation sites addSecondaryGcpVSocket '{"addSecondaryGcpVSocketInput":{"gcpConfig":{"interfaceIp":"192.0.2.1","loadBalancerIp":"192.0.2.1"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites addSecondaryGcpVSocket '{
    "addSecondaryGcpVSocketInput": {
        "gcpConfig": {
            "interfaceIp": "192.0.2.1",
            "loadBalancerIp": "192.0.2.1"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.addSecondaryGcpVSocket ####

`accountId` [ID] - (required) N/A
`addSecondaryGcpVSocketInput` [AddSecondaryGcpVSocketInput] - (required) N/A
