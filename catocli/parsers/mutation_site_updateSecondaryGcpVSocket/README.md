
## CATO-CLI - mutation.site.updateSecondaryGcpVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSecondaryGcpVSocket) for documentation on this operation.

### Usage for mutation.site.updateSecondaryGcpVSocket:

```bash
catocli mutation site updateSecondaryGcpVSocket -h

catocli mutation site updateSecondaryGcpVSocket <json>

catocli mutation site updateSecondaryGcpVSocket --json-file mutation.site.updateSecondaryGcpVSocket.json

catocli mutation site updateSecondaryGcpVSocket '{"updateSecondaryGcpVSocketInput":{"gcpConfigInput":{"interfaceIp":"example_value","loadBalancerIp":"example_value"},"id":"id"}}'

catocli mutation site updateSecondaryGcpVSocket '{
    "updateSecondaryGcpVSocketInput": {
        "gcpConfigInput": {
            "interfaceIp": "example_value",
            "loadBalancerIp": "example_value"
        },
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.site.updateSecondaryGcpVSocket ####

`accountId` [ID] - (required) N/A    
`updateSecondaryGcpVSocketInput` [UpdateSecondaryGcpVSocketInput] - (required) N/A    
