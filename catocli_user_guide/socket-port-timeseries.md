# Socket Port Metrics Time Series Query Guide

The `socketPortMetricsTimeSeries` query provides time-based analysis of socket interface performance, enabling detailed monitoring of traffic patterns, throughput trends, and capacity utilization over time.

## Overview

This guide focuses specifically on the time series variant of socket port metrics, which adds temporal analysis capabilities to interface monitoring. For general socket port metrics information, see the main [Socket Port Metrics](./socket-port-metrics.md) guide.

## Key Features

- **Temporal Analysis**: Track interface performance over time with configurable granularity
- **Trend Identification**: Identify usage patterns, peak hours, and growth trends
- **Capacity Planning**: Historical analysis for future capacity requirements
- **Performance Monitoring**: Real-time and historical performance tracking
- **Anomaly Detection**: Identify unusual traffic patterns or performance issues

## Basic Usage

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

## Time Bucket Configuration

The time series analysis is controlled by the `buckets` parameter:

### Common Configurations

#### Hourly Analysis
```json
{"buckets": 24, "timeFrame": "last.P1D"}    // 24 hours, 1-hour buckets
{"buckets": 168, "timeFrame": "last.P7D"}   // 7 days, 1-hour buckets
```

#### Daily Analysis
```json
{"buckets": 7, "timeFrame": "last.P7D"}     // 7 days, daily buckets
{"buckets": 30, "timeFrame": "last.P1M"}    // 30 days, daily buckets
```

#### High-Resolution Monitoring
```json
{"buckets": 72, "timeFrame": "last.PT6H"}   // 6 hours, 5-minute buckets
{"buckets": 288, "timeFrame": "last.P1D"}   // 24 hours, 5-minute buckets
```

## Time Series Use Cases

### 1. Daily Traffic Patterns

Analyze interface traffic patterns throughout the day:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_downstream"},
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename daily_traffic_patterns.csv
```

### 2. Weekly Capacity Analysis

Track weekly utilization patterns for capacity planning:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 168,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "throughput_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename weekly_capacity_analysis.csv
```

### 3. Long-Term Throughput Trends

Analyze throughput trends over extended periods:

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
}' -f csv --csv-filename longterm_throughput_trends.csv
```

### 4. Peak Hour Identification

Identify peak traffic hours with high-resolution monitoring:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 96,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename peak_hour_analysis.csv
```

### 5. Multi-Site Performance Comparison

Compare performance trends across multiple sites:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 48,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"},
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename multisite_performance.csv
```

### 6. Real-Time Performance Monitoring

High-frequency monitoring for real-time analysis:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 60,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "latency"},
        {"aggType": "avg", "fieldName": "packet_loss"},
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.PT1H"
}'
```

## Advanced Time Series Analysis

### Business Hours Focus

Analyze performance during specific business hours:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 32,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "utc.2023-10-{15/09:00:00--15/17:00:00}"
}' -f csv --csv-filename business_hours_utilization.csv
```

### Weekend vs Weekday Comparison

Compare traffic patterns between weekdays and weekends:

```bash
# Weekday analysis
catocli query socketPortMetricsTimeSeries '{
    "buckets": 120,
    "socketPortMetricsDimension": [{"fieldName": "site_name"}],
    "socketPortMetricsMeasure": [{"aggType": "sum", "fieldName": "bytes_total"}],
    "timeFrame": "utc.2023-10-{09/00:00:00--13/23:59:59}"
}' -f csv --csv-filename weekday_traffic.csv

# Weekend analysis  
catocli query socketPortMetricsTimeSeries '{
    "buckets": 48,
    "socketPortMetricsDimension": [{"fieldName": "site_name"}],
    "socketPortMetricsMeasure": [{"aggType": "sum", "fieldName": "bytes_total"}],
    "timeFrame": "utc.2023-10-{14/00:00:00--15/23:59:59}"
}' -f csv --csv-filename weekend_traffic.csv
```

### Growth Trend Analysis

Analyze month-over-month growth trends:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 30,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_total"},
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.P1M"
}' -f csv --csv-filename monthly_growth_trends.csv
```

## Performance Monitoring Dashboards

### Executive Dashboard Data

High-level metrics for executive reporting:

```bash
#!/bin/bash
# Executive dashboard - daily summary
catocli query socketPortMetricsTimeSeries '{
    "buckets": 7,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "executive_dashboard_$(date +%Y%m%d).csv"
```

### Operations Dashboard Data

Detailed operational metrics:

```bash
#!/bin/bash
# Operations dashboard - hourly breakdown
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "avg", "fieldName": "latency"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "ops_dashboard_$(date +%Y%m%d_%H%M).csv"
```

## Capacity Planning Analysis

### Monthly Capacity Report

Comprehensive capacity planning analysis:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 720,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "throughput_total"}
    ],
    "timeFrame": "last.P1M"
}' -f csv --csv-filename monthly_capacity_report.csv
```

### Interface Upgrade Planning

Identify interfaces approaching capacity limits:

```bash
catocli query socketPortMetricsTimeSeries '{
    "socketPortMetricsFilter": [
        {
            "fieldName": "utilization_total",
            "operator": "gte",
            "values": ["75"]
        }
    ],
    "buckets": 168,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename interface_upgrade_candidates.csv
```

## Automation Scripts

### Automated Threshold Monitoring

```bash
#!/bin/bash
# Monitor interfaces exceeding 90% utilization
THRESHOLD=90
OUTPUT_FILE="/tmp/high_utilization_interfaces.csv"

catocli query socketPortMetricsTimeSeries '{
    "socketPortMetricsFilter": [
        {
            "fieldName": "utilization_total",
            "operator": "gte",
            "values": ["'$THRESHOLD'"]
        }
    ],
    "buckets": 12,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.PT1H"
}' -f csv --csv-filename "$OUTPUT_FILE"

# Check if any interfaces exceed threshold
if [ -s "$OUTPUT_FILE" ]; then
    echo "ALERT: High utilization interfaces detected!"
    cat "$OUTPUT_FILE"
fi
```

### Weekly Capacity Planning Report

```bash
#!/bin/bash
# Automated weekly capacity planning report
WEEK=$(date +%Y-W%V)
REPORT_DIR="/reports/capacity"
mkdir -p "$REPORT_DIR"

catocli query socketPortMetricsTimeSeries '{
    "buckets": 168,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"},
        {"fieldName": "socket_interface"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"},
        {"aggType": "max", "fieldName": "utilization_total"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "${REPORT_DIR}/capacity_report_${WEEK}.csv" --append-timestamp

echo "Weekly capacity report generated: ${REPORT_DIR}/capacity_report_${WEEK}.csv"
```

## Data Visualization Recommendations

### Time Series Charts

1. **Line Charts**: Best for showing utilization trends over time
2. **Area Charts**: Good for showing traffic volume changes
3. **Stacked Charts**: Compare multiple interfaces or sites
4. **Heat Maps**: Show patterns across time and interfaces

### Key Metrics to Visualize

1. **Utilization Over Time**: Track capacity usage patterns
2. **Peak vs Average**: Compare peak and average utilization
3. **Growth Trends**: Show month-over-month or year-over-year growth
4. **Site Comparisons**: Compare performance across locations

## Best Practices for Time Series Analysis

### Granularity Selection
- **High-resolution (5-min buckets)**: For real-time monitoring and troubleshooting
- **Hourly buckets**: For daily and weekly trend analysis
- **Daily buckets**: For long-term capacity planning

### Performance Considerations
- Use appropriate time ranges to balance detail with query performance
- Limit dimensions when analyzing long time periods
- Consider using filters to focus on specific interfaces or sites

### Data Interpretation
- Look for consistent patterns across similar time periods
- Identify seasonal trends (daily, weekly, monthly)
- Monitor for gradual increases that may indicate growth
- Watch for sudden spikes that may indicate issues

## Integration with Alerting Systems

### Threshold-Based Alerting

```bash
#!/bin/bash
# Integration with alerting system
ALERT_THRESHOLD=85
CRITICAL_THRESHOLD=95

# Get current utilization data
RESULT=$(catocli query socketPortMetricsTimeSeries '{
    "buckets": 1,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "avg", "fieldName": "utilization_total"}
    ],
    "timeFrame": "last.PT15M"
}' -raw)

# Process results and send alerts (implementation depends on alerting system)
echo "$RESULT" | jq -r '.data[] | select(.utilization_total > '$ALERT_THRESHOLD') | "ALERT: \(.socket_interface) at \(.site_name): \(.utilization_total)%"'
```

## Related Operations

- [Socket Port Metrics](./socket-port-metrics.md) - For aggregated interface analysis
- [Account Metrics](./account-metrics.md) - For broader network performance
- [Events Time Series](./events-timeseries.md) - For connectivity event correlation

## API Reference

For complete field descriptions and parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-socketPortMetricsTimeSeries).