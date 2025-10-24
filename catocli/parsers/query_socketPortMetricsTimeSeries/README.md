
## CATO-CLI - query.socketPortMetricsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetricsTimeSeries) for documentation on this operation.

### Usage for query.socketPortMetricsTimeSeries:

```bash
catocli query socketPortMetricsTimeSeries -h

catocli query socketPortMetricsTimeSeries <json>

catocli query socketPortMetricsTimeSeries "$(cat < query.socketPortMetricsTimeSeries.json)"

catocli query socketPortMetricsTimeSeries '{"buckets":1,"perSecond":true,"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","fieldName":"account_id","trend":true},"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'

catocli query socketPortMetricsTimeSeries '{
    "buckets": 1,
    "perSecond": true,
    "socketPortMetricsDimension": {
        "fieldName": "account_id"
    },
    "socketPortMetricsFilter": {
        "fieldName": "account_id",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "socketPortMetricsMeasure": {
        "aggType": "sum",
        "fieldName": "account_id",
        "trend": true
    },
    "timeFrame": "example_value",
    "useDefaultSizeBucket": true,
    "withMissingData": true
}'
```

## Advanced Usage
### Additional Examples
- 1 Day sum of traffic by site, socket_interface, device_id
- 1 Day sum of traffic by site, socket_interface, device_id as csv
- Interface traffic patterns throughout the day
- Weekly average utilization patterns
- Throughput trends over extended periods
- Peak traffic hours with high-resolution monitoring
- Multi-Site Performance Comparison
- Performance during specific business hours
- Traffic patterns between weekdays and weekends
- Weekend analysis
- Analyze month-over-month growth trends
- High-level metrics for executive reporting
- High-level metrics for executive reporting - daily summary

# 1 Day sum of traffic by site, socket_interface, device_id

```bash
# 1 Day sum of traffic by site, socket_interface, device_id as csv
catocli query socketPortMetricsTimeSeries
    "buckets": 24,
    "socketPortMetricsDimension": [
        {
            "fieldName": "socket_interface"
        },
        {
            "fieldName": "device_id"
        },
        {
            "fieldName": "site_id"
        },
        {
            "fieldName": "site_name"
        }
    ],
    "socketPortMetricsFilter": [],
    "socketPortMetricsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "bytes_downstream"
        },
        {
            "aggType": "sum",
            "fieldName": "bytes_upstream"
        },
        {
            "aggType": "sum",
            "fieldName": "bytes_total"
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv
```

# Interface traffic patterns throughout the day

```bash
# Interface traffic patterns throughout the day
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

# Weekly average utilization patterns

```bash
# Weekly average utilization patterns
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

# Throughput trends over extended periods

```bash
# Throughput trends over extended periods
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

# Peak traffic hours with high-resolution monitoring

```bash
# Peak traffic hours with high-resolution monitoring
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

# Multi-Site Performance Comparison

```bash
# Multi-Site Performance Comparison
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

# Performance during specific business hours

```bash
# Performance during specific business hours
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

# Traffic patterns between weekdays and weekends

```bash
# Traffic patterns between weekdays and weekends
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

# Analyze month-over-month growth trends

```bash
# Analyze month-over-month growth trends
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

# High-level metrics for executive reporting

```bash
# High-level metrics for executive reporting - daily summary
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


#### Operation Arguments for query.socketPortMetricsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`buckets` [Int] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (required) N/A    
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (required) N/A    
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
