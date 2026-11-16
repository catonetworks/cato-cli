
## CATO-CLI - mutation.report.generateReport:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.report.generateReport) for documentation on this operation.

### Usage for mutation.report.generateReport:

```bash
catocli mutation report generateReport -h

catocli mutation report generateReport <json>

catocli mutation report generateReport --json-file mutation.report.generateReport.json

catocli mutation report generateReport '{"reportGenerateReportInput":{"reportConfigurationId":"id"}}'

catocli mutation report generateReport '{
    "reportGenerateReportInput": {
        "reportConfigurationId": "id"
    }
}'
```

#### Operation Arguments for mutation.report.generateReport ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportGenerateReportInput` [ReportGenerateReportInput] - (required) ID of the report configuration to generate the report from.
