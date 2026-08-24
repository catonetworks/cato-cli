
## CATO-CLI - query.networkConfig:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig) for documentation on this operation.

### Usage for query.networkConfig:

```bash
catocli query networkConfig -h

catocli query networkConfig <json>

catocli query networkConfig --json-file query.networkConfig.json

catocli query networkConfig '{"networkConfigDhcpOptionListInput":{"networkConfigDhcpOptionFilterInput":{"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"tag":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"type":{"eq":"ASCII","in":"ASCII","neq":"ASCII","nin":"ASCII"}},"networkConfigDhcpOptionSortInput":{"tag":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"networkConfigDhcpOptionRefInput":{"by":"ID","input":"string"},"networkConfigDhcpRelayGroupListInput":{"networkConfigDhcpRelayGroupFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"networkConfigDhcpRelayGroupSortInput":{"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"networkConfigDhcpRelayGroupRefInput":{"by":"ID","input":"string"},"networkConfigDnsForwardingRuleListInput":{"networkConfigDnsForwardingRuleFilterInput":{"domain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"networkConfigDnsForwardingRuleSortInput":{"domain":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"networkConfigDnsForwardingRuleRefInput":{"by":"ID","input":"string"},"networkConfigDnsServerSetListInput":{"networkConfigDnsServerSetFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"networkConfigDnsServerSetSortInput":{"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"networkConfigDnsServerSetRefInput":{"by":"ID","input":"string"},"networkConfigDnsSuffixSetListInput":{"networkConfigDnsSuffixSetFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"networkConfigDnsSuffixSetSortInput":{"name":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"networkConfigDnsSuffixSetRefInput":{"by":"ID","input":"string"},"siteRefInput":{"by":"ID","input":"string"}}'

catocli query networkConfig '{
    "networkConfigDhcpOptionListInput": {
        "networkConfigDhcpOptionFilterInput": {
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
        "networkConfigDhcpOptionSortInput": {
            "tag": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "networkConfigDhcpOptionRefInput": {
        "by": "ID",
        "input": "string"
    },
    "networkConfigDhcpRelayGroupListInput": {
        "networkConfigDhcpRelayGroupFilterInput": {
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
        "networkConfigDhcpRelayGroupSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "networkConfigDhcpRelayGroupRefInput": {
        "by": "ID",
        "input": "string"
    },
    "networkConfigDnsForwardingRuleListInput": {
        "networkConfigDnsForwardingRuleFilterInput": {
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
        "networkConfigDnsForwardingRuleSortInput": {
            "domain": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "networkConfigDnsForwardingRuleRefInput": {
        "by": "ID",
        "input": "string"
    },
    "networkConfigDnsServerSetListInput": {
        "networkConfigDnsServerSetFilterInput": {
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
        "networkConfigDnsServerSetSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "networkConfigDnsServerSetRefInput": {
        "by": "ID",
        "input": "string"
    },
    "networkConfigDnsSuffixSetListInput": {
        "networkConfigDnsSuffixSetFilterInput": {
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
        "networkConfigDnsSuffixSetSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
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

`accountId` [ID] - (required) N/A    
`networkConfigDhcpOptionListInput` [NetworkConfigDhcpOptionListInput] - (required) N/A    
`networkConfigDhcpOptionRefInput` [NetworkConfigDhcpOptionRefInput] - (required) N/A    
`networkConfigDhcpRelayGroupListInput` [NetworkConfigDhcpRelayGroupListInput] - (required) N/A    
`networkConfigDhcpRelayGroupRefInput` [NetworkConfigDhcpRelayGroupRefInput] - (required) N/A    
`networkConfigDnsForwardingRuleListInput` [NetworkConfigDnsForwardingRuleListInput] - (required) N/A    
`networkConfigDnsForwardingRuleRefInput` [NetworkConfigDnsForwardingRuleRefInput] - (required) N/A    
`networkConfigDnsServerSetListInput` [NetworkConfigDnsServerSetListInput] - (required) N/A    
`networkConfigDnsServerSetRefInput` [NetworkConfigDnsServerSetRefInput] - (required) N/A    
`networkConfigDnsSuffixSetListInput` [NetworkConfigDnsSuffixSetListInput] - (required) N/A    
`networkConfigDnsSuffixSetRefInput` [NetworkConfigDnsSuffixSetRefInput] - (required) N/A    
`siteRefInput` [SiteRefInput] - (required) N/A    
