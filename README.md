# Cato Networks GraphQL API CLI

The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API](https://api.catonetworks.com/api/v1/graphql2) easily integrating into configurations management, orchestration or automation frameworks to support the DevOps model.

## Overview

CatoCLI is a command-line interface that provides access to the Cato Networks GraphQL API, enabling you to:
- Generate detailed network and security reports
- Analyze user and application activity
- Monitor network performance and events
- Export data in multiple formats (JSON, CSV)
- Automate reporting and monitoring tasks

## Prerequisites

- Python 3.6 or higher
- CatoCLI installed (`pip3 install catocli`)
- Valid Cato Networks API token and Account ID
- Proper authentication configuration (see [Authentication Setup](#authentication-setup))

## Installation  

`pip3 install catocli`

## Authentication Setup

Configure your CatoCLI profile before using any query operations:

```bash
# Interactive configuration
catocli configure set

# Non-interactive configuration
catocli configure set --cato-token "your-api-token" --account-id "12345"

# List configured profiles
catocli configure list

# Show current profile
catocli configure show
```

### Documentation

For detailed information about profile management, see [PROFILES.md](PROFILES.md).

[CLICK HERE](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API) to see how create an API key to authenticate.

## Running the CLI
	catocli -h
	catocli query -h
	catocli query entityLookup -h
	catocli query entityLookup '{"type":"country"}`
    
    // Override the accountID value as a cli argument
	catocli query entityLookup -accountID=12345 '{"type":"country"}`

## Check out run locally not as pip package
	git clone git@github.com:Cato-Networks/cato-cli.git
	cd cato-cli
	python3 -m catocli -h

### Advanced cato-cli Topics

- [Common Patterns & Best Practices](./catocli_user_guide/common-patterns.md) - Output formats, time frames, filtering patterns
- [Python Integration - Windows](./catocli_user_guide/python-integration-windows.md) - Windows-specific Python automation examples
- [Python Integration - Unix/Linux/macOS](./catocli_user_guide/python-integration-unix.md) - Unix-based Python integration guide
- [SIEM Integration Guide](./catocli_user_guide/siem-integration.md) - Real-time security event streaming to SIEM platforms
- [Terraform Rules Integration](./catocli_user_guide/terraform-rules-integration.md) - Export/import policy rules to Terraform for IaC management

## Custom Report Query Operations

### Custom Report Analytics Queries

| Operation | Description | Guide |
|-----------|-------------|--------|
| [Account Metrics](./catocli_user_guide/account-metrics.md) | Network performance metrics by site, user, or interface | 📊 |
| [Application Statistics](./catocli_user_guide/app-stats.md) | User activity and application usage analysis | 📱 |
| [Application Statistics Time Series](./catocli_user_guide/app-stats-timeseries.md) | Traffic analysis over time with hourly/daily breakdowns | 📈 |
| [Events Time Series](./catocli_user_guide/events-timeseries.md) | Security events, connectivity, and threat analysis | 🔒 |
| [Socket Port Metrics](./catocli_user_guide/socket-port-metrics.md) | Socket interface performance and traffic analysis | 🔌 |
| [Socket Port Time Series](./catocli_user_guide/socket-port-timeseries.md) | Socket performance metrics over time | ⏱️ |

## Quick Start Examples

### Basic Network Health Check
```bash
# Get last hour account metrics
catocli query accountMetrics '{"timeFrame":"last.PT1H"}'
```

### User Activity Report (csv format)
```bash
# Export user activity for the last month to CSV
catocli query appStats '{
    "appStatsFilter": [],
    "appStatsSort": [],
    "dimension": [ { "fieldName": "user_name" }, { "fieldName": "domain" } ],
    "measure": [
        { "aggType": "sum", "fieldName": "upstream" },
        { "aggType": "sum", "fieldName": "downstream" },
        { "aggType": "sum", "fieldName": "traffic" },
        { "aggType": "sum", "fieldName": "flows_created" }
    ],
    "timeFrame": "last.P1D"
}' -f csv --csv-filename appStats_daily_user_activity_report.csv
```

### Security Events Analysis
```bash
# Weekly security events breakdown
catocli query eventsTimeSeries '{
    "buckets": 7,
    "eventsFilter": [{"fieldName": "event_type", "operator": "is", "values": ["Security"]}],
    "eventsMeasure": [{"aggType": "sum", "fieldName": "event_count"}],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename eventsTimeSeries_weekly_security_events_report.csv
```

## Output Formats

CatoCLI supports multiple output formats:

- **Enhanced JSON** (default): Formatted with granularity adjustments
- **Raw JSON**: Original API response with `-raw` flag
- **CSV**: Structured data export with `-f csv`
- **Custom CSV**: Named files with `--csv-filename` and `--append-timestamp`

## Time Frame Options

Common time frame patterns:
- `last.PT1H` - Last hour
- `last.P1D` - Last day  
- `last.P7D` - Last week
- `last.P1M` - Last month
- `utc.2023-02-{28/00:00:00--28/23:59:59}` - Custom UTC range

## Getting Help

- Use `-h` or `--help` with any command for detailed usage
- Check the [Cato API Documentation](https://api.catonetworks.com/documentation/)
- Review individual operation guides linked above


This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8

## Requirements:
    python 3.6 or higher
    
## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## Installing the correct version for environment:
https://www.python.org/downloads/
