
## CATO-CLI - query.access:
[Click here](https://api.catonetworks.com/documentation/#query-query.access) for documentation on this operation.

### Usage for query.access:

```bash
catocli query access -h

catocli query access <json>

catocli query access --json-file query.access.json

catocli query access '{"accessRemoteAccessEntityListInput":{"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}}}'

catocli query access '{
    "accessRemoteAccessEntityListInput": {
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.access ####

`accessRemoteAccessEntityListInput` [AccessRemoteAccessEntityListInput] - (optional) N/A
`accountId` [ID] - (required) Unique identifier of the Cato account.
