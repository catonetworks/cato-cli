
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

```bash
catocli query eventsTimeSeries -h

catocli query eventsTimeSeries <json>

catocli query eventsTimeSeries --json-file query.eventsTimeSeries.json

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

## Field Name Reference

### Valid values for eventsDimension, eventsFilter, and eventsMeasure
Valid values: `access_method`, `account_id`, `action`, `actions_taken`, `activity_resource_id`, `actor_type`, `ad_name`, `adaptive_rule_ids`, `adaptive_rule_names`, `adaptive_rule_scope`, `adaptive_rule_threat_categories`, `alert_id`, `always_on_configuration`, `analyst_verdict`, `api_name`, `api_type`, `app_activity`, `app_activity_category`, `app_activity_type`, `app_stack`, `application_id`, `application_name`, `application_risk`, `auth_method`, `authentication_type`, `bgp_cato_asn`, `bgp_cato_ip`, `bgp_error_code`, `bgp_peer_asn`, `bgp_peer_ip`, `bgp_route_cidr`, `bgp_suberror_code`, `bypass_duration_sec`, `bypass_method`, `bypass_reason`, `categories`, `cato_app`, `classification`, `client_cert_expires`, `client_cert_name`, `client_class`, `client_connection_mode`, `client_version`, `collaborator_name`, `collaborators`, `confidence_level`, `configured_host_name`, `congestion_algorithm`, `connect_on_boot`, `connection_origin`, `connector_id`, `connector_name`, `connector_status`, `connector_type`, `container_name`, `correlation_id`, `criticality`, `custom_category_id`, `custom_category_name`, `dest_country`, `dest_country_code`, `dest_group_id`, `dest_group_name`, `dest_ip`, `dest_is_site_or_vpn`, `dest_pid`, `dest_port`, `dest_process_cmdline`, `dest_process_parent_path`, `dest_process_parent_pid`, `dest_process_path`, `dest_site_id`, `dest_site_name`, `detection_name`, `detection_stage`, `device_categories`, `device_certificate`, `device_id`, `device_manufacturer`, `device_model`, `device_name`, `device_os_type`, `device_posture_profile`, `device_type`, `directory_host_name`, `directory_ip`, `directory_sync_result`, `directory_sync_type`, `disinfect_result`, `dlp_fail_mode`, `dlp_profiles`, `dlp_scan_types`, `dns_protection_category`, `dns_query`, `dns_request_type`, `domain_name`, `egress_pop_name`, `egress_site_name`, `email_subject`, `endpoint_id`, `engine_type`, `epp_engine_type`, `epp_profile`, `event_count`, `event_id`, `event_message`, `event_sub_type`, `event_type`, `failure_reason`, `file_hash`, `file_name`, `file_operation`, `file_size`, `file_type`, `final_object_status`, `flows_cardinality`, `full_path_url`, `guest_user`, `host_ip`, `host_mac`, `http_request_method`, `http_response_code`, `incident_aggregation`, `incident_id`, `indication`, `indicator`, `initial_object_status`, `internalId`, `ip_protocol`, `is_admin`, `is_admin_activity`, `is_compliant`, `is_managed`, `is_sanctioned_app`, `is_sinkhole`, `ISP_name`, `key_name`, `labels`, `link_health_is_congested`, `link_health_jitter`, `link_health_latency`, `link_health_pkt_loss`, `link_type`, `logged_in_user`, `login_type`, `matched_data_types`, `mitre_attack_subtechniques`, `mitre_attack_tactics`, `mitre_attack_techniques`, `network_access`, `network_rule`, `notification_api_error`, `notification_description`, `object_id`, `object_name`, `object_type`, `office_mode`, `os_type`, `os_version`, `out_of_band_access`, `owner`, `pac_file`, `parent_connector_name`, `pop_name`, `precedence`, `processes_count`, `producer`, `projects`, `prompt_action`, `provider_name`, `public_ip`, `qos_priority`, `qos_reported_time`, `quarantine_folder_path`, `quarantine_uuid`, `raw_data`, `recommended_actions`, `reference_url`, `referer_url`, `region_name`, `registration_code`, `request_size`, `resource_id`, `resource_name`, `resource_type`, `response_size`, `risk_level`, `rule_expiration_time`, `rule_id`, `rule_name`, `service_name`, `severity`, `sharing_scope`, `sign_in_event_types`, `signature_id`, `socket_interface`, `socket_interface_id`, `socket_new_version`, `socket_old_version`, `socket_reset`, `socket_role`, `socket_serial`, `socket_version`, `split_tunnel_configuration`, `src_country`, `src_country_code`, `src_ip`, `src_is_site_or_vpn`, `src_isp_ip`, `src_pid`, `src_port`, `src_process_cmdline`, `src_process_parent_path`, `src_process_parent_pid`, `src_process_path`, `src_site_id`, `src_site_name`, `static_host`, `status`, `story_id`, `subnet_name`, `subscription_name`, `targets_cardinality`, `tcp_acceleration`, `tenant_id`, `tenant_name`, `tenant_restriction_rule_name`, `threat_confidence`, `threat_name`, `threat_reference`, `threat_score`, `threat_type`, `threat_verdict`, `time`, `time_str`, `title`, `tls_certificate_error`, `tls_error_description`, `tls_error_type`, `tls_inspection`, `tls_rule_name`, `tls_version`, `traffic_direction`, `transaction_size`, `translated_client_ip`, `translated_server_ip`, `trigger`, `trust_type`, `trusted_networks`, `tunnel_ip_protocol`, `tunnel_protocol`, `upgrade_end_time`, `upgrade_initiated_by`, `upgrade_start_time`, `url`, `user_agent`, `user_awareness_method`, `user_id`, `user_name`, `user_origin`, `user_reference_id`, `user_risk_level`, `vendor`, `vendor_collaborator_id`, `vendor_device_id`, `vendor_device_name`, `vendor_event_id`, `vendor_policy_description`, `vendor_policy_id`, `vendor_policy_name`, `vendor_user_id`, `visible_device_id`, `vpn_lan_access`, `vpn_user_email`, `wifi_authentication_type`, `wifi_channel`, `wifi_description`, `wifi_radio_band`, `wifi_signal_strength`, `wifi_ssid`, `windows_domain_name`, `xff`




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
