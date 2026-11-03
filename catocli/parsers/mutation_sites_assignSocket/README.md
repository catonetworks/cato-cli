
## CATO-CLI - mutation.sites.assignSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.assignSocket) for documentation on this operation.

### Usage for mutation.sites.assignSocket:

```bash
catocli mutation sites assignSocket -h

catocli mutation sites assignSocket <json>

catocli mutation sites assignSocket --json-file mutation.sites.assignSocket.json

catocli mutation sites assignSocket '{"siteAssignSocketInput":{"description":"string","site":{"by":"ID","input":"string"},"socketIdentifier":"string"}}'

catocli mutation sites assignSocket '{
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

#### Operation Arguments for mutation.sites.assignSocket ####

`accountId` [ID] - (required) N/A
`siteAssignSocketInput` [SiteAssignSocketInput] - (required) N/A
