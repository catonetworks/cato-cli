
## CATO-CLI - mutation.networkConfig.dhcp.createOption:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.createOption) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.createOption:

```bash
catocli mutation networkConfig dhcp createOption -h

catocli mutation networkConfig dhcp createOption <json>

catocli mutation networkConfig dhcp createOption --json-file mutation.networkConfig.dhcp.createOption.json

catocli mutation networkConfig dhcp createOption '{"networkConfigDhcpCreateOptionInput":{"option":{"description":"string","tag":1,"type":"ASCII","value":"string"}}}'

catocli mutation networkConfig dhcp createOption '{
    "networkConfigDhcpCreateOptionInput": {
        "option": {
            "description": "string",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.createOption ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpCreateOptionInput` [NetworkConfigDhcpCreateOptionInput] - (required) N/A    
