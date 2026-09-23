
## CATO-CLI - mutation.networkConfig.dns.createServerSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.createServerSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.createServerSet:

```bash
catocli mutation networkConfig dns createServerSet -h

catocli mutation networkConfig dns createServerSet <json>

catocli mutation networkConfig dns createServerSet --json-file mutation.networkConfig.dns.createServerSet.json

catocli mutation networkConfig dns createServerSet '{"networkConfigDnsCreateServerSetInput":{"dnsServerSet":{"name":"string","server":["example1","example2"]}}}'

catocli mutation networkConfig dns createServerSet '{
    "networkConfigDnsCreateServerSetInput": {
        "dnsServerSet": {
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.createServerSet ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsCreateServerSetInput` [NetworkConfigDnsCreateServerSetInput] - (required) N/A    
