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
