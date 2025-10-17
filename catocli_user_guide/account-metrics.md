# Account Metrics Query Guide

The `accountMetrics` query provides comprehensive network performance metrics for your Cato Networks environment, including bandwidth utilization, latency, packet loss, and health scores.

## Overview

Account metrics help you monitor and analyze:
- **Network Performance**: Bandwidth usage, throughput, and traffic patterns
- **Connection Quality**: Latency, jitter, packet loss, and health scores
- **Interface Statistics**: Per-device and per-interface metrics
- **User Activity**: Per-user network performance and usage

## Basic Usage

```bash
catocli query accountMetrics '{"timeFrame":"last.PT1H"}'
```

## Query Structure

```json
{
  "buckets": 24,                    // Number of time buckets for aggregation
  "groupDevices": true,             // Group metrics by device
  "groupInterfaces": true,          // Group metrics by interface
  "labels": ["label1", "label2"],   // Specific metrics to retrieve
  "perSecond": true,                // Convert to per-second rates
  "siteIDs": ["132814"],           // Filter by specific sites
  "userIDs": ["0"],                // Filter by specific users
  "timeFrame": "last.P1D",         // Time range for the query
  "toRate": true,                   // Convert cumulative values to rates
  "useDefaultSizeBucket": true,     // Use default time bucket sizing
  "withMissingData": true           // Include periods with no data
}
```

## Available Metrics (Labels)

### Bandwidth Metrics
- `bytesDownstream` - Downstream bytes
- `bytesUpstream` - Upstream bytes  
- `bytesTotal` - Total bytes
- `bytesDownstreamMax` - Peak downstream bytes
- `bytesUpstreamMax` - Peak upstream bytes

### Packet Metrics
- `packetsDownstream` - Downstream packets
- `packetsUpstream` - Upstream packets
- `packetsDiscardedDownstream` - Discarded downstream packets
- `packetsDiscardedUpstream` - Discarded upstream packets
- `packetsDiscardedDownstreamPcnt` - Downstream discard percentage
- `packetsDiscardedUpstreamPcnt` - Upstream discard percentage

### Quality Metrics
- `health` - Overall connection health score
- `jitterDownstream` - Downstream jitter
- `jitterUpstream` - Upstream jitter
- `lastMileLatency` - Last mile latency
- `lastMilePacketLoss` - Last mile packet loss percentage
- `rtt` - Round-trip time

### Loss Metrics
- `lostDownstream` - Lost downstream packets
- `lostUpstream` - Lost upstream packets
- `lostDownstreamPcnt` - Downstream loss percentage
- `lostUpstreamPcnt` - Upstream loss percentage

### Connection Metrics
- `tunnelAge` - Tunnel connection age

## Common Use Cases

### 1. Comprehensive Site Health Check

Monitor all key performance indicators for a specific site:

```bash
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
}'
```

### 2. User Performance Analysis

Analyze network performance for specific users:

```bash
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
    "timeFrame": "last.PT1H",
    "userIDs": ["0"]
}'
```

### 3. Quick Health Overview

Get a simple health snapshot without filters:

```bash
catocli query accountMetrics '{
    "timeFrame": "last.PT1H"
}'
```

### 4. Detailed Bandwidth Analysis

Focus on bandwidth utilization with packet loss metrics:

```bash
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
}'
```

## Time Frame Options

### Relative Time Frames
- `last.PT1H` - Last 1 hour
- `last.PT6H` - Last 6 hours  
- `last.P1D` - Last 1 day
- `last.P7D` - Last 7 days
- `last.P1M` - Last 1 month

### Absolute Time Frames
```bash
# Specific UTC date range
"timeFrame": "utc.2023-10-{15/00:00:00--15/23:59:59}"
```

## Bucket Configuration

The `buckets` parameter determines how your time frame is divided:

- **24 buckets over 1 day** = 1-hour intervals
- **48 buckets over 2 days** = 1-hour intervals  
- **168 buckets over 7 days** = 1-hour intervals
- **720 buckets over 30 days** = 1-hour intervals

### 5. Performance Metrics for Specific Sites (Custom Timeframe)

Analyze performance for multiple sites within a specific date range:

```bash
catocli query accountMetrics '{
    "timeFrame": "utc.2023-02-{28/00:00:00--28/23:59:59}",
    "siteIDs": ["456", "789"]
}'
```

### 6. High Availability Site Analysis (Last Day)

Monitor site health without device grouping for simplified analysis:

```bash
catocli query accountMetrics '{
    "timeFrame": "last.P1D",
    "groupDevices": false
}'
```

## Output Options

### Default JSON Output
```bash
catocli query accountMetrics '{...}'
```

### Raw API Response
```bash
catocli query accountMetrics '{...}' -raw
```

### CSV Export
```bash
catocli query accountMetrics '{...}' -f csv --csv-filename site_performance_report.csv
```

## Filtering Best Practices

### Site-Specific Analysis
```json
{
  "siteIDs": ["site1", "site2"],
  "groupDevices": true,
  "groupInterfaces": true
}
```

### User-Specific Analysis  
```json
{
  "userIDs": ["user1", "user2"],
  "labels": ["health", "lastMileLatency", "packetsDownstream"]
}
```

### Performance Optimization
```json
{
  "useDefaultSizeBucket": true,
  "perSecond": true,
  "toRate": true,
  "withMissingData": false
}
```

## Troubleshooting Common Issues

### High Latency Detection
```bash
# Focus on latency and jitter metrics
catocli query accountMetrics '{
    "labels": ["lastMileLatency", "rtt", "jitterDownstream", "jitterUpstream"],
    "timeFrame": "last.PT6H",
    "buckets": 24
}'
```

### Packet Loss Analysis
```bash
# Monitor packet loss percentages
catocli query accountMetrics '{
    "labels": ["lostDownstreamPcnt", "lostUpstreamPcnt", "packetsDiscardedDownstreamPcnt"],
    "timeFrame": "last.P1D",
    "withMissingData": true
}'
```

### Bandwidth Utilization
```bash
# Peak usage analysis
catocli query accountMetrics '{
    "labels": ["bytesDownstreamMax", "bytesUpstreamMax", "bytesTotal"],
    "timeFrame": "last.P7D",
    "buckets": 168,
    "perSecond": true
}'
```

## Integration Examples

### Automated Monitoring Script
```bash
#!/bin/bash
# Daily health check report
catocli query accountMetrics '{
    "labels": ["health", "lastMileLatency", "lostDownstreamPcnt"],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "daily_health_$(date +%Y%m%d).csv" --append-timestamp
```

### Performance Baseline Collection
```bash
# Weekly performance baseline
catocli query accountMetrics '{
    "buckets": 168,
    "labels": ["bytesDownstream", "bytesUpstream", "health", "rtt"],
    "timeFrame": "last.P7D",
    "groupDevices": true
}' -f csv --csv-filename weekly_baseline.csv
```

## Related Operations

- [Application Statistics](./app-stats.md) - For user and application activity
- [Events Time Series](./events-timeseries.md) - For security and connectivity events
- [Socket Port Metrics](./socket-port-metrics.md) - For interface-specific metrics

## API Reference

For complete field descriptions and additional parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-accountMetrics).