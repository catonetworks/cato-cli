
## CATO-CLI - mutation.policy.applicationControl.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.updateRule) for documentation on this operation.

### Usage for mutation.policy.applicationControl.updateRule:

`catocli mutation policy applicationControl updateRule -h`

`catocli mutation policy applicationControl updateRule <json>`

`catocli mutation policy applicationControl updateRule "$(cat < mutation.policy.applicationControl.updateRule.json)"`

`catocli mutation policy applicationControl updateRule '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"applicationControlUpdateRuleInput":{"applicationControlUpdateRuleDataInput":{"applicationRule":{"accessMethod":{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"action":"BLOCK","application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":"APPLICATION","customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"applicationActivitySatisfy":"ANY","applicationContext":{"applicationTenant":{"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}},"applicationCriteria":{"attributes":{"complianceAttributes":{"hippa":"ANY","isae3402":"ANY","iso27001":"ANY","pciDss":"ANY","soc1":"ANY","soc2":"ANY","soc3":"ANY","sox":"ANY"},"securityAttributes":{"auditTrail":"ANY","encryptionAtRest":"ANY","httpSecurityHeaders":"ANY","mfa":"ANY","rbac":"ANY","rememberPassword":"ANY","sso":"ANY","tlsEnforcement":"ANY","trustedCertificate":"ANY"}},"originCountry":{"by":"ID","input":"string"},"risk":{"risk":"example_value","riskOperator":"IS"}},"applicationCriteriaSatisfy":"ANY","device":{"by":"ID","input":"string"},"schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"severity":"HIGH","source":{"country":{"by":"ID","input":"string"},"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}},"dataRule":{"accessMethod":{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"action":"BLOCK","application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":"APPLICATION","customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"applicationActivitySatisfy":"ANY","applicationContext":{"applicationTenant":{"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}}},"device":{"by":"ID","input":"string"},"dlpProfile":{"contentProfile":{"by":"ID","input":"string"},"edmProfile":{"by":"ID","input":"string"}},"fileAttribute":{"contentTypeGroupValues":{"by":"ID","input":"string"},"contentTypeValues":{"by":"ID","input":"string"},"fileAttribute":"CONTENT_TYPE","operator":"IS","value":"string"},"fileAttributeSatisfy":"ANY","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"severity":"HIGH","source":{"country":{"by":"ID","input":"string"},"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}},"description":"string","enabled":true,"fileRule":{"accessMethod":{"accessMethod":"USER_AGENT","operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"action":"BLOCK","application":{"appCategory":{"by":"ID","input":"string"},"application":{"by":"ID","input":"string"},"applicationType":"APPLICATION","customApp":{"by":"ID","input":"string"},"customCategory":{"by":"ID","input":"string"},"sanctionedAppsCategory":{"by":"ID","input":"string"}},"applicationActivity":{"activity":{"by":"ID","input":"string"},"field":{"by":"ID","input":"string"},"operator":"IS","value":"string","valueSet":{"by":"ID","input":"string"}},"applicationActivitySatisfy":"ANY","device":{"by":"ID","input":"string"},"fileAttribute":{"contentTypeGroupValues":{"by":"ID","input":"string"},"contentTypeValues":{"by":"ID","input":"string"},"fileAttribute":"CONTENT_TYPE","operator":"IS","value":"string"},"fileAttributeSatisfy":"ANY","schedule":{"activeOn":"ALWAYS","customRecurring":{"days":"SUNDAY","from":"example_value","to":"example_value"},"customTimeframe":{"from":"example_value","to":"example_value"}},"severity":"HIGH","source":{"country":{"by":"ID","input":"string"},"floatingSubnet":{"by":"ID","input":"string"},"globalIpRange":{"by":"ID","input":"string"},"group":{"by":"ID","input":"string"},"host":{"by":"ID","input":"string"},"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"networkInterface":{"by":"ID","input":"string"},"site":{"by":"ID","input":"string"},"siteNetworkSubnet":{"by":"ID","input":"string"},"subnet":["example1","example2"],"systemGroup":{"by":"ID","input":"string"},"user":{"by":"ID","input":"string"},"usersGroup":{"by":"ID","input":"string"}},"tracking":{"alert":{"enabled":true,"frequency":"HOURLY","mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"event":{"enabled":true}}},"name":"string","ruleType":"APPLICATION"},"id":"id"}}'`

`catocli mutation policy applicationControl updateRule -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "applicationControlUpdateRuleInput": {
        "applicationControlUpdateRuleDataInput": {
            "applicationRule": {
                "accessMethod": {
                    "accessMethod": "USER_AGENT",
                    "operator": "IS",
                    "value": "string",
                    "valueSet": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "action": "BLOCK",
                "application": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
                        "by": "ID",
                        "input": "string"
                    },
                    "applicationType": "APPLICATION",
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
                "applicationActivity": {
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
                },
                "applicationActivitySatisfy": "ANY",
                "applicationContext": {
                    "applicationTenant": {
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
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
                    "originCountry": {
                        "by": "ID",
                        "input": "string"
                    },
                    "risk": {
                        "risk": "example_value",
                        "riskOperator": "IS"
                    }
                },
                "applicationCriteriaSatisfy": "ANY",
                "device": {
                    "by": "ID",
                    "input": "string"
                },
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
                "severity": "HIGH",
                "source": {
                    "country": {
                        "by": "ID",
                        "input": "string"
                    },
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
            "dataRule": {
                "accessMethod": {
                    "accessMethod": "USER_AGENT",
                    "operator": "IS",
                    "value": "string",
                    "valueSet": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "action": "BLOCK",
                "application": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
                        "by": "ID",
                        "input": "string"
                    },
                    "applicationType": "APPLICATION",
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
                "applicationActivity": {
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
                },
                "applicationActivitySatisfy": "ANY",
                "applicationContext": {
                    "applicationTenant": {
                        "operator": "IS",
                        "value": "string",
                        "valueSet": {
                            "by": "ID",
                            "input": "string"
                        }
                    }
                },
                "device": {
                    "by": "ID",
                    "input": "string"
                },
                "dlpProfile": {
                    "contentProfile": {
                        "by": "ID",
                        "input": "string"
                    },
                    "edmProfile": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "fileAttribute": {
                    "contentTypeGroupValues": {
                        "by": "ID",
                        "input": "string"
                    },
                    "contentTypeValues": {
                        "by": "ID",
                        "input": "string"
                    },
                    "fileAttribute": "CONTENT_TYPE",
                    "operator": "IS",
                    "value": "string"
                },
                "fileAttributeSatisfy": "ANY",
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
                "severity": "HIGH",
                "source": {
                    "country": {
                        "by": "ID",
                        "input": "string"
                    },
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
            "description": "string",
            "enabled": true,
            "fileRule": {
                "accessMethod": {
                    "accessMethod": "USER_AGENT",
                    "operator": "IS",
                    "value": "string",
                    "valueSet": {
                        "by": "ID",
                        "input": "string"
                    }
                },
                "action": "BLOCK",
                "application": {
                    "appCategory": {
                        "by": "ID",
                        "input": "string"
                    },
                    "application": {
                        "by": "ID",
                        "input": "string"
                    },
                    "applicationType": "APPLICATION",
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
                "applicationActivity": {
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
                },
                "applicationActivitySatisfy": "ANY",
                "device": {
                    "by": "ID",
                    "input": "string"
                },
                "fileAttribute": {
                    "contentTypeGroupValues": {
                        "by": "ID",
                        "input": "string"
                    },
                    "contentTypeValues": {
                        "by": "ID",
                        "input": "string"
                    },
                    "fileAttribute": "CONTENT_TYPE",
                    "operator": "IS",
                    "value": "string"
                },
                "fileAttributeSatisfy": "ANY",
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
                "severity": "HIGH",
                "source": {
                    "country": {
                        "by": "ID",
                        "input": "string"
                    },
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
            "name": "string",
            "ruleType": "APPLICATION"
        },
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.updateRule ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`applicationControlUpdateRuleInput` [ApplicationControlUpdateRuleInput] - (required) N/A    
