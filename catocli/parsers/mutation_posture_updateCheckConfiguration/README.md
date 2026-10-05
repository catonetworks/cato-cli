
## CATO-CLI - mutation.posture.updateCheckConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.updateCheckConfiguration) for documentation on this operation.

### Usage for mutation.posture.updateCheckConfiguration:

```bash
catocli mutation posture updateCheckConfiguration -h

catocli mutation posture updateCheckConfiguration <json>

catocli mutation posture updateCheckConfiguration --json-file mutation.posture.updateCheckConfiguration.json

catocli mutation posture updateCheckConfiguration '{"postureUpdateCheckConfigurationInput":{"suppressedCheckStatus":[{"id":"string","status":"ENABLED"}]}}'

catocli mutation posture updateCheckConfiguration '{
    "postureUpdateCheckConfigurationInput": {
        "suppressedCheckStatus": [
            {
                "id": "string",
                "status": "ENABLED"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.posture.updateCheckConfiguration ####

`accountId` [ID] - (required) ID of the account whose Posture configuration or findings are modified.
`postureUpdateCheckConfigurationInput` [PostureUpdateCheckConfigurationInput] - (required) Checks to enable or disable and their desired statuses.
