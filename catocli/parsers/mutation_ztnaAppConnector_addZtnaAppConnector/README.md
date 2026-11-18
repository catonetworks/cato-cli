
## CATO-CLI - mutation.ztnaAppConnector.addZtnaAppConnector:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.ztnaAppConnector.addZtnaAppConnector) for documentation on this operation.

### Usage for mutation.ztnaAppConnector.addZtnaAppConnector:

```bash
catocli mutation ztnaAppConnector addZtnaAppConnector -h

catocli mutation ztnaAppConnector addZtnaAppConnector <json>

catocli mutation ztnaAppConnector addZtnaAppConnector --json-file mutation.ztnaAppConnector.addZtnaAppConnector.json

catocli mutation ztnaAppConnector addZtnaAppConnector '{"addZtnaAppConnectorInput":{"description":"string","groupName":"string","lanInterface":{"ipAssignment":"DHCP","staticAddress":{"gateway":"192.0.2.1","localIp":"192.0.2.1","primaryDnsServer":"192.0.2.1","secondaryDnsServer":"192.0.2.1","subnet":"192.0.2.0/24"}},"location":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"America/New_York"},"name":"string","pooledBandwidthAllocation":[{"bw":1,"licenseId":"id"}],"preferredPopLocation":{"automatic":true,"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}},"type":"VIRTUAL"}}'

catocli mutation ztnaAppConnector addZtnaAppConnector '{
    "addZtnaAppConnectorInput": {
        "description": "string",
        "groupName": "string",
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
        "pooledBandwidthAllocation": [
            {
                "bw": 1,
                "licenseId": "id"
            }
        ],
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
