# 1 Day sum of traffic by site, socket_interface, device_id

```bash
# 1 Day sum of traffic by site, socket_interface, device_id
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {
            "fieldName": "socket_interface"
        },
        {
            "fieldName": "device_id"
        },
        {
            "fieldName": "site_id"
        },
        {
            "fieldName": "site_name"
        }
    ],
    "socketPortMetricsFilter": [],
    "socketPortMetricsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "bytes_upstream"
        },
        {
            "aggType": "sum",
            "fieldName": "bytes_downstream"
        },
        {
            "aggType": "sum",
            "fieldName": "bytes_total"
        }
    ],
    "socketPortMetricsSort": [],
    "timeFrame": "last.P1D"
}'
```

# Traffic patterns by site and interface

```bash
# Traffic patterns by site and interface
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {"fieldName": "socket_interface"},
        {"fieldName": "device_id"},
        {"fieldName": "site_id"},
        {"fieldName": "site_name"}
    ],
    "socketPortMetricsMeasure": [
        {"aggType": "sum", "fieldName": "bytes_upstream"},
        {"aggType": "sum", "fieldName": "bytes_downstream"},
        {"aggType": "sum", "fieldName": "bytes_total"}
    ],
    "socketPortMetricsSort": [
        {"fieldName": "bytes_total", "order": "desc"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetrics_traffic_by_site_interface.csv
```

# Traffic distribution across devices

```bash
# Traffic distribution across devices
catocli query socketPortMetrics '{
    "socketPortMetricsDimension": [
        {
            "fieldName": "device_id"
        },
        {
            "fieldName": "site_name"
        }
    ],
    "socketPortMetricsFilter": [],
    "socketPortMetricsMeasure": [
        {
            "aggType": "sum",
            "fieldName": "bytes_total"
        },
        {
            "aggType": "avg",
            "fieldName": "throughput_downstream"
        },
        {
            "aggType": "avg",
            "fieldName": "throughput_upstream"
        }
    ],
    "socketPortMetricsSort": [
        {
            "fieldName": "bytes_total",
            "order": "desc"
        }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename socketPortMetrics_site_bw_by_device.csv
```
