
## CATO-CLI - mutation.ztnaAppConnector.upgradeZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.upgradeZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.upgradeZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector upgradeZtnaAppConnector -h

catocli mutation ztnaAppConnector upgradeZtnaAppConnector <json>

catocli mutation ztnaAppConnector upgradeZtnaAppConnector --json-file mutation.ztnaAppConnector.upgradeZtnaAppConnector.json

catocli mutation ztnaAppConnector upgradeZtnaAppConnector '{"upgradeZtnaAppConnectorInput":{"ztnaAppConnectorUpgradeRequest":{"targetVersion":"string","ztnaAppConnector":{"by":"ID","input":"string"}}}}'

catocli mutation ztnaAppConnector upgradeZtnaAppConnector '{
    "upgradeZtnaAppConnectorInput": {
        "ztnaAppConnectorUpgradeRequest": {
            "targetVersion": "string",
            "ztnaAppConnector": {
                "by": "ID",
                "input": "string"
            }
        }
    }
}'
```

#### Operation Arguments for mutation.ztnaAppConnector.upgradeZtnaAppConnector ####

`accountId` [ID] - (required) N/A    
`upgradeZtnaAppConnectorInput` [UpgradeZtnaAppConnectorInput] - (required) N/A    
