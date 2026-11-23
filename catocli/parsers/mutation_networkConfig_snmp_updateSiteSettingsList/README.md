
## CATO-CLI - mutation.networkConfig.snmp.updateSiteSettingsList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.updateSiteSettingsList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.updateSiteSettingsList:

```bash
catocli mutation networkConfig snmp updateSiteSettingsList -h

catocli mutation networkConfig snmp updateSiteSettingsList <json>

catocli mutation networkConfig snmp updateSiteSettingsList --json-file mutation.networkConfig.snmp.updateSiteSettingsList.json

catocli mutation networkConfig snmp updateSiteSettingsList '{"networkConfigSnmpUpdateSiteSettingsListInput":{"siteSettings":[{"enabled":true,"profile":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}}]}}'

catocli mutation networkConfig snmp updateSiteSettingsList '{
    "networkConfigSnmpUpdateSiteSettingsListInput": {
        "siteSettings": [
            {
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
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.updateSiteSettingsList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpUpdateSiteSettingsListInput` [NetworkConfigSnmpUpdateSiteSettingsListInput] - (required) N/A
