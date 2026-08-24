
## CATO-CLI - mutation.networkConfig:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig) for documentation on this operation.

### Usage for mutation.networkConfig:

```bash
catocli mutation networkConfig -h

catocli mutation networkConfig <json>

catocli mutation networkConfig --json-file mutation.networkConfig.json

catocli mutation networkConfig '{"networkConfigDhcpCreateOptionInput":{"networkConfigDhcpOptionCreateInput":{"description":"string","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpCreateRelayGroupInput":{"networkConfigDhcpRelayGroupCreateInput":{"name":"string","server":["example1","example2"]}},"networkConfigDhcpDeleteOptionInput":{"id":["id1","id2"]},"networkConfigDhcpDeleteRelayGroupInput":{"id":["id1","id2"]},"networkConfigDhcpSetOptionInput":{"networkConfigDhcpOptionUpsertInput":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpSetRelayGroupInput":{"networkConfigDhcpRelayGroupUpsertInput":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDhcpUpdateOptionInput":{"networkConfigDhcpOptionUpdateInput":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpUpdateRelayGroupInput":{"networkConfigDhcpRelayGroupUpdateInput":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDhcpUpdateSettingsInput":{"leaseTime":1,"networkConfigDhcpRelayInput":{"enabled":true,"group":{"by":"ID","input":"string"},"timeout":1}},"networkConfigDnsCreateForwardingRuleInput":{"networkConfigDnsForwardingRuleCreateInput":{"domain":"example_value","server":["example1","example2"]}},"networkConfigDnsCreateServerSetInput":{"networkConfigDnsServerSetCreateInput":{"name":"string","server":["example1","example2"]}},"networkConfigDnsCreateSuffixSetInput":{"networkConfigDnsSuffixSetCreateInput":{"name":"string","suffix":["example1","example2"]}},"networkConfigDnsDeleteForwardingRuleInput":{"id":["id1","id2"]},"networkConfigDnsDeleteServerSetInput":{"id":["id1","id2"]},"networkConfigDnsDeleteSuffixSetInput":{"id":["id1","id2"]},"networkConfigDnsRemoveSiteSettingsInput":{"siteRefInput":{"by":"ID","input":"string"}},"networkConfigDnsSetForwardingRuleInput":{"networkConfigDnsForwardingRuleUpsertInput":{"domain":"example_value","id":"id","server":["example1","example2"]}},"networkConfigDnsSetServerSetInput":{"networkConfigDnsServerSetUpsertInput":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDnsSetSuffixSetInput":{"networkConfigDnsSuffixSetUpsertInput":{"id":"id","name":"string","suffix":["example1","example2"]}},"networkConfigDnsUpdateForwardingRuleInput":{"networkConfigDnsForwardingRuleUpdateInput":{"domain":"example_value","id":"id","server":["example1","example2"]}},"networkConfigDnsUpdateServerSetInput":{"networkConfigDnsServerSetUpdateInput":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDnsUpdateSettingsInput":{"acceptDnsRequestsOnLanInterfaceIp":true,"primaryServer":"example_value","secondaryServer":"example_value","suffix":["example1","example2"]},"networkConfigDnsUpdateSiteSettingsInput":{"networkConfigDnsSiteSettingsUpdateInput":{"primaryServer":"example_value","secondaryServer":"example_value","site":{"by":"ID","input":"string"},"suffix":["example1","example2"]}},"networkConfigDnsUpdateSuffixSetInput":{"networkConfigDnsSuffixSetUpdateInput":{"id":"id","name":"string","suffix":["example1","example2"]}}}'

catocli mutation networkConfig '{
    "networkConfigDhcpCreateOptionInput": {
        "networkConfigDhcpOptionCreateInput": {
            "description": "string",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpCreateRelayGroupInput": {
        "networkConfigDhcpRelayGroupCreateInput": {
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDhcpDeleteOptionInput": {
        "id": [
            "id1",
            "id2"
        ]
    },
    "networkConfigDhcpDeleteRelayGroupInput": {
        "id": [
            "id1",
            "id2"
        ]
    },
    "networkConfigDhcpSetOptionInput": {
        "networkConfigDhcpOptionUpsertInput": {
            "description": "string",
            "id": "id",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpSetRelayGroupInput": {
        "networkConfigDhcpRelayGroupUpsertInput": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDhcpUpdateOptionInput": {
        "networkConfigDhcpOptionUpdateInput": {
            "description": "string",
            "id": "id",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpUpdateRelayGroupInput": {
        "networkConfigDhcpRelayGroupUpdateInput": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDhcpUpdateSettingsInput": {
        "leaseTime": 1,
        "networkConfigDhcpRelayInput": {
            "enabled": true,
            "group": {
                "by": "ID",
                "input": "string"
            },
            "timeout": 1
        }
    },
    "networkConfigDnsCreateForwardingRuleInput": {
        "networkConfigDnsForwardingRuleCreateInput": {
            "domain": "example_value",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsCreateServerSetInput": {
        "networkConfigDnsServerSetCreateInput": {
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsCreateSuffixSetInput": {
        "networkConfigDnsSuffixSetCreateInput": {
            "name": "string",
            "suffix": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsDeleteForwardingRuleInput": {
        "id": [
            "id1",
            "id2"
        ]
    },
    "networkConfigDnsDeleteServerSetInput": {
        "id": [
            "id1",
            "id2"
        ]
    },
    "networkConfigDnsDeleteSuffixSetInput": {
        "id": [
            "id1",
            "id2"
        ]
    },
    "networkConfigDnsRemoveSiteSettingsInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    },
    "networkConfigDnsSetForwardingRuleInput": {
        "networkConfigDnsForwardingRuleUpsertInput": {
            "domain": "example_value",
            "id": "id",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsSetServerSetInput": {
        "networkConfigDnsServerSetUpsertInput": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsSetSuffixSetInput": {
        "networkConfigDnsSuffixSetUpsertInput": {
            "id": "id",
            "name": "string",
            "suffix": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateForwardingRuleInput": {
        "networkConfigDnsForwardingRuleUpdateInput": {
            "domain": "example_value",
            "id": "id",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateServerSetInput": {
        "networkConfigDnsServerSetUpdateInput": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateSettingsInput": {
        "acceptDnsRequestsOnLanInterfaceIp": true,
        "primaryServer": "example_value",
        "secondaryServer": "example_value",
        "suffix": [
            "example1",
            "example2"
        ]
    },
    "networkConfigDnsUpdateSiteSettingsInput": {
        "networkConfigDnsSiteSettingsUpdateInput": {
            "primaryServer": "example_value",
            "secondaryServer": "example_value",
            "site": {
                "by": "ID",
                "input": "string"
            },
            "suffix": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateSuffixSetInput": {
        "networkConfigDnsSuffixSetUpdateInput": {
            "id": "id",
            "name": "string",
            "suffix": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpCreateOptionInput` [NetworkConfigDhcpCreateOptionInput] - (required) N/A    
`networkConfigDhcpCreateRelayGroupInput` [NetworkConfigDhcpCreateRelayGroupInput] - (required) N/A    
`networkConfigDhcpDeleteOptionInput` [NetworkConfigDhcpDeleteOptionInput] - (required) N/A    
`networkConfigDhcpDeleteRelayGroupInput` [NetworkConfigDhcpDeleteRelayGroupInput] - (required) N/A    
`networkConfigDhcpSetOptionInput` [NetworkConfigDhcpSetOptionInput] - (required) N/A    
`networkConfigDhcpSetRelayGroupInput` [NetworkConfigDhcpSetRelayGroupInput] - (required) N/A    
`networkConfigDhcpUpdateOptionInput` [NetworkConfigDhcpUpdateOptionInput] - (required) N/A    
`networkConfigDhcpUpdateRelayGroupInput` [NetworkConfigDhcpUpdateRelayGroupInput] - (required) N/A    
`networkConfigDhcpUpdateSettingsInput` [NetworkConfigDhcpUpdateSettingsInput] - (required) N/A    
`networkConfigDnsCreateForwardingRuleInput` [NetworkConfigDnsCreateForwardingRuleInput] - (required) N/A    
`networkConfigDnsCreateServerSetInput` [NetworkConfigDnsCreateServerSetInput] - (required) N/A    
`networkConfigDnsCreateSuffixSetInput` [NetworkConfigDnsCreateSuffixSetInput] - (required) N/A    
`networkConfigDnsDeleteForwardingRuleInput` [NetworkConfigDnsDeleteForwardingRuleInput] - (required) N/A    
`networkConfigDnsDeleteServerSetInput` [NetworkConfigDnsDeleteServerSetInput] - (required) N/A    
`networkConfigDnsDeleteSuffixSetInput` [NetworkConfigDnsDeleteSuffixSetInput] - (required) N/A    
`networkConfigDnsRemoveSiteSettingsInput` [NetworkConfigDnsRemoveSiteSettingsInput] - (required) N/A    
`networkConfigDnsSetForwardingRuleInput` [NetworkConfigDnsSetForwardingRuleInput] - (required) N/A    
`networkConfigDnsSetServerSetInput` [NetworkConfigDnsSetServerSetInput] - (required) N/A    
`networkConfigDnsSetSuffixSetInput` [NetworkConfigDnsSetSuffixSetInput] - (required) N/A    
`networkConfigDnsUpdateForwardingRuleInput` [NetworkConfigDnsUpdateForwardingRuleInput] - (required) N/A    
`networkConfigDnsUpdateServerSetInput` [NetworkConfigDnsUpdateServerSetInput] - (required) N/A    
`networkConfigDnsUpdateSettingsInput` [NetworkConfigDnsUpdateSettingsInput] - (required) N/A    
`networkConfigDnsUpdateSiteSettingsInput` [NetworkConfigDnsUpdateSiteSettingsInput] - (required) N/A    
`networkConfigDnsUpdateSuffixSetInput` [NetworkConfigDnsUpdateSuffixSetInput] - (required) N/A    
