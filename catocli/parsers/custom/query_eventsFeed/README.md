
## CATO-CLI - Enhanced query.eventsFeed:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsFeed) for documentation on this operation.

### Basic Usage for query.eventsFeed:

```bash
# Show help for all available options
catocli query eventsFeed -h

# Standard eventsFeed query (basic GraphQL mode)
catocli query eventsFeed '{"marker": ""}'

# Start from beginning of event queue
catocli query eventsFeed '{"marker": ""}' -p

# Use a JSON file for complex queries
catocli query eventsFeed "$(cat query.eventsFeed.json)"
```

### Enhanced Usage (with advanced features):

The enhanced eventsFeed supports additional features like marker persistence, continuous polling, filtering, and streaming.

```bash
# Basic enhanced mode: fetch once and print events
catocli query eventsFeed --print-events --prettify

# Start from beginning with run mode (continuous polling)
catocli query eventsFeed --run --print-events -v

# Use marker file for persistent position tracking
catocli query eventsFeed --marker-file=./events-marker.txt --print-events

# Continuous mode with marker persistence
catocli query eventsFeed --run --marker-file=./events-marker.txt --print-events -v

# Filter by event types
catocli query eventsFeed --print-events --event-types="Connectivity,Security"

# Filter by event sub-types
catocli query eventsFeed --print-events --event-sub-types="Internet Firewall,WAN Firewall"

# Network streaming with newlines
catocli query eventsFeed --run -n 192.168.1.100:8000 --append-new-line -v

# Send to Azure Sentinel
catocli query eventsFeed --run -z "workspace-id:shared-key"

# Combined: display locally AND stream to network
catocli query eventsFeed --run --print-events --prettify -n 192.168.1.100:8000 -anl

# With fetch and runtime limits
catocli query eventsFeed --run --print-events --fetch-limit=50 --runtime-limit=3600

# Very verbose debugging
catocli query eventsFeed --marker-file=./marker.txt --print-events -vv
```


#### Operation Arguments for query.eventsFeed ####

##### Core GraphQL Arguments:
`accountIDs` [ID[]] - (required) List of Unique Account Identifiers.    
`eventFeedFieldFilterInput` [EventFeedFieldFilterInput[]] - (required) N/A    
`fieldNames` [EventFieldName[]] - (required) N/A Default Value: ['access_method', 'account_id', 'action', 'actions_taken', 'ad_name', 'alert_id', 'always_on_configuration', 'analyst_verdict', 'api_name', 'api_type', 'app_activity', 'app_activity_category', 'app_activity_type', 'app_stack', 'application_id', 'application_name', 'application_risk', 'auth_method', 'authentication_type', 'bgp_cato_asn', 'bgp_cato_ip', 'bgp_error_code', 'bgp_peer_asn', 'bgp_peer_ip', 'bgp_route_cidr', 'bgp_suberror_code', 'bypass_duration_sec', 'bypass_method', 'bypass_reason', 'categories', 'cato_app', 'classification', 'client_cert_expires', 'client_cert_name', 'client_class', 'client_version', 'collaborator_name', 'collaborators', 'confidence_level', 'configured_host_name', 'congestion_algorithm', 'connect_on_boot', 'connection_origin', 'connector_name', 'connector_status', 'connector_type', 'container_name', 'correlation_id', 'criticality', 'custom_category_id', 'custom_category_name', 'dest_country', 'dest_country_code', 'dest_group_id', 'dest_group_name', 'dest_ip', 'dest_is_site_or_vpn', 'dest_pid', 'dest_port', 'dest_process_cmdline', 'dest_process_parent_path', 'dest_process_parent_pid', 'dest_process_path', 'dest_site_id', 'dest_site_name', 'detection_name', 'detection_stage', 'device_categories', 'device_certificate', 'device_id', 'device_manufacturer', 'device_model', 'device_name', 'device_os_type', 'device_posture_profile', 'device_type', 'directory_host_name', 'directory_ip', 'directory_sync_result', 'directory_sync_type', 'disinfect_result', 'dlp_fail_mode', 'dlp_profiles', 'dlp_scan_types', 'dns_protection_category', 'dns_query', 'domain_name', 'egress_pop_name', 'egress_site_name', 'email_subject', 'endpoint_id', 'engine_type', 'epp_engine_type', 'epp_profile', 'event_count', 'event_id', 'event_message', 'event_sub_type', 'event_type', 'failure_reason', 'file_hash', 'file_name', 'file_operation', 'file_size', 'file_type', 'final_object_status', 'flows_cardinality', 'full_path_url', 'guest_user', 'host_ip', 'host_mac', 'http_request_method', 'incident_aggregation', 'incident_id', 'indication', 'indicator', 'initial_object_status', 'internalId', 'ip_protocol', 'is_admin', 'is_admin_activity', 'is_compliant', 'is_managed', 'is_sanctioned_app', 'is_sinkhole', 'ISP_name', 'key_name', 'labels', 'link_health_is_congested', 'link_health_jitter', 'link_health_latency', 'link_health_pkt_loss', 'link_type', 'logged_in_user', 'login_type', 'matched_data_types', 'mitre_attack_subtechniques', 'mitre_attack_tactics', 'mitre_attack_techniques', 'network_access', 'network_rule', 'notification_api_error', 'notification_description', 'object_id', 'object_name', 'object_type', 'office_mode', 'os_type', 'os_version', 'out_of_band_access', 'owner', 'pac_file', 'parent_connector_name', 'pop_name', 'precedence', 'processes_count', 'producer', 'projects', 'prompt_action', 'provider_name', 'public_ip', 'qos_priority', 'qos_reported_time', 'quarantine_folder_path', 'quarantine_uuid', 'raw_data', 'recommended_actions', 'reference_url', 'referer_url', 'region_name', 'registration_code', 'resource_id', 'risk_level', 'rule_id', 'rule_name', 'service_name', 'severity', 'sharing_scope', 'sign_in_event_types', 'signature_id', 'socket_interface', 'socket_interface_id', 'socket_new_version', 'socket_old_version', 'socket_reset', 'socket_role', 'socket_serial', 'socket_version', 'split_tunnel_configuration', 'src_country', 'src_country_code', 'src_ip', 'src_is_site_or_vpn', 'src_isp_ip', 'src_pid', 'src_port', 'src_process_cmdline', 'src_process_parent_path', 'src_process_parent_pid', 'src_process_path', 'src_site_id', 'src_site_name', 'static_host', 'status', 'story_id', 'subnet_name', 'subscription_name', 'targets_cardinality', 'tcp_acceleration', 'tenant_id', 'tenant_name', 'tenant_restriction_rule_name', 'threat_confidence', 'threat_name', 'threat_reference', 'threat_score', 'threat_type', 'threat_verdict', 'time', 'time_str', 'title', 'tls_certificate_error', 'tls_error_description', 'tls_error_type', 'tls_inspection', 'tls_rule_name', 'tls_version', 'traffic_direction', 'translated_client_ip', 'translated_server_ip', 'trigger', 'trust_type', 'trusted_networks', 'tunnel_ip_protocol', 'tunnel_protocol', 'upgrade_end_time', 'upgrade_initiated_by', 'upgrade_start_time', 'url', 'user_agent', 'user_awareness_method', 'user_id', 'user_name', 'user_reference_id', 'user_risk_level', 'vendor', 'vendor_collaborator_id', 'vendor_device_id', 'vendor_device_name', 'vendor_event_id', 'vendor_policy_description', 'vendor_policy_id', 'vendor_policy_name', 'vendor_user_id', 'visible_device_id', 'vpn_lan_access', 'vpn_user_email', 'windows_domain_name', 'xff']   
`marker` [String] - (required) Marker to use to get results from    

##### Enhanced Features Arguments:
`--run` [Flag] - Enable run mode with continuous polling and advanced features
`--print-events` [Flag] - Print event records to console  
`--prettify` [Flag] - Prettify JSON output  
`--marker` [String] - Initial marker value (default: "", start of queue)  
`--marker-file` [String] - Marker file location for persistence (default: ./events-marker.txt)  
`--event-types` [String] - Comma-separated list of event types to filter on  
`--event-sub-types` [String] - Comma-separated list of event sub types to filter on  
`--fetch-limit` [Integer] - Stop if a fetch returns less than this number of events (default: 1)  
`--runtime-limit` [Integer] - Stop after this many seconds (default: unlimited)  
`-vv, --very-verbose` [Flag] - Print detailed debug information  
`--append-new-line, -anl` [Flag] - Append newline character (\n) to events sent via -n or -z  
`-n, --stream-events` [String] - Send events to host:port TCP  
`-z, --sentinel` [String] - Send to Azure Sentinel customerid:sharedkey  
`-v` [Flag] - Verbose output (inherited from catocli)  
`-p` [Flag] - Pretty print (inherited from catocli)

##### Key Features:
- **Native Authentication**: Uses ~/.cato profile credentials automatically  
- **Compression**: Leverages catocli's built-in gzip compression for performance  
- **Marker Persistence**: Automatically saves position in event queue  
- **Continuous Polling**: Supports long-running event collection  
- **Advanced Filtering**: Filter by event types and sub-types  
- **Network Streaming**: Stream events to TCP endpoints  
- **Azure Sentinel**: Direct integration with Microsoft Sentinel  
- **Rate Limiting**: Built-in API rate limit handling
