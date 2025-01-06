
## CATO-CLI - query.site:
[Click here](https://api.catonetworks.com/documentation/#query-site) for documentation on this operation.

### Usage for query.site:

`catocli query site -h`

`catocli query site <json>`

`catocli query site "$(cat < site.json)"`

`catocli query site '{"bgpPeerListInput": {"siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "bgpPeerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "cloudInterconnectConnectionConnectivityInput": {"id": {"id": "ID"}}, "cloudInterconnectPhysicalConnectionIdInput": {"haRole": {"haRole": "enum(HaRole)"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "cloudInterconnectPhysicalConnectionInput": {"id": {"id": "ID"}}, "siteBgpStatusInput": {"siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for query.site ####
`accountId` [ID] - (required) N/A 
`bgpPeerListInput` [BgpPeerListInput] - (required) N/A 
`bgpPeerRefInput` [BgpPeerRefInput] - (required) N/A 
`cloudInterconnectConnectionConnectivityInput` [CloudInterconnectConnectionConnectivityInput] - (required) N/A 
`cloudInterconnectPhysicalConnectionIdInput` [CloudInterconnectPhysicalConnectionIdInput] - (required) N/A 
`cloudInterconnectPhysicalConnectionInput` [CloudInterconnectPhysicalConnectionInput] - (required) N/A 
`siteBgpStatusInput` [SiteBgpStatusInput] - (required) N/A 
