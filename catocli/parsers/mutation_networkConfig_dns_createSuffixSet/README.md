
## CATO-CLI - mutation.networkConfig.dns.createSuffixSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.createSuffixSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.createSuffixSet:

```bash
catocli mutation networkConfig dns createSuffixSet -h

catocli mutation networkConfig dns createSuffixSet <json>

catocli mutation networkConfig dns createSuffixSet --json-file mutation.networkConfig.dns.createSuffixSet.json

catocli mutation networkConfig dns createSuffixSet '{"networkConfigDnsCreateSuffixSetInput":{"dnsSuffixSet":[{"name":"string","suffix":["example.com"]}]}}'

catocli mutation networkConfig dns createSuffixSet '{
    "networkConfigDnsCreateSuffixSetInput": {
        "dnsSuffixSet": [
            {
                "name": "string",
                "suffix": [
                    "example.com"
                ]
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.createSuffixSet ####

`accountId` [ID] - (required) N/A
`networkConfigDnsCreateSuffixSetInput` [NetworkConfigDnsCreateSuffixSetInput] - (required) N/A
