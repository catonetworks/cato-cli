# Common Patterns & Best Practices Guide

This guide covers common patterns, output formats, time frame conventions, and best practices that apply across all CatoCLI query operations.

## Output Formats

CatoCLI supports multiple output formats to suit different use cases and integration requirements.

### Enhanced JSON (Default)

The default output format provides formatted JSON with additional processing:
- Granularity multiplication applied to sum aggregations
- Readable formatting and structure
- Enhanced field descriptions where applicable

```bash
catocli query accountMetrics '{
    "timeFrame": "last.P1D"
}'
```

### Raw JSON

Returns the original API response without any formatting or processing:

```bash
catocli query accountMetrics '{
    "timeFrame": "last.P1D"
}' -raw
```

**Use cases:**
- API integration where exact API response is needed
- Debugging or comparing with direct API calls
- When granularity multiplication is not desired

### CSV Export

Export data to CSV format for analysis in spreadsheet applications:

```bash
catocli query accountMetrics '{
    "timeFrame": "last.P1D"
}' -f csv --csv-filename report.csv
```

**CSV Options:**
- `--csv-filename filename`: Specify custom filename
- `--append-timestamp`: Add timestamp to filename
- Default filename based on query type if not specified

### CSV with Timestamps

Automatically append timestamp to CSV filenames:

```bash
catocli query accountMetrics '{
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "daily_report" --append-timestamp
# Creates: daily_report_20231015_143022.csv
```

## Time Frame Patterns

Time frames are consistent across all query types, supporting both relative and absolute specifications.

### Relative Time Frames

#### ISO 8601 Duration Format
- `last.PT1H` - Last 1 hour
- `last.PT6H` - Last 6 hours
- `last.P1D` - Last 1 day
- `last.P7D` - Last 7 days (1 week)
- `last.P1M` - Last 1 month
- `last.P3M` - Last 3 months
- `last.P1Y` - Last 1 year

#### Common Patterns
```json
// Recent activity (short term)
{"timeFrame": "last.PT1H"}   // Last hour
{"timeFrame": "last.PT6H"}   // Last 6 hours

// Daily analysis
{"timeFrame": "last.P1D"}    // Last day

// Weekly/monthly reporting
{"timeFrame": "last.P7D"}    // Last week
{"timeFrame": "last.P1M"}    // Last month

// Long-term trends
{"timeFrame": "last.P3M"}    // Last quarter
{"timeFrame": "last.P1Y"}    // Last year
```

### Absolute Time Frames

Use UTC format for specific date/time ranges:

```json
// Single day
"timeFrame": "utc.2023-10-{15/00:00:00--15/23:59:59}"

// Date range
"timeFrame": "utc.2023-10-{01/00:00:00--31/23:59:59}"

// Business hours
"timeFrame": "utc.2023-10-{15/09:00:00--15/17:00:00}"

// Weekend analysis
"timeFrame": "utc.2023-10-{14/00:00:00--15/23:59:59}"
```

### Time Frame Best Practices

1. **Performance Consideration**: Shorter time frames generally perform better
2. **Bucket Alignment**: For time series, align bucket count with time frame duration
3. **Business Context**: Use absolute times for specific periods, relative for ongoing monitoring
4. **Data Retention**: Consider data retention policies when using longer time frames

## Bucket Configuration (Time Series Queries)

For time series queries, the `buckets` parameter determines granularity:

### Common Bucket Patterns

#### High-Resolution Monitoring
```json
{"buckets": 12, "timeFrame": "last.PT1H"}   // 5-minute intervals
{"buckets": 72, "timeFrame": "last.PT6H"}   // 5-minute intervals
{"buckets": 288, "timeFrame": "last.P1D"}   // 5-minute intervals
```

#### Hourly Analysis
```json
{"buckets": 24, "timeFrame": "last.P1D"}    // Hourly for 1 day
{"buckets": 168, "timeFrame": "last.P7D"}   // Hourly for 1 week
{"buckets": 720, "timeFrame": "last.P1M"}   // Hourly for 1 month
```

#### Daily Analysis
```json
{"buckets": 7, "timeFrame": "last.P7D"}     // Daily for 1 week
{"buckets": 30, "timeFrame": "last.P1M"}    // Daily for 1 month
{"buckets": 365, "timeFrame": "last.P1Y"}   // Daily for 1 year
```

### Bucket Calculation
```
Bucket Interval = Time Frame Duration / Number of Buckets

Examples:
- 24 buckets over 1 day = 1-hour intervals
- 168 buckets over 7 days = 1-hour intervals
- 12 buckets over 1 hour = 5-minute intervals
```

## Filtering Patterns

### Filter Structure
All queries support a consistent filter structure:

```json
{
  "filter": [
    {
      "fieldName": "field_to_filter",
      "operator": "filter_operator", 
      "values": ["value1", "value2"]
    }
  ]
}
```

### Common Filter Operators
- `is` - Exact match
- `in` - Match any of the provided values
- `contains` - Contains substring
- `gt` / `gte` - Greater than / greater than or equal
- `lt` / `lte` - Less than / less than or equal
- `not` - Does not match

### Filter Examples

#### Site-Specific Analysis
```json
{
  "filter": [
    {
      "fieldName": "site_name",
      "operator": "in",
      "values": ["HQ", "Branch Office", "Remote Site"]
    }
  ]
}
```

#### High-Risk Applications
```json
{
  "filter": [
    {
      "fieldName": "risk_score",
      "operator": "gte",
      "values": ["7"]
    }
  ]
}
```

#### Traffic Direction
```json
{
  "filter": [
    {
      "fieldName": "traffic_direction",
      "operator": "is",
      "values": ["WANBOUND"]
    }
  ]
}
```

## Sorting Patterns

### Sort Structure
```json
{
  "sort": [
    {
      "fieldName": "field_to_sort_by",
      "order": "desc"  // or "asc"
    }
  ]
}
```

### Common Sort Patterns

#### By Volume (Descending)
```json
{"sort": [{"fieldName": "bytes_total", "order": "desc"}]}
{"sort": [{"fieldName": "traffic", "order": "desc"}]}
{"sort": [{"fieldName": "event_count", "order": "desc"}]}
```

#### By Performance (Descending)
```json
{"sort": [{"fieldName": "utilization_total", "order": "desc"}]}
{"sort": [{"fieldName": "threat_score", "order": "desc"}]}
{"sort": [{"fieldName": "latency", "order": "desc"}]}
```

#### Alphabetical
```json
{"sort": [{"fieldName": "site_name", "order": "asc"}]}
{"sort": [{"fieldName": "user_name", "order": "asc"}]}
```

## Dimension and Measure Patterns

### Common Dimension Combinations

#### User Analysis
```json
"dimension": [
  {"fieldName": "user_name"},
  {"fieldName": "site_name"},
  {"fieldName": "application_name"}
]
```

#### Site Analysis
```json
"dimension": [
  {"fieldName": "site_name"},
  {"fieldName": "socket_interface"},
  {"fieldName": "device_id"}
]
```

#### Application Analysis
```json
"dimension": [
  {"fieldName": "application_name"},
  {"fieldName": "application_category"},
  {"fieldName": "risk_score"}
]
```

### Common Measure Combinations

#### Traffic Analysis
```json
"measure": [
  {"aggType": "sum", "fieldName": "upstream"},
  {"aggType": "sum", "fieldName": "downstream"},
  {"aggType": "sum", "fieldName": "traffic"}
]
```

#### Performance Analysis
```json
"measure": [
  {"aggType": "avg", "fieldName": "latency"},
  {"aggType": "avg", "fieldName": "packet_loss"},
  {"aggType": "avg", "fieldName": "utilization_total"}
]
```

#### Count Analysis
```json
"measure": [
  {"aggType": "sum", "fieldName": "event_count"},
  {"aggType": "count_distinct", "fieldName": "user_name"},
  {"aggType": "sum", "fieldName": "flows_created"}
]
```

## Aggregation Types

### Numerical Aggregations
- `sum` - Total of all values
- `avg` - Average value
- `min` - Minimum value
- `max` - Maximum value

### Count Aggregations
- `count` - Count of records
- `count_distinct` - Count of unique values

### Usage Guidelines
- Use `sum` for totals (bytes, events, flows)
- Use `avg` for rates and ratios (utilization, scores)
- Use `count_distinct` for unique entity counts
- Use `max` for peak values, `min` for baseline values

## Integration Patterns

### Script Integration

#### Basic Shell Script Pattern
```bash
#!/bin/bash
# Configuration
DATE=$(date +%Y%m%d)
OUTPUT_DIR="/reports"
QUERY_TYPE="accountMetrics"

# Execute query
catocli query $QUERY_TYPE '{
    "timeFrame": "last.P1D"
}' -f csv --csv-filename "${OUTPUT_DIR}/daily_report_${DATE}.csv"

echo "Report generated: ${OUTPUT_DIR}/daily_report_${DATE}.csv"
```

#### Error Handling Pattern
```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

QUERY_RESULT=$(catocli query accountMetrics '{
    "timeFrame": "last.P1D"
}' 2>&1) || {
    echo "Query failed: $QUERY_RESULT"
    exit 1
}

echo "Query successful"
echo "$QUERY_RESULT"
```

### Cron Automation

#### Daily Reports
```bash
# Daily report at 6 AM
0 6 * * * /path/to/daily_report.sh

# Weekly report on Sundays at 7 AM  
0 7 * * 0 /path/to/weekly_report.sh

# Monthly report on 1st at 8 AM
0 8 1 * * /path/to/monthly_report.sh
```

### CI/CD Integration

#### GitLab CI Example
```yaml
generate_reports:
  script:
    - catocli query accountMetrics '{"timeFrame":"last.P1D"}' -f csv --csv-filename daily_report.csv
    - upload-to-storage daily_report.csv
  artifacts:
    paths:
      - daily_report.csv
    expire_in: 7 days
```

## Performance Optimization

### Query Optimization
1. **Use specific time frames** - Avoid overly broad time ranges
2. **Apply filters early** - Filter data before aggregation
3. **Limit dimensions** - Only include necessary grouping fields
4. **Choose appropriate bucket sizes** - Balance detail with performance

### Data Volume Management
1. **Paginate large results** - Use reasonable limits for large datasets
2. **Break up large queries** - Split very large time ranges
3. **Use streaming for large exports** - Consider batch processing for massive datasets

### Caching Strategies
1. **Cache common queries** - Store frequently used results
2. **Incremental updates** - Only query new data since last run
3. **Pre-computed reports** - Generate common reports in advance

## Error Handling Patterns

### Common Error Scenarios
1. **Authentication failures** - Invalid tokens or credentials
2. **Rate limiting** - Too many requests per time period
3. **Invalid queries** - Malformed JSON or invalid parameters
4. **Network timeouts** - Large queries or network issues
5. **Data availability** - Requested time range not available

### Error Handling Best Practices
```bash
# Retry logic
for i in {1..3}; do
    if catocli query accountMetrics '{"timeFrame":"last.P1D"}'; then
        break
    else
        echo "Attempt $i failed, retrying..."
        sleep 5
    fi
done

# Validate before processing
if command -v catocli >/dev/null 2>&1; then
    echo "CatoCLI is available"
else
    echo "CatoCLI not found, please install"
    exit 1
fi
```

## Data Quality Patterns

### Data Validation
1. **Check for empty results** - Validate data before processing
2. **Verify time ranges** - Ensure data covers expected period
3. **Validate metrics** - Check for reasonable values

### Data Consistency
1. **Consistent naming** - Use standard field names across queries
2. **Standard time frames** - Use consistent time frame patterns
3. **Uniform aggregation** - Apply consistent aggregation types

## Security Best Practices

### Credential Management
1. **Use profiles** - Configure authentication with catocli profiles
2. **Avoid hardcoded tokens** - Never embed tokens in scripts
3. **Environment variables** - Use secure environment variable practices
4. **Rotate credentials** - Regularly update API tokens

### Data Handling
1. **Secure storage** - Store exported data securely
2. **Access controls** - Limit access to sensitive reports
3. **Data retention** - Implement appropriate data retention policies
4. **Audit logging** - Log query execution for compliance

## Monitoring and Alerting

### Operational Monitoring
1. **Query success rates** - Monitor for query failures
2. **Response times** - Track query performance
3. **Data freshness** - Verify data recency
4. **Resource usage** - Monitor system resources

### Alerting Patterns
1. **Threshold-based alerts** - Alert on metric thresholds
2. **Trend-based alerts** - Alert on unusual trends
3. **Availability alerts** - Alert on service availability
4. **Error rate alerts** - Alert on high error rates

## Documentation Standards

### Script Documentation
1. **Header comments** - Purpose, author, version
2. **Parameter documentation** - Document all configurable parameters
3. **Example usage** - Provide usage examples
4. **Dependencies** - List required tools and permissions

### Report Documentation
1. **Metadata** - Include generation time, parameters used
2. **Field descriptions** - Explain column meanings
3. **Data sources** - Document data sources and time ranges
4. **Limitations** - Note any data limitations or caveats

This guide provides the foundation for effective use of CatoCLI across all query types. Combine these patterns with the specific examples in each query guide for optimal results.