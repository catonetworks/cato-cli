
## CATO-CLI - mutation.networkConfig.dns.updateSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSettings:

```bash
catocli mutation networkConfig dns updateSettings -h

catocli mutation networkConfig dns updateSettings <json>

catocli mutation networkConfig dns updateSettings --json-file mutation.networkConfig.dns.updateSettings.json

catocli mutation networkConfig dns updateSettings '{"networkConfigDnsUpdateSettingsInput":{"acceptDnsRequestsOnLanInterfaceIp":true,"primaryServer":"192.0.2.1","secondaryServer":"192.0.2.1","suffix":["example.com"]}}'

catocli mutation networkConfig dns updateSettings '{
    "networkConfigDnsUpdateSettingsInput": {
        "acceptDnsRequestsOnLanInterfaceIp": true,
        "primaryServer": "192.0.2.1",
        "secondaryServer": "192.0.2.1",
        "suffix": [
            "example.com"
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSettings ####

`accountId` [ID] - (required) N/A
`networkConfigDnsUpdateSettingsInput` [NetworkConfigDnsUpdateSettingsInput] - (required) N/A
