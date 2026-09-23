
## CATO-CLI - query.posture.accountSummaryList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.accountSummaryList) for documentation on this operation.

### Usage for query.posture.accountSummaryList:

```bash
catocli query posture accountSummaryList -h

catocli query posture accountSummaryList <json>

catocli query posture accountSummaryList --json-file query.posture.accountSummaryList.json

catocli query posture accountSummaryList '{"postureAccountSummaryListInput":{"sort":{"accountName":{"direction":"ASC","priority":1},"score":{"direction":"ASC","priority":1}}}}'

catocli query posture accountSummaryList '{
    "postureAccountSummaryListInput": {
        "sort": {
            "accountName": {
                "direction": "ASC",
                "priority": 1
            },
            "score": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.posture.accountSummaryList ####

`accountId` [ID] - (required) N/A    
`postureAccountSummaryListInput` [PostureAccountSummaryListInput] - (required) N/A    
