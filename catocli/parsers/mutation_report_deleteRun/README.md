
## CATO-CLI - mutation.report.deleteRun:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.report.deleteRun) for documentation on this operation.

### Usage for mutation.report.deleteRun:

```bash
catocli mutation report deleteRun -h

catocli mutation report deleteRun <json>

catocli mutation report deleteRun --json-file mutation.report.deleteRun.json

catocli mutation report deleteRun '{"reportDeleteRunInput":{"id":"id"}}'

catocli mutation report deleteRun '{
    "reportDeleteRunInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.report.deleteRun ####

`accountId` [ID] - (required) ID of the account whose report configurations and runs are modified.
`reportDeleteRunInput` [ReportDeleteRunInput] - (required) ID of the report run to delete.
