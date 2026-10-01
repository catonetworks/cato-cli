
## CATO-CLI - mutation.site.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.addCloudInterconnectPhysicalConnection:

```bash
catocli mutation site addCloudInterconnectPhysicalConnection -h

catocli mutation site addCloudInterconnectPhysicalConnection <json>

catocli mutation site addCloudInterconnectPhysicalConnection --json-file mutation.site.addCloudInterconnectPhysicalConnection.json

catocli mutation site addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":100,"sVlan":100},"downstreamBwLimit":100,"encapsulationMethod":"DOT1Q","haRole":"PRIMARY","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","serviceProviderName":"string","site":{"by":"ID","input":"string"},"subnet":"192.0.2.0/24","upstreamBwLimit":100,"vlan":100}}'

catocli mutation site addCloudInterconnectPhysicalConnection '{
    "addCloudInterconnectPhysicalConnectionInput": {
        "QinQVlanConfiguration": {
            "cVlan": 100,
            "sVlan": 100
        },
        "downstreamBwLimit": 100,
        "encapsulationMethod": "DOT1Q",
        "haRole": "PRIMARY",
        "popLocation": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "192.0.2.1",
        "privateSiteIp": "192.0.2.1",
        "serviceProviderName": "string",
        "site": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "192.0.2.0/24",
        "upstreamBwLimit": 100,
        "vlan": 100
    }
}'
```

#### Operation Arguments for mutation.site.addCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A
