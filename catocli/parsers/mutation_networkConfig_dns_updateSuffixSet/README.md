
## CATO-CLI - mutation.networkConfig.dns.updateSuffixSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateSuffixSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateSuffixSet:

```bash
catocli mutation networkConfig dns updateSuffixSet -h

catocli mutation networkConfig dns updateSuffixSet <json>

catocli mutation networkConfig dns updateSuffixSet --json-file mutation.networkConfig.dns.updateSuffixSet.json

catocli mutation networkConfig dns updateSuffixSet '{"networkConfigDnsUpdateSuffixSetInput":{"dnsSuffixSet":{"id":"id","name":"string","suffix":["example1","example2"]}}}'

catocli mutation networkConfig dns updateSuffixSet '{
    "networkConfigDnsUpdateSuffixSetInput": {
        "dnsSuffixSet": {
            "id": "id",
            "name": "string",
            "suffix": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateSuffixSet ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsUpdateSuffixSetInput` [NetworkConfigDnsUpdateSuffixSetInput] - (required) N/A    
