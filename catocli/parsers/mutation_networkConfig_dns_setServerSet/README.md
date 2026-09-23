
## CATO-CLI - mutation.networkConfig.dns.setServerSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.setServerSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.setServerSet:

```bash
catocli mutation networkConfig dns setServerSet -h

catocli mutation networkConfig dns setServerSet <json>

catocli mutation networkConfig dns setServerSet --json-file mutation.networkConfig.dns.setServerSet.json

catocli mutation networkConfig dns setServerSet '{"accountId":"id","networkConfigDnsSetServerSetInput":{"dnsServerSet":{"id":"id","name":"string","server":["example1","example2"]}}}'

catocli mutation networkConfig dns setServerSet '{
    "accountId": "id",
    "networkConfigDnsSetServerSetInput": {
        "dnsServerSet": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.setServerSet ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsSetServerSetInput` [NetworkConfigDnsSetServerSetInput] - (required) N/A    
