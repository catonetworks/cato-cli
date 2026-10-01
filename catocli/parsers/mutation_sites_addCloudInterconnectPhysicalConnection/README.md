
## CATO-CLI - mutation.sites.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectPhysicalConnection:

```bash
catocli mutation sites addCloudInterconnectPhysicalConnection -h

catocli mutation sites addCloudInterconnectPhysicalConnection <json>

catocli mutation sites addCloudInterconnectPhysicalConnection --json-file mutation.sites.addCloudInterconnectPhysicalConnection.json

catocli mutation sites addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":100,"sVlan":100},"downstreamBwLimit":100,"encapsulationMethod":"DOT1Q","haRole":"PRIMARY","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"192.0.2.1","privateSiteIp":"192.0.2.1","serviceProviderName":"string","site":{"by":"ID","input":"string"},"subnet":"192.0.2.0/24","upstreamBwLimit":100,"vlan":100}}'

catocli mutation sites addCloudInterconnectPhysicalConnection '{
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

#### Operation Arguments for mutation.sites.addCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A
