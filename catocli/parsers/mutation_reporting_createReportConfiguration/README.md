
## CATO-CLI - mutation.reporting.createReportConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.reporting.createReportConfiguration) for documentation on this operation.

### Usage for mutation.reporting.createReportConfiguration:

```bash
catocli mutation reporting createReportConfiguration -h

catocli mutation reporting createReportConfiguration <json>

catocli mutation reporting createReportConfiguration --json-file mutation.reporting.createReportConfiguration.json

catocli mutation reporting createReportConfiguration '{"reportingCreateReportConfigurationInput":{"enabled":true,"filter":[{"field":"SITE_NAME","operator":"is","value":["string1","string2"]}],"mailingList":{"by":"ID","input":"string"},"name":"string","renderingFormat":"PDF","schedule":{"dayOfMonth":"FIRST_DAY","dayOfWeek":"SUNDAY","frequency":"DAILY"},"templateId":"id","timeFrame":"last.P1D","timeZone":"America/New_York"}}'

catocli mutation reporting createReportConfiguration '{
    "reportingCreateReportConfigurationInput": {
        "enabled": true,
        "filter": [
            {
                "field": "SITE_NAME",
                "operator": "is",
                "value": [
                    "string1",
                    "string2"
                ]
            }
        ],
        "mailingList": {
            "by": "ID",
            "input": "string"
        },
        "name": "string",
        "renderingFormat": "PDF",
        "schedule": {
            "dayOfMonth": "FIRST_DAY",
            "dayOfWeek": "SUNDAY",
            "frequency": "DAILY"
        },
        "templateId": "id",
        "timeFrame": "last.P1D",
        "timeZone": "America/New_York"
    }
}'
```

#### Operation Arguments for mutation.reporting.createReportConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportingCreateReportConfigurationInput` [ReportingCreateReportConfigurationInput] - (required) Name, template, data filters, schedule, and delivery settings of the new report configuration.
