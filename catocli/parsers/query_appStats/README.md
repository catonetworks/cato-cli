
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStats) for documentation on this operation.

### Usage for query.appStats:

```bash
catocli query appStats -h

catocli query appStats <json>

catocli query appStats --json-file query.appStats.json

catocli query appStats '{"appStatsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"appStatsSort":{"fieldName":"account_id","order":"asc"},"dimension":{"fieldName":"account_id"},"from":1,"limit":1,"measure":{"aggType":"sum","fieldName":"account_id","trend":true},"timeFrame":"example_value"}'

catocli query appStats '{
    "appStatsFilter": {
        "fieldName": "account_id",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "appStatsSort": {
        "fieldName": "account_id",
        "order": "asc"
    },
    "dimension": {
        "fieldName": "account_id"
    },
    "from": 1,
    "limit": 1,
    "measure": {
        "aggType": "sum",
        "fieldName": "account_id",
        "trend": true
    },
    "timeFrame": "example_value"
}'
```

## Advanced Usage
### Additional Examples
- Query to export user activity as in flows_created, for distinct users (user_name) for the last day
- Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day
- Track daily user engagement and flow creation
- Analyze applications by usage and security risk
- Analyze applications by usage and security risk:
- Top applications weekly by bandwidth
- Daily per-user bandwidth consumption
- Monthly traffic patterns by country

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
## Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day exported to csv format
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
}' -f csv --csv-filename app_user_account_metrics_report.csv
```

# Track daily user engagement and flow creation

```bash
# Track daily user engagement and flow creation
catocli query appStats '{
    "dimension": [
      {"fieldName": "user_name"},
      {"fieldName": "domain"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "flows_created"},
        {"aggType": "count_distinct", "fieldName": "user_name"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appstats_user_activity.csv
```

# Analyze applications by usage and security risk

```bash
# Analyze applications by usage and security risk:
catocli query appStats '{
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "user_name"},
        {"fieldName": "risk_score"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "downstream"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appstats_user_risk_report.csv
```

# Top applications weekly by bandwidth

```bash
# Top applications weekly by bandwidth
catocli query appStats '{
    "dimension": [{"fieldName": "application_name"}],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "appStatsSort": [
        {"fieldName": "traffic", "order": "desc"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appstats_app_utilization.csv
```

# Daily per-user bandwidth consumption

```bash
# Daily per-user bandwidth consumption
catocli query appStats '{
    "dimension": [
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "downstream"},
        {"aggType": "sum", "fieldName": "upstream"},
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appstats_user_bw.csv
```

### 5. High-Risk Application Analysis

Focus on applications with elevated risk scores:

```bash
catocli query appStats '{
    "appStatsFilter": [
        {
            "fieldName": "risk_score",
            "operator": "gte", 
            "values": ["5"]
        }
    ],
    "appStatsSort": [
        {
            "fieldName": "risk_score",
            "order": "desc"
        }
    ],
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "risk_score"},
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appstats_app_by_risk.csv
```

# Monthly traffic patterns by country

```bash
# Monthly traffic patterns by country
catocli query appStats '{
    "dimension": [
        {"fieldName": "site_country"},
        {"fieldName": "src_site_country_code"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "count_distinct", "fieldName": "user_name"}
    ],
    "timeFrame": "last.P1M"
}' -f csv --csv-filename=appstats_by_country.csv
```

## Field Name Reference

### Valid values for appStatsFilter, dimension and measure
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


#### Operation Arguments for query.appStats ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`appStatsSort` [AppStatsSort[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
