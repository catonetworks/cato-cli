
## CATO-CLI - mutation.reporting.deleteReportRun:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.reporting.deleteReportRun) for documentation on this operation.

### Usage for mutation.reporting.deleteReportRun:

```bash
catocli mutation reporting deleteReportRun -h

catocli mutation reporting deleteReportRun <json>

catocli mutation reporting deleteReportRun --json-file mutation.reporting.deleteReportRun.json

catocli mutation reporting deleteReportRun '{"reportingDeleteReportRunInput":{"id":"id"}}'

catocli mutation reporting deleteReportRun '{
    "reportingDeleteReportRunInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.reporting.deleteReportRun ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportingDeleteReportRunInput` [ReportingDeleteReportRunInput] - (required) ID of the report run to delete.
