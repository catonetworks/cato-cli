
## CATO-CLI - mutation.report.deleteConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.report.deleteConfiguration) for documentation on this operation.

### Usage for mutation.report.deleteConfiguration:

```bash
catocli mutation report deleteConfiguration -h

catocli mutation report deleteConfiguration <json>

catocli mutation report deleteConfiguration --json-file mutation.report.deleteConfiguration.json

catocli mutation report deleteConfiguration '{"reportDeleteConfigurationInput":{"id":"id"}}'

catocli mutation report deleteConfiguration '{
    "reportDeleteConfigurationInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.report.deleteConfiguration ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportDeleteConfigurationInput` [ReportDeleteConfigurationInput] - (required) ID of the report configuration to delete.
