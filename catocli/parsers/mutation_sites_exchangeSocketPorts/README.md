
## CATO-CLI - mutation.sites.exchangeSocketPorts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.exchangeSocketPorts) for documentation on this operation.

### Usage for mutation.sites.exchangeSocketPorts:

```bash
catocli mutation sites exchangeSocketPorts -h

catocli mutation sites exchangeSocketPorts <json>

catocli mutation sites exchangeSocketPorts --json-file mutation.sites.exchangeSocketPorts.json

catocli mutation sites exchangeSocketPorts '{"exchangeSocketPortsInput":{"firstInterface":{"interfaceId":"LAN1"},"secondInterface":{"interfaceId":"LAN1"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites exchangeSocketPorts '{
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

#### Operation Arguments for mutation.sites.exchangeSocketPorts ####

`accountId` [ID] - (required) N/A    
`exchangeSocketPortsInput` [ExchangeSocketPortsInput] - (required) N/A    
