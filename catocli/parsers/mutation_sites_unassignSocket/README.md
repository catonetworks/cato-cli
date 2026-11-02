
## CATO-CLI - mutation.sites.unassignSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.unassignSocket) for documentation on this operation.

### Usage for mutation.sites.unassignSocket:

```bash
catocli mutation sites unassignSocket -h

catocli mutation sites unassignSocket <json>

catocli mutation sites unassignSocket --json-file mutation.sites.unassignSocket.json

catocli mutation sites unassignSocket '{"siteUnassignSocketInput":{"site":{"by":"ID","input":"string"},"socketIdentifier":"string"}}'

catocli mutation sites unassignSocket '{
    "siteUnassignSocketInput": {
        "site": {
            "by": "ID",
            "input": "string"
        },
        "socketIdentifier": "string"
    }
}'
```

#### Operation Arguments for mutation.sites.unassignSocket ####

`accountId` [ID] - (required) N/A
`siteUnassignSocketInput` [SiteUnassignSocketInput] - (required) N/A
