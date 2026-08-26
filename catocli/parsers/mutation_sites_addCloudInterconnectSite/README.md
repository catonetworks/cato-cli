
## CATO-CLI - mutation.sites.addCloudInterconnectSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addCloudInterconnectSite) for documentation on this operation.

### Usage for mutation.sites.addCloudInterconnectSite:

```bash
catocli mutation sites addCloudInterconnectSite -h

catocli mutation sites addCloudInterconnectSite <json>

catocli mutation sites addCloudInterconnectSite --json-file mutation.sites.addCloudInterconnectSite.json

catocli mutation sites addCloudInterconnectSite '{"addCloudInterconnectSiteInput":{"description":"string","name":"string","siteLocation":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH"}}'

catocli mutation sites addCloudInterconnectSite '{
    "addCloudInterconnectSiteInput": {
        "description": "string",
        "name": "string",
        "siteLocation": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "siteType": "BRANCH"
    }
}'
```

#### Operation Arguments for mutation.sites.addCloudInterconnectSite ####

`accountId` [ID] - (required) N/A    
`addCloudInterconnectSiteInput` [AddCloudInterconnectSiteInput] - (required) N/A    
