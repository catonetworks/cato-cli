
## CATO-CLI - mutation.reporting.generateReport:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.reporting.generateReport) for documentation on this operation.

### Usage for mutation.reporting.generateReport:

```bash
catocli mutation reporting generateReport -h

catocli mutation reporting generateReport <json>

catocli mutation reporting generateReport --json-file mutation.reporting.generateReport.json

catocli mutation reporting generateReport '{"reportingGenerateReportInput":{"reportConfigurationId":"id"}}'

catocli mutation reporting generateReport '{
    "reportingGenerateReportInput": {
        "reportConfigurationId": "id"
    }
}'
```

#### Operation Arguments for mutation.reporting.generateReport ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportingGenerateReportInput` [ReportingGenerateReportInput] - (required) ID of the report configuration to generate the report from.
