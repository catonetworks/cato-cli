
## CATO-CLI - mutation.site.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.updateCloudInterconnectPhysicalConnection:

`catocli mutation site updateCloudInterconnectPhysicalConnection -h`

`catocli mutation site updateCloudInterconnectPhysicalConnection <json>`

`catocli mutation site updateCloudInterconnectPhysicalConnection "$(cat < mutation.site.updateCloudInterconnectPhysicalConnection.json)"`

`catocli mutation site updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput":{"downstreamBwLimit":"example_value","encapsulationMethod":"DOT1Q","id":"id","popLocationRefInput":{"by":"ID","input":"string"},"privateCatoIp":"example_value","privateSiteIp":"example_value","serviceProviderName":"string","subnet":"example_value","upstreamBwLimit":"example_value"}}'`

`catocli mutation site updateCloudInterconnectPhysicalConnection -p '{
    "updateCloudInterconnectPhysicalConnectionInput": {
        "downstreamBwLimit": "example_value",
        "encapsulationMethod": "DOT1Q",
        "id": "id",
        "popLocationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "privateCatoIp": "example_value",
        "privateSiteIp": "example_value",
        "serviceProviderName": "string",
        "subnet": "example_value",
        "upstreamBwLimit": "example_value"
    }
}'`


#### Operation Arguments for mutation.site.updateCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A    
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A    
