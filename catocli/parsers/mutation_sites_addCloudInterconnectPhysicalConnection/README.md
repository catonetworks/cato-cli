
## CATO-CLI - mutation.sites.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectPhysicalConnection:

`catocli mutation sites addCloudInterconnectPhysicalConnection -h`

`catocli mutation sites addCloudInterconnectPhysicalConnection <json>`

`catocli mutation sites addCloudInterconnectPhysicalConnection "$(cat < addCloudInterconnectPhysicalConnection.json)"`

`catocli mutation sites addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput": {"downstreamBwLimit": {"downstreamBwLimit": "NetworkBandwidth"}, "encapsulationMethod": {"encapsulationMethod": "enum(TaggingMethod)"}, "haRole": {"haRole": "enum(HaRole)"}, "popLocationRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "serviceProviderName": {"serviceProviderName": "String"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": "NetworkSubnet"}, "upstreamBwLimit": {"upstreamBwLimit": "NetworkBandwidth"}}}'`

#### Operation Arguments for mutation.sites.addCloudInterconnectPhysicalConnection ####
`accountId` [ID] - (required) N/A 
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A 
