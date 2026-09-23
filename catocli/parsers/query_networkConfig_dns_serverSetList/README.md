
## CATO-CLI - query.networkConfig.dns.serverSetList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dns.serverSetList) for documentation on this operation.

### Usage for query.networkConfig.dns.serverSetList:

```bash
catocli query networkConfig dns serverSetList -h

catocli query networkConfig dns serverSetList <json>

catocli query networkConfig dns serverSetList --json-file query.networkConfig.dns.serverSetList.json

catocli query networkConfig dns serverSetList '{"accountId":"id","networkConfigDnsServerSetListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig dns serverSetList '{
    "accountId": "id",
    "networkConfigDnsServerSetListInput": {
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

#### Operation Arguments for query.networkConfig.dns.serverSetList ####

`accountId` [ID] - (required) N/A    
`networkConfigDnsServerSetListInput` [NetworkConfigDnsServerSetListInput] - (required) N/A    
