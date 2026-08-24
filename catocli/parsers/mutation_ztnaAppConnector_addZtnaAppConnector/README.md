
## CATO-CLI - mutation.ztnaAppConnector.addZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.addZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.addZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector addZtnaAppConnector -h

catocli mutation ztnaAppConnector addZtnaAppConnector <json>

catocli mutation ztnaAppConnector addZtnaAppConnector --json-file mutation.ztnaAppConnector.addZtnaAppConnector.json

catocli mutation ztnaAppConnector addZtnaAppConnector '{"addZtnaAppConnectorInput":{"description":"string","groupName":"string","name":"string","type":"VIRTUAL","ztnaAppConnectorLocationInput":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"example_value"},"ztnaAppConnectorPreferredPopLocationInput":{"automatic":true,"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}}}}'

catocli mutation ztnaAppConnector addZtnaAppConnector '{
    "addZtnaAppConnectorInput": {
        "description": "string",
        "groupName": "string",
        "name": "string",
        "type": "VIRTUAL",
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

#### Operation Arguments for mutation.ztnaAppConnector.addZtnaAppConnector ####

`accountId` [ID] - (required) N/A    
`addZtnaAppConnectorInput` [AddZtnaAppConnectorInput] - (required) N/A    
