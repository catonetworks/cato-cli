
## CATO-CLI - mutation.networkConfig.dns.updateSiteSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSiteSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSiteSettings:

```bash
catocli mutation networkConfig dns updateSiteSettings -h

catocli mutation networkConfig dns updateSiteSettings <json>

catocli mutation networkConfig dns updateSiteSettings --json-file mutation.networkConfig.dns.updateSiteSettings.json

catocli mutation networkConfig dns updateSiteSettings '{"networkConfigDnsUpdateSiteSettingsInput":{"siteSettings":[{"primaryServer":"192.0.2.1","secondaryServer":"192.0.2.1","site":{"by":"ID","input":"string"},"suffix":["example.com"]}]}}'

catocli mutation networkConfig dns updateSiteSettings '{
    "networkConfigDnsUpdateSiteSettingsInput": {
        "siteSettings": [
            {
                "primaryServer": "192.0.2.1",
                "secondaryServer": "192.0.2.1",
                "site": {
                    "by": "ID",
                    "input": "string"
                },
                "suffix": [
                    "example.com"
                ]
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSiteSettings ####

`accountId` [ID] - (required) N/A
`networkConfigDnsUpdateSiteSettingsInput` [NetworkConfigDnsUpdateSiteSettingsInput] - (required) N/A
