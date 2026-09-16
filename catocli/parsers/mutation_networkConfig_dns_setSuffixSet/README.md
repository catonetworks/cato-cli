
## CATO-CLI - mutation.networkConfig.dns.setSuffixSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.setSuffixSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.setSuffixSet:

```bash
catocli mutation networkConfig dns setSuffixSet -h

catocli mutation networkConfig dns setSuffixSet <json>

catocli mutation networkConfig dns setSuffixSet --json-file mutation.networkConfig.dns.setSuffixSet.json

catocli mutation networkConfig dns setSuffixSet '{"networkConfigDnsSetSuffixSetInput":{"dnsSuffixSet":{"id":"id","name":"string","suffix":["example1","example2"]}}}'

catocli mutation networkConfig dns setSuffixSet '{
    "networkConfigDnsSetSuffixSetInput": {
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

#### Operation Arguments for mutation.networkConfig.dns.setSuffixSet ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsSetSuffixSetInput` [NetworkConfigDnsSetSuffixSetInput] - (required) N/A    
