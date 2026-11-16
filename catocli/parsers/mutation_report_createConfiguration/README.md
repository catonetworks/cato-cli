
## CATO-CLI - mutation.report.createConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.report.createConfiguration) for documentation on this operation.

### Usage for mutation.report.createConfiguration:

```bash
catocli mutation report createConfiguration -h

catocli mutation report createConfiguration <json>

catocli mutation report createConfiguration --json-file mutation.report.createConfiguration.json

catocli mutation report createConfiguration '{"reportCreateConfigurationInput":{"enabled":true,"filter":[{"field":"SITE_NAME","operator":"is","value":["string1","string2"]}],"name":"string","renderingFormat":"PDF","schedule":{"dayOfMonth":"FIRST_DAY","dayOfWeek":"SUNDAY","frequency":"DAILY"},"subscriptionId":"id","templateId":"id","timeFrame":"last.P1D","timeZone":"America/New_York"}}'

catocli mutation report createConfiguration '{
    "reportCreateConfigurationInput": {
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
        "name": "string",
        "renderingFormat": "PDF",
        "schedule": {
            "dayOfMonth": "FIRST_DAY",
            "dayOfWeek": "SUNDAY",
            "frequency": "DAILY"
        },
        "subscriptionId": "id",
        "templateId": "id",
        "timeFrame": "last.P1D",
        "timeZone": "America/New_York"
    }
}'
```

#### Operation Arguments for mutation.report.createConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportCreateConfigurationInput` [ReportCreateConfigurationInput] - (required) Name, template, data filters, schedule, and delivery settings of the new report configuration.
