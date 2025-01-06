
## CATO-CLI - mutation.sites.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.updateCloudInterconnectPhysicalConnection:

`catocli mutation sites updateCloudInterconnectPhysicalConnection -h`

`catocli mutation sites updateCloudInterconnectPhysicalConnection <json>`

`catocli mutation sites updateCloudInterconnectPhysicalConnection "$(cat < updateCloudInterconnectPhysicalConnection.json)"`

`catocli mutation sites updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput": {"downstreamBwLimit": {"downstreamBwLimit": "NetworkBandwidth"}, "encapsulationMethod": {"encapsulationMethod": "enum(TaggingMethod)"}, "id": {"id": "ID"}, "popLocationRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "serviceProviderName": {"serviceProviderName": "String"}, "subnet": {"subnet": "NetworkSubnet"}, "upstreamBwLimit": {"upstreamBwLimit": "NetworkBandwidth"}}}'`

#### Operation Arguments for mutation.sites.updateCloudInterconnectPhysicalConnection ####
`accountId` [ID] - (required) N/A 
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A 
