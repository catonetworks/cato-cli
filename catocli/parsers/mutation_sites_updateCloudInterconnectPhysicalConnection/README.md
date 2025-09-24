
## CATO-CLI - mutation.sites.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.updateCloudInterconnectPhysicalConnection:

`catocli mutation sites updateCloudInterconnectPhysicalConnection -h`

`catocli mutation sites updateCloudInterconnectPhysicalConnection <json>`

`catocli mutation sites updateCloudInterconnectPhysicalConnection "$(cat < mutation.sites.updateCloudInterconnectPhysicalConnection.json)"`

`catocli mutation sites updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput":{"downstreamBwLimit":"example_value","encapsulationMethod":"DOT1Q","id":"id","popLocationRefInput":{"by":"ID","input":"string"},"privateCatoIp":"example_value","privateSiteIp":"example_value","serviceProviderName":"string","subnet":"example_value","upstreamBwLimit":"example_value"}}'`

`catocli mutation sites updateCloudInterconnectPhysicalConnection -p '{
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


#### Operation Arguments for mutation.sites.updateCloudInterconnectPhysicalConnection ####

`accountId` [ID] - (required) N/A    
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A    
