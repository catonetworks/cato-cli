
## CATO-CLI - mutation.sites.updateSiteSocketConfiguration:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteSocketConfiguration) for documentation on this operation.

### Usage for mutation.sites.updateSiteSocketConfiguration:

```bash
catocli mutation sites updateSiteSocketConfiguration -h

catocli mutation sites updateSiteSocketConfiguration <json>

catocli mutation sites updateSiteSocketConfiguration --json-file mutation.sites.updateSiteSocketConfiguration.json

catocli mutation sites updateSiteSocketConfiguration '{"updateSiteSocketConfigurationInput":{"siteRefInput":{"by":"ID","input":"string"},"socketConfigurationInput":{"description":"string"}}}'

catocli mutation sites updateSiteSocketConfiguration '{
    "updateSiteSocketConfigurationInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "socketConfigurationInput": {
            "description": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSiteSocketConfiguration ####

`accountId` [ID] - (required) N/A    
`updateSiteSocketConfigurationInput` [UpdateSiteSocketConfigurationInput] - (required) N/A    
