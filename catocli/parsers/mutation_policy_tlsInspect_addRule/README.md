
## CATO-CLI - mutation.policy.tlsInspect.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.addRule) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.addRule:

`catocli mutation policy tlsInspect addRule -h`

`catocli mutation policy tlsInspect addRule <json>`

`catocli mutation policy tlsInspect addRule "$(cat < mutation.policy.tlsInspect.addRule.json)"`

`catocli mutation policy tlsInspect addRule '{"tlsInspectAddRuleInput":{"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"},"tlsInspectAddRuleDataInput":{"action":"INSPECT","application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"country":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"customService":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"customServiceIp":{"ip":"example_value","ipRange":{"from":"example_value","to":"example_value"},"name":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"remoteAsn":["example1","example2"],"service":{"by":"ID","input":"string"},"subnet":["example1","example2"],"tlsInspectCategory":"POPULAR_CLOUD_APPS"},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","devicePostureProfile":{"by":"ID","input":"string"},"enabled":true,"name":"string","platform":"WINDOWS","source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"untrustedCertificateAction":"ALLOW"}},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect addRule -p '{
    "tlsInspectAddRuleInput": {
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "tlsInspectAddRuleDataInput": {
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
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.addRule ####

`accountId` [ID] - (required) N/A    
`tlsInspectAddRuleInput` [TlsInspectAddRuleInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
