# Application Statistics Time Series Query Guide

The `appStatsTimeSeries` query provides time-based analysis of application usage and user activity, enabling you to track traffic patterns, user behavior, and application consumption trends over specified time periods with granular time buckets.

## Overview

Application statistics time series help you analyze:
- **Traffic Trends**: Bandwidth usage patterns over time
- **Peak Usage Analysis**: Identify high-traffic periods and applications
- **User Activity Patterns**: Track user behavior across different time periods
- **Application Performance**: Monitor application usage trends and seasonal patterns
- **Capacity Planning**: Understand usage patterns for network planning
- **Filtered Analysis**: Focus on specific traffic types (WANBOUND, LANBOUND)

## Basic Usage

```bash
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [{"fieldName": "user_name"}, {"fieldName": "application_name"}],
    "measure": [{"aggType": "sum", "fieldName": "traffic"}],
    "timeFrame": "last.P1D"
}'
```

## Query Structure

```json
{
  "appStatsFilter": [],           // Filters to apply to the data
  "buckets": 24,                  // Number of time buckets to divide the timeFrame
  "dimension": [                  // Fields to group results by
    {"fieldName": "user_name"},
    {"fieldName": "application_name"}
  ],
  "measure": [                    // Metrics to calculate over time
    {"aggType": "sum", "fieldName": "upstream"},
    {"aggType": "sum", "fieldName": "downstream"},
    {"aggType": "sum", "fieldName": "traffic"}
  ],
  "timeFrame": "last.P1D"        // Time range for analysis
}
```

## Time Buckets Configuration

The `buckets` parameter determines how your time frame is divided:

### Common Bucket Configurations
- **24 buckets over 1 day** = 1-hour intervals
- **48 buckets over 2 days** = 1-hour intervals
- **168 buckets over 7 days** = 1-hour intervals
- **720 buckets over 30 days** = 1-hour intervals
- **12 buckets over 1 hour** = 5-minute intervals

### Examples by Time Frame
```json
// Hourly breakdown for one day
{"buckets": 24, "timeFrame": "last.P1D"}

// 6-hour breakdown for one week  
{"buckets": 28, "timeFrame": "last.P7D"}

// Daily breakdown for one month
{"buckets": 30, "timeFrame": "last.P1M"}

// 15-minute intervals for 6 hours
{"buckets": 24, "timeFrame": "last.PT6H"}
```

## Available Dimensions

Same as [Application Statistics](./app-stats.md):

### User Dimensions
- `user_name` - Username
- `user_id` - User identifier  
- `user_email` - User email address

### Application Dimensions
- `application_name` - Application name
- `application_category` - Application category
- `application_subcategory` - Application subcategory
- `risk_score` - Application risk score

### Network Dimensions
- `site_name` - Site name
- `site_id` - Site identifier
- `src_country` - Source country
- `dst_country` - Destination country

### Traffic Dimensions
- `traffic_direction` - Traffic direction (WANBOUND, LANBOUND)
- `protocol` - Network protocol

## Available Measures

### Traffic Measures
- `upstream` - Upstream bytes over time
- `downstream` - Downstream bytes over time
- `traffic` - Total traffic bytes over time

### Session Measures  
- `flows_created` - Number of flows/sessions created over time
- `session_duration` - Session duration over time

## Common Use Cases

### 1. Hourly Traffic Analysis

Track traffic patterns throughout the day:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "application_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "downstream"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}'
```

### 2. WAN-Bound Traffic Analysis

Focus on outbound internet traffic with hourly breakdown:

```bash
catocli query appStatsTimeSeries '{
    "appStatsFilter": [
        {
            "fieldName": "traffic_direction",
            "operator": "is",
            "values": ["WANBOUND"]
        }
    ],
    "buckets": 24,
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "downstream"}
    ],
    "timeFrame": "last.P1D"
}'
```

### 3. Weekly Usage Patterns

Analyze usage patterns over a full week:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 168,
    "dimension": [
        {"fieldName": "application_category"},
        {"fieldName": "site_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename weekly_usage_patterns.csv
```

### 4. High-Resolution Monitoring

5-minute intervals for detailed monitoring:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 72,
    "dimension": [
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.PT6H"
}'
```

### 5. Peak Hours Identification

Focus on business hours with 15-minute granularity:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 32,
    "dimension": [
        {"fieldName": "application_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "utc.2023-10-{15/08:00:00--15/16:00:00}"
}'
```

### 6. User Activity Correlation

Track user activity patterns with application usage:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 48,
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "application_category"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "session_duration"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename user_activity_correlation.csv
```

## Advanced Filtering

### Traffic Direction Filtering

#### WAN-Bound Traffic Only
```json
{
  "appStatsFilter": [
    {
      "fieldName": "traffic_direction",
      "operator": "is", 
      "values": ["WANBOUND"]
    }
  ]
}
```

#### LAN-Bound Traffic Only  
```json
{
  "appStatsFilter": [
    {
      "fieldName": "traffic_direction",
      "operator": "is",
      "values": ["LANBOUND"]
    }
  ]
}
```

### Application Category Filtering
```json
{
  "appStatsFilter": [
    {
      "fieldName": "application_category",
      "operator": "in",
      "values": ["Social Media", "Streaming", "Gaming"]
    }
  ]
}
```

### Risk-Based Filtering
```json
{
  "appStatsFilter": [
    {
      "fieldName": "risk_score",
      "operator": "gte",
      "values": ["7"]
    }
  ]
}
```

### Site-Specific Filtering
```json
{
  "appStatsFilter": [
    {
      "fieldName": "site_name", 
      "operator": "in",
      "values": ["HQ", "Branch Office"]
    }
  ]
}
```

## Output Format Options

### Enhanced JSON (Default)
```bash
catocli query appStatsTimeSeries '{...}'
```

### CSV Export for Analysis
```bash
catocli query appStatsTimeSeries '{...}' -f csv --csv-filename traffic_trends.csv
```

### Raw JSON for Integration
```bash
catocli query appStatsTimeSeries '{...}' -raw
```

### CSV with Timestamp
```bash
catocli query appStatsTimeSeries '{...}' -f csv --csv-filename hourly_analysis --append-timestamp
```

## Time Frame Options

### Relative Time Frames
- `last.PT1H` - Last hour (use with 12 buckets for 5-min intervals)
- `last.PT6H` - Last 6 hours  
- `last.P1D` - Last day (use with 24 buckets for hourly)
- `last.P7D` - Last week (use with 168 buckets for hourly)
- `last.P1M` - Last month (use with 720 buckets for hourly)

### Absolute Time Frames
```bash
# Business hours analysis
"timeFrame": "utc.2023-10-{15/09:00:00--15/17:00:00}"

# Weekend analysis  
"timeFrame": "utc.2023-10-{14/00:00:00--15/23:59:59}"

# Monthly comparison
"timeFrame": "utc.2023-10-{01/00:00:00--31/23:59:59}"
```

## Advanced Analysis Examples

### Peak Usage Detection
```bash
catocli query appStatsTimeSeries '{
    "buckets": 168,
    "dimension": [
        {"fieldName": "application_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename peak_usage_analysis.csv
```

### Security Risk Trending
```bash
catocli query appStatsTimeSeries '{
    "appStatsFilter": [
        {
            "fieldName": "risk_score",
            "operator": "gte", 
            "values": ["8"]
        }
    ],
    "buckets": 72,
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "risk_score"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P3D"
}' -f csv --csv-filename security_risk_trending.csv
```

### Multi-Site Comparison
```bash
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [
        {"fieldName": "site_name"},
        {"fieldName": "application_category"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename multi_site_comparison.csv
```

### Productivity vs Entertainment Analysis
```bash
catocli query appStatsTimeSeries '{
    "appStatsFilter": [
        {
            "fieldName": "application_category",
            "operator": "in",
            "values": ["Business", "Collaboration", "Entertainment", "Gaming", "Social Media"]
        }
    ],
    "buckets": 48,
    "dimension": [
        {"fieldName": "application_category"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "session_duration"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename productivity_analysis.csv
```

## Integration and Automation

### Daily Traffic Pattern Report
```bash
#!/bin/bash
# Generate daily traffic patterns report
DATE=$(date +%Y%m%d)
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [{"fieldName": "application_category"}],
    "measure": [{"aggType": "sum", "fieldName": "traffic"}],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "daily_traffic_patterns_${DATE}.csv"
```

### Weekly Trend Analysis
```bash
#!/bin/bash
# Weekly application usage trends
catocli query appStatsTimeSeries '{
    "buckets": 168,
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "weekly_trends.csv" --append-timestamp
```

### Real-Time Monitoring Script
```bash
#!/bin/bash
# 6-hour window with 5-minute granularity for real-time monitoring
catocli query appStatsTimeSeries '{
    "buckets": 72,
    "dimension": [{"fieldName": "application_name"}],
    "measure": [{"aggType": "sum", "fieldName": "traffic"}],
    "timeFrame": "last.PT6H"
}' -f csv --csv-filename "realtime_monitoring.csv"
```

## Performance and Best Practices

### Bucket Size Guidelines
- **Small buckets** (< 50): Good for detailed analysis, shorter time frames
- **Medium buckets** (50-200): Balance between detail and performance  
- **Large buckets** (> 200): Use for long-term trends, may impact performance

### Dimension Optimization
- Limit dimensions to essential fields only
- Use filtering to reduce dataset size before analysis
- Consider user vs application focus based on analysis needs

### Time Frame Considerations
- Use relative time frames for dynamic reporting
- Use absolute time frames for historical analysis
- Match bucket count to desired granularity

## Data Analysis Tips

### Identifying Patterns
1. **Peak Hours**: Look for consistent high-traffic periods
2. **Seasonal Trends**: Compare week-over-week or month-over-month
3. **Anomaly Detection**: Identify unusual spikes or drops
4. **User Behavior**: Correlate time patterns with user activity

### Visualization Recommendations
1. **Line Charts**: For traffic trends over time
2. **Stacked Charts**: For application category breakdown
3. **Heat Maps**: For hour-of-day vs day-of-week analysis
4. **Bar Charts**: For comparing peak usage periods

## Related Operations

- [Application Statistics](./app-stats.md) - For aggregated application analysis
- [Account Metrics](./account-metrics.md) - For network performance over time
- [Events Time Series](./events-timeseries.md) - For security events correlation

## API Reference

For complete field descriptions and additional parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-appStatsTimeSeries).