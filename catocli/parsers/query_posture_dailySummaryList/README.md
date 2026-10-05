
## CATO-CLI - query.posture.dailySummaryList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.dailySummaryList) for documentation on this operation.

### Usage for query.posture.dailySummaryList:

```bash
catocli query posture dailySummaryList -h

catocli query posture dailySummaryList <json>

catocli query posture dailySummaryList --json-file query.posture.dailySummaryList.json

catocli query posture dailySummaryList '{"postureDailySummaryListInput":{"filter":{"timeFrame":"last.P1D"}}}'

catocli query posture dailySummaryList '{
    "postureDailySummaryListInput": {
        "filter": {
            "timeFrame": "last.P1D"
        }
    }
}'
```

#### Operation Arguments for query.posture.dailySummaryList ####

`accountId` [ID] - (required) ID of the account whose Posture data is queried.
`postureDailySummaryListInput` [PostureDailySummaryListInput] - (required) Time-range filter for daily Posture summary snapshots.
