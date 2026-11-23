
## CATO-CLI - query.networkConfig.snmp.siteSettingsList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.snmp.siteSettingsList) for documentation on this operation.

### Usage for query.networkConfig.snmp.siteSettingsList:

```bash
catocli query networkConfig snmp siteSettingsList -h

catocli query networkConfig snmp siteSettingsList <json>

catocli query networkConfig snmp siteSettingsList --json-file query.networkConfig.snmp.siteSettingsList.json

catocli query networkConfig snmp siteSettingsList '{"networkConfigSnmpSiteSettingsListInput":{"filter":{"enabled":{"eq":true,"neq":true},"site":{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]}},"paging":{"from":1,"limit":1},"sort":{"site":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig snmp siteSettingsList '{
    "networkConfigSnmpSiteSettingsListInput": {
        "filter": {
            "enabled": {
                "eq": true,
                "neq": true
            },
            "site": {
                "eq": {
                    "by": "ID",
                    "input": "string"
                },
                "in": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "neq": {
                    "by": "ID",
                    "input": "string"
                },
                "nin": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "site": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.networkConfig.snmp.siteSettingsList ####

`accountId` [ID] - (required) ID of the account whose network configuration is requested.
`networkConfigSnmpSiteSettingsListInput` [NetworkConfigSnmpSiteSettingsListInput] - (required) N/A
