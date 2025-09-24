
## CATO-CLI - mutation.policy.wanFirewall.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.updateRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updateRule:

`catocli mutation policy wanFirewall updateRule -h`

`catocli mutation policy wanFirewall updateRule <json>`

`catocli mutation policy wanFirewall updateRule "$(cat < mutation.policy.wanFirewall.updateRule.json)"`

`catocli mutation policy wanFirewall updateRule '{"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanFirewallUpdateRuleInput":{"id":"id","wanFirewallUpdateRuleDataInput":{"action":"BLOCK","activePeriod":{"effectiveFrom":"example_value","expiresAt":"example_value","useEffectiveFrom":true,"useExpiresAt":true},"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"sanctionedAppsCategory":{"by":"ID","input":"string"},"subnet":["example1","example2"]},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"description":"string","destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"device":{"by":"ID","input":"string"},"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":"WINDOWS","direction":"TO","enabled":true,"exceptions":{"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"domain":["example1","example2"],"fqdn":["example1","example2"],"globalIpRange":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"sanctionedAppsCategory":{"by":"ID","input":"string"},"subnet":["example1","example2"]},"connectionOrigin":"ANY","country":{"by":"ID","input":"string"},"destination":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"device":{"by":"ID","input":"string"},"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":"WINDOWS","direction":"TO","name":"string","service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"standard":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}}},"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"service":{"custom":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"standard":{"by":"ID","input":"string"}},"source":{"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}}}}'`

`catocli mutation policy wanFirewall updateRule -p '{
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanFirewallUpdateRuleInput": {
        "id": "id",
        "wanFirewallUpdateRuleDataInput": {
            "action": "BLOCK",
            "activePeriod": {
                "effectiveFrom": "example_value",
                "expiresAt": "example_value",
                "useEffectiveFrom": true,
                "useExpiresAt": true
            },
            "application": {
                "appCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "application": {
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
                "sanctionedAppsCategory": {
                    "by": "ID",
                    "input": "string"
                },
                "subnet": [
                    "example1",
                    "example2"
                ]
            },
            "connectionOrigin": "ANY",
            "country": {
                "by": "ID",
                "input": "string"
            },
            "description": "string",
            "destination": {
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
            "direction": "TO",
            "enabled": true,
            "exceptions": {
                "application": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
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
                    "sanctionedAppsCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "subnet": [
                        "example1",
                        "example2"
                    ]
                },
                "connectionOrigin": "ANY",
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "destination": {
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
                "direction": "TO",
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
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.updateRule ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
`wanFirewallUpdateRuleInput` [WanFirewallUpdateRuleInput] - (required) N/A    
