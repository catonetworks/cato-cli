
## CATO-CLI - mutation.policy.internetFirewall.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.addRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addRule:

`catocli mutation policy internetFirewall addRule -h`

`catocli mutation policy internetFirewall addRule <json>`

`catocli mutation policy internetFirewall addRule "$(cat < mutation.policy.internetFirewall.addRule.json)"`

`catocli mutation policy internetFirewall addRule '{"internetFirewallAddRuleInput":{"internetFirewallAddRuleDataInput":{"action":"BLOCK","activePeriod":{"effectiveFrom":"example_value","expiresAt":"example_value","useEffectiveFrom":true,"useExpiresAt":true},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","destination":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"containers":{"fqdnContainer":{"by":"ID","input":"string"},"ipAddressRangeContainer":{"by":"ID","input":"string"}},"country":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"remoteAsn":["example1","example2"],"sanctionedAppsCategory":{"by":"ID","input":"string"},"subnet":["example1","example2"]},"device":{"by":"ID","input":"string"},"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":"WINDOWS","enabled":true,"exceptions":{"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"destination":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"containers":{"fqdnContainer":{"by":"ID","input":"string"},"ipAddressRangeContainer":{"by":"ID","input":"string"}},"country":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"remoteAsn":["example1","example2"],"sanctionedAppsCategory":{"by":"ID","input":"string"},"subnet":["example1","example2"]},"device":{"by":"ID","input":"string"},"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":"WINDOWS","name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"standard":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"standard":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}},"policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy internetFirewall addRule -p '{
    "internetFirewallAddRuleInput": {
        "internetFirewallAddRuleDataInput": {
            "action": "BLOCK",
            "activePeriod": {
                "effectiveFrom": "example_value",
                "expiresAt": "example_value",
                "useEffectiveFrom": true,
                "useExpiresAt": true
            },
            "connectionOrigin": "ANY",
            "country": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "destination": {
                "appCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "application": {
                    "by": "ID",
                    "input": "string"
                },
                "containers": {
                    "fqdnContainer": {
                        "by": "ID",
                        "input": "string"
                    },
                    "ipAddressRangeContainer": {
                        "by": "ID",
                        "input": "string"
                    }
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
                "sanctionedAppsCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "subnet": [
                    "example1",
                    "example2"
                ]
            },
            "device": {
                "by": "ID",
                "input": "string"
            },
            "deviceAttributes": {
                "category": [
                    "string1",
                    "string2"
                ],
                "manufacturer": [
                    "string1",
                    "string2"
                ],
                "model": [
                    "string1",
                    "string2"
                ],
                "os": [
                    "string1",
                    "string2"
                ],
                "osVersion": [
                    "string1",
                    "string2"
                ],
                "type": [
                    "string1",
                    "string2"
                ]
            },
            "deviceOS": "WINDOWS",
            "enabled": true,
            "exceptions": {
                "connectionOrigin": "ANY",
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "destination": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
                        "by": "ID",
                        "input": "string"
                    },
                    "containers": {
                        "fqdnContainer": {
                            "by": "ID",
                            "input": "string"
                        },
                        "ipAddressRangeContainer": {
                            "by": "ID",
                            "input": "string"
                        }
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
                    "sanctionedAppsCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "subnet": [
                        "example1",
                        "example2"
                    ]
                },
                "device": {
                    "by": "ID",
                    "input": "string"
                },
                "deviceAttributes": {
                    "category": [
                        "string1",
                        "string2"
                    ],
                    "manufacturer": [
                        "string1",
                        "string2"
                    ],
                    "model": [
                        "string1",
                        "string2"
                    ],
                    "os": [
                        "string1",
                        "string2"
                    ],
                    "osVersion": [
                        "string1",
                        "string2"
                    ],
                    "type": [
                        "string1",
                        "string2"
                    ]
                },
                "deviceOS": "WINDOWS",
                "name": "string",
                "service": {
                    "custom": {
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
                    "standard": {
                        "by": "ID",
                        "input": "string"
                    }
                },
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
                }
            },
            "name": "string",
            "schedule": {
                "activeOn": "ALWAYS",
                "customRecurring": {
                    "days": "SUNDAY",
                    "from": "example_value",
                    "to": "example_value"
                },
                "customTimeframe": {
                    "from": "example_value",
                    "to": "example_value"
                }
            },
            "service": {
                "custom": {
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
                "standard": {
                    "by": "ID",
                    "input": "string"
                }
            },
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
            "tracking": {
                "alert": {
                    "enabled": true,
                    "frequency": "HOURLY",
                    "mailingList": {
                        "by": "ID",
                        "input": "string"
                    },
                    "subscriptionGroup": {
                        "by": "ID",
                        "input": "string"
                    },
                    "webhook": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "event": {
                    "enabled": true
                }
            }
        },
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.addRule ####

`accountId` [ID] - (required) N/A    
`internetFirewallAddRuleInput` [InternetFirewallAddRuleInput] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
