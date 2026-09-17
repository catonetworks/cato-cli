
## CATO-CLI - mutation.networkConfig.dns.createForwardingRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.createForwardingRule) for documentation on this operation.

### Usage for mutation.networkConfig.dns.createForwardingRule:

```bash
catocli mutation networkConfig dns createForwardingRule -h

catocli mutation networkConfig dns createForwardingRule <json>

catocli mutation networkConfig dns createForwardingRule --json-file mutation.networkConfig.dns.createForwardingRule.json

catocli mutation networkConfig dns createForwardingRule '{"networkConfigDnsCreateForwardingRuleInput":{"forwardingRule":{"domain":"example_value","server":["example1","example2"]}}}'

catocli mutation networkConfig dns createForwardingRule '{
    "networkConfigDnsCreateForwardingRuleInput": {
        "forwardingRule": {
            "domain": "example_value",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dns.createForwardingRule ####

