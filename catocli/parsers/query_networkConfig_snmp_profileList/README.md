
## CATO-CLI - query.networkConfig.snmp.profileList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.snmp.profileList) for documentation on this operation.

### Usage for query.networkConfig.snmp.profileList:

```bash
catocli query networkConfig snmp profileList -h

catocli query networkConfig snmp profileList <json>

catocli query networkConfig snmp profileList --json-file query.networkConfig.snmp.profileList.json

catocli query networkConfig snmp profileList '{"networkConfigSnmpProfileListInput":{"filter":{"profile":{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]},"username":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig snmp profileList '{
    "networkConfigSnmpProfileListInput": {
        "filter": {
            "profile": {
                "eq": {
                    "by": "ID",
                    "input": "string"
                },
                "in": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "neq": {
                    "by": "ID",
                    "input": "string"
                },
                "nin": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "username": {
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

#### Operation Arguments for query.networkConfig.snmp.profileList ####

`accountId` [ID] - (required) ID of the account whose network configuration is requested.
`networkConfigSnmpProfileListInput` [NetworkConfigSnmpProfileListInput] - (required) N/A
