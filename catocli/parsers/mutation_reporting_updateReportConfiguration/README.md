
## CATO-CLI - mutation.reporting.updateReportConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.reporting.updateReportConfiguration) for documentation on this operation.

### Usage for mutation.reporting.updateReportConfiguration:

```bash
catocli mutation reporting updateReportConfiguration -h

catocli mutation reporting updateReportConfiguration <json>

catocli mutation reporting updateReportConfiguration --json-file mutation.reporting.updateReportConfiguration.json

catocli mutation reporting updateReportConfiguration '{"reportingUpdateReportConfigurationInput":{"enabled":true,"filter":[{"field":"SITE_NAME","operator":"is","value":["string1","string2"]}],"id":"id","mailingList":{"by":"ID","input":"string"},"name":"string","renderingFormat":"PDF","schedule":{"dayOfMonth":"FIRST_DAY","dayOfWeek":"SUNDAY","frequency":"DAILY"},"templateId":"id","timeFrame":"last.P1D","timeZone":"America/New_York"}}'

catocli mutation reporting updateReportConfiguration '{
    "reportingUpdateReportConfigurationInput": {
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
        "id": "id",
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

#### Operation Arguments for mutation.reporting.updateReportConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportingUpdateReportConfigurationInput` [ReportingUpdateReportConfigurationInput] - (required) ID of the report configuration and the complete set of its new values.
