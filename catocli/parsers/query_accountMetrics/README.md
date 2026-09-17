
## CATO-CLI - query.accountMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountMetrics) for documentation on this operation.

### Usage for query.accountMetrics:

```bash
catocli query accountMetrics -h

catocli query accountMetrics <json>

catocli query accountMetrics --json-file query.accountMetrics.json

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

## Field Name Reference

### Valid values for labels
Valid values: `bytesDownstream`, `bytesDownstreamMax`, `bytesTotal`, `bytesUpstream`, `bytesUpstreamMax`, `health`, `jitterDownstream`, `jitterUpstream`, `lastMileLatency`, `lastMilePacketLoss`, `lostDownstream`, `lostDownstreamPcnt`, `lostUpstream`, `lostUpstreamPcnt`, `packetsDiscardedDownstream`, `packetsDiscardedDownstreamPcnt`, `packetsDiscardedUpstream`, `packetsDiscardedUpstreamPcnt`, `packetsDownstream`, `packetsUpstream`, `rtt`, `tunnelAge`



#### Operation Arguments for query.accountMetrics ####

