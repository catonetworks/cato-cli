
## CATO-CLI - mutation.site.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.updateCloudInterconnectPhysicalConnection:

```bash
catocli mutation site updateCloudInterconnectPhysicalConnection -h

catocli mutation site updateCloudInterconnectPhysicalConnection <json>

catocli mutation site updateCloudInterconnectPhysicalConnection --json-file mutation.site.updateCloudInterconnectPhysicalConnection.json

catocli mutation site updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":100,"sVlan":100},"downstreamBwLimit":100,"encapsulationMethod":"DOT1Q","id":"id","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","serviceProviderName":"string","subnet":"192.0.2.0/24","upstreamBwLimit":100,"vlan":100}}'

catocli mutation site updateCloudInterconnectPhysicalConnection '{
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

#### Operation Arguments for mutation.site.updateCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A
