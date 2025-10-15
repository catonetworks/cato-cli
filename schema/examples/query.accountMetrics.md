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

# Example all values and lables for a single user

```bash
# Example all values and lables for a single user
catocli query accountMetrics '{
    "buckets": 24,
    "labels": [
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
        "packetsUpstream"
    ],
    "timeFrame": "last.PT1H",
    "userIDs": [
        "0"
    ]
}'
```

# Last hour no filters

```bash
# Last hour no filters
catocli query accountMetrics '{ 
    "timeFrame":"last.PT1H"
}'
```