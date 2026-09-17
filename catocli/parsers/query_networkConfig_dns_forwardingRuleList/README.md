
## CATO-CLI - query.networkConfig.dns.forwardingRuleList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dns.forwardingRuleList) for documentation on this operation.

### Usage for query.networkConfig.dns.forwardingRuleList:

```bash
catocli query networkConfig dns forwardingRuleList -h

catocli query networkConfig dns forwardingRuleList <json>

catocli query networkConfig dns forwardingRuleList --json-file query.networkConfig.dns.forwardingRuleList.json

catocli query networkConfig dns forwardingRuleList '{"networkConfigDnsForwardingRuleListInput":{"filter":{"domain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"domain":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig dns forwardingRuleList '{
    "networkConfigDnsForwardingRuleListInput": {
        "filter": {
            "domain": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "domain": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.networkConfig.dns.forwardingRuleList ####

