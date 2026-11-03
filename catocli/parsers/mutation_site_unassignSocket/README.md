
## CATO-CLI - mutation.site.unassignSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.unassignSocket) for documentation on this operation.

### Usage for mutation.site.unassignSocket:

```bash
catocli mutation site unassignSocket -h

catocli mutation site unassignSocket <json>

catocli mutation site unassignSocket --json-file mutation.site.unassignSocket.json

catocli mutation site unassignSocket '{"siteUnassignSocketInput":{"site":{"by":"ID","input":"string"},"socketIdentifier":"string"}}'

catocli mutation site unassignSocket '{
    "siteUnassignSocketInput": {
        "site": {
            "by": "ID",
            "input": "string"
        },
        "socketIdentifier": "string"
    }
}'
```

#### Operation Arguments for mutation.site.unassignSocket ####

`accountId` [ID] - (required) N/A
`siteUnassignSocketInput` [SiteUnassignSocketInput] - (required) N/A
