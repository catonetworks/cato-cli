
## CATO-CLI - mutation.policy.applicationControl.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.addRule) for documentation on this operation.

### Usage for mutation.policy.applicationControl.addRule:

```bash
catocli mutation policy applicationControl addRule -h

catocli mutation policy applicationControl addRule <json>

catocli mutation policy applicationControl addRule --json-file mutation.policy.applicationControl.addRule.json

catocli mutation policy applicationControl addRule '{"applicationControlAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"applicationRule":{"accessMethod":[{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"action":"BLOCK","actionConfig":{"userNotification":[{"by":"ID","input":"string"}]},"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":["APPLICATION"],"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":[{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"applicationActivitySatisfy":"ANY","applicationContext":{"applicationTenant":[{"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}]},"applicationCriteria":{"attributes":{"complianceAttributes":{"hippa":"ANY","isae3402":"ANY","iso27001":"ANY","pciDss":"ANY","soc1":"ANY","soc2":"ANY","soc3":"ANY","sox":"ANY"},"securityAttributes":{"auditTrail":"ANY","encryptionAtRest":"ANY","httpSecurityHeaders":"ANY","mfa":"ANY","rbac":"ANY","rememberPassword":"ANY","sso":"ANY","tlsEnforcement":"ANY","trustedCertificate":"ANY"}},"originCountry":[{"by":"ID","input":"string"}],"risk":[{"risk":3,"riskOperator":"IS"}]},"applicationCriteriaSatisfy":"ANY","device":[{"by":"ID","input":"string"}],"schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"severity":"HIGH","source":{"country":[{"by":"ID","input":"string"}],"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}}},"dataRule":{"accessMethod":[{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"action":"BLOCK","actionConfig":{"userNotification":[{"by":"ID","input":"string"}]},"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":["APPLICATION"],"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":[{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"applicationActivitySatisfy":"ANY","applicationContext":{"applicationTenant":[{"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}]},"applicationCriteria":{"attributes":{"complianceAttributes":{"hippa":"ANY","isae3402":"ANY","iso27001":"ANY","pciDss":"ANY","soc1":"ANY","soc2":"ANY","soc3":"ANY","sox":"ANY"},"securityAttributes":{"auditTrail":"ANY","encryptionAtRest":"ANY","httpSecurityHeaders":"ANY","mfa":"ANY","rbac":"ANY","rememberPassword":"ANY","sso":"ANY","tlsEnforcement":"ANY","trustedCertificate":"ANY"}},"originCountry":[{"by":"ID","input":"string"}],"risk":[{"risk":3,"riskOperator":"IS"}]},"applicationCriteriaSatisfy":"ANY","device":[{"by":"ID","input":"string"}],"dlpProfile":{"contentProfile":[{"by":"ID","input":"string"}],"edmProfile":[{"by":"ID","input":"string"}]},"fileAttribute":[{"contentTypeGroupValues":[{"by":"ID","input":"string"}],"contentTypeValues":[{"by":"ID","input":"string"}],"fileAttribute":"CONTENT_TYPE","operator":"IS","value":"string"}],"fileAttributeSatisfy":"ANY","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"severity":"HIGH","source":{"country":[{"by":"ID","input":"string"}],"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}}},"description":"string","enabled":true,"fileRule":{"accessMethod":[{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"action":"BLOCK","actionConfig":{"userNotification":[{"by":"ID","input":"string"}]},"application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":["APPLICATION"],"customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":[{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}],"applicationActivitySatisfy":"ANY","applicationContext":{"applicationTenant":[{"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}]},"applicationCriteria":{"attributes":{"complianceAttributes":{"hippa":"ANY","isae3402":"ANY","iso27001":"ANY","pciDss":"ANY","soc1":"ANY","soc2":"ANY","soc3":"ANY","sox":"ANY"},"securityAttributes":{"auditTrail":"ANY","encryptionAtRest":"ANY","httpSecurityHeaders":"ANY","mfa":"ANY","rbac":"ANY","rememberPassword":"ANY","sso":"ANY","tlsEnforcement":"ANY","trustedCertificate":"ANY"}},"originCountry":[{"by":"ID","input":"string"}],"risk":[{"risk":3,"riskOperator":"IS"}]},"applicationCriteriaSatisfy":"ANY","device":[{"by":"ID","input":"string"}],"fileAttribute":[{"contentTypeGroupValues":[{"by":"ID","input":"string"}],"contentTypeValues":[{"by":"ID","input":"string"}],"fileAttribute":"CONTENT_TYPE","operator":"IS","value":"string"}],"fileAttributeSatisfy":"ANY","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":["SUNDAY"],"from":"12:34:56","to":"12:34:56"},"customTimeframe":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"severity":"HIGH","source":{"country":[{"by":"ID","input":"string"}],"floatingSubnet":[{"by":"ID","input":"string"}],"globalIpRange":[{"by":"ID","input":"string"}],"group":[{"by":"ID","input":"string"}],"host":[{"by":"ID","input":"string"}],"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"networkInterface":[{"by":"ID","input":"string"}],"site":[{"by":"ID","input":"string"}],"siteNetworkSubnet":[{"by":"ID","input":"string"}],"subnet":["192.0.2.0/24"],"systemGroup":[{"by":"ID","input":"string"}],"user":[{"by":"ID","input":"string"}],"usersGroup":[{"by":"ID","input":"string"}]},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"event":{"enabled":true}}},"name":"string","ruleType":"APPLICATION"}},"applicationControlPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy applicationControl addRule '{
    "applicationControlAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "applicationRule": {
                "accessMethod": [
                    {
                        "accessMethod": "USER_AGENT",
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "action": "BLOCK",
                "actionConfig": {
                    "userNotification": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
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
                    "applicationType": [
                        "APPLICATION"
                    ],
                    "customApp": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "sanctionedAppsCategory": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "applicationActivity": [
                    {
                        "activity": {
                            "by": "ID",
                            "input": "string"
                        },
                        "field": {
                            "by": "ID",
                            "input": "string"
                        },
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "applicationActivitySatisfy": "ANY",
                "applicationContext": {
                    "applicationTenant": [
                        {
                            "operator": "IS",
                            "value": "string",
                            "valueSet": {
                                "by": "ID",
                                "input": "string"
                            }
                        }
                    ]
                },
                "applicationCriteria": {
                    "attributes": {
                        "complianceAttributes": {
                            "hippa": "ANY",
                            "isae3402": "ANY",
                            "iso27001": "ANY",
                            "pciDss": "ANY",
                            "soc1": "ANY",
                            "soc2": "ANY",
                            "soc3": "ANY",
                            "sox": "ANY"
                        },
                        "securityAttributes": {
                            "auditTrail": "ANY",
                            "encryptionAtRest": "ANY",
                            "httpSecurityHeaders": "ANY",
                            "mfa": "ANY",
                            "rbac": "ANY",
                            "rememberPassword": "ANY",
                            "sso": "ANY",
                            "tlsEnforcement": "ANY",
                            "trustedCertificate": "ANY"
                        }
                    },
                    "originCountry": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "risk": [
                        {
                            "risk": 3,
                            "riskOperator": "IS"
                        }
                    ]
                },
                "applicationCriteriaSatisfy": "ANY",
                "device": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
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
                "severity": "HIGH",
                "source": {
                    "country": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
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
            },
            "dataRule": {
                "accessMethod": [
                    {
                        "accessMethod": "USER_AGENT",
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "action": "BLOCK",
                "actionConfig": {
                    "userNotification": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
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
                    "applicationType": [
                        "APPLICATION"
                    ],
                    "customApp": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "sanctionedAppsCategory": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "applicationActivity": [
                    {
                        "activity": {
                            "by": "ID",
                            "input": "string"
                        },
                        "field": {
                            "by": "ID",
                            "input": "string"
                        },
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "applicationActivitySatisfy": "ANY",
                "applicationContext": {
                    "applicationTenant": [
                        {
                            "operator": "IS",
                            "value": "string",
                            "valueSet": {
                                "by": "ID",
                                "input": "string"
                            }
                        }
                    ]
                },
                "applicationCriteria": {
                    "attributes": {
                        "complianceAttributes": {
                            "hippa": "ANY",
                            "isae3402": "ANY",
                            "iso27001": "ANY",
                            "pciDss": "ANY",
                            "soc1": "ANY",
                            "soc2": "ANY",
                            "soc3": "ANY",
                            "sox": "ANY"
                        },
                        "securityAttributes": {
                            "auditTrail": "ANY",
                            "encryptionAtRest": "ANY",
                            "httpSecurityHeaders": "ANY",
                            "mfa": "ANY",
                            "rbac": "ANY",
                            "rememberPassword": "ANY",
                            "sso": "ANY",
                            "tlsEnforcement": "ANY",
                            "trustedCertificate": "ANY"
                        }
                    },
                    "originCountry": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "risk": [
                        {
                            "risk": 3,
                            "riskOperator": "IS"
                        }
                    ]
                },
                "applicationCriteriaSatisfy": "ANY",
                "device": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "dlpProfile": {
                    "contentProfile": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "edmProfile": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
                },
                "fileAttribute": [
                    {
                        "contentTypeGroupValues": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "contentTypeValues": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "fileAttribute": "CONTENT_TYPE",
                        "operator": "IS",
                        "value": "string"
                    }
                ],
                "fileAttributeSatisfy": "ANY",
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
                "severity": "HIGH",
                "source": {
                    "country": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
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
            },
            "description": "string",
            "enabled": true,
            "fileRule": {
                "accessMethod": [
                    {
                        "accessMethod": "USER_AGENT",
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "action": "BLOCK",
                "actionConfig": {
                    "userNotification": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ]
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
                    "applicationType": [
                        "APPLICATION"
                    ],
                    "customApp": {
                        "by": "ID",
                        "input": "string"
                    },
                    "customCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "sanctionedAppsCategory": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "applicationActivity": [
                    {
                        "activity": {
                            "by": "ID",
                            "input": "string"
                        },
                        "field": {
                            "by": "ID",
                            "input": "string"
                        },
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                ],
                "applicationActivitySatisfy": "ANY",
                "applicationContext": {
                    "applicationTenant": [
                        {
                            "operator": "IS",
                            "value": "string",
                            "valueSet": {
                                "by": "ID",
                                "input": "string"
                            }
                        }
                    ]
                },
                "applicationCriteria": {
                    "attributes": {
                        "complianceAttributes": {
                            "hippa": "ANY",
                            "isae3402": "ANY",
                            "iso27001": "ANY",
                            "pciDss": "ANY",
                            "soc1": "ANY",
                            "soc2": "ANY",
                            "soc3": "ANY",
                            "sox": "ANY"
                        },
                        "securityAttributes": {
                            "auditTrail": "ANY",
                            "encryptionAtRest": "ANY",
                            "httpSecurityHeaders": "ANY",
                            "mfa": "ANY",
                            "rbac": "ANY",
                            "rememberPassword": "ANY",
                            "sso": "ANY",
                            "tlsEnforcement": "ANY",
                            "trustedCertificate": "ANY"
                        }
                    },
                    "originCountry": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
                    "risk": [
                        {
                            "risk": 3,
                            "riskOperator": "IS"
                        }
                    ]
                },
                "applicationCriteriaSatisfy": "ANY",
                "device": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "fileAttribute": [
                    {
                        "contentTypeGroupValues": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "contentTypeValues": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "fileAttribute": "CONTENT_TYPE",
                        "operator": "IS",
                        "value": "string"
                    }
                ],
                "fileAttributeSatisfy": "ANY",
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
                "severity": "HIGH",
                "source": {
                    "country": [
                        {
                            "by": "ID",
                            "input": "string"
                        }
                    ],
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
            },
            "name": "string",
            "ruleType": "APPLICATION"
        }
    },
    "applicationControlPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.applicationControl.addRule ####

`accountId` [ID] - (required) N/A
`applicationControlAddRuleInput` [ApplicationControlAddRuleInput] - (required) N/A
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A
