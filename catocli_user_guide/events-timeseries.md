# Events Time Series Query Guide

The `eventsTimeSeries` query provides time-based analysis of security events, connectivity issues, and network activities within your Cato Networks environment. This powerful tool enables you to track incidents over time, identify patterns, and perform forensic analysis.

## Overview

Events time series help you analyze:
- **Security Events**: Threat detection, firewall blocks, and security policy violations
- **Connectivity Events**: Connection status, socket connectivity, and network availability
- **Threat Analysis**: Risk assessment and threat scoring over time
- **Operational Events**: System status, configuration changes, and network health
- **Forensic Analysis**: Detailed event investigation and pattern identification
- **Trend Detection**: Event frequency patterns and anomaly identification

## Basic Usage

```bash
catocli query eventsTimeSeries '{
    "buckets": 24,
    "eventsMeasure": [{"aggType": "sum", "fieldName": "event_count"}],
    "timeFrame": "last.P1D"
}'
```

## Query Structure

```json
{
  "buckets": 24,                    // Number of time buckets to divide the timeFrame
  "eventsDimension": [              // Fields to group events by
    {"fieldName": "rule_name"}
  ],
  "eventsFilter": [                 // Filters to apply to events
    {
      "fieldName": "event_sub_type",
      "operator": "is",
      "values": ["Internet Firewall"]
    }
  ],
  "eventsMeasure": [                // Metrics to calculate
    {"aggType": "sum", "fieldName": "event_count"}
  ],
  "timeFrame": "last.P7D"          // Time range for analysis
}
```

## Available Dimensions

Group your results by these event fields:

### Security Dimensions
- `rule_name` - Security rule or policy name
- `event_type` - Type of event (Security, Connectivity, etc.)
- `event_sub_type` - Specific event subtype
- `threat_type` - Type of detected threat
- `threat_score` - Numerical threat score

### Network Dimensions
- `src_ip` - Source IP address
- `dst_ip` - Destination IP address
- `src_country` - Source country
- `dst_country` - Destination country
- `socket_interface` - Socket interface identifier
- `site_name` - Site name
- `site_id` - Site identifier

### User and Device Dimensions
- `user_name` - Username associated with event
- `device_name` - Device name
- `src_is_site_or_vpn` - Source type (Site, VPN)

### Protocol Dimensions
- `protocol` - Network protocol
- `port` - Port number
- `application_name` - Associated application

## Available Measures

### Count Measures
- `event_count` - Number of events
- `unique_sources` - Count of unique source IPs
- `unique_destinations` - Count of unique destination IPs

### Score Measures
- `threat_score` - Threat severity scores
- `risk_level` - Risk level assessments

### Duration Measures
- `session_duration` - Duration of sessions/connections
- `response_time` - Response times for events

## Aggregation Types

- `sum` - Total count or sum of values
- `avg` - Average value over the time period
- `count` - Count of event records
- `count_distinct` - Count of unique values
- `max` - Maximum value in the time period
- `min` - Minimum value in the time period

## Common Use Cases

### 1. Internet Firewall Events Analysis

Track firewall activity over time by rule:

```bash
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [
        {"fieldName": "rule_name"}
    ],
    "eventsFilter": [
        {
            "fieldName": "event_sub_type",
            "operator": "is",
            "values": ["Internet Firewall"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P7D"
}'
```

### 2. Site Connectivity Monitoring

Monitor site connectivity events and patterns:

```bash
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "src_is_site_or_vpn",
            "operator": "is",
            "values": ["Site"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P7D"
}'
```

### 3. High-Frequency Event Detection

Detect potential DDoS or throttling with high-resolution monitoring:

```bash
catocli query eventsTimeSeries '{
    "buckets": 12,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "src_is_site_or_vpn",
            "operator": "is", 
            "values": ["Site"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.PT1H"
}'
```

### 4. Security Events Analysis

Focus on security-related events with daily breakdown:

```bash
catocli query eventsTimeSeries '{
    "buckets": 24,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Security"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "utc.2023-02-{28/00:00:00--28/23:59:59}"
}'
```

### 5. Connectivity Events by Country

Analyze connectivity patterns by geographic location:

```bash
catocli query eventsTimeSeries '{
    "buckets": 7,
    "eventsDimension": [
        {"fieldName": "src_country"}
    ],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Connectivity"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "utc.2023-03-{01/00:00:00--07/23:59:59}"
}'
```

### 6. High-Threat Score Analysis

Monitor high-severity threats with trend analysis:

```bash
catocli query eventsTimeSeries '{
    "buckets": 31,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Security"]
        },
        {
            "fieldName": "threat_score",
            "operator": "gt",
            "values": ["50"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "avg", "fieldName": "threat_score"}
    ],
    "timeFrame": "utc.2023-01-{01/00:00:00--31/23:59:59}"
}'
```

### 7. Socket Connectivity Analysis

Monitor socket interface connection events:

```bash
catocli query eventsTimeSeries '{
    "buckets": 28,
    "eventsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Connectivity"]
        },
        {
            "fieldName": "event_sub_type",
            "operator": "in",
            "values": ["Connected", "Disconnected"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "utc.2023-02-{01/00:00:00--28/23:59:59}"
}'
```

## Advanced Filtering

### Filter Structure
```json
{
  "eventsFilter": [
    {
      "fieldName": "field_name",
      "operator": "operator_type",
      "values": ["value1", "value2"]
    }
  ]
}
```

### Available Operators
- `is` - Exact match
- `in` - Match any of the provided values
- `gt` - Greater than (numerical values)
- `gte` - Greater than or equal
- `lt` - Less than
- `lte` - Less than or equal
- `contains` - Contains substring
- `not` - Does not match

### Common Filter Examples

#### Security Event Types
```json
{
  "eventsFilter": [
    {
      "fieldName": "event_type",
      "operator": "is",
      "values": ["Security"]
    }
  ]
}
```

#### High Threat Scores
```json
{
  "eventsFilter": [
    {
      "fieldName": "threat_score",
      "operator": "gte",
      "values": ["80"]
    }
  ]
}
```

#### Specific Source Countries
```json
{
  "eventsFilter": [
    {
      "fieldName": "src_country",
      "operator": "in",
      "values": ["CN", "RU", "KP"]
    }
  ]
}
```

#### Connection Events
```json
{
  "eventsFilter": [
    {
      "fieldName": "event_sub_type",
      "operator": "in",
      "values": ["Connected", "Disconnected", "Connection Failed"]
    }
  ]
}
```

## Time Buckets and Granularity

### High-Resolution Monitoring (5-minute intervals)
```json
{"buckets": 12, "timeFrame": "last.PT1H"}
```

### Hourly Analysis  
```json
{"buckets": 24, "timeFrame": "last.P1D"}
{"buckets": 168, "timeFrame": "last.P7D"}
```

### Daily Analysis
```json
{"buckets": 7, "timeFrame": "last.P7D"}
{"buckets": 30, "timeFrame": "last.P1M"}
```

### Granularity Multiplication

The CLI automatically applies granularity multiplication to sum aggregations for meaningful totals:

**Example:**
- Original API value: 0.096 events per period  
- Granularity: 3600 seconds (1 hour)
- Computed value: 0.096 × 3600 = 345.6 total events

Use the `-raw` flag to see original unprocessed values.

## Output Format Options

### Enhanced JSON (Default)
Returns formatted JSON with granularity multiplication applied:
```bash
catocli query eventsTimeSeries '{...}'
```

### Raw JSON Format
Returns original API response without formatting:
```bash
catocli query eventsTimeSeries '{...}' -raw
```

### CSV Format
Exports data to CSV with granularity-adjusted values:
```bash
catocli query eventsTimeSeries '{...}' -f csv
```

### Custom CSV with Timestamp
```bash
catocli query eventsTimeSeries '{...}' -f csv --csv-filename "security_events" --append-timestamp
```

## Advanced Analysis Examples

### Threat Intelligence Analysis
```bash
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [
        {"fieldName": "src_country"},
        {"fieldName": "threat_type"}
    ],
    "eventsFilter": [
        {
            "fieldName": "threat_score",
            "operator": "gte",
            "values": ["70"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"},
        {"aggType": "avg", "fieldName": "threat_score"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename threat_intelligence_analysis.csv
```

### Network Availability Assessment  
```bash
catocli query eventsTimeSeries '{
    "buckets": 288,
    "eventsDimension": [
        {"fieldName": "site_name"}
    ],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Connectivity"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename network_availability.csv
```

### Security Rule Effectiveness
```bash
catocli query eventsTimeSeries '{
    "buckets": 24,
    "eventsDimension": [
        {"fieldName": "rule_name"}
    ],
    "eventsFilter": [
        {
            "fieldName": "event_sub_type",
            "operator": "is",
            "values": ["Internet Firewall"]
        }
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"},
        {"aggType": "count_distinct", "fieldName": "src_ip"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename security_rule_effectiveness.csv
```

### User Activity Correlation
```bash
catocli query eventsTimeSeries '{
    "buckets": 48,
    "eventsDimension": [
        {"fieldName": "user_name"},
        {"fieldName": "event_type"}
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename user_activity_events.csv
```

## Integration and Automation

### Security Monitoring Dashboard Data
```bash
#!/bin/bash
# Hourly security events for dashboard
catocli query eventsTimeSeries '{
    "buckets": 24,
    "eventsFilter": [
        {"fieldName": "event_type", "operator": "is", "values": ["Security"]}
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "security_dashboard_$(date +%Y%m%d_%H%M).csv"
```

### Weekly Threat Report
```bash
#!/bin/bash
# Weekly threat analysis report
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [
        {"fieldName": "threat_type"},
        {"fieldName": "src_country"}
    ],
    "eventsFilter": [
        {"fieldName": "threat_score", "operator": "gte", "values": ["60"]}
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"},
        {"aggType": "avg", "fieldName": "threat_score"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "weekly_threat_report.csv" --append-timestamp
```

### Real-Time Alerting Data
```bash
#!/bin/bash
# High-resolution monitoring for alerting
catocli query eventsTimeSeries '{
    "buckets": 12,
    "eventsFilter": [
        {"fieldName": "threat_score", "operator": "gte", "values": ["90"]}
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.PT1H"
}' > /tmp/high_severity_events.json
```

### Site Health Monitoring
```bash  
#!/bin/bash
# Monitor site connectivity health
catocli query eventsTimeSeries '{
    "buckets": 96,
    "eventsDimension": [
        {"fieldName": "site_name"}
    ],
    "eventsFilter": [
        {"fieldName": "event_type", "operator": "is", "values": ["Connectivity"]}
    ],
    "eventsMeasure": [
        {"aggType": "sum", "fieldName": "event_count"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "site_health_$(date +%Y%m%d).csv"
```

## Best Practices

### Performance Optimization
1. **Use specific filters**: Reduce dataset size with targeted filters
2. **Appropriate bucket sizes**: Balance detail with performance
3. **Limit dimensions**: Use only necessary dimension fields
4. **Time frame consideration**: Avoid overly broad ranges for high-resolution queries

### Security Analysis Tips
1. **Baseline establishment**: Regular monitoring to establish normal patterns
2. **Anomaly detection**: Look for unusual spikes or patterns
3. **Correlation analysis**: Compare events across different dimensions
4. **Trend identification**: Monitor changes in threat patterns over time

### Monitoring Strategies
1. **Layered approach**: Combine high-resolution and long-term analysis
2. **Multi-dimensional analysis**: Use different dimension combinations
3. **Automated reporting**: Set up regular report generation
4. **Threshold-based alerting**: Monitor for specific event thresholds

## Troubleshooting Common Issues

### High Event Volumes
- Use specific filters to reduce dataset size
- Increase bucket count for better granularity
- Consider shorter time frames for detailed analysis

### Missing Data
- Check time frame alignment with event occurrence
- Verify filter criteria don't exclude expected events
- Use `withMissingData` parameter where applicable

### Performance Issues
- Reduce number of dimensions
- Use more specific event type filters
- Consider breaking large queries into smaller time chunks

## Related Operations

- [Account Metrics](./account-metrics.md) - For network performance correlation
- [Application Statistics](./app-stats.md) - For user activity correlation  
- [Socket Port Metrics](./socket-port-metrics.md) - For infrastructure health

## API Reference

For complete field descriptions and additional parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-eventsTimeSeries).

## Additional Resources

- [Cato Management Application Events](https://support.catonetworks.com/hc/en-us/articles/4413280536081) - Event types and descriptions
- [Security Policy Configuration](https://support.catonetworks.com/) - Understanding security rules and policies