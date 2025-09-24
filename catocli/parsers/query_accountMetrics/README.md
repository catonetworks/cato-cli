
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

`catocli query accountMetrics -h`

`catocli query accountMetrics <json>`

`catocli query accountMetrics "$(cat < query.accountMetrics.json)"`

`catocli query accountMetrics '{"buckets":1,"groupDevices":true,"groupInterfaces":true,"labels":"bytesUpstream","perSecond":true,"siteIDs":["id1","id2"],"timeFrame":"example_value","toRate":true,"types":["string1","string2"],"useDefaultSizeBucket":true,"userIDs":["id1","id2"],"withMissingData":true}'`

`catocli query accountMetrics -p '{
    "buckets": 1,
    "groupDevices": true,
    "groupInterfaces": true,
    "labels": "bytesUpstream",
    "perSecond": true,
    "siteIDs": [
        "id1",
        "id2"
    ],
    "timeFrame": "example_value",
    "toRate": true,
    "types": [
        "string1",
        "string2"
    ],
    "useDefaultSizeBucket": true,
    "userIDs": [
        "id1",
        "id2"
    ],
    "withMissingData": true
}'`


#### Operation Arguments for query.accountMetrics ####

`accountID` [ID] - (required) Unique Identifier of Account.    
`buckets` [Int] - (required) number of buckets, defaults to 10, max 1000    
`groupDevices` [Boolean] - (required) When the boolean argument groupDevices is set to __true__, then the analytics for all the
Sockets (usually two in high availability) are aggregated as one result.

For the best results for aggregated Sockets, we recommend that there is consistent
names and functionality (for example Destination) for the links on both Sockets.    
`groupInterfaces` [Boolean] - (required) When the boolean argument groupInterfaces is set to __true__, then the data for all the
interfaces are aggregated to a single interface.    
`labels` [TimeseriesMetricType[]] - (required) N/A Default Value: ['bytesUpstream', 'bytesDownstream', 'bytesUpstreamMax', 'bytesDownstreamMax', 'packetsUpstream', 'packetsDownstream', 'lostUpstream', 'lostDownstream', 'lostUpstreamPcnt', 'lostDownstreamPcnt', 'packetsDiscardedDownstream', 'packetsDiscardedUpstream', 'packetsDiscardedUpstreamPcnt', 'packetsDiscardedDownstreamPcnt', 'jitterUpstream', 'jitterDownstream', 'bytesTotal', 'rtt', 'health', 'tunnelAge', 'lastMilePacketLoss', 'lastMileLatency']   
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`siteIDs` [ID[]] - (required) A list of unique IDs for each site. If specified, only sites in this list are returned. Otherwise, all sites are returned.    
`timeFrame` [TimeFrame] - (required) The time frame for the data that the query returns. The argument is in the format type.time value. This argument is mandatory.    
`toRate` [Boolean] - (required) Normalize collected metrics as per-second values    
`types` [String[]] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`userIDs` [ID[]] - (required) A list of unique IDs for each user. If specified, only users in this list are returned. Otherwise, no user metrics are returned.    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
