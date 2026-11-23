
## CATO-CLI - mutation.container.delete:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.delete) for documentation on this operation.

### Usage for mutation.container.delete:

```bash
catocli mutation container delete -h

catocli mutation container delete <json>

catocli mutation container delete --json-file mutation.container.delete.json

catocli mutation container delete '{"deleteContainerInput":{"ref":{"by":"ID","input":"string"}}}'

catocli mutation container delete '{
    "deleteContainerInput": {
        "ref": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.container.delete ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`deleteContainerInput` [DeleteContainerInput] - (required) Reference identifying the container to delete.
