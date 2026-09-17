
## CATO-CLI - mutation.sites.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.updateCloudInterconnectPhysicalConnection:

```bash
catocli mutation sites updateCloudInterconnectPhysicalConnection -h

catocli mutation sites updateCloudInterconnectPhysicalConnection <json>

catocli mutation sites updateCloudInterconnectPhysicalConnection --json-file mutation.sites.updateCloudInterconnectPhysicalConnection.json

catocli mutation sites updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput":{"QinQVlanConfiguration":{"cVlan":"example_value","sVlan":"example_value"},"downstreamBwLimit":"example_value","encapsulationMethod":"DOT1Q","id":"id","popLocation":{"by":"ID","input":"string"},"privateCatoIp":"example_value","privateSiteIp":"example_value","serviceProviderName":"string","subnet":"example_value","upstreamBwLimit":"example_value","vlan":"example_value"}}'

catocli mutation sites updateCloudInterconnectPhysicalConnection '{
    "updateCloudInterconnectPhysicalConnectionInput": {
        "QinQVlanConfiguration": {
            "cVlan": "example_value",
            "sVlan": "example_value"
        },
        "downstreamBwLimit": "example_value",
        "encapsulationMethod": "DOT1Q",
        "id": "id",
        "popLocation": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "example_value",
        "privateSiteIp": "example_value",
        "serviceProviderName": "string",
        "subnet": "example_value",
        "upstreamBwLimit": "example_value",
        "vlan": "example_value"
    }
}'
```

#### Operation Arguments for mutation.sites.updateCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A    
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A    
