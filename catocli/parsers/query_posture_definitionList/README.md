
## CATO-CLI - query.posture.definitionList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.definitionList) for documentation on this operation.

### Usage for query.posture.definitionList:

```bash
catocli query posture definitionList -h

catocli query posture definitionList <json>

catocli query posture definitionList --json-file query.posture.definitionList.json

catocli query posture definitionList '{"accountId":"id","postureDefinitionListInput":{"sort":{"name":{"direction":"ASC","priority":1},"severity":{"direction":"ASC","priority":1}}}}'

catocli query posture definitionList '{
    "accountId": "id",
    "postureDefinitionListInput": {
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "severity": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.posture.definitionList ####

`accountId` [ID] - (required) N/A    
`postureDefinitionListInput` [PostureDefinitionListInput] - (required) N/A    
