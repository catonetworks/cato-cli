
## CATO-CLI - mutation.site.assignSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.assignSocket) for documentation on this operation.

### Usage for mutation.site.assignSocket:

```bash
catocli mutation site assignSocket -h

catocli mutation site assignSocket <json>

catocli mutation site assignSocket --json-file mutation.site.assignSocket.json

catocli mutation site assignSocket '{"siteAssignSocketInput":{"description":"string","site":{"by":"ID","input":"string"},"socketIdentifier":"string"}}'

catocli mutation site assignSocket '{
    "siteAssignSocketInput": {
        "description": "string",
        "site": {
            "by": "ID",
            "input": "string"
        },
        "socketIdentifier": "string"
    }
}'
```

#### Operation Arguments for mutation.site.assignSocket ####

`accountId` [ID] - (required) N/A
`siteAssignSocketInput` [SiteAssignSocketInput] - (required) N/A
