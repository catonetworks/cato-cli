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
    "perSecond": false,
    "timeFrame": "last.P1D"
}'
```

## IMPORTANT USAGE NOTE

Set `perSecond` to `false` on all timeSeries calls.  When perSecond is set to true (default), the API divides the returned value by the granularity period (e.g., 300 seconds for 5-minute intervals), giving you a per-second rate that requires multiplying back by the granularity to get the actual total for that time period. Setting perSecond to false returns the raw aggregate value for each time bucket directly, making the data immediately interpretable without additional calculation.

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
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_daily_traffic_patterns.csv
```

### 2. Weekly BW Analysis

Track weekly average utilization patterns

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "perSecond": false,
    "socketPortMetricsDimension": [
        { "fieldName": "site_name" }
    ],
    "socketPortMetricsFilter": [],
    "socketPortMetricsMeasure": [
        {
            "aggType": "avg",
            "fieldName": "throughput_downstream"
        },
        {
            "aggType": "avg",
            "fieldName": "throughput_upstream"
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_weekly_bw_analysis.csv
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
    "perSecond": false,
    "timeFrame": "last.P2M"
}' -f csv --csv-filename socketPortMetricsTimeSeries_longterm_throughput_trends.csv
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
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_peak_hour_analysis.csv
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
        {"aggType": "sum", "fieldName": "throughput_downstream"},
        {"aggType": "sum", "fieldName": "throughput_upstream"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "perSecond": false,
    "timeFrame": "last.P2D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_multisite_performance.csv
```

## Advanced Time Series Analysis

### 6. Business Hours Focus

Analyze performance during specific business hours:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 24,
    "perSecond": false,
    "socketPortMetricsDimension": [
        { "fieldName": "site_name" },
        { "fieldName": "socket_interface" }
    ],
    "socketPortMetricsFilter": [],
    "socketPortMetricsMeasure": [
        { "aggType": "avg", "fieldName": "bytes_upstream" },
        { "aggType": "avg", "fieldName": "bytes_total" },
        { "aggType": "avg", "fieldName": "bytes_downstream" }
    ],
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_business_hours_utilization.csv
```

### 7. Weekend vs Weekday Comparison

Compare traffic patterns between weekdays and weekends:

```bash
# Weekday analysis
catocli query socketPortMetricsTimeSeries '{
    "buckets": 120,
    "socketPortMetricsDimension": [{"fieldName": "site_name"}],
    "socketPortMetricsMeasure": [{"aggType": "sum", "fieldName": "bytes_total"}],
    "perSecond": false,
    "timeFrame": "utc.2025-10-{13/00:00:00--17/23:59:59}"
}' -f csv --csv-filename socketPortMetricsTimeSeries_weekday_traffic.csv

# Weekend analysis  
catocli query socketPortMetricsTimeSeries '{
    "buckets": 48,
    "socketPortMetricsDimension": [{"fieldName": "site_name"}],
    "socketPortMetricsMeasure": [{"aggType": "sum", "fieldName": "bytes_total"}],
    "timeFrame": "utc.2025-10-{18/00:00:00--19/23:59:59}"
}' -f csv --csv-filename socketPortMetricsTimeSeries_weekend_traffic.csv
```

### 8. Growth Trend Analysis

Analyze month-over-month growth trends:

```bash
catocli query socketPortMetricsTimeSeries '{
    "buckets": 30,
    "socketPortMetricsDimension": [
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        { "aggType": "avg", "fieldName": "bytes_upstream" },
        { "aggType": "avg", "fieldName": "bytes_total" },
        { "aggType": "avg", "fieldName": "bytes_downstream" }
    ],
    "perSecond": false,
    "timeFrame": "last.P1M"
}' -f csv --csv-filename socketPortMetricsTimeSeries_monthly_growth_trends.csv
```

## Performance Monitoring Dashboards

### 9. Executive Dashboard Data

High-level metrics for executive reporting:

```bash
# Executive dashboard - daily summary
catocli query socketPortMetricsTimeSeries '{
    "buckets": 7,
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        { "aggType": "sum", "fieldName": "bytes_upstream" },
        { "aggType": "sum", "fieldName": "bytes_total" },
        { "aggType": "sum", "fieldName": "bytes_downstream" },
        { "aggType": "avg", "fieldName": "throughput_downstream" },
        { "aggType": "avg", "fieldName": "throughput_upstream" }
    ],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename socketPortMetricsTimeSeries_executive_dashboard.csv --append-timestamp
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

## Related Operations

- [Socket Port Metrics](./socket-port-metrics.md) - For aggregated interface analysis
- [Account Metrics](./account-metrics.md) - For broader network performance
- [Events Time Series](./events-timeseries.md) - For connectivity event correlation

## API Reference

For complete field descriptions and parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-socketPortMetricsTimeSeries).