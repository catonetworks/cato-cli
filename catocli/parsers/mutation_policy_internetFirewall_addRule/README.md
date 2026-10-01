
## CATO-CLI - mutation.policy.internetFirewall.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.addRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addRule:

```bash
catocli mutation policy internetFirewall addRule -h

catocli mutation policy internetFirewall addRule <json>

catocli mutation policy internetFirewall addRule --json-file mutation.policy.internetFirewall.addRule.json

catocli mutation policy internetFirewall addRule '{"internetFirewallAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"action":"BLOCK","actionConfig":{"rbiProfile":[{"by":"ID","input":"string"}],"userNotification":[{"by":"ID","input":"string"}]},"activePeriod":{"effectiveFrom":"2026-01-02T15:04:05Z","expiresAt":"2026-01-02T15:04:05Z","useEffectiveFrom":true,"useExpiresAt":true},"country":[{"by":"ID","input":"string"}],"description":"string","destination":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"containers":{"fqdnContainer":[{"by":"ID","input":"string"}],"ipAddressRangeContainer":[{"by":"ID","input":"string"}]},"country":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"domain":["internal.example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"remoteAsn":[65536],"sanctionedAppsCategory":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"]},"device":[{"by":"ID","input":"string"}],"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":["WINDOWS"],"enabled":true,"exceptions":[{"country":[{"by":"ID","input":"string"}],"destination":{"appCategory":[{"by":"ID","input":"string"}],"application":[{"by":"ID","input":"string"}],"containers":{"fqdnContainer":[{"by":"ID","input":"string"}],"ipAddressRangeContainer":[{"by":"ID","input":"string"}]},"country":[{"by":"ID","input":"string"}],"customApp":[{"by":"ID","input":"string"}],"customCategory":[{"by":"ID","input":"string"}],"domain":["internal.example.com"],"fqdn":["host.example.com"],"globalIpRange":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"remoteAsn":[65536],"sanctionedAppsCategory":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"]},"device":[{"by":"ID","input":"string"}],"deviceAttributes":{"category":["string1","string2"],"manufacturer":["string1","string2"],"model":["string1","string2"],"os":["string1","string2"],"osVersion":["string1","string2"],"type":["string1","string2"]},"deviceOS":["WINDOWS"],"name":"string","service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"standard":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]}}],"name":"string","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"service":{"custom":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"standard":[{"by":"ID","input":"string"}]},"source":{"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}}}},"internetFirewallPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy internetFirewall addRule '{
    "internetFirewallAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "action": "BLOCK",
            "actionConfig": {
                "rbiProfile": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
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
            "country": [
                {
                    "by": "ID",
                    "input": "string"
                }
            ],
            "description": "string",
            "destination": {
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
                "containers": {
                    "fqdnContainer": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "ipAddressRangeContainer": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
                },
                "country": [
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
                "remoteAsn": [
                    65536
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
            "enabled": true,
            "exceptions": [
                {
                    "country": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "destination": {
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
                        "containers": {
                            "fqdnContainer": [
                                {
                                    "by": "ID",
                                    "input": "string"
                                }
                            ],
                            "ipAddressRangeContainer": [
                                {
                                    "by": "ID",
                                    "input": "string"
                                }
                            ]
                        },
                        "country": [
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
                        "remoteAsn": [
                            65536
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
    "internetFirewallPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.internetFirewall.addRule ####

`accountId` [ID] - (required) N/A
`internetFirewallAddRuleInput` [InternetFirewallAddRuleInput] - (required) N/A
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A
