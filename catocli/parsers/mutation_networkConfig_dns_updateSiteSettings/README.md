
## CATO-CLI - mutation.networkConfig.dns.updateSiteSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSiteSettings) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSiteSettings:

```bash
catocli mutation networkConfig dns updateSiteSettings -h

catocli mutation networkConfig dns updateSiteSettings <json>

catocli mutation networkConfig dns updateSiteSettings --json-file mutation.networkConfig.dns.updateSiteSettings.json

catocli mutation networkConfig dns updateSiteSettings '{"networkConfigDnsUpdateSiteSettingsInput":{"siteSettings":{"primaryServer":"example_value","secondaryServer":"example_value","site":{"by":"ID","input":"string"},"suffix":["example1","example2"]}}}'

catocli mutation networkConfig dns updateSiteSettings '{
    "networkConfigDnsUpdateSiteSettingsInput": {
        "siteSettings": {
            "primaryServer": "example_value",
            "secondaryServer": "example_value",
            "site": {
                "by": "ID",
                "input": "string"
            },
            "suffix": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSiteSettings ####

