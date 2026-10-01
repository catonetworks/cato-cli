
## CATO-CLI - mutation.networkConfig.dns.updateServerSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateServerSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateServerSet:

```bash
catocli mutation networkConfig dns updateServerSet -h

catocli mutation networkConfig dns updateServerSet <json>

catocli mutation networkConfig dns updateServerSet --json-file mutation.networkConfig.dns.updateServerSet.json

catocli mutation networkConfig dns updateServerSet '{"networkConfigDnsUpdateServerSetInput":{"dnsServerSet":[{"id":"id","name":"string","server":["192.0.2.1"]}]}}'

catocli mutation networkConfig dns updateServerSet '{
    "networkConfigDnsUpdateServerSetInput": {
        "dnsServerSet": [
            {
                "id": "id",
                "name": "string",
                "server": [
                    "192.0.2.1"
                ]
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.updateServerSet ####

`accountId` [ID] - (required) N/A
`networkConfigDnsUpdateServerSetInput` [NetworkConfigDnsUpdateServerSetInput] - (required) N/A
