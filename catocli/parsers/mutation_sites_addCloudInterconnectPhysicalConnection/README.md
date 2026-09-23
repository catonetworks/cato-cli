
## CATO-CLI - mutation.sites.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectPhysicalConnection:

```bash
catocli mutation sites addCloudInterconnectPhysicalConnection -h

catocli mutation sites addCloudInterconnectPhysicalConnection <json>

catocli mutation sites addCloudInterconnectPhysicalConnection --json-file mutation.sites.addCloudInterconnectPhysicalConnection.json

catocli mutation sites addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":"example_value","sVlan":"example_value"},"downstreamBwLimit":"example_value","encapsulationMethod":"DOT1Q","haRole":"PRIMARY","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"example_value","privateSiteIp":"example_value","serviceProviderName":"string","site":{"by":"ID","input":"string"},"subnet":"example_value","upstreamBwLimit":"example_value","vlan":"example_value"}}'

catocli mutation sites addCloudInterconnectPhysicalConnection '{
    "addCloudInterconnectPhysicalConnectionInput": {
        "QinQVlanConfiguration": {
            "cVlan": "example_value",
            "sVlan": "example_value"
        },
        "downstreamBwLimit": "example_value",
        "encapsulationMethod": "DOT1Q",
        "haRole": "PRIMARY",
        "popLocation": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "example_value",
        "privateSiteIp": "example_value",
        "serviceProviderName": "string",
        "site": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "example_value",
        "upstreamBwLimit": "example_value",
        "vlan": "example_value"
    }
}'
```

#### Operation Arguments for mutation.sites.addCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A    
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A    
