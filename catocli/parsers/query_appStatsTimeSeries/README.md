
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

```bash
catocli query appStatsTimeSeries -h

catocli query appStatsTimeSeries <json>

catocli query appStatsTimeSeries --json-file query.appStatsTimeSeries.json

catocli query appStatsTimeSeries '{"appStatsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"buckets":1,"dimension":{"fieldName":"account_id"},"measure":{"aggType":"sum","fieldName":"account_id","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'

catocli query appStatsTimeSeries '{
    "appStatsFilter": {
        "fieldName": "account_id",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "buckets": 1,
    "dimension": {
        "fieldName": "account_id"
    },
    "measure": {
        "aggType": "sum",
        "fieldName": "account_id",
        "trend": true
    },
    "perSecond": true,
    "timeFrame": "example_value",
    "useDefaultSizeBucket": true,
    "withMissingData": true
}'
```

## Advanced Usage
### Additional Examples
- Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets
- Traffic patterns throughout the day
- Wanbound traffic with hourly breakdown
- Usage patterns over a full week
- 5-minute intervals for detailed monitoring
- Business hours with 15-minute granularity
- User activity patterns with application usage

# Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

```bash
# Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets
catocli query appStatsTimeSeries '{
    "appStatsFilter": [],
    "buckets": 24,
    "dimension": [
        {
            "fieldName": "user_name"
        },
        {
            "fieldName": "application_name"
        }
    ],
    "perSecond": false,
    "measure": [
        {
            "aggType": "sum",
            "fieldName": "upstream"
        },
        {
            "aggType": "sum",
            "fieldName": "downstream"
        },
        {
            "aggType": "sum",
            "fieldName": "traffic"
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appStatsTimeSeries_app_bw.csv
```

# Traffic patterns throughout the day

```bash
# Traffic patterns throughout the day
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "application_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "downstream"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appStatsTimeSeries_user_app.csv
```

# Wanbound traffic with hourly breakdown

```bash
# Wanbound traffic with hourly breakdown
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
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "downstream"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appStatsTimeSeries_user_wan.csv
```

# Usage patterns over a full week

```bash
# Usage patterns over a full week
catocli query appStatsTimeSeries '{
    "buckets": 168,
    "dimension": [
        {"fieldName": "category"},
        {"fieldName": "src_site_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename appStatsTimeSeries_weekly_usage_category.csv
```

# 5-minute intervals for detailed monitoring

```bash
# 5-minute intervals for detailed monitoring
catocli query appStatsTimeSeries '{
    "buckets": 72,
    "dimension": [
        {"fieldName": "user_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.PT6H"
}' -f csv --csv-filename appStatsTimeSeries_high_resolution_user.csv
```

# Business hours with 15-minute granularity

```bash
# Business hours with 15-minute granularity
catocli query appStatsTimeSeries '{
    "buckets": 32,
    "dimension": [
        {"fieldName": "application_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "utc.2025-10-{15/08:00:00--15/16:00:00}"
}' -f csv --csv-filename appStatsTimeSeries_bus_hours.csv
```

# User activity patterns with application usage

```bash
# User activity patterns with application usage
catocli query appStatsTimeSeries '{
    "buckets": 48,
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "categories"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename appStatsTimeSeries_user_by_category.csv
```

## Post-Aggregation Filter Examples (postAggFilters)

### 1. High-Bandwidth Users Over Time (>500MB per hour)

Track users whose traffic exceeds 500MB per hour bucket over the last day:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 24,
    "dimension": [
        {"fieldName": "user_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "traffic",
                "operator": "gt",
                "values": ["524288000"]
            }
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appStatsTimeSeries_high_traffic_users.csv
```

### 2. Applications with Minimum Flow Count Threshold

Identify applications creating at least 50 flows per time bucket over a week:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 168,
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "category"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "flows_created"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "flows_created",
                "operator": "gte",
                "values": ["50"]
            }
        }
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appStatsTimeSeries_high_flow_apps.csv
```

### 3. Peak Upstream Traffic Analysis

Show time series where maximum upstream traffic exceeds 100MB in any 15-minute interval:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 96,
    "dimension": [
        {"fieldName": "src_site_name"},
        {"fieldName": "application_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "max", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "max",
            "filter": {
                "fieldName": "upstream",
                "operator": "gt",
                "values": ["104857600"]
            }
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appStatsTimeSeries_peak_upstream.csv
```

### 4. Monitoring Users with Traffic Between Thresholds

Track users with traffic between 100MB and 500MB per bucket over 2 days:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 48,
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "src_site_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "downstream"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "traffic",
                "operator": "between",
                "values": ["104857600", "524288000"]
            }
        }
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename=appStatsTimeSeries_moderate_traffic_users.csv
```

### 5. High-Activity Periods for Cloud Applications

Analyze cloud applications with average traffic exceeding 50MB per bucket during business hours:

```bash
catocli query appStatsTimeSeries '{
    "buckets": 32,
    "dimension": [
        {"fieldName": "application_name"}
    ],
    "perSecond": false,
    "measure": [
        {"aggType": "avg", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "count", "fieldName": "flows_created"}
    ],
    "appStatsFilter": [
        {
            "fieldName": "is_cloud_app",
            "operator": "is",
            "values": ["true"]
        }
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "avg",
            "filter": {
                "fieldName": "traffic",
                "operator": "gte",
                "values": ["52428800"]
            }
        }
    ],
    "timeFrame": "utc.2025-10-{15/08:00:00--15/16:00:00}"
}' -f csv --csv-filename=appStatsTimeSeries_cloud_app_peaks.csv
```

## Field Name Reference

### Valid values for appStatsPostAggFilter, appStatsFilter, dimension and measure
Valid values: `ad_name`, `app`, `application`, `application_description`, `application_id`, `application_name`, `application_risk_level`, `application_risk_score`, `categories`, `category`, `configured_host_name`, `description`, `dest_ip`, `dest_is_site_or_vpn`, `dest_site`, `dest_site_id`, `dest_site_name`, `device_name`, `discovered_app`, `domain`, `downstream`, `flows_created`, `hq_location`, `ip`, `is_cloud_app`, `is_sanctioned_app`, `ISP_name`, `new_app`, `risk_level`, `risk_score`, `sanctioned`, `site_country`, `site_state`, `socket_interface`, `src_country`, `src_country_code`, `src_ip`, `src_is_site_or_vpn`, `src_isp_ip`, `src_site_country_code`, `src_site_id`, `src_site_name`, `src_site_state`, `subnet`, `subnet_name`, `tld`, `traffic`, `traffic_direction`, `upstream`, `user_id`, `user_name`, `vpn_user_id`




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


#### Operation Arguments for query.appStatsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`buckets` [Int] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
