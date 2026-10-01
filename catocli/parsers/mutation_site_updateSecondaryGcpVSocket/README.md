
## CATO-CLI - mutation.site.updateSecondaryGcpVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSecondaryGcpVSocket) for documentation on this operation.

### Usage for mutation.site.updateSecondaryGcpVSocket:

```bash
catocli mutation site updateSecondaryGcpVSocket -h

catocli mutation site updateSecondaryGcpVSocket <json>

catocli mutation site updateSecondaryGcpVSocket --json-file mutation.site.updateSecondaryGcpVSocket.json

catocli mutation site updateSecondaryGcpVSocket '{"updateSecondaryGcpVSocketInput":{"gcpConfig":{"interfaceIp":"192.0.2.1","loadBalancerIp":"192.0.2.1"},"id":"id"}}'

catocli mutation site updateSecondaryGcpVSocket '{
    "updateSecondaryGcpVSocketInput": {
        "gcpConfig": {
            "interfaceIp": "192.0.2.1",
            "loadBalancerIp": "192.0.2.1"
        },
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.site.updateSecondaryGcpVSocket ####

`accountId` [ID] - (required) N/A
`updateSecondaryGcpVSocketInput` [UpdateSecondaryGcpVSocketInput] - (required) N/A
