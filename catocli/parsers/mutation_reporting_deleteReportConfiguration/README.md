
## CATO-CLI - mutation.reporting.deleteReportConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.reporting.deleteReportConfiguration) for documentation on this operation.

### Usage for mutation.reporting.deleteReportConfiguration:

```bash
catocli mutation reporting deleteReportConfiguration -h

catocli mutation reporting deleteReportConfiguration <json>

catocli mutation reporting deleteReportConfiguration --json-file mutation.reporting.deleteReportConfiguration.json

catocli mutation reporting deleteReportConfiguration '{"reportingDeleteReportConfigurationInput":{"id":"id"}}'

catocli mutation reporting deleteReportConfiguration '{
    "reportingDeleteReportConfigurationInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.reporting.deleteReportConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportingDeleteReportConfigurationInput` [ReportingDeleteReportConfigurationInput] - (required) ID of the report configuration to delete.
