
## CATO-CLI - mutation.networkConfig.snmp.removeSiteSettingsList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.removeSiteSettingsList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.removeSiteSettingsList:

```bash
catocli mutation networkConfig snmp removeSiteSettingsList -h

catocli mutation networkConfig snmp removeSiteSettingsList <json>

catocli mutation networkConfig snmp removeSiteSettingsList --json-file mutation.networkConfig.snmp.removeSiteSettingsList.json

catocli mutation networkConfig snmp removeSiteSettingsList '{"networkConfigSnmpRemoveSiteSettingsListInput":{"site":[{"by":"ID","input":"string"}]}}'

catocli mutation networkConfig snmp removeSiteSettingsList '{
    "networkConfigSnmpRemoveSiteSettingsListInput": {
        "site": [
            {
                "by": "ID",
                "input": "string"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.removeSiteSettingsList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpRemoveSiteSettingsListInput` [NetworkConfigSnmpRemoveSiteSettingsListInput] - (required) N/A
