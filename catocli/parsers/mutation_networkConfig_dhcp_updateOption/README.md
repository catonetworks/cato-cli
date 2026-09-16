
## CATO-CLI - mutation.networkConfig.dhcp.updateOption:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.updateOption) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.updateOption:

```bash
catocli mutation networkConfig dhcp updateOption -h

catocli mutation networkConfig dhcp updateOption <json>

catocli mutation networkConfig dhcp updateOption --json-file mutation.networkConfig.dhcp.updateOption.json

catocli mutation networkConfig dhcp updateOption '{"networkConfigDhcpUpdateOptionInput":{"option":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}}}'

catocli mutation networkConfig dhcp updateOption '{
    "networkConfigDhcpUpdateOptionInput": {
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

#### Operation Arguments for mutation.networkConfig.dhcp.updateOption ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpUpdateOptionInput` [NetworkConfigDhcpUpdateOptionInput] - (required) N/A    
