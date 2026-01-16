# Application Statistics Query Guide

The `appStats` query provides comprehensive analysis of user activity and application usage within your Cato Networks environment, enabling you to understand traffic patterns, application usage, and user behavior.

## Overview

Application statistics help you analyze:
- **User Activity**: Flow creation, session counts, and traffic patterns per user
- **Application Usage**: Bandwidth consumption and session patterns by application
- **Risk Analysis**: Application risk scores and security-related traffic
- **Traffic Distribution**: Upstream, downstream, and total traffic analysis
- **Usage Trends**: Application and user behavior over specified time periods

## Basic Usage

```bash
catocli query appStats '{
    "dimension": [{"fieldName": "user_name"}],
    "measure": [{"aggType": "sum", "fieldName": "flows_created"}],
    "timeFrame": "last.P1M"
}'
```

## Query Structure

```json
{
  "appStatsFilter": [],           // Filters to apply to the data
  "appStatsSort": [],             // Sort criteria for results
  "dimension": [                  // Fields to group results by
    {"fieldName": "user_name"}
  ],
  "measure": [                    // Metrics to calculate
    {
      "aggType": "sum",           // Aggregation type
      "fieldName": "flows_created"
    }
  ],
  "timeFrame": "last.P1D"        // Time range for analysis
}
```

## Available Dimensions

Group your results by these fields:

### User Dimensions
- `user_name` - Username
- `user_id` - User identifier
- `user_email` - User email address

### Application Dimensions  
- `application_name` - Application name
- `application_category` - Application category
- `application_subcategory` - Application subcategory
- `risk_score` - Application risk score

### Network Dimensions
- `site_name` - Site name
- `site_id` - Site identifier
- `src_country` - Source country
- `dst_country` - Destination country

### Traffic Dimensions
- `traffic_direction` - Traffic direction (WANBOUND, LANBOUND)
- `protocol` - Network protocol

## Available Measures

Calculate these metrics with various aggregation types:

### Traffic Measures
- `downstream` - Downstream bytes
- `upstream` - Upstream bytes  
- `traffic` - Total traffic bytes

### Session Measures
- `flows_created` - Number of flows/sessions created
- `session_duration` - Session duration

### Count Measures
- `user_name` - Distinct user count (with `count_distinct`)
- `application_name` - Distinct application count

## Aggregation Types

- `sum` - Total/sum of values
- `avg` - Average value
- `count` - Count of records
- `count_distinct` - Count of unique values
- `max` - Maximum value
- `min` - Minimum value

## Common Use Cases

### 1. User Activity Analysis

Track daily user engagement and flow creation:

```bash
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

### 2. Application Usage Report with Risk Assessment

Analyze applications by usage and security risk:

```bash
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

### 3. Top Applications by Traffic

Identify weekly bandwidth-heavy applications:

```bash
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

### 4. User Traffic Distribution

Analyze daily per-user bandwidth consumption:

```bash
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

### 6. Geographic Traffic Analysis

Analyze traffic patterns by country:

```bash
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

## Post-Aggregation Filter Examples (postAggFilters)

### 1. High-Traffic Users (>1GB Total Traffic)

Find users whose total traffic exceeds 1GB over the last 2 days:

```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "traffic",
                "operator": "gt",
                "values": ["1073741824"]
            }
        }
    ],
    "appStatsSort": [
        {"fieldName": "traffic", "order": "desc"}
    ],
    "timeFrame": "last.P2D"
}' -f csv --csv-filename=appstats_high_traffic_users.csv
```

### 2. Applications with Average Traffic Above Threshold

Identify applications where average traffic per flow exceeds 10MB:

```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "application_name"}
    ],
    "measure": [
        {"aggType": "avg", "fieldName": "traffic"},
        {"aggType": "count", "fieldName": "flows_created"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "avg",
            "filter": {
                "fieldName": "traffic",
                "operator": "gte",
                "values": ["10485760"]
            }
        }
    ],
    "appStatsSort": [
        {"fieldName": "traffic", "order": "desc"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appstats_high_avg_traffic_apps.csv
```

### 3. Active Users with Flow Count Range

Find users who created between 100 and 1000 flows in the last day:

```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "user_name"},
        {"fieldName": "src_site_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "flows_created"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "flows_created",
                "operator": "between",
                "values": ["100", "1000"]
            }
        }
    ],
    "appStatsSort": [
        {"fieldName": "flows_created", "order": "desc"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename=appstats_active_users_flow_range.csv
```

### 4. Top Applications by Maximum Downstream Traffic

Show applications where maximum downstream traffic in a single flow exceeds 500MB:

```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "category"}
    ],
    "measure": [
        {"aggType": "max", "fieldName": "downstream"},
        {"aggType": "sum", "fieldName": "downstream"},
        {"aggType": "count", "fieldName": "flows_created"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "max",
            "filter": {
                "fieldName": "downstream",
                "operator": "gt",
                "values": ["524288000"]
            }
        }
    ],
    "appStatsSort": [
        {"fieldName": "downstream", "order": "desc"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appstats_high_max_downstream.csv
```

### 5. Sites with Multiple Active Users and High Traffic

Find sites with more than 5 distinct users and total traffic exceeding 5GB:

```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "src_site_name"},
        {"fieldName": "site_country"}
    ],
    "measure": [
        {"aggType": "count_distinct", "fieldName": "user_name"},
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "appStatsPostAggFilter": [
        {
            "aggType": "count_distinct",
            "filter": {
                "fieldName": "user_name",
                "operator": "gt",
                "values": ["5"]
            }
        },
        {
            "aggType": "sum",
            "filter": {
                "fieldName": "traffic",
                "operator": "gte",
                "values": ["5368709120"]
            }
        }
    ],
    "appStatsSort": [
        {"fieldName": "traffic", "order": "desc"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename=appstats_active_sites.csv
```

## Filtering Options

### Filter Structure
```json
{
  "appStatsFilter": [
    {
      "fieldName": "field_to_filter",
      "operator": "filter_operator",
      "values": ["value1", "value2"]
    }
  ]
}
```

### Available Operators
- `is` - Exact match
- `in` - Match any of the values
- `gt` - Greater than
- `gte` - Greater than or equal
- `lt` - Less than
- `lte` - Less than or equal
- `contains` - Contains substring

### Common Filter Examples

#### Filter by Application Category
```json
{
  "appStatsFilter": [
    {
      "fieldName": "application_category",
      "operator": "is",
      "values": ["Social Media"]
    }
  ]
}
```

#### Filter by Risk Score Range
```json
{
  "appStatsFilter": [
    {
      "fieldName": "risk_score",
      "operator": "gte",
      "values": ["5"]
    }
  ]
}
```

#### Filter by Traffic Direction
```json
{
  "appStatsFilter": [
    {
      "fieldName": "traffic_direction", 
      "operator": "is",
      "values": ["WANBOUND"]
    }
  ]
}
```

## Sorting Results

### Sort Structure
```json
{
  "appStatsSort": [
    {
      "fieldName": "field_to_sort_by",
      "order": "desc"  // or "asc"
    }
  ]
}
```

### Common Sort Examples

#### Sort by Traffic Volume
```json
{
  "appStatsSort": [
    {"fieldName": "traffic", "order": "desc"}
  ]
}
```

#### Sort by User Activity
```json
{
  "appStatsSort": [
    {"fieldName": "flows_created", "order": "desc"}
  ]
}
```

## Output Formats

### Enhanced JSON (Default)
```bash
catocli query appStats '{...}'
```

### CSV Export
```bash
catocli query appStats '{...}' -f csv --csv-filename report.csv
```

### Raw JSON
```bash
catocli query appStats '{...}' -raw
```

## Time Frame Options

### Relative Time Frames
- `last.PT1H` - Last hour
- `last.P1D` - Last day
- `last.P7D` - Last week  
- `last.P1M` - Last month
- `last.P3M` - Last 3 months

### Absolute Time Frames
```bash
"timeFrame": "utc.2023-10-{01/00:00:00--31/23:59:59}"
```

## Advanced Examples

### Security-Focused Analysis
```bash
catocli query appStats '{
    "appStatsFilter": [
        {"fieldName": "risk_score", "operator": "gte", "values": ["8"]},
        {"fieldName": "application_category", "operator": "in", "values": ["File Sharing", "Proxy"]}
    ],
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "user_name"},
        {"fieldName": "risk_score"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "appStatsSort": [
        {"fieldName": "risk_score", "order": "desc"}
    ],
    "timeFrame": "last.P30D"
}' -f csv --csv-filename security_risk_analysis.csv
```

### Productivity Analysis
```bash
catocli query appStats '{
    "appStatsFilter": [
        {"fieldName": "application_category", "operator": "in", 
         "values": ["Business", "Collaboration", "Productivity"]}
    ],
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "session_duration"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P7D"
}'
```

### Site Comparison Report
```bash
catocli query appStats '{
    "dimension": [
        {"fieldName": "site_name"},
        {"fieldName": "application_category"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "count_distinct", "fieldName": "user_name"}
    ],
    "appStatsSort": [
        {"fieldName": "traffic", "order": "desc"}
    ],
    "timeFrame": "last.P1M"
}' -f csv --csv-filename site_comparison.csv
```

## Best Practices

### Performance Optimization
1. **Limit dimensions**: Use only necessary dimension fields
2. **Specific time frames**: Avoid overly broad time ranges for large datasets  
3. **Filter early**: Apply filters to reduce data volume
4. **Sort wisely**: Sort by measured fields rather than dimensions

### Useful Combinations
1. **User + Application + Risk**: Identify risky user behavior
2. **Site + Application**: Compare usage across locations
3. **Time-based filtering**: Focus on business hours or specific periods
4. **Traffic direction**: Separate inbound vs outbound analysis

### Data Export Tips
1. Use descriptive CSV filenames with timestamps
2. Include relevant dimensions in the filename
3. Export large datasets in smaller time chunks
4. Use raw format for API integration

## Integration Examples

### Daily User Activity Report
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
catocli query appStats '{
    "dimension": [{"fieldName": "user_name"}],
    "measure": [
        {"aggType": "sum", "fieldName": "flows_created"},
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "user_activity_${DATE}.csv"
```

### Weekly Application Risk Assessment
```bash
#!/bin/bash
catocli query appStats '{
    "appStatsFilter": [
        {"fieldName": "risk_score", "operator": "gte", "values": ["6"]}
    ],
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "risk_score"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "count_distinct", "fieldName": "user_name"}
    ],
    "timeFrame": "last.P7D"
}' -f csv --csv-filename "weekly_risk_assessment.csv" --append-timestamp
```

## Related Operations

- [Application Time Series](./app-stats-timeseries.md) - For time-based application analysis
- [Account Metrics](./account-metrics.md) - For network performance metrics
- [Events Time Series](./events-timeseries.md) - For security event correlation

## API Reference

For complete field descriptions and additional parameters, see the [Cato API Documentation](https://api.catonetworks.com/documentation/#query-appStats).