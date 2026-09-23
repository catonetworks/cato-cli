
## CATO-CLI - query.networkConfig.dns.suffixSetList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dns.suffixSetList) for documentation on this operation.

### Usage for query.networkConfig.dns.suffixSetList:

```bash
catocli query networkConfig dns suffixSetList -h

catocli query networkConfig dns suffixSetList <json>

catocli query networkConfig dns suffixSetList --json-file query.networkConfig.dns.suffixSetList.json

catocli query networkConfig dns suffixSetList '{"accountId":"id","networkConfigDnsSuffixSetListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig dns suffixSetList '{
    "accountId": "id",
    "networkConfigDnsSuffixSetListInput": {
        "filter": {
            "name": {
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
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.networkConfig.dns.suffixSetList ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsSuffixSetListInput` [NetworkConfigDnsSuffixSetListInput] - (required) N/A    
