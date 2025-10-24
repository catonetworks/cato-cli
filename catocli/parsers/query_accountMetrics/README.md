
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

```bash
catocli query accountMetrics -h

catocli query accountMetrics <json>

catocli query accountMetrics "$(cat < query.accountMetrics.json)"

catocli query accountMetrics '{"buckets":1,"groupDevices":true,"groupInterfaces":true,"labels":"bytesUpstream","perSecond":true,"siteIDs":["id1","id2"],"timeFrame":"example_value","toRate":true,"types":["string1","string2"],"useDefaultSizeBucket":true,"userIDs":["id1","id2"],"withMissingData":true}'

catocli query accountMetrics '{
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
}'
```

## Advanced Usage
### Additional Examples
- Example all values and lables
- Example all values and lables for a single account
- Monitor all key performance indicators for a specific site:
- Analyze network performance for specific users:
- Get a simple health snapshot without filters:
- Focus on bandwidth utilization with packet loss metrics
- Last hour no filters

# Example all values and lables

```bash
# Example all values and lables for a single account
catocli query accountMetrics '{
    "buckets": 24,
    "groupDevices": true,
    "groupInterfaces": true,
    "labels": [
        "bytesDownstream",
        "bytesDownstreamMax",
        "bytesTotal",
        "bytesUpstream",
        "bytesUpstreamMax",
        "health",
        "jitterDownstream",
        "jitterUpstream",
        "lastMileLatency",
        "lastMilePacketLoss",
        "lostDownstream",
        "lostDownstreamPcnt",
        "lostUpstream",
        "lostUpstreamPcnt",
        "packetsDiscardedDownstream",
        "packetsDiscardedDownstreamPcnt",
        "packetsDiscardedUpstream",
        "packetsDiscardedUpstreamPcnt",
        "packetsDownstream",
        "packetsUpstream",
        "rtt",
        "tunnelAge"
    ],
    "perSecond": true,
    "siteIDs": [
        "132814"
    ],
    "timeFrame": "last.P1D",
    "toRate": true,
    "useDefaultSizeBucket": true,
    "withMissingData": true
}' 
```

# Monitor all key performance indicators for a specific site:

```bash
# Monitor all key performance indicators for a specific site:
catocli query accountMetrics '{
    "buckets": 24,
    "groupDevices": true,
    "groupInterfaces": true,
    "labels": [
        "bytesDownstream",
        "bytesUpstream",
        "health",
        "lastMileLatency",
        "lastMilePacketLoss",
        "rtt"
    ],
    "siteIDs": ["132814"],
    "timeFrame": "last.P1D",
    "perSecond": true,
    "toRate": true
}' -f csv --csv-filename=accountmetrics_site.csv
```

# Analyze network performance for specific users:

```bash
# Analyze network performance for specific users:
catocli query accountMetrics '{
    "buckets": 24,
    "labels": [
        "health",
        "jitterDownstream", 
        "jitterUpstream",
        "lastMileLatency",
        "lastMilePacketLoss",
        "packetsDownstream",
        "packetsUpstream"
    ],
    "timeFrame": "last.P1D",
    "userIDs": ["1000000"]
}' -f csv --csv-filename=accountmetrics_user.csv
```

# Get a simple health snapshot without filters:

```bash
# Get a simple health snapshot without filters:
catocli query accountMetrics '{
    "timeFrame": "last.PT1H"
}' -f csv --csv-filename=accountmetrics_health.csv
```

# Focus on bandwidth utilization with packet loss metrics

```bash
# Focus on bandwidth utilization with packet loss metrics
catocli query accountMetrics '{
    "buckets": 48,
    "labels": [
        "bytesDownstream",
        "bytesUpstream", 
        "bytesTotal",
        "bytesDownstreamMax",
        "bytesUpstreamMax",
        "lostDownstreamPcnt",
        "lostUpstreamPcnt"
    ],
    "siteIDs": ["132814"],
    "timeFrame": "last.P2D",
    "perSecond": true,
    "withMissingData": true
}' -f csv --csv-filename=accountmetrics_packet_loss.csv
```

# Last hour no filters

```bash
# Last hour no filters
catocli query accountMetrics '{ 
    "timeFrame":"last.PT1H"
}'
```



#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- "last.PT5M" = Previous 5 minutes
- "last.PT1H" = Previous 1 hour  
- "last.P1D" = Previous 1 day
- "last.P14D" = Previous 14 days
- "last.P1M" = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: "utc.2023-02-{28/00:00:00--28/23:59:59}"  
- Multiple days: "utc.2023-02-{25/00:00:00--28/23:59:59}"  
- Specific hours: "utc.2023-02-{28/09:00:00--28/17:00:00}"
- Across months: "utc.2023-{01-28/00:00:00--02-03/23:59:59}"


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
