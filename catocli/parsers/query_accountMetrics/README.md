
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

`catocli query accountMetrics -h`

`catocli query accountMetrics <json>`

`catocli query accountMetrics "$(cat < accountMetrics.json)"`

`catocli query accountMetrics '{"buckets": "Int", "groupDevices": "Boolean", "groupInterfaces": "Boolean", "labels": "enum(TimeseriesMetricType)", "perSecond": "Boolean", "siteIDs": ["ID"], "timeFrame": "TimeFrame", "toRate": "Boolean", "types": ["String"], "userIDs": ["ID"], "withMissingData": "Boolean"}'`

#### Operation Arguments for query.accountMetrics ####
`accountID` [ID] - (optional) Unique Identifier of Account. 
`buckets` [Int] - (optional) number of buckets, defaults to 10, max 1000 
`groupDevices` [Boolean] - (optional) When the boolean argument groupDevices is set to __true__, then the analytics for all the
Sockets (usually two in high availability) are aggregated as one result.

For the best results for aggregated Sockets, we recommend that there is consistent
names and functionality (for example Destination) for the links on both Sockets. 
`groupInterfaces` [Boolean] - (optional) When the boolean argument groupInterfaces is set to __true__, then the data for all the
interfaces are aggregated to a single interface. 
`labels` [TimeseriesMetricType[]] - (optional) N/A Default Value: ['bytesUpstream', 'bytesDownstream', 'bytesUpstreamMax', 'bytesDownstreamMax', 'packetsUpstream', 'packetsDownstream', 'lostUpstream', 'lostDownstream', 'lostUpstreamPcnt', 'lostDownstreamPcnt', 'packetsDiscardedDownstream', 'packetsDiscardedUpstream', 'packetsDiscardedUpstreamPcnt', 'packetsDiscardedDownstreamPcnt', 'jitterUpstream', 'jitterDownstream', 'bytesTotal', 'rtt', 'health', 'tunnelAge', 'lastMilePacketLoss', 'lastMileLatency']
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`siteIDs` [ID[]] - (optional) A list of unique IDs for each site. If specified, only sites in this list are returned. Otherwise, all sites are returned. 
`timeFrame` [TimeFrame] - (required) The time frame for the data that the query returns. The argument is in the format type.time value. This argument is mandatory. 
`toRate` [Boolean] - (optional) Normalize collected metrics as per-second values 
`types` [String[]] - (optional) N/A 
`userIDs` [ID[]] - (optional) A list of unique IDs for each user. If specified, only users in this list are returned. Otherwise, no user metrics are returned. 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
