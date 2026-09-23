
## CATO-CLI - mutation.site.exchangeSocketPorts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.exchangeSocketPorts) for documentation on this operation.

### Usage for mutation.site.exchangeSocketPorts:

```bash
catocli mutation site exchangeSocketPorts -h

catocli mutation site exchangeSocketPorts <json>

catocli mutation site exchangeSocketPorts --json-file mutation.site.exchangeSocketPorts.json

catocli mutation site exchangeSocketPorts '{"exchangeSocketPortsInput":{"firstInterface":{"interfaceId":"LAN1"},"secondInterface":{"interfaceId":"LAN1"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site exchangeSocketPorts '{
    "exchangeSocketPortsInput": {
        "firstInterface": {
            "interfaceId": "LAN1"
        },
        "secondInterface": {
            "interfaceId": "LAN1"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.exchangeSocketPorts ####

`accountId` [ID] - (required) N/A    
`exchangeSocketPortsInput` [ExchangeSocketPortsInput] - (required) N/A    
