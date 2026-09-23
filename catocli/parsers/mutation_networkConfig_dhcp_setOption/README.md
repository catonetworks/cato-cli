
## CATO-CLI - mutation.networkConfig.dhcp.setOption:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.setOption) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.setOption:

```bash
catocli mutation networkConfig dhcp setOption -h

catocli mutation networkConfig dhcp setOption <json>

catocli mutation networkConfig dhcp setOption --json-file mutation.networkConfig.dhcp.setOption.json

catocli mutation networkConfig dhcp setOption '{"networkConfigDhcpSetOptionInput":{"option":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}}}'

catocli mutation networkConfig dhcp setOption '{
    "networkConfigDhcpSetOptionInput": {
        "option": {
            "description": "string",
            "id": "id",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.setOption ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpSetOptionInput` [NetworkConfigDhcpSetOptionInput] - (required) N/A    
