
## CATO-CLI - mutation.site.updateSiteSocketConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteSocketConfiguration) for documentation on this operation.

### Usage for mutation.site.updateSiteSocketConfiguration:

```bash
catocli mutation site updateSiteSocketConfiguration -h

catocli mutation site updateSiteSocketConfiguration <json>

catocli mutation site updateSiteSocketConfiguration --json-file mutation.site.updateSiteSocketConfiguration.json

catocli mutation site updateSiteSocketConfiguration '{"updateSiteSocketConfigurationInput":{"primarySocketConfiguration":{"description":"string"},"secondarySocketConfiguration":{"description":"string"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateSiteSocketConfiguration '{
    "updateSiteSocketConfigurationInput": {
        "primarySocketConfiguration": {
            "description": "string"
        },
        "secondarySocketConfiguration": {
            "description": "string"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateSiteSocketConfiguration ####

`accountId` [ID] - (required) N/A    
`updateSiteSocketConfigurationInput` [UpdateSiteSocketConfigurationInput] - (required) N/A    
