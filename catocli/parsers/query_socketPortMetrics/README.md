
## CATO-CLI - query.socketPortMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetrics) for documentation on this operation.

### Usage for query.socketPortMetrics:

```bash
catocli query socketPortMetrics -h

catocli query socketPortMetrics <json>

catocli query socketPortMetrics --json-file query.socketPortMetrics.json

catocli query socketPortMetrics '{"from":1,"limit":1,"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","alias":"string","fieldName":"account_id","trend":true},"socketPortMetricsPostAggFilter":{"aggType":"sum","filter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]}},"socketPortMetricsSort":{"alias":"string","fieldName":"account_id","order":"asc"},"timeFrame":"example_value"}'

catocli query socketPortMetrics '{
    "from": 1,
    "limit": 1,
    "socketPortMetricsDimension": {
        "fieldName": "account_id"
    },
    "socketPortMetricsFilter": {
        "fieldName": "account_id",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "socketPortMetricsMeasure": {
        "aggType": "sum",
        "alias": "string",
        "fieldName": "account_id",
        "trend": true
    },
    "socketPortMetricsPostAggFilter": {
        "aggType": "sum",
        "filter": {
            "fieldName": "account_id",
            "operator": "is",
            "values": [
                "string1",
                "string2"
            ]
        }
    },
    "socketPortMetricsSort": {
        "alias": "string",
        "fieldName": "account_id",
        "order": "asc"
    },
    "timeFrame": "example_value"
}'
```

## Advanced Usage
### Additional Examples
- 1 Day sum of traffic by site, socket_interface, device_id
- Traffic patterns by site and interface
- Traffic distribution across devices

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

## Field Name Reference

### Valid values for socketPortMetricsDimension, and socketPortMetricsMeasure
Valid values: `account_id`, `bytes_downstream`, `bytes_total`, `bytes_upstream`, `cellular_rsrp`, `cellular_rsrq`, `cellular_rssi`, `cellular_signal_strength`, `cellular_sinr`, `device_id`, `ha_role`, `physical_interface_type`, `sim_num`, `site_id`, `site_name`, `socket_interface`, `socket_interface_role`, `throughput_downstream`, `throughput_upstream`, `transport_type`



#### Operation Arguments for query.socketPortMetrics ####

