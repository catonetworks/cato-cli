
## CATO-CLI - mutation.sites.updateSecondaryGcpVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSecondaryGcpVSocket) for documentation on this operation.

### Usage for mutation.sites.updateSecondaryGcpVSocket:

```bash
catocli mutation sites updateSecondaryGcpVSocket -h

catocli mutation sites updateSecondaryGcpVSocket <json>

catocli mutation sites updateSecondaryGcpVSocket --json-file mutation.sites.updateSecondaryGcpVSocket.json

catocli mutation sites updateSecondaryGcpVSocket '{"updateSecondaryGcpVSocketInput":{"gcpConfigInput":{"interfaceIp":"example_value","loadBalancerIp":"example_value"},"id":"id"}}'

catocli mutation sites updateSecondaryGcpVSocket '{
    "updateSecondaryGcpVSocketInput": {
        "gcpConfigInput": {
            "interfaceIp": "example_value",
            "loadBalancerIp": "example_value"
        },
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.sites.updateSecondaryGcpVSocket ####

`accountId` [ID] - (required) N/A    
`updateSecondaryGcpVSocketInput` [UpdateSecondaryGcpVSocketInput] - (required) N/A    
