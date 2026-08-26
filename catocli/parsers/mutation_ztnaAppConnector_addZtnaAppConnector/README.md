
## CATO-CLI - mutation.ztnaAppConnector.addZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.addZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.addZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector addZtnaAppConnector -h

catocli mutation ztnaAppConnector addZtnaAppConnector <json>

catocli mutation ztnaAppConnector addZtnaAppConnector --json-file mutation.ztnaAppConnector.addZtnaAppConnector.json

catocli mutation ztnaAppConnector addZtnaAppConnector '{"addZtnaAppConnectorInput":{"description":"string","groupName":"string","location":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"example_value"},"name":"string","preferredPopLocation":{"automatic":true,"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}},"type":"VIRTUAL"}}'

catocli mutation ztnaAppConnector addZtnaAppConnector '{
    "addZtnaAppConnectorInput": {
        "description": "string",
        "groupName": "string",
        "location": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "example_value"
        },
        "name": "string",
        "preferredPopLocation": {
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
        },
        "type": "VIRTUAL"
    }
}'
```

#### Operation Arguments for mutation.ztnaAppConnector.addZtnaAppConnector ####

`accountId` [ID] - (required) N/A    
`addZtnaAppConnectorInput` [AddZtnaAppConnectorInput] - (required) N/A    
