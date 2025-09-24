
## CATO-CLI - mutation.site.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.addCloudInterconnectPhysicalConnection:

`catocli mutation site addCloudInterconnectPhysicalConnection -h`

`catocli mutation site addCloudInterconnectPhysicalConnection <json>`

`catocli mutation site addCloudInterconnectPhysicalConnection "$(cat < mutation.site.addCloudInterconnectPhysicalConnection.json)"`

`catocli mutation site addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput":{"downstreamBwLimit":"example_value","encapsulationMethod":"DOT1Q","haRole":"PRIMARY","popLocationRefInput":{"by":"ID","input":"string"},"privateCatoIp":"example_value","privateSiteIp":"example_value","serviceProviderName":"string","siteRefInput":{"by":"ID","input":"string"},"subnet":"example_value","upstreamBwLimit":"example_value"}}'`

`catocli mutation site addCloudInterconnectPhysicalConnection -p '{
    "addCloudInterconnectPhysicalConnectionInput": {
        "downstreamBwLimit": "example_value",
        "encapsulationMethod": "DOT1Q",
        "haRole": "PRIMARY",
        "popLocationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "example_value",
        "privateSiteIp": "example_value",
        "serviceProviderName": "string",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "example_value",
        "upstreamBwLimit": "example_value"
    }
}'`


#### Operation Arguments for mutation.site.addCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A    
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A    
