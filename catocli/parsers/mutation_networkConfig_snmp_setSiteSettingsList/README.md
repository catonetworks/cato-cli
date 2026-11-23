
## CATO-CLI - mutation.networkConfig.snmp.setSiteSettingsList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.setSiteSettingsList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.setSiteSettingsList:

```bash
catocli mutation networkConfig snmp setSiteSettingsList -h

catocli mutation networkConfig snmp setSiteSettingsList <json>

catocli mutation networkConfig snmp setSiteSettingsList --json-file mutation.networkConfig.snmp.setSiteSettingsList.json

catocli mutation networkConfig snmp setSiteSettingsList '{"networkConfigSnmpSetSiteSettingsListInput":{"siteSettings":[{"enabled":true,"profile":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"}}]}}'

catocli mutation networkConfig snmp setSiteSettingsList '{
    "networkConfigSnmpSetSiteSettingsListInput": {
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

#### Operation Arguments for mutation.networkConfig.snmp.setSiteSettingsList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpSetSiteSettingsListInput` [NetworkConfigSnmpSetSiteSettingsListInput] - (required) N/A
