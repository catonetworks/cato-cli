
## CATO-CLI - mutation.policy.siteWebProxy.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.moveSection) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.moveSection:

```bash
catocli mutation policy siteWebProxy moveSection -h

catocli mutation policy siteWebProxy moveSection <json>

catocli mutation policy siteWebProxy moveSection --json-file mutation.policy.siteWebProxy.moveSection.json

catocli mutation policy siteWebProxy moveSection '{"accountId":"id","policyMoveSectionInput":{"id":"id","to":{"position":"AFTER_SECTION","ref":"id"}},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy moveSection '{
    "accountId": "id",
    "policyMoveSectionInput": {
        "id": "id",
        "to": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
