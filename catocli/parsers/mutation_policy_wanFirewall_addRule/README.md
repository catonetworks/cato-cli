
## CATO-CLI - mutation.policy.wanFirewall.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.addRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.addRule:

```bash
catocli mutation policy wanFirewall addRule -h

catocli mutation policy wanFirewall addRule <json>

catocli mutation policy wanFirewall addRule --json-file mutation.policy.wanFirewall.addRule.json

catocli mutation policy wanFirewall addRule '{"wanFirewallAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":"BLOCK","actionConfig":{"userNotification":[{"by":"ID","input":"string"}]},"activePeriod":{"effectiveFrom":"2026-01-02T15:04:05Z","expiresAt":"2026-01-02T15:04:05Z","useEffectiveFrom":true,"useExpiresAt":true},"application":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"domain":["internal.example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"sanctionedAppsCategory":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"]},"country":[{"by":"ID","input":"string"}],"description":"string","destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"device":[{"by":"ID","input":"string"}],"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":["WINDOWS"],"direction":"TO","enabled":true,"exceptions":[{"application":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"domain":["internal.example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"sanctionedAppsCategory":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"]},"country":[{"by":"ID","input":"string"}],"destination":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"device":[{"by":"ID","input":"string"}],"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":["WINDOWS"],"direction":"TO","name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"standard":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}],"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"standard":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}}}},"wanFirewallPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy wanFirewall addRule '{
    "wanFirewallAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "action": "BLOCK",
            "actionConfig": {
                "userNotification": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "activePeriod": {
                "effectiveFrom": "2026-01-02T15:04:05Z",
                "expiresAt": "2026-01-02T15:04:05Z",
                "useEffectiveFrom": true,
                "useExpiresAt": true
            },
            "application": {
                "appCategory": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "application": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "customApp": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "customCategory": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "domain": [
                    "internal.example.com"
                ],
                "fqdn": [
                    "host.example.com"
                ],
                "globalIpRange": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "ip": [
                    "192.0.2.1"
                ],
                "ipRange": [
                    {
                        "from": "192.0.2.1",
                        "to": "192.0.2.1"
                    }
                ],
                "sanctionedAppsCategory": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ]
            },
            "country": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "description": "string",
            "destination": {
                "floatingSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "globalIpRange": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "group": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "host": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "ip": [
                    "192.0.2.1"
                ],
                "ipRange": [
                    {
                        "from": "192.0.2.1",
                        "to": "192.0.2.1"
                    }
                ],
                "networkInterface": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "site": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "siteNetworkSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ],
                "systemGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "user": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "usersGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "device": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
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
            "deviceOS": [
                "WINDOWS"
            ],
            "direction": "TO",
            "enabled": true,
            "exceptions": [
                {
                    "application": {
                        "appCategory": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "application": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "customApp": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "customCategory": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "domain": [
                            "internal.example.com"
                        ],
                        "fqdn": [
                            "host.example.com"
                        ],
                        "globalIpRange": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "ip": [
                            "192.0.2.1"
                        ],
                        "ipRange": [
                            {
                                "from": "192.0.2.1",
                                "to": "192.0.2.1"
                            }
                        ],
                        "sanctionedAppsCategory": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "subnet": [
                            "192.0.2.0/24"
                        ]
                    },
                    "country": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "destination": {
                        "floatingSubnet": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "globalIpRange": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "group": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "host": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "ip": [
                            "192.0.2.1"
                        ],
                        "ipRange": [
                            {
                                "from": "192.0.2.1",
                                "to": "192.0.2.1"
                            }
                        ],
                        "networkInterface": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "site": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "siteNetworkSubnet": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "subnet": [
                            "192.0.2.0/24"
                        ],
                        "systemGroup": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "user": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "usersGroup": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    },
                    "device": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
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
                    "deviceOS": [
                        "WINDOWS"
                    ],
                    "direction": "TO",
                    "name": "string",
                    "service": {
                        "custom": [
                            {
                                "port": [
                                    443
                                ],
                                "portRange": {
                                    "from": 443,
                                    "to": 443
                                },
                                "protocol": "ANY"
                            }
                        ],
                        "standard": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    },
                    "source": {
                        "floatingSubnet": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "globalIpRange": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "group": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "host": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "ip": [
                            "192.0.2.1"
                        ],
                        "ipRange": [
                            {
                                "from": "192.0.2.1",
                                "to": "192.0.2.1"
                            }
                        ],
                        "networkInterface": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "site": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "siteNetworkSubnet": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "subnet": [
                            "192.0.2.0/24"
                        ],
                        "systemGroup": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "user": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "usersGroup": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                }
            ],
            "name": "string",
            "schedule": {
                "activeOn": "ALWAYS",
                "customRecurring": {
                    "days": [
                        "SUNDAY"
                    ],
                    "from": "12:34:56",
                    "to": "12:34:56"
                },
                "customTimeframe": {
                    "from": "2026-01-02T15:04:05Z",
                    "to": "2026-01-02T15:04:05Z"
                }
            },
            "service": {
                "custom": [
                    {
                        "port": [
                            443
                        ],
                        "portRange": {
                            "from": 443,
                            "to": 443
                        },
                        "protocol": "ANY"
                    }
                ],
                "standard": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "source": {
                "floatingSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "globalIpRange": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "group": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "host": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "ip": [
                    "192.0.2.1"
                ],
                "ipRange": [
                    {
                        "from": "192.0.2.1",
                        "to": "192.0.2.1"
                    }
                ],
                "networkInterface": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "site": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "siteNetworkSubnet": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subnet": [
                    "192.0.2.0/24"
                ],
                "systemGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "user": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "usersGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "tracking": {
                "alert": {
                    "enabled": true,
                    "frequency": "HOURLY",
                    "mailingList": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "subscriptionGroup": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "webhook": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
                },
                "event": {
                    "enabled": true
                }
            }
        }
    },
    "wanFirewallPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.wanFirewall.addRule ####

`accountId` [ID] - (required) N/A
`wanFirewallAddRuleInput` [WanFirewallAddRuleInput] - (required) N/A
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A
