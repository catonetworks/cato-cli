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
