
## CATO-CLI - mutation.sites.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.updateCloudInterconnectPhysicalConnection:

```bash
catocli mutation sites updateCloudInterconnectPhysicalConnection -h

catocli mutation sites updateCloudInterconnectPhysicalConnection <json>

catocli mutation sites updateCloudInterconnectPhysicalConnection --json-file mutation.sites.updateCloudInterconnectPhysicalConnection.json

catocli mutation sites updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":100,"sVlan":100},"downstreamBwLimit":100,"encapsulationMethod":"DOT1Q","id":"id","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","serviceProviderName":"string","subnet":"192.0.2.0/24","upstreamBwLimit":100,"vlan":100}}'

catocli mutation sites updateCloudInterconnectPhysicalConnection '{
    "updateCloudInterconnectPhysicalConnectionInput": {
        "QinQVlanConfiguration": {
            "cVlan": 100,
            "sVlan": 100
        },
        "downstreamBwLimit": 100,
        "encapsulationMethod": "DOT1Q",
        "id": "id",
        "popLocation": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "192.0.2.1",
        "privateSiteIp": "192.0.2.1",
        "serviceProviderName": "string",
        "subnet": "192.0.2.0/24",
        "upstreamBwLimit": 100,
        "vlan": 100
    }
}'
```

#### Operation Arguments for mutation.sites.updateCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A
