
## CATO-CLI - mutation.networkConfig.snmp.updateSiteSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.updateSiteSettings) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.updateSiteSettings:

```bash
catocli mutation networkConfig snmp updateSiteSettings -h

catocli mutation networkConfig snmp updateSiteSettings <json>

catocli mutation networkConfig snmp updateSiteSettings --json-file mutation.networkConfig.snmp.updateSiteSettings.json

catocli mutation networkConfig snmp updateSiteSettings '{"networkConfigSnmpUpdateSiteSettingsInput":{"siteSettings":{"enabled":true,"profile":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}}}}'

catocli mutation networkConfig snmp updateSiteSettings '{
    "networkConfigSnmpUpdateSiteSettingsInput": {
        "siteSettings": {
            "enabled": true,
            "profile": {
                "by": "ID",
                "input": "string"
            },
            "site": {
                "by": "ID",
                "input": "string"
            }
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.updateSiteSettings ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpUpdateSiteSettingsInput` [NetworkConfigSnmpUpdateSiteSettingsInput] - (required) N/A
