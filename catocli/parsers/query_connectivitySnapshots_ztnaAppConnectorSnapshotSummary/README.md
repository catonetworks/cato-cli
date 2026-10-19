
## CATO-CLI - query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary:
[Click here](https://api.catonetworks.com/documentation/#query-query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary) for documentation on this operation.

### Usage for query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary:

```bash
catocli query connectivitySnapshots ztnaAppConnectorSnapshotSummary -h

catocli query connectivitySnapshots ztnaAppConnectorSnapshotSummary <json>

catocli query connectivitySnapshots ztnaAppConnectorSnapshotSummary --json-file query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary.json

catocli query connectivitySnapshots ztnaAppConnectorSnapshotSummary '{"ztnaAppConnectorSnapshotSummaryInput":{"filter":{"connectivityStatus":[{"eq":"CONNECTED","in":["CONNECTED"],"neq":"CONNECTED","nin":["CONNECTED"]}]}}}'

catocli query connectivitySnapshots ztnaAppConnectorSnapshotSummary '{
    "ztnaAppConnectorSnapshotSummaryInput": {
        "filter": {
            "connectivityStatus": [
                {
                    "eq": "CONNECTED",
                    "in": [
                        "CONNECTED"
                    ],
                    "neq": "CONNECTED",
                    "nin": [
                        "CONNECTED"
                    ]
                }
            ]
        }
    }
}'
```

#### Operation Arguments for query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary ####

`accountId` [ID] - (required) N/A
`ztnaAppConnectorSnapshotSummaryInput` [ZtnaAppConnectorSnapshotSummaryInput] - (required) N/A
