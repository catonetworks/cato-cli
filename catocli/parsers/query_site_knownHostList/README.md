
## CATO-CLI - query.site.knownHostList:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.knownHostList) for documentation on this operation.

### Usage for query.site.knownHostList:

```bash
catocli query site knownHostList -h

catocli query site knownHostList <json>

catocli query site knownHostList --json-file query.site.knownHostList.json

catocli query site knownHostList '{"siteKnownHostListInput":{"paging":{"from":1,"limit":1},"site":{"by":"ID","input":"string"}}}'

catocli query site knownHostList '{
    "siteKnownHostListInput": {
        "paging": {
            "from": 1,
            "limit": 1
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for query.site.knownHostList ####

`accountId` [ID] - (required) N/A    
`siteKnownHostListInput` [SiteKnownHostListInput] - (required) N/A    
