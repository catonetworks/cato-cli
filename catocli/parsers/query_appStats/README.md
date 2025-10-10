
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStats) for documentation on this operation.

### Usage for query.appStats:

```bash
catocli query appStats -h

catocli query appStats <json>

catocli query appStats "$(cat < query.appStats.json)"

catocli query appStats '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"appStatsSort":{"fieldName":"ad_name","order":"asc"},"dimension":{"fieldName":"ad_name"},"from":1,"limit":1,"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"timeFrame":"example_value"}'

catocli query appStats '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "appStatsSort": {
        "fieldName": "ad_name",
        "order": "asc"
    },
    "dimension": {
        "fieldName": "ad_name"
    },
    "from": 1,
    "limit": 1,
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
        "trend": true
    },
    "timeFrame": "example_value"
}'
```

## Advanced Usage
### Additional Examples
- Query to export user activity as in flows_created, for distinct users (user_name) for the last day
- Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day

# Query to export user activity as in flows_created, for distinct users (user_name) for the last day

```bash
# Query to export user activity as in flows_created, for distinct users (user_name) for the last day
catocli query appStats '{
    "appStatsFilter": [],
    "appStatsSort": [],
    "dimension": [
        {
            "fieldName": "user_name"
        }
    ],
    "measure": [
        {
            "aggType": "sum",
            "fieldName": "flows_created"
        },
        {
            "aggType": "count_distinct",
            "fieldName": "user_name"
        }
    ],
    "timeFrame": "last.P1M"
}'
```

# Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day

```bash
## Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day
catocli query appStats '{
    "appStatsFilter": [],
    "appStatsSort": [],
    "dimension": [
        {
            "fieldName": "application_name"
        },
        {
            "fieldName": "user_name"
        },
        {
            "fieldName": "risk_score"
        }
    ],
    "measure": [
        {
            "aggType": "sum",
            "fieldName": "downstream"
        },
        {
            "aggType": "sum",
            "fieldName": "upstream"
        },
        {
            "aggType": "sum",
            "fieldName": "traffic"
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv
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


#### Operation Arguments for query.appStats ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`appStatsSort` [AppStatsSort[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
