
## CATO-CLI - query.networkConfig.dhcp.optionList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dhcp.optionList) for documentation on this operation.

### Usage for query.networkConfig.dhcp.optionList:

```bash
catocli query networkConfig dhcp optionList -h

catocli query networkConfig dhcp optionList <json>

catocli query networkConfig dhcp optionList --json-file query.networkConfig.dhcp.optionList.json

catocli query networkConfig dhcp optionList '{"networkConfigDhcpOptionListInput":{"filter":{"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"tag":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"type":{"eq":"ASCII","in":"ASCII","neq":"ASCII","nin":"ASCII"}},"paging":{"from":1,"limit":1},"sort":{"tag":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig dhcp optionList '{
    "networkConfigDhcpOptionListInput": {
        "filter": {
            "description": {
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
            },
            "tag": {
                "between": [
                    1,
                    2
                ],
                "eq": 1,
                "gt": 1,
                "gte": 1,
                "in": [
                    1,
                    2
                ],
                "lt": 1,
                "lte": 1,
                "neq": 1,
                "nin": [
                    1,
                    2
                ]
            },
            "type": {
                "eq": "ASCII",
                "in": "ASCII",
                "neq": "ASCII",
                "nin": "ASCII"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "tag": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.networkConfig.dhcp.optionList ####

