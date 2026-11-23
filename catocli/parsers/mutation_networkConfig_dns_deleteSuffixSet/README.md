
## CATO-CLI - mutation.networkConfig.dns.deleteSuffixSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.deleteSuffixSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.deleteSuffixSet:

```bash
catocli mutation networkConfig dns deleteSuffixSet -h

catocli mutation networkConfig dns deleteSuffixSet <json>

catocli mutation networkConfig dns deleteSuffixSet --json-file mutation.networkConfig.dns.deleteSuffixSet.json

catocli mutation networkConfig dns deleteSuffixSet '{"networkConfigDnsDeleteSuffixSetInput":{"id":["id1","id2"]}}'

catocli mutation networkConfig dns deleteSuffixSet '{
    "networkConfigDnsDeleteSuffixSetInput": {
        "id": [
            "id1",
            "id2"
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.deleteSuffixSet ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigDnsDeleteSuffixSetInput` [NetworkConfigDnsDeleteSuffixSetInput] - (required) Input for deleting DNS suffix sets.
