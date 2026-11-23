
## CATO-CLI - mutation.networkConfig.dns.updateSuffixSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSuffixSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSuffixSet:

```bash
catocli mutation networkConfig dns updateSuffixSet -h

catocli mutation networkConfig dns updateSuffixSet <json>

catocli mutation networkConfig dns updateSuffixSet --json-file mutation.networkConfig.dns.updateSuffixSet.json

catocli mutation networkConfig dns updateSuffixSet '{"networkConfigDnsUpdateSuffixSetInput":{"dnsSuffixSet":[{"id":"id","name":"string","suffix":["example.com"]}]}}'

catocli mutation networkConfig dns updateSuffixSet '{
    "networkConfigDnsUpdateSuffixSetInput": {
        "dnsSuffixSet": [
            {
                "id": "id",
                "name": "string",
                "suffix": [
                    "example.com"
                ]
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSuffixSet ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigDnsUpdateSuffixSetInput` [NetworkConfigDnsUpdateSuffixSetInput] - (required) Input for updating existing DNS suffix sets, addressed by id.
