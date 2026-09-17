
## CATO-CLI - mutation.networkConfig.dns.setForwardingRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.setForwardingRule) for documentation on this operation.

### Usage for mutation.networkConfig.dns.setForwardingRule:

```bash
catocli mutation networkConfig dns setForwardingRule -h

catocli mutation networkConfig dns setForwardingRule <json>

catocli mutation networkConfig dns setForwardingRule --json-file mutation.networkConfig.dns.setForwardingRule.json

catocli mutation networkConfig dns setForwardingRule '{"networkConfigDnsSetForwardingRuleInput":{"forwardingRule":{"domain":"example_value","id":"id","server":["example1","example2"]}}}'

catocli mutation networkConfig dns setForwardingRule '{
    "networkConfigDnsSetForwardingRuleInput": {
        "forwardingRule": {
            "domain": "example_value",
            "id": "id",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.setForwardingRule ####

