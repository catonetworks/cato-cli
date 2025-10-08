
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

```bash
catocli query appStatsTimeSeries -h

catocli query appStatsTimeSeries <json>

catocli query appStatsTimeSeries "$(cat < query.appStatsTimeSeries.json)"

catocli query appStatsTimeSeries '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"dimension":{"fieldName":"ad_name"},"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"timeFrame":"example_value"}'

catocli query appStatsTimeSeries '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "dimension": {
        "fieldName": "ad_name"
    },
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
        "trend": true
    },
    "timeFrame": "example_value"
}'
```

## Advanced Usage
# Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

```bash
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
    "timeFrame": "last.PT1H"
}'
```

# Query to export WANBOUND traffic including upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

```bash
catocli query appStatsTimeSeries '{
    "appStatsFilter": [
        {
            "fieldName": "traffic_direction",
            "operator": "is",
            "values": [
                "WANBOUND"
            ]
        }
    ],
    "buckets": 24,
    "dimension": [
        {
            "fieldName": "application_name"
        },
        {
            "fieldName": "user_name"
        }
    ],
    "measure": [
        {
            "aggType": "sum",
            "fieldName": "traffic"
        },
        {
            "aggType": "sum",
            "fieldName": "upstream"
        },
        {
            "aggType": "sum",
            "fieldName": "downstream"
        }
    ],
    "timeFrame": "last.P1D"
}'
```



#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- `"last.PT5M"` = Previous 5 minutes
- `"last.PT1H"` = Previous 1 hour  
- `"last.P1D"` = Previous 1 day
- `"last.P14D"` = Previous 14 days
- `"last.P1M"` = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: `"utc.2023-02-{28/00:00:00--28/23:59:59}"`
- Multiple days: `"utc.2023-02-{25/00:00:00--28/23:59:59}"`  
- Specific hours: `"utc.2023-02-{28/09:00:00--28/17:00:00}"`
- Across months: `"utc.2023-{01-28/00:00:00--02-03/23:59:59}"`


#### Operation Arguments for query.appStatsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
