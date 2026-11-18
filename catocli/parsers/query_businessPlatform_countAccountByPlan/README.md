
## CATO-CLI - query.businessPlatform.countAccountByPlan:
[Click here](https://api.catonetworks.com/documentation/#query-query.businessPlatform.countAccountByPlan) for documentation on this operation.

### Usage for query.businessPlatform.countAccountByPlan:

```bash
catocli query businessPlatform countAccountByPlan -h

catocli query businessPlatform countAccountByPlan <json>

catocli query businessPlatform countAccountByPlan --json-file query.businessPlatform.countAccountByPlan.json

catocli query businessPlatform countAccountByPlan '{"businessPlatformCountAccountByPlanInput":{"filter":{"includeMSP":true}}}'

catocli query businessPlatform countAccountByPlan '{
    "businessPlatformCountAccountByPlanInput": {
        "filter": {
            "includeMSP": true
        }
    }
}'
```

#### Operation Arguments for query.businessPlatform.countAccountByPlan ####

`accountId` [ID] - (required) N/A
`businessPlatformCountAccountByPlanInput` [BusinessPlatformCountAccountByPlanInput] - (required) Optional input with filter criteria.
