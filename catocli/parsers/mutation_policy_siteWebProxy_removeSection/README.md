
## CATO-CLI - mutation.policy.siteWebProxy.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.removeSection) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.removeSection:

```bash
catocli mutation policy siteWebProxy removeSection -h

catocli mutation policy siteWebProxy removeSection <json>

catocli mutation policy siteWebProxy removeSection --json-file mutation.policy.siteWebProxy.removeSection.json

catocli mutation policy siteWebProxy removeSection '{"accountId":"id","policyRemoveSectionInput":{"id":"id"},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy removeSection '{
    "accountId": "id",
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
