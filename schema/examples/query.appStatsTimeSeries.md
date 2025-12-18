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

## Field Name Reference

### Valid values for appStatsFilter, dimension and measure
Valid values: `ad_name`, `app`, `application`, `application_description`, `application_id`, `application_name`, `application_risk_level`, `application_risk_score`, `categories`, `category`, `configured_host_name`, `description`, `dest_ip`, `dest_is_site_or_vpn`, `dest_site`, `dest_site_id`, `dest_site_name`, `device_name`, `discovered_app`, `domain`, `downstream`, `flows_created`, `hq_location`, `ip`, `is_cloud_app`, `is_sanctioned_app`, `ISP_name`, `new_app`, `risk_level`, `risk_score`, `sanctioned`, `site_country`, `site_state`, `socket_interface`, `src_country`, `src_country_code`, `src_ip`, `src_is_site_or_vpn`, `src_isp_ip`, `src_site_country_code`, `src_site_id`, `src_site_name`, `src_site_state`, `subnet`, `subnet_name`, `tld`, `traffic`, `traffic_direction`, `upstream`, `user_id`, `user_name`, `vpn_user_id`
