
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

```bash
catocli query eventsTimeSeries -h

catocli query eventsTimeSeries <json>

catocli query eventsTimeSeries "$(cat < query.eventsTimeSeries.json)"

catocli query eventsTimeSeries '{"buckets":1,"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","fieldName":"access_method","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'

catocli query eventsTimeSeries '{
    "buckets": 1,
    "eventsDimension": {
        "fieldName": "access_method"
    },
    "eventsFilter": {
        "fieldName": "access_method",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "eventsMeasure": {
        "aggType": "sum",
        "fieldName": "access_method",
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
- Weekly break down by hour of Internet Firewall events by rule_name
- Weekly hourly breakdown by hour of sum of site events
- 1 hour 5 min increment of sum of site events used for detecting throttling
- 1 hour 5 min increments of sum of site events used for detecting throttling
- Basic event count - weekly hourly
- Security Events Analysis
- Security Events Analysis - Daily breakdown of security events
- Connectivity Events by Country
- Connectivity Events by Country - Weekly breakdown with country dimensions
- Socket Connectivity Analysis
- Socket Connectivity Analysis - Connection events by socket interface

# Weekly break down by hour of Internet Firewall events by rule_name

```bash
# Weekly break down by hour of Internet Firewall events by rule_name
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [
        {
            "fieldName": "rule_name"
        }
    ],
    "eventsFilter": [
        {
            "fieldName": "event_sub_type",
            "operator": "is",
            "values": [
                "Internet Firewall"
            ]
        }
    ],
    "eventsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=eventsTimeSeries_by_subType.csv
```

# Weekly hourly breakdown by hour of sum of site events

```bash
# Weekly hourly breakdown by hour of sum of site events
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "src_is_site_or_vpn",
            "operator": "is",
            "values": [
                "Site"
            ]
        }
    ],
    "eventsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=eventsTimeSeries_hourly_site_events.csv
```


# 1 hour 5 min increment of sum of site events used for detecting throttling

```bash
# 1 hour 5 min increments of sum of site events used for detecting throttling
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [],
    "eventsFilter": [
        {
            "fieldName": "src_is_site_or_vpn",
            "operator": "is",
            "values": [
                "Site"
            ]
        }
    ],
    "eventsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=eventsTimeSeries_15_min_site_events.csv
```

# Basic event count - weekly hourly

```bash
# Basic event count - weekly hourly
catocli query eventsTimeSeries '{
    "buckets": 168,
    "eventsDimension": [
        {
            "fieldName": "rule_name"
        }
    ],
    "eventsFilter": [],
    "eventsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=eventsTimeSeries_weekly_hourly_events.csv
```

# Security Events Analysis

```bash
# Security Events Analysis - Daily breakdown of security events
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
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=eventsTimeSeries_daily_security_events.csv
```

# Connectivity Events by Country

```bash
# Connectivity Events by Country - Weekly breakdown with country dimensions
catocli query eventsTimeSeries '{
    "buckets": 7,
    "eventsDimension": [
        {
            "fieldName": "src_country"
        }
    ],
    "eventsFilter": [
        {
            "fieldName": "event_type",
            "operator": "is",
            "values": ["Connectivity"]
        }
    ],
    "eventsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=eventsTimeSeries_weekly_daily_by_country.csv
```

# Socket Connectivity Analysis

```bash
# Socket Connectivity Analysis - Connection events by socket interface
catocli query eventsTimeSeries '{
    "buckets": 7,
    "eventsDimension": [
        {
            "fieldName": "socket_interface"
        }
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
        {
            "aggType": "sum",
            "fieldName": "event_count"
        }
    ],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=eventsTimeSeries_daily_socket_connect.csv
```

## Output Format Options

The eventsTimeSeries query supports multiple output formats:

### Enhanced JSON Format (default)
Returns formatted JSON with granularity multiplication applied to sum aggregations when appropriate:
```bash
catocli query eventsTimeSeries '{...}'
```

### Raw JSON Format
Returns the original API response without formatting:
```bash
catocli query eventsTimeSeries '{...}' -raw
```

### CSV Format
Exports data to CSV file with granularity-adjusted values:
```bash
catocli query eventsTimeSeries '{...}' -f csv
```

### Custom CSV filename with timestamp
```bash
catocli query eventsTimeSeries '{...}' -f csv --csv-filename "my_events" --append-timestamp
```

## Granularity Multiplication

When using sum aggregations on count fields like `event_count`, the formatter automatically multiplies fractional values by the granularity period to provide meaningful totals. This is especially useful for time-series data where the API returns normalized values that need to be scaled to the actual time period.

**Example:**
- Original API value: 0.096 events per period
- Granularity: 3600 seconds (1 hour)
- Computed value: 0.096 × 3600 = 345.6 total events

Use the `-raw` flag to see the original unprocessed values if needed.

## Additional Resources

- [Cato API Documentation](https://api.catonetworks.com/documentation/#query-eventsTimeSeries)






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


#### Operation Arguments for query.eventsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`buckets` [Int] - (required) N/A    
`eventsDimension` [EventsDimension[]] - (required) N/A    
`eventsFilter` [EventsFilter[]] - (required) N/A    
`eventsMeasure` [EventsMeasure[]] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
