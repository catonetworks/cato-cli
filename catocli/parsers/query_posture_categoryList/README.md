
## CATO-CLI - query.posture.categoryList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.categoryList) for documentation on this operation.

### Usage for query.posture.categoryList:

```bash
catocli query posture categoryList -h

catocli query posture categoryList <json>

catocli query posture categoryList --json-file query.posture.categoryList.json

catocli query posture categoryList '{"postureCategoryListInput":{"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query posture categoryList '{
    "postureCategoryListInput": {
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.posture.categoryList ####

`accountId` [ID] - (required) N/A    
`postureCategoryListInput` [PostureCategoryListInput] - (required) N/A    
