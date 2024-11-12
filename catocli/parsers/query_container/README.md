
## CATO-CLI - query.container:
[Click here](https://api.catonetworks.com/documentation/#query-container) for documentation on this operation.

### Usage for query.container:

`catocli query container -h`

`catocli query container <json>`

`catocli query container "$(cat < container.json)"`

`catocli query container '{"containerSearchInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "types": {"types": "enum(ContainerType)"}}, "downloadFqdnContainerFileInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "downloadIpAddressRangeContainerFileInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "fqdnContainerSearchFqdnInput": {"fqdn": {"fqdn": "Fqdn"}}, "fqdnContainerSearchInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "ipAddressRangeContainerSearchInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "ipAddressRangeContainerSearchIpAddressRangeInput": {"ipAddressRangeInput": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}}}'`

#### Operation Arguments for query.container ####
`accountId` [ID] - (required) N/A 
`containerSearchInput` [ContainerSearchInput] - (required) N/A 
`downloadFqdnContainerFileInput` [DownloadFqdnContainerFileInput] - (required) N/A 
`downloadIpAddressRangeContainerFileInput` [DownloadIpAddressRangeContainerFileInput] - (required) N/A 
`fqdnContainerSearchFqdnInput` [FqdnContainerSearchFqdnInput] - (required) N/A 
`fqdnContainerSearchInput` [FqdnContainerSearchInput] - (required) N/A 
`ipAddressRangeContainerSearchInput` [IpAddressRangeContainerSearchInput] - (required) N/A 
`ipAddressRangeContainerSearchIpAddressRangeInput` [IpAddressRangeContainerSearchIpAddressRangeInput] - (required) N/A 
