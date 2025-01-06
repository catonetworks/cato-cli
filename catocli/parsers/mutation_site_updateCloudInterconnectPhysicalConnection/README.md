
## CATO-CLI - mutation.site.updateCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.updateCloudInterconnectPhysicalConnection:

`catocli mutation site updateCloudInterconnectPhysicalConnection -h`

`catocli mutation site updateCloudInterconnectPhysicalConnection <json>`

`catocli mutation site updateCloudInterconnectPhysicalConnection "$(cat < updateCloudInterconnectPhysicalConnection.json)"`

`catocli mutation site updateCloudInterconnectPhysicalConnection '{"updateCloudInterconnectPhysicalConnectionInput": {"downstreamBwLimit": {"downstreamBwLimit": "NetworkBandwidth"}, "encapsulationMethod": {"encapsulationMethod": "enum(TaggingMethod)"}, "id": {"id": "ID"}, "popLocationRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "serviceProviderName": {"serviceProviderName": "String"}, "subnet": {"subnet": "NetworkSubnet"}, "upstreamBwLimit": {"upstreamBwLimit": "NetworkBandwidth"}}}'`

#### Operation Arguments for mutation.site.updateCloudInterconnectPhysicalConnection ####
`accountId` [ID] - (required) N/A 
`updateCloudInterconnectPhysicalConnectionInput` [UpdateCloudInterconnectPhysicalConnectionInput] - (required) N/A 
