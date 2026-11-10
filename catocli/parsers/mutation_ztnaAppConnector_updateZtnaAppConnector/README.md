
## CATO-CLI - mutation.ztnaAppConnector.updateZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.updateZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.updateZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector updateZtnaAppConnector -h

catocli mutation ztnaAppConnector updateZtnaAppConnector <json>

catocli mutation ztnaAppConnector updateZtnaAppConnector --json-file mutation.ztnaAppConnector.updateZtnaAppConnector.json

catocli mutation ztnaAppConnector updateZtnaAppConnector '{"updateZtnaAppConnectorInput":{"description":"string","groupName":"string","id":"id","lanInterface":{"ipAssignment":"DHCP","staticAddress":{"gateway":"192.0.2.1","localIp":"192.0.2.1","primaryDnsServer":"192.0.2.1","secondaryDnsServer":"192.0.2.1","subnet":"192.0.2.0/24"}},"location":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"America/New_York"},"name":"string","preferredPopLocation":{"automatic":true,"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}}}}'

catocli mutation ztnaAppConnector updateZtnaAppConnector '{
    "updateZtnaAppConnectorInput": {
        "description": "string",
        "groupName": "string",
        "id": "id",
        "lanInterface": {
            "ipAssignment": "DHCP",
            "staticAddress": {
                "gateway": "192.0.2.1",
                "localIp": "192.0.2.1",
                "primaryDnsServer": "192.0.2.1",
                "secondaryDnsServer": "192.0.2.1",
                "subnet": "192.0.2.0/24"
            }
        },
        "location": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "America/New_York"
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
        }
    }
}'
```

#### Operation Arguments for mutation.ztnaAppConnector.updateZtnaAppConnector ####

`accountId` [ID] - (required) N/A
`updateZtnaAppConnectorInput` [UpdateZtnaAppConnectorInput] - (required) N/A
