
## CATO-CLI - mutation.networkConfig.dns.setServerSet:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.setServerSet) for documentation on this operation.

### Usage for mutation.networkConfig.dns.setServerSet:

```bash
catocli mutation networkConfig dns setServerSet -h

catocli mutation networkConfig dns setServerSet <json>

catocli mutation networkConfig dns setServerSet --json-file mutation.networkConfig.dns.setServerSet.json

catocli mutation networkConfig dns setServerSet '{"networkConfigDnsSetServerSetInput":{"dnsServerSet":[{"id":"id","name":"string","server":["192.0.2.1"]}]}}'

catocli mutation networkConfig dns setServerSet '{
    "networkConfigDnsSetServerSetInput": {
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

#### Operation Arguments for mutation.networkConfig.dns.setServerSet ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigDnsSetServerSetInput` [NetworkConfigDnsSetServerSetInput] - (required) Input for replacing the whole DNS server set collection.
