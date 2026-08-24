
## CATO-CLI - mutation.ztnaAppConnector.updateZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.updateZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.updateZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector updateZtnaAppConnector -h

catocli mutation ztnaAppConnector updateZtnaAppConnector <json>

catocli mutation ztnaAppConnector updateZtnaAppConnector --json-file mutation.ztnaAppConnector.updateZtnaAppConnector.json

catocli mutation ztnaAppConnector updateZtnaAppConnector '{"updateZtnaAppConnectorInput":{"description":"string","groupName":"string","id":"id","name":"string","ztnaAppConnectorLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"example_value"},"ztnaAppConnectorPreferredPopLocationInput":{"automatic":true,"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}}}}'

catocli mutation ztnaAppConnector updateZtnaAppConnector '{
    "updateZtnaAppConnectorInput": {
        "description": "string",
        "groupName": "string",
        "id": "id",
        "name": "string",
        "ztnaAppConnectorLocationInput": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "example_value"
        },
        "ztnaAppConnectorPreferredPopLocationInput": {
            "automatic": true,
            "preferredOnly": true,
            "primary": {
                "by": "ID",
                "input": "string"
            },
            "secondary": {
                "by": "ID",
                "input": "string"
            }
        }
    }
}'
```

#### Operation Arguments for mutation.ztnaAppConnector.updateZtnaAppConnector ####

`accountId` [ID] - (required) N/A    
`updateZtnaAppConnectorInput` [UpdateZtnaAppConnectorInput] - (required) N/A    
