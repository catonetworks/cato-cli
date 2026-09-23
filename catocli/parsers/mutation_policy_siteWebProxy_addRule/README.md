
## CATO-CLI - mutation.policy.siteWebProxy.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.addRule) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.addRule:

```bash
catocli mutation policy siteWebProxy addRule -h

catocli mutation policy siteWebProxy addRule <json>

catocli mutation policy siteWebProxy addRule --json-file mutation.policy.siteWebProxy.addRule.json

catocli mutation policy siteWebProxy addRule '{"accountId":"id","siteWebProxyAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"associatedSite":{"by":"ID","input":"string"},"authenticationConfig":{"kerberosConfig":{"encryptedKeytab":"string","isEnabled":true},"method":"NONE"},"description":"string","enabled":true,"fqdn":"example_value","name":"string","port":"example_value","shouldAssociateWithAllSites":true}},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy addRule '{
    "accountId": "id",
    "siteWebProxyAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "associatedSite": {
                "by": "ID",
                "input": "string"
            },
            "authenticationConfig": {
                "kerberosConfig": {
                    "encryptedKeytab": "string",
                    "isEnabled": true
                },
                "method": "NONE"
            },
            "description": "string",
            "enabled": true,
            "fqdn": "example_value",
            "name": "string",
            "port": "example_value",
            "shouldAssociateWithAllSites": true
        }
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.addRule ####

`accountId` [ID] - (required) N/A    
`siteWebProxyAddRuleInput` [SiteWebProxyAddRuleInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
