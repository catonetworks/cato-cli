
## CATO-CLI - query.networkConfig.dns.forwardingRule:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dns.forwardingRule) for documentation on this operation.

### Usage for query.networkConfig.dns.forwardingRule:

```bash
catocli query networkConfig dns forwardingRule -h

catocli query networkConfig dns forwardingRule <json>

catocli query networkConfig dns forwardingRule --json-file query.networkConfig.dns.forwardingRule.json

catocli query networkConfig dns forwardingRule '{"networkConfigDnsForwardingRuleRefInput":{"by":"ID","input":"string"}}'

catocli query networkConfig dns forwardingRule '{
    "networkConfigDnsForwardingRuleRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.networkConfig.dns.forwardingRule ####

`accountId` [ID] - (required) ID of the account whose network configuration is requested.
`networkConfigDnsForwardingRuleRefInput` [NetworkConfigDnsForwardingRuleRefInput] - (required) A reference to an existing DNS forwarding rule. NAME means its domain, unique per account.
