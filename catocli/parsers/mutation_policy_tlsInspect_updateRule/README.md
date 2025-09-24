
## CATO-CLI - mutation.policy.tlsInspect.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.updateRule) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.updateRule:

`catocli mutation policy tlsInspect updateRule -h`

`catocli mutation policy tlsInspect updateRule <json>`

`catocli mutation policy tlsInspect updateRule "$(cat < mutation.policy.tlsInspect.updateRule.json)"`

`catocli mutation policy tlsInspect updateRule '{"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"tlsInspectUpdateRuleInput":{"id":"id","tlsInspectUpdateRuleDataInput":{"action":"INSPECT","application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"country":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"customService":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"customServiceIp":{"ip":"example_value","ipRange":{"from":"example_value","to":"example_value"},"name":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"remoteAsn":["example1","example2"],"service":{"by":"ID","input":"string"},"subnet":["example1","example2"],"tlsInspectCategory":"POPULAR_CLOUD_APPS"},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","devicePostureProfile":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"untrustedCertificateAction":"ALLOW"}}}'`

`catocli mutation policy tlsInspect updateRule -p '{
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "tlsInspectUpdateRuleInput": {
        "id": "id",
        "tlsInspectUpdateRuleDataInput": {
            "action": "INSPECT",
            "application": {
                "appCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "application": {
                    "by": "ID",
                    "input": "string"
                },
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "customApp": {
                    "by": "ID",
                    "input": "string"
                },
                "customCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "customService": {
                    "port": [
                        "example1",
                        "example2"
                    ],
                    "portRange": {
                        "from": "example_value",
                        "to": "example_value"
                    },
                    "protocol": "ANY"
                },
                "customServiceIp": {
                    "ip": "example_value",
                    "ipRange": {
                        "from": "example_value",
                        "to": "example_value"
                    },
                    "name": "string"
                },
                "domain": [
                    "example1",
                    "example2"
                ],
                "fqdn": [
                    "example1",
                    "example2"
                ],
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                },
                "ip": [
                    "example1",
                    "example2"
                ],
                "ipRange": {
                    "from": "example_value",
                    "to": "example_value"
                },
                "remoteAsn": [
                    "example1",
                    "example2"
                ],
                "service": {
                    "by": "ID",
                    "input": "string"
                },
                "subnet": [
                    "example1",
                    "example2"
                ],
                "tlsInspectCategory": "POPULAR_CLOUD_APPS"
            },
            "connectionOrigin": "ANY",
            "country": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "devicePostureProfile": {
                "by": "ID",
                "input": "string"
            },
            "enabled": true,
            "name": "string",
            "platform": "WINDOWS",
            "source": {
                "floatingSubnet": {
                    "by": "ID",
                    "input": "string"
                },
                "globalIpRange": {
                    "by": "ID",
                    "input": "string"
                },
                "group": {
                    "by": "ID",
                    "input": "string"
                },
                "host": {
                    "by": "ID",
                    "input": "string"
                },
                "ip": [
                    "example1",
                    "example2"
                ],
                "ipRange": {
                    "from": "example_value",
                    "to": "example_value"
                },
                "networkInterface": {
                    "by": "ID",
                    "input": "string"
                },
                "site": {
                    "by": "ID",
                    "input": "string"
                },
                "siteNetworkSubnet": {
                    "by": "ID",
                    "input": "string"
                },
                "subnet": [
                    "example1",
                    "example2"
                ],
                "systemGroup": {
                    "by": "ID",
                    "input": "string"
                },
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "usersGroup": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "untrustedCertificateAction": "ALLOW"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.updateRule ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
`tlsInspectUpdateRuleInput` [TlsInspectUpdateRuleInput] - (required) N/A    
