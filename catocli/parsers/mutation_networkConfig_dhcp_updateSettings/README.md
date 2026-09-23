
## CATO-CLI - mutation.networkConfig.dhcp.updateSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.updateSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.updateSettings:

```bash
catocli mutation networkConfig dhcp updateSettings -h

catocli mutation networkConfig dhcp updateSettings <json>

catocli mutation networkConfig dhcp updateSettings --json-file mutation.networkConfig.dhcp.updateSettings.json

catocli mutation networkConfig dhcp updateSettings '{"networkConfigDhcpUpdateSettingsInput":{"leaseTime":1,"relay":{"enabled":true,"group":{"by":"ID","input":"string"},"timeout":1}}}'

catocli mutation networkConfig dhcp updateSettings '{
    "networkConfigDhcpUpdateSettingsInput": {
        "leaseTime": 1,
        "relay": {
            "enabled": true,
            "group": {
                "by": "ID",
                "input": "string"
            },
            "timeout": 1
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.updateSettings ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpUpdateSettingsInput` [NetworkConfigDhcpUpdateSettingsInput] - (required) N/A    
