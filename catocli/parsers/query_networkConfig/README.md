
## CATO-CLI - query.networkConfig:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig) for documentation on this operation.

### Usage for query.networkConfig:

```bash
catocli query networkConfig -h

catocli query networkConfig <json>

catocli query networkConfig --json-file query.networkConfig.json

catocli query networkConfig '{"networkConfigDhcpOptionListInput":{"filter":{"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"tag":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"type":{"eq":"ASCII","in":"ASCII","neq":"ASCII","nin":"ASCII"}},"paging":{"from":1,"limit":1},"sort":{"tag":{"direction":"ASC","priority":1}}},"networkConfigDhcpOptionRefInput":{"by":"ID","input":"string"},"networkConfigDhcpRelayGroupListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}},"networkConfigDhcpRelayGroupRefInput":{"by":"ID","input":"string"},"networkConfigDnsForwardingRuleListInput":{"filter":{"domain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"domain":{"direction":"ASC","priority":1}}},"networkConfigDnsForwardingRuleRefInput":{"by":"ID","input":"string"},"networkConfigDnsServerSetListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}},"networkConfigDnsServerSetRefInput":{"by":"ID","input":"string"},"networkConfigDnsSuffixSetListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}},"networkConfigDnsSuffixSetRefInput":{"by":"ID","input":"string"},"siteRefInput":{"by":"ID","input":"string"}}'

catocli query networkConfig '{
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
    },
    "networkConfigDhcpOptionRefInput": {
        "by": "ID",
        "input": "string"
    },
    "networkConfigDhcpRelayGroupListInput": {
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
    },
    "networkConfigDhcpRelayGroupRefInput": {
        "by": "ID",
        "input": "string"
    },
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
    },
    "networkConfigDnsForwardingRuleRefInput": {
        "by": "ID",
        "input": "string"
    },
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
    },
    "networkConfigDnsServerSetRefInput": {
        "by": "ID",
        "input": "string"
    },
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
    },
    "networkConfigDnsSuffixSetRefInput": {
        "by": "ID",
        "input": "string"
    },
    "siteRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.networkConfig ####

