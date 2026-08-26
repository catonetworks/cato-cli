# Cato Networks GraphQL API CLI

`catocli` is a command-line client for the
[Cato Networks GraphQL API](https://api.catonetworks.com/api/v1/graphql2).
It supports interactive use and automation for querying, reporting, and
managing Cato account configuration.

Use it to:

- Query network, security, user, and application data
- Manage supported Cato configuration through GraphQL mutations
- Export results as JSON or CSV
- Automate workflows with profiles, files, and command-line overrides

## Requirements

- Python 3.10 or newer (tested with Python 3.10 through 3.14)
- A Cato API token and account ID

See
[Generating API Keys for the Cato API](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API)
for token setup.

## Installation

```bash
python3 -m pip install --upgrade catocli
catocli --version
```

## Quick start

Configure the default profile:

```bash
# Interactive setup
catocli configure set

# Or non-interactive setup
catocli configure set --cato-token "your-api-token" --account-id "12345"
```

Run a query:

```bash
catocli query entityLookup '{"type":"country"}'
```

Inspect available commands and operation-specific arguments:

```bash
catocli --help
catocli query --help
catocli query entityLookup --help
```

Credentials are stored in the local profile configuration. Do not place API
tokens in source files, shell history, or committed scripts. See
[Profile Management](PROFILES.md) for named profiles and environment
selection.

## Configuration

```bash
# List profiles
catocli configure list

# Show the active profile
catocli configure show

# Select a profile
catocli configure use prod

# Override the configured account for one operation
catocli query entityLookup -accountID 12345 '{"type":"country"}'
```

For shell completion setup, see [Tab Completion](TAB_COMPLETION.md).

## JSON input

Pass variables inline or load them from a file:

```bash
catocli query site networkRangeList \
  '{"networkRangeListInput":{"site":{"by":"ID","input":"527548"}}}'

catocli query site networkRangeList \
  --json-file query.site.networkRangeList.json
```

Operation help includes a generated input example:

```bash
catocli query site networkRangeList --help
```

## Run from source

```bash
git clone https://github.com/Cato-Networks/cato-cli.git
cd cato-cli
python3 -m catocli --help
```

## Guides

- [Common Patterns and Best Practices](./catocli_user_guide/common-patterns.md):
  output formats, time frames, and filtering
- [Python Integration on Windows](./catocli_user_guide/python-integration-windows.md)
- [Python Integration on Unix, Linux, and macOS](./catocli_user_guide/python-integration-unix.md)
- [SIEM Integration](./catocli_user_guide/siem-integration.md):
  real-time security event streaming
- [Terraform Rules Integration](./catocli_user_guide/terraform-rules-integration.md):
  policy export and import for infrastructure as code

### Reporting guides

- [Account Metrics](./catocli_user_guide/account-metrics.md):
  network performance by site, user, or interface
- [Application Statistics](./catocli_user_guide/app-stats.md):
  user and application activity
- [Application Statistics Time Series](./catocli_user_guide/app-stats-timeseries.md):
  traffic over time
- [Events Time Series](./catocli_user_guide/events-timeseries.md):
  security, connectivity, and threat events
- [Socket Port Metrics](./catocli_user_guide/socket-port-metrics.md):
  socket interface performance
- [Socket Port Time Series](./catocli_user_guide/socket-port-timeseries.md):
  socket performance over time

## Examples

### Account metrics

```bash
catocli query accountMetrics '{"timeFrame":"last.PT1H"}'
```

### User activity CSV

```bash
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

### Security event analysis

```bash
catocli query eventsTimeSeries '{
    "buckets": 7,
    "eventsFilter": [{"fieldName": "event_type", "operator": "is", "values": ["Security"]}],
    "eventsMeasure": [{"aggType": "sum", "fieldName": "event_count"}],
    "perSecond": false,
    "timeFrame": "last.P7D"
}' -f csv --csv-filename eventsTimeSeries_weekly_security_events_report.csv
```

## Output formats

Reporting operations support:

- Enhanced JSON output by default
- Original API JSON with `--raw`
- CSV output with `-f csv`
- Custom filenames with `--csv-filename`
- Timestamped filenames with `--append-timestamp`

Check operation help before using format-specific options:

```bash
catocli query appStats --help
```

## Time frames

Common time frame patterns:

- `last.PT1H`: last hour
- `last.P1D`: last day
- `last.P7D`: last seven days
- `last.P1M`: last month
- `utc.2026-08-{01/00:00:00--01/23:59:59}`: custom UTC range

## Getting Help

- Add `-h` or `--help` to any command
- Read the [Cato API documentation](https://api.catonetworks.com/documentation/)
- Verify installed versions with `catocli --version` and `python3 --version`
- Download Python from [python.org](https://www.python.org/downloads/)

## License

See [LICENSE](LICENSE).
