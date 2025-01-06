
## CATO-CLI - mutation.site.addCloudInterconnectPhysicalConnection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addCloudInterconnectPhysicalConnection) for documentation on this operation.

### Usage for mutation.site.addCloudInterconnectPhysicalConnection:

`catocli mutation site addCloudInterconnectPhysicalConnection -h`

`catocli mutation site addCloudInterconnectPhysicalConnection <json>`

`catocli mutation site addCloudInterconnectPhysicalConnection "$(cat < addCloudInterconnectPhysicalConnection.json)"`

`catocli mutation site addCloudInterconnectPhysicalConnection '{"addCloudInterconnectPhysicalConnectionInput": {"downstreamBwLimit": {"downstreamBwLimit": "NetworkBandwidth"}, "encapsulationMethod": {"encapsulationMethod": "enum(TaggingMethod)"}, "haRole": {"haRole": "enum(HaRole)"}, "popLocationRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "serviceProviderName": {"serviceProviderName": "String"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": "NetworkSubnet"}, "upstreamBwLimit": {"upstreamBwLimit": "NetworkBandwidth"}}}'`

#### Operation Arguments for mutation.site.addCloudInterconnectPhysicalConnection ####
`accountId` [ID] - (required) N/A 
`addCloudInterconnectPhysicalConnectionInput` [AddCloudInterconnectPhysicalConnectionInput] - (required) N/A 
