
## CATO-CLI - query.container:
[Click here](https://api.catonetworks.com/documentation/#query-container) for documentation on this operation.

### Usage for query.container:

`catocli query container -h`

`catocli query container <json>`

`catocli query container "$(cat < container.json)"`

`catocli query container '{"ContainerSearchInput": {"ContainerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "types": {"types": "enum(ContainerType)"}}, "DownloadFqdnContainerFileInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "DownloadIpAddressRangeContainerFileInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "FqdnContainerSearchFqdnInput": {"fqdn": {"fqdn": "Fqdn"}}, "FqdnContainerSearchInput": {"ContainerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "IpAddressRangeContainerSearchInput": {"ContainerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "IpAddressRangeContainerSearchIpAddressRangeInput": {"IpAddressRangeInput": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}}}'`

#### Operation Arguments for query.container ####
`ContainerSearchInput` [ContainerSearchInput] - (required) N/A 
`DownloadFqdnContainerFileInput` [DownloadFqdnContainerFileInput] - (required) N/A 
`DownloadIpAddressRangeContainerFileInput` [DownloadIpAddressRangeContainerFileInput] - (required) N/A 
`FqdnContainerSearchFqdnInput` [FqdnContainerSearchFqdnInput] - (required) N/A 
`FqdnContainerSearchInput` [FqdnContainerSearchInput] - (required) N/A 
`IpAddressRangeContainerSearchInput` [IpAddressRangeContainerSearchInput] - (required) N/A 
`IpAddressRangeContainerSearchIpAddressRangeInput` [IpAddressRangeContainerSearchIpAddressRangeInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
