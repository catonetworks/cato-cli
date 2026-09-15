
## CATO-CLI - mutation.networkConfig:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig) for documentation on this operation.

### Usage for mutation.networkConfig:

```bash
catocli mutation networkConfig -h

catocli mutation networkConfig <json>

catocli mutation networkConfig --json-file mutation.networkConfig.json

catocli mutation networkConfig '{"networkConfigDhcpCreateOptionInput":{"option":{"description":"string","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpCreateRelayGroupInput":{"relayGroup":{"name":"string","server":["example1","example2"]}},"networkConfigDhcpDeleteOptionInput":{"id":["id1","id2"]},"networkConfigDhcpDeleteRelayGroupInput":{"id":["id1","id2"]},"networkConfigDhcpSetOptionInput":{"option":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpSetRelayGroupInput":{"relayGroup":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDhcpUpdateOptionInput":{"option":{"description":"string","id":"id","tag":1,"type":"ASCII","value":"string"}},"networkConfigDhcpUpdateRelayGroupInput":{"relayGroup":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDhcpUpdateSettingsInput":{"leaseTime":1,"relay":{"enabled":true,"group":{"by":"ID","input":"string"},"timeout":1}},"networkConfigDnsCreateForwardingRuleInput":{"forwardingRule":{"domain":"example_value","server":["example1","example2"]}},"networkConfigDnsCreateServerSetInput":{"dnsServerSet":{"name":"string","server":["example1","example2"]}},"networkConfigDnsCreateSuffixSetInput":{"dnsSuffixSet":{"name":"string","suffix":["example1","example2"]}},"networkConfigDnsDeleteForwardingRuleInput":{"id":["id1","id2"]},"networkConfigDnsDeleteServerSetInput":{"id":["id1","id2"]},"networkConfigDnsDeleteSuffixSetInput":{"id":["id1","id2"]},"networkConfigDnsRemoveSiteSettingsInput":{"site":{"by":"ID","input":"string"}},"networkConfigDnsSetForwardingRuleInput":{"forwardingRule":{"domain":"example_value","id":"id","server":["example1","example2"]}},"networkConfigDnsSetServerSetInput":{"dnsServerSet":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDnsSetSuffixSetInput":{"dnsSuffixSet":{"id":"id","name":"string","suffix":["example1","example2"]}},"networkConfigDnsUpdateForwardingRuleInput":{"forwardingRule":{"domain":"example_value","id":"id","server":["example1","example2"]}},"networkConfigDnsUpdateServerSetInput":{"dnsServerSet":{"id":"id","name":"string","server":["example1","example2"]}},"networkConfigDnsUpdateSettingsInput":{"acceptDnsRequestsOnLanInterfaceIp":true,"primaryServer":"example_value","secondaryServer":"example_value","suffix":["example1","example2"]},"networkConfigDnsUpdateSiteSettingsInput":{"siteSettings":{"primaryServer":"example_value","secondaryServer":"example_value","site":{"by":"ID","input":"string"},"suffix":["example1","example2"]}},"networkConfigDnsUpdateSuffixSetInput":{"dnsSuffixSet":{"id":"id","name":"string","suffix":["example1","example2"]}}}'

catocli mutation networkConfig '{
    "networkConfigDhcpCreateOptionInput": {
        "option": {
            "description": "string",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpCreateRelayGroupInput": {
        "relayGroup": {
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
        "option": {
            "description": "string",
            "id": "id",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpSetRelayGroupInput": {
        "relayGroup": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDhcpUpdateOptionInput": {
        "option": {
            "description": "string",
            "id": "id",
            "tag": 1,
            "type": "ASCII",
            "value": "string"
        }
    },
    "networkConfigDhcpUpdateRelayGroupInput": {
        "relayGroup": {
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
        "relay": {
            "enabled": true,
            "group": {
                "by": "ID",
                "input": "string"
            },
            "timeout": 1
        }
    },
    "networkConfigDnsCreateForwardingRuleInput": {
        "forwardingRule": {
            "domain": "example_value",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsCreateServerSetInput": {
        "dnsServerSet": {
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsCreateSuffixSetInput": {
        "dnsSuffixSet": {
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
        "site": {
            "by": "ID",
            "input": "string"
        }
    },
    "networkConfigDnsSetForwardingRuleInput": {
        "forwardingRule": {
            "domain": "example_value",
            "id": "id",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsSetServerSetInput": {
        "dnsServerSet": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsSetSuffixSetInput": {
        "dnsSuffixSet": {
            "id": "id",
            "name": "string",
            "suffix": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateForwardingRuleInput": {
        "forwardingRule": {
            "domain": "example_value",
            "id": "id",
            "server": [
                "example1",
                "example2"
            ]
        }
    },
    "networkConfigDnsUpdateServerSetInput": {
        "dnsServerSet": {
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
        "siteSettings": {
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
        "dnsSuffixSet": {
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

