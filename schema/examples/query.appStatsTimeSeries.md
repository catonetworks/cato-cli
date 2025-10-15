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
}'
```

# Query to export WANBOUND traffic including upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

```bash
# Query to export WANBOUND traffic including upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets
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