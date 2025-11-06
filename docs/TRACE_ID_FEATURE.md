# API Tracing Feature

## Overview

The `--trace-id` flag enables API request tracing for all catocli GraphQL operations. When enabled, the CLI will:

1. Add `x-force-tracing: true` header to the outbound API request
2. Extract the `Trace_id` header from the API response
3. Display the trace ID above the JSON response output

## Usage

Add the `--trace-id` flag to any catocli query or mutation command:

```bash
# Query example
catocli query devices --trace-id '{}'

# With parameters
catocli query accountSnapshot --trace-id '{"siteIDs": ["12345"]}'

# Mutation example
catocli mutation admin addAdmin --trace-id '{"email": "admin@example.com", ...}'
```

## Output Example

When `--trace-id` is enabled, the trace ID will be displayed before the JSON response:

```
Trace-ID: 3629656138731602964

{
  "data": {
    ...
  }
}
```

If the API doesn't return a `Trace_id` header, a warning will be displayed:

```
Warning: x-force-tracing header was sent but no Trace-ID received in response

{
  "data": {
    ...
  }
}
```

## Implementation Details

### Files Modified

1. **schema/catolib.py**
   - Added `--trace-id` argument to parser generation
   - All auto-generated parsers now include this flag

2. **graphql_client/api/call_api.py**
   - Added logic to include `x-force-tracing: true` header when flag is set
   - Modified `call_api()` to return full response tuple (data, status, headers) when trace_id is enabled

3. **catocli/parsers/customParserApiClient.py**
   - Added trace ID extraction logic from response headers
   - Display trace ID before JSON output

### How It Works

1. **Request Phase:**
   - When `--trace-id` flag is detected, `call_api.py` adds `x-force-tracing: true` to request headers
   - The API request is sent with this header

2. **Response Phase:**
   - When `--trace-id` is enabled, `call_api()` returns the full response tuple including headers
   - `customParserApiClient.py` extracts `Trace_id` from response headers (case-insensitive search for trace_id, x-trace-id, or traceid)
   - The trace ID is printed to stdout before the JSON response

3. **Compatibility:**
   - When `--trace-id` is NOT used, behavior remains unchanged
   - The feature is backward compatible with existing scripts

## Use Cases

### Debugging API Issues
```bash
# Get trace ID for troubleshooting with Cato support
catocli query events --trace-id '{"from": "2024-01-01T00:00:00Z", "to": "2024-01-02T00:00:00Z"}'
```

### Performance Analysis
```bash
# Track slow API calls by correlating trace IDs with backend logs
catocli query accountMetrics --trace-id '{}' > metrics.json
# Share the trace ID with support team for investigation
```

### Automated Monitoring
```bash
#!/bin/bash
# Script to collect trace IDs for monitoring
OUTPUT=$(catocli query devices --trace-id '{}')
TRACE_ID=$(echo "$OUTPUT" | grep "Trace-ID:" | cut -d' ' -f2)
echo "Request trace ID: $TRACE_ID"
```

## Regenerating Parsers

After modifying the parser generation logic, regenerate all parsers:

```bash
cd schema
python3 catolib.py
```

This will regenerate all parser files with the updated `--trace-id` flag.

## Testing

Test the trace-id feature with a simple command:

```bash
# Test with devices query
catocli query devices --trace-id '{}'

# Expected output:
# Trace-ID: 3629656138731602964
# 
# {
#   "data": {
#     ...
#   }
# }
```

## Notes

- The trace ID is only displayed when the `--trace-id` flag is used
- The feature works with all query and mutation operations
- The trace ID is extracted case-insensitively from response headers
- Compatible with other flags like `-v` (verbose), `-p` (pretty print), etc.
