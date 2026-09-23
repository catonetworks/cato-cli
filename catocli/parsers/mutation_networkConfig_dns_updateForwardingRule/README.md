
## CATO-CLI - mutation.networkConfig.dns.updateForwardingRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dns.updateForwardingRule) for documentation on this operation.

### Usage for mutation.networkConfig.dns.updateForwardingRule:

```bash
catocli mutation networkConfig dns updateForwardingRule -h

catocli mutation networkConfig dns updateForwardingRule <json>

catocli mutation networkConfig dns updateForwardingRule --json-file mutation.networkConfig.dns.updateForwardingRule.json

catocli mutation networkConfig dns updateForwardingRule '{"accountId":"id","networkConfigDnsUpdateForwardingRuleInput":{"forwardingRule":{"domain":"example_value","id":"id","server":["example1","example2"]}}}'

catocli mutation networkConfig dns updateForwardingRule '{
    "accountId": "id",
    "networkConfigDnsUpdateForwardingRuleInput": {
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

#### Operation Arguments for mutation.networkConfig.dns.updateForwardingRule ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsUpdateForwardingRuleInput` [NetworkConfigDnsUpdateForwardingRuleInput] - (required) N/A    
