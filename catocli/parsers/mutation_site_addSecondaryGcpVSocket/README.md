
## CATO-CLI - mutation.site.addSecondaryGcpVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSecondaryGcpVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryGcpVSocket:

```bash
catocli mutation site addSecondaryGcpVSocket -h

catocli mutation site addSecondaryGcpVSocket <json>

catocli mutation site addSecondaryGcpVSocket --json-file mutation.site.addSecondaryGcpVSocket.json

catocli mutation site addSecondaryGcpVSocket '{"addSecondaryGcpVSocketInput":{"gcpConfigInput":{"interfaceIp":"example_value","loadBalancerIp":"example_value"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation site addSecondaryGcpVSocket '{
    "addSecondaryGcpVSocketInput": {
        "gcpConfigInput": {
            "interfaceIp": "example_value",
            "loadBalancerIp": "example_value"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.addSecondaryGcpVSocket ####

`accountId` [ID] - (required) N/A    
`addSecondaryGcpVSocketInput` [AddSecondaryGcpVSocketInput] - (required) N/A    
