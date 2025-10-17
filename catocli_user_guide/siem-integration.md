# CatoCLI SIEM Integration Guide

This guide demonstrates how to integrate CatoCLI's `eventsFeed` query with various SIEM (Security Information and Event Management) platforms for real-time security monitoring and analysis.

## Overview

The CatoCLI `eventsFeed` query provides real-time streaming access to Cato Networks security and network events, making it ideal for SIEM integration. The eventsFeed supports:

- **Continuous polling** with persistent marker tracking
- **Event filtering** by type and sub-type
- **Multiple output formats** (JSON, network streaming, Azure Sentinel)
- **Real-time streaming** to network endpoints
- **Built-in Azure Sentinel integration**

## Event Types and Categories

CatoCLI eventsFeed supports various event types including:

- **Security Events**: Internet Firewall, WAN Firewall, Anti-Malware, IPS
- **Connectivity Events**: Site connectivity, WAN link status, tunnels
- **Network Events**: Bandwidth utilization, performance metrics
- **Authentication Events**: User login/logout, VPN connections

## Basic eventsFeed Usage

### Simple Event Retrieval
```bash
# Fetch events once and display
catocli query eventsFeed --print-events --prettify

# Start from beginning of event queue
catocli query eventsFeed '{"marker": ""}' --print-events
```

### Continuous Event Streaming
```bash
# Continuous polling with marker persistence
catocli query eventsFeed --run --print-events --marker-file=./events-marker.txt -v

# Filter by specific event types
catocli query eventsFeed --run --print-events --event-types="Security,Connectivity"

# Filter by event sub-types
catocli query eventsFeed --run --print-events --event-sub-types="Internet Firewall,WAN Firewall"
```

## SIEM Platform Integrations

### 1. Microsoft Azure Sentinel

Azure Sentinel has built-in support in CatoCLI:

```bash
# Direct integration with Azure Sentinel
catocli query eventsFeed --run -z "workspace-id:shared-key"

# With event filtering and local display
catocli query eventsFeed --run --print-events --prettify -z "workspace-id:shared-key" --event-types="Security"
```

**Setup Steps:**
1. Obtain your Azure Sentinel workspace ID and shared key
2. Configure CatoCLI with your Cato API credentials
3. Run the command with your workspace credentials
4. Events will automatically appear in Azure Sentinel under custom logs

### 2. Splunk Integration

#### Method 1: TCP Network Streaming
```bash
# Stream events to Splunk Universal Forwarder
catocli query eventsFeed --run -n 192.168.1.100:8000 --append-new-line -v

# With event filtering
catocli query eventsFeed --run -n 192.168.1.100:8000 --append-new-line --event-types="Security,Connectivity"
```

**Splunk Configuration (inputs.conf):**
```ini
[tcp://8000]
connection_host = ip
sourcetype = cato_events
index = security
```

#### Method 2: File-based Integration
```bash
# Write events to file for Splunk monitoring
catocli query eventsFeed --run --print-events > /var/log/cato/events.log &

# With log rotation
catocli query eventsFeed --run --print-events --fetch-limit=1000 --runtime-limit=3600 >> /var/log/cato/events-$(date +%Y%m%d).log
```

**Splunk Configuration (inputs.conf):**
```ini
[monitor:///var/log/cato/events*.log]
sourcetype = cato_events
index = security
```

### 3. Elasticsearch/ELK Stack

#### Using Logstash TCP Input
```bash
# Stream to Logstash
catocli query eventsFeed --run -n localhost:5000 --append-new-line --prettify
```

**Logstash Configuration:**
```ruby
input {
  tcp {
    port => 5000
    codec => json_lines
  }
}

filter {
  mutate {
    add_field => { "source" => "cato_networks" }
  }
  
  date {
    match => [ "timestamp", "ISO8601" ]
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "cato-events-%{+YYYY.MM.dd}"
  }
}
```

#### Using Filebeat
```bash
# Write to file for Filebeat monitoring
catocli query eventsFeed --run --print-events --prettify > /var/log/cato/events.json
```

**Filebeat Configuration (filebeat.yml):**
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/cato/events.json
  json.keys_under_root: true
  json.add_error_key: true
  fields:
    source: cato_networks
  fields_under_root: true

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "cato-events-%{+yyyy.MM.dd}"
```

### 4. QRadar Integration

#### Using Syslog Protocol
```bash
# Convert JSON to syslog format and send to QRadar
catocli query eventsFeed --run --print-events | \
while read line; do
  echo "<134>$(date '+%b %d %H:%M:%S') cato-events: $line" | nc -u qradar-host 514
done
```

#### Using File Collection
```bash
# Generate QRadar-formatted logs
catocli query eventsFeed --run --print-events --event-types="Security" | \
awk '{print strftime("%Y-%m-%d %H:%M:%S"), "CATO", $0}' >> /var/log/cato-qradar.log
```

### 5. IBM Security QRadar LEEF Format

```bash
# Convert to LEEF format for QRadar
catocli query eventsFeed --run --print-events | \
python3 -c "
import sys
import json
for line in sys.stdin:
    try:
        event = json.loads(line.strip())
        leef = f\"LEEF:2.0|Cato Networks|CatoCLI|1.0|{event.get('eventType', 'Unknown')}|\"
        print(leef + '|'.join([f'{k}={v}' for k,v in event.items()]))
    except:
        pass
" | nc -u qradar-host 514
```

## Advanced Integration Patterns

### High Availability Setup
```bash
#!/bin/bash
# HA eventsFeed script with failover

MARKER_FILE="/var/lib/cato/events-marker.txt"
LOG_FILE="/var/log/cato/events.log"
LOCK_FILE="/var/lock/cato-eventsfeed.lock"

# Prevent multiple instances
exec 200>"$LOCK_FILE"
flock -n 200 || exit 1

while true; do
    catocli query eventsFeed \
        --run \
        --print-events \
        --marker-file="$MARKER_FILE" \
        --runtime-limit=3600 \
        --event-types="Security,Connectivity" >> "$LOG_FILE" 2>&1
    
    # Restart after 1 hour or on failure
    sleep 5
done
```

### Event Filtering and Enrichment
```python
#!/usr/bin/env python3
import subprocess
import json
import sys
import logging

def enrich_event(event):
    """Add additional context to events."""
    event['enriched_timestamp'] = event.get('timestamp')
    event['severity'] = 'high' if event.get('eventType') == 'Security' else 'medium'
    return event

def main():
    cmd = [
        'catocli', 'query', 'eventsFeed',
        '--run', '--print-events',
        '--event-types=Security'
    ]
    
    process = subprocess.Popen(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    for line in process.stdout:
        try:
            event = json.loads(line.strip())
            enriched_event = enrich_event(event)
            
            # Send to SIEM (example: TCP socket)
            print(json.dumps(enriched_event))
            sys.stdout.flush()
            
        except json.JSONDecodeError:
            logging.warning(f"Invalid JSON: {line.strip()}")

if __name__ == "__main__":
    main()
```

### Docker Integration
```dockerfile
FROM python:3.9-slim

RUN pip install catocli

COPY eventsfeed-siem.py /app/
COPY catocli-config /root/.cato/

WORKDIR /app

CMD ["python", "eventsfeed-siem.py"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  cato-eventsfeed:
    build: .
    environment:
      - SIEM_HOST=splunk-host
      - SIEM_PORT=8000
    volumes:
      - ./logs:/var/log/cato
    restart: unless-stopped
```

## Event Schema and Fields

Common event fields in CatoCLI eventsFeed:

```json
{
  "timestamp": "2023-12-01T10:30:00Z",
  "eventType": "Security",
  "eventSubType": "Internet Firewall",
  "sourceIP": "192.168.1.100",
  "destinationIP": "8.8.8.8",
  "protocol": "TCP",
  "port": 80,
  "action": "BLOCK",
  "ruleName": "Block Malicious Sites",
  "siteName": "Branch Office",
  "userName": "john.doe@company.com",
  "severity": "High",
  "threatName": "Malware.Generic"
}
```

## Monitoring and Troubleshooting

### Health Monitoring Script
```bash
#!/bin/bash
# Monitor eventsFeed health

MARKER_FILE="/var/lib/cato/events-marker.txt"
LAST_UPDATE=$(stat -c %Y "$MARKER_FILE" 2>/dev/null || echo 0)
CURRENT_TIME=$(date +%s)
AGE=$((CURRENT_TIME - LAST_UPDATE))

if [ $AGE -gt 300 ]; then  # 5 minutes
    echo "WARNING: EventsFeed marker not updated in $AGE seconds"
    # Restart eventsFeed or send alert
fi
```

### Debug Mode
```bash
# Enable verbose debugging
catocli query eventsFeed --run --print-events -vv --marker-file=./debug-marker.txt

# Test connectivity without continuous mode
catocli query eventsFeed --print-events --fetch-limit=5
```

## Best Practices

1. **Use Marker Files**: Always use `--marker-file` for persistent position tracking
2. **Event Filtering**: Filter events at source using `--event-types` and `--event-sub-types`
3. **Rate Limiting**: Use `--fetch-limit` and `--runtime-limit` to control resource usage
4. **Error Handling**: Implement proper error handling and restart logic
5. **Monitoring**: Monitor the health of your eventsFeed integration
6. **Security**: Protect API credentials and use secure transport protocols

## Troubleshooting Common Issues

1. **Missing Events**: Check marker file permissions and network connectivity
2. **High CPU Usage**: Reduce fetch frequency or add event filtering
3. **Memory Issues**: Implement log rotation and cleanup procedures
4. **Authentication Errors**: Verify CatoCLI profile configuration
5. **Network Issues**: Test connectivity to SIEM endpoints

This guide provides comprehensive integration patterns for connecting CatoCLI eventsFeed with major SIEM platforms. Adapt the examples to your specific environment and security requirements.