
## CATO-CLI - mutation.networkConfig.snmp.removeSiteSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.removeSiteSettings) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.removeSiteSettings:

```bash
catocli mutation networkConfig snmp removeSiteSettings -h

catocli mutation networkConfig snmp removeSiteSettings <json>

catocli mutation networkConfig snmp removeSiteSettings --json-file mutation.networkConfig.snmp.removeSiteSettings.json

catocli mutation networkConfig snmp removeSiteSettings '{"networkConfigSnmpRemoveSiteSettingsInput":{"site":{"by":"ID","input":"string"}}}'

catocli mutation networkConfig snmp removeSiteSettings '{
    "networkConfigSnmpRemoveSiteSettingsInput": {
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.removeSiteSettings ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpRemoveSiteSettingsInput` [NetworkConfigSnmpRemoveSiteSettingsInput] - (required) N/A
