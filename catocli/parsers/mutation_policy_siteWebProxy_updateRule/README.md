
## CATO-CLI - mutation.policy.siteWebProxy.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.updateRule) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.updateRule:

```bash
catocli mutation policy siteWebProxy updateRule -h

catocli mutation policy siteWebProxy updateRule <json>

catocli mutation policy siteWebProxy updateRule --json-file mutation.policy.siteWebProxy.updateRule.json

catocli mutation policy siteWebProxy updateRule '{"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}},"siteWebProxyUpdateRuleInput":{"id":"id","rule":{"associatedSite":{"by":"ID","input":"string"},"authenticationConfig":{"kerberosConfig":{"encryptedKeytab":"string","isEnabled":true},"method":"NONE"},"description":"string","enabled":true,"fqdn":"example_value","name":"string","port":"example_value","shouldAssociateWithAllSites":true}}}'

catocli mutation policy siteWebProxy updateRule '{
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "siteWebProxyUpdateRuleInput": {
        "id": "id",
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
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.updateRule ####

`accountId` [ID] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
`siteWebProxyUpdateRuleInput` [SiteWebProxyUpdateRuleInput] - (required) N/A    
