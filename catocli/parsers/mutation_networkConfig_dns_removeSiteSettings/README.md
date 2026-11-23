
## CATO-CLI - mutation.networkConfig.dns.removeSiteSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.removeSiteSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dns.removeSiteSettings:

```bash
catocli mutation networkConfig dns removeSiteSettings -h

catocli mutation networkConfig dns removeSiteSettings <json>

catocli mutation networkConfig dns removeSiteSettings --json-file mutation.networkConfig.dns.removeSiteSettings.json

catocli mutation networkConfig dns removeSiteSettings '{"networkConfigDnsRemoveSiteSettingsInput":{"site":[{"by":"ID","input":"string"}]}}'

catocli mutation networkConfig dns removeSiteSettings '{
    "networkConfigDnsRemoveSiteSettingsInput": {
        "site": [
            {
                "by": "ID",
                "input": "string"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.removeSiteSettings ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigDnsRemoveSiteSettingsInput` [NetworkConfigDnsRemoveSiteSettingsInput] - (required) Input for removing the DNS override from one or more sites.
