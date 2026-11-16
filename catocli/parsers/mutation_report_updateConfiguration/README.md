
## CATO-CLI - mutation.report.updateConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.report.updateConfiguration) for documentation on this operation.

### Usage for mutation.report.updateConfiguration:

```bash
catocli mutation report updateConfiguration -h

catocli mutation report updateConfiguration <json>

catocli mutation report updateConfiguration --json-file mutation.report.updateConfiguration.json

catocli mutation report updateConfiguration '{"reportUpdateConfigurationInput":{"enabled":true,"filter":[{"field":"SITE_NAME","operator":"is","value":["string1","string2"]}],"id":"id","name":"string","renderingFormat":"PDF","schedule":{"dayOfMonth":"FIRST_DAY","dayOfWeek":"SUNDAY","frequency":"DAILY"},"subscriptionId":"id","templateId":"id","timeFrame":"last.P1D","timeZone":"America/New_York"}}'

catocli mutation report updateConfiguration '{
    "reportUpdateConfigurationInput": {
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

#### Operation Arguments for mutation.report.updateConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportUpdateConfigurationInput` [ReportUpdateConfigurationInput] - (required) ID of the report configuration and the complete set of its new values.
