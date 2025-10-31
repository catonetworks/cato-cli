
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

```bash
catocli query appStatsTimeSeries -h

catocli query appStatsTimeSeries <json>

catocli query appStatsTimeSeries "$(cat < query.appStatsTimeSeries.json)"

catocli query appStatsTimeSeries '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"buckets":1,"dimension":{"fieldName":"ad_name"},"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'

catocli query appStatsTimeSeries '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "buckets": 1,
    "dimension": {
        "fieldName": "ad_name"
    },
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
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
