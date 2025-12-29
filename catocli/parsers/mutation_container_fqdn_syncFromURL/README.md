
## CATO-CLI - mutation.container.fqdn.syncFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.syncFromURL) for documentation on this operation.

### Usage for mutation.container.fqdn.syncFromURL:

```bash
catocli mutation container fqdn syncFromURL -h

catocli mutation container fqdn syncFromURL <json>

catocli mutation container fqdn syncFromURL --json-file mutation.container.fqdn.syncFromURL.json

catocli mutation container fqdn syncFromURL '{"syncFqdnContainerFromUrlInput":{"containerRefInput":{"by":"ID","input":"string"}}}'

catocli mutation container fqdn syncFromURL '{
    "syncFqdnContainerFromUrlInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.container.fqdn.syncFromURL ####

`accountId` [ID] - (required) N/A    
`syncFqdnContainerFromUrlInput` [SyncFqdnContainerFromUrlInput] - (required) N/A    
