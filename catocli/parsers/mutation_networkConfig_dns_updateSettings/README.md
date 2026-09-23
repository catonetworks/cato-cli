
## CATO-CLI - mutation.networkConfig.dns.updateSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSettings:

```bash
catocli mutation networkConfig dns updateSettings -h

catocli mutation networkConfig dns updateSettings <json>

catocli mutation networkConfig dns updateSettings --json-file mutation.networkConfig.dns.updateSettings.json

catocli mutation networkConfig dns updateSettings '{"networkConfigDnsUpdateSettingsInput":{"acceptDnsRequestsOnLanInterfaceIp":true,"primaryServer":"example_value","secondaryServer":"example_value","suffix":["example1","example2"]}}'

catocli mutation networkConfig dns updateSettings '{
    "networkConfigDnsUpdateSettingsInput": {
        "acceptDnsRequestsOnLanInterfaceIp": true,
        "primaryServer": "example_value",
        "secondaryServer": "example_value",
        "suffix": [
            "example1",
            "example2"
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSettings ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsUpdateSettingsInput` [NetworkConfigDnsUpdateSettingsInput] - (required) N/A    
