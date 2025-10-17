# Socket Port Metrics Query Guide

The `socketPortMetrics` and `socketPortMetricsTimeSeries` queries provide detailed analysis of socket interface performance, traffic patterns, and throughput metrics within your Cato Networks infrastructure.

## Overview

Socket port metrics help you analyze:
- **Interface Performance**: Traffic throughput and utilization per socket interface
- **Device-Level Analysis**: Per-device traffic patterns and performance
- **Site Connectivity**: Traffic patterns and performance by site
- **Capacity Planning**: Understanding interface utilization for planning
- **Network Optimization**: Identifying bottlenecks and optimization opportunities
- **Trend Analysis**: Traffic patterns over time (time series variant)

## Basic Usage

### Socket Port Metrics (Aggregated)
```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}'
```

### Socket Port Metrics Time Series
```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}'
```

## Query Structure

### Socket Port Metrics Structure
```json
{
  "socketPortMetricsDimension": [    // Fields to group results by
    {"fieldName": "socket_interface"},
    {"fieldName": "device_id"},
    {"fieldName": "site_name"}
  ],
  "socketPortMetricsFilter": [],     // Filters to apply to data
  "socketPortMetricsMeasure": [      // Metrics to calculate
    {"aggType": "sum", "fieldName": "bytes_upstream"},
    {"aggType": "sum", "fieldName": "bytes_downstream"},
    {"aggType": "sum", "fieldName": "bytes_total"}
  ],
  "socketPortMetricsSort": [],       // Sort criteria
  "timeFrame": "last.P1D"           // Time range for analysis
}
```

### Socket Port Metrics Time Series Structure
```json
{
  "buckets": 24,                     // Number of time buckets
  "socketPortMetricsDimension": [    // Fields to group results by
    {"fieldName": "socket_interface"},
    {"fieldName": "device_id"},
    {"fieldName": "site_name"}
  ],
  "socketPortMetricsFilter": [],     // Filters to apply to data
  "socketPortMetricsMeasure": [      // Metrics to calculate over time
    {"aggType": "sum", "fieldName": "bytes_downstream"},
    {"aggType": "sum", "fieldName": "bytes_upstream"},
    {"aggType": "sum", "fieldName": "bytes_total"}
  ],
  "timeFrame": "last.P1D"           // Time range for analysis
}
```

## Available Dimensions

Group your results by these fields:

### Interface Dimensions
- `socket_interface` - Socket interface identifier
- `device_id` - Device identifier
- `device_name` - Device name
- `interface_name` - Interface name

### Location Dimensions
- `site_id` - Site identifier  
- `site_name` - Site name
- `site_location` - Site location/address

### Network Dimensions
- `network_segment` - Network segment identifier
- `vlan_id` - VLAN identifier

## Available Measures

### Traffic Measures
- `bytes_upstream` - Upstream bytes
- `bytes_downstream` - Downstream bytes
- `bytes_total` - Total bytes (upstream + downstream)

### Throughput Measures
- `throughput_upstream` - Upstream throughput
- `throughput_downstream` - Downstream throughput
- `throughput_total` - Total throughput

### Utilization Measures
- `utilization_upstream` - Upstream utilization percentage
- `utilization_downstream` - Downstream utilization percentage
- `utilization_total` - Total utilization percentage

### Packet Measures
- `packets_upstream` - Upstream packet count
- `packets_downstream` - Downstream packet count
- `packets_total` - Total packet count

### Performance Measures
- `latency` - Interface latency
- `packet_loss` - Packet loss percentage
- `error_rate` - Error rate

## Common Use Cases

### 1. Site Traffic Analysis

Analyze traffic patterns by site and interface:

```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "device_id"},
        {"fieldName": "site_id"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_downstream"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}'
```

### 2. Interface Performance Over Time

Track interface performance with hourly breakdown:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "device_id"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_downstream"},
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename interface_performance_hourly.csv
```

### 3. Long-Term Throughput Analysis

Analyze throughput patterns over extended periods:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 120,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "device_id"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "throughput_downstream"},
        {"aggType": "sum", "fieldName": "throughput_upstream"}
    ],
    "timeFrame": "last.P2M"
}'
```

### 4. Top Traffic Interfaces

Identify highest traffic interfaces with sorting:

```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "socketPortMetricsSort": [
        {"fieldName": "bytes_total", "order": "desc"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename top_traffic_interfaces.csv
```

### 5. Site Comparison Analysis

Compare traffic patterns across multiple sites:

```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"},
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_downstream"},
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.P1D"
}'
```

### 6. Device-Level Traffic Distribution

Analyze traffic distribution across devices:

```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "device_id"},
        {"fieldName": "device_name"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"},
        {"aggType": "avg", "fieldName": "throughput_total"}
    ],
    "socketPortMetricsSort": [
        {"fieldName": "bytes_total", "order": "desc"}
    ],
    "timeFrame": "last.P1D"
}'
```

## Filtering Options

### Filter Structure
```json
{
  "socketPortMetricsFilter": [
    {
      "fieldName": "field_to_filter",
      "operator": "filter_operator",
      "values": ["value1", "value2"]
    }
  ]
}
```

### Available Operators
- `is` - Exact match
- `in` - Match any of the values
- `gt` - Greater than
- `gte` - Greater than or equal
- `lt` - Less than
- `lte` - Less than or equal
- `contains` - Contains substring

### Common Filter Examples

#### Filter by Site
```json
{
  "socketPortMetricsFilter": [
    {
      "fieldName": "site_name",
      "operator": "in",
      "values": ["HQ", "Branch Office"]
    }
  ]
}
```

#### Filter by Interface Type
```json
{
  "socketPortMetricsFilter": [
    {
      "fieldName": "socket_interface",
      "operator": "contains",
      "values": ["eth"]
    }
  ]
}
```

#### Filter by High Utilization
```json
{
  "socketPortMetricsFilter": [
    {
      "fieldName": "utilization_total",
      "operator": "gte",
      "values": ["80"]
    }
  ]
}
```

## Sorting Results

### Sort Structure
```json
{
  "socketPortMetricsSort": [
    {
      "fieldName": "field_to_sort_by",
      "order": "desc"  // or "asc"
    }
  ]
}
```

### Common Sort Examples

#### Sort by Total Traffic
```json
{
  "socketPortMetricsSort": [
    {"fieldName": "bytes_total", "order": "desc"}
  ]
}
```

#### Sort by Utilization
```json
{
  "socketPortMetricsSort": [
    {"fieldName": "utilization_total", "order": "desc"}
  ]
}
```

## Time Series Analysis

### Bucket Configuration for Time Series

#### Hourly Analysis (24 hours)
```json
{"buckets": 24, "timeFrame": "last.P1D"}
```

#### Daily Analysis (30 days)
```json
{"buckets": 30, "timeFrame": "last.P1M"}
```

#### High-Resolution (5-minute intervals)
```json
{"buckets": 72, "timeFrame": "last.PT6H"}
```

### Time Series Use Cases

#### Weekly Traffic Patterns
```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 168,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename weekly_traffic_patterns.csv
```

#### Peak Usage Identification
```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 48,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "throughput_total"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename peak_usage_analysis.csv
```

## Output Format Options

### Default JSON Output
```bash
catocli query socketPortMetrics '{...}'
```

### CSV Export
```bash
catocli query socketPortMetrics '{...}' -f csv --csv-filename socket_metrics.csv
```

### Raw JSON
```bash
catocli query socketPortMetrics '{...}' -raw
```

### CSV with Timestamp
```bash
catocli query socketPortMetricsTimeSeries '{...}' -f csv --csv-filename socket_trends --append-timestamp
```

## Advanced Analysis Examples

### Capacity Planning Analysis
```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 720,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "throughput_total"}
    ],
    "timeFrame": "last.P1M"
}' -f csv --csv-filename capacity_planning_analysis.csv
```

### Performance Monitoring Dashboard
```bash
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"},
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "latency"},
        {"aggType": "avg", "fieldName": "packet_loss"},
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.PT1H"
}' -f csv --csv-filename performance_dashboard.csv
```

### Network Bottleneck Identification
```bash
catocli query socketPortMetrics '{
    "socketPortMetricsFilter": [
        {
            "fieldName": "utilization_total",
            "operator": "gte",
            "values": ["90"]
        }
    ],
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"},
        {"fieldName": "device_id"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "socketPortMetricsSort": [
        {"fieldName": "utilization_total", "order": "desc"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename network_bottlenecks.csv
```

### Site-to-Site Traffic Comparison
```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_downstream"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename site_traffic_comparison.csv
```

## Integration and Automation

### Daily Interface Report
```bash
#!/bin/bash
# Daily interface performance report
DATE=$(date +%Y%m%d)
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"},
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "daily_interface_report_${DATE}.csv"
```

### Weekly Capacity Planning Report
```bash
#!/bin/bash
# Weekly capacity planning analysis
catocli query socketPortMetricsTimeSeries '{
    "buckets": 168,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "max", "fieldName": "utilization_total"},
        {"aggType": "avg", "fieldName": "throughput_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "weekly_capacity_report.csv" --append-timestamp
```

### Real-Time Performance Monitoring
```bash
#!/bin/bash
# Real-time interface performance monitoring
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "avg", "fieldName": "packet_loss"}
    ],
    "timeFrame": "last.PT15M"
}' > /tmp/realtime_interface_status.json
```

## Best Practices

### Performance Optimization
1. **Limit dimensions**: Use only necessary dimension fields for better performance
2. **Strategic filtering**: Apply filters to reduce dataset size
3. **Appropriate time frames**: Match time frame to analysis requirements
4. **Bucket sizing**: Balance detail with performance for time series

### Monitoring Strategies
1. **Multi-layer approach**: Combine real-time and historical analysis
2. **Threshold-based alerting**: Monitor for utilization and performance thresholds
3. **Regular reporting**: Establish consistent reporting schedules
4. **Trend analysis**: Use time series for capacity planning

### Data Analysis Tips
1. **Baseline establishment**: Create performance baselines for comparison
2. **Peak identification**: Identify peak usage patterns
3. **Anomaly detection**: Monitor for unusual traffic patterns
4. **Capacity planning**: Use historical data for future planning

## Troubleshooting Common Issues

### High Utilization Interfaces
```bash
# Identify high utilization interfaces
catocli query socketPortMetrics '{
    "socketPortMetricsFilter": [
        {"fieldName": "utilization_total", "operator": "gte", "values": ["85"]}
    ],
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.P1D"
}'
```

### Performance Degradation Analysis
```bash
# Analyze performance metrics over time
catocli query socketPortMetricsTimeSeries '{
    "buckets": 48,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "latency"},
        {"aggType": "avg", "fieldName": "packet_loss"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename performance_degradation.csv
```

## Related Operations

- [Account Metrics](./account-metrics.md) - For broader network performance metrics
- [Events Time Series](./events-timeseries.md) - For connectivity event correlation
- [Application Statistics](./app-stats.md) - For application traffic correlation

## API Reference

For complete field descriptions and additional parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-socketPortMetrics) and [Socket Port Time Series Documentation](https://api.catonetworks.com/documentation/#query-socketPortMetricsTimeSeries).