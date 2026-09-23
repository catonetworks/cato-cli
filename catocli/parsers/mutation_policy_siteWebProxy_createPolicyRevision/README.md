
## CATO-CLI - mutation.policy.siteWebProxy.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.createPolicyRevision:

```bash
catocli mutation policy siteWebProxy createPolicyRevision -h

catocli mutation policy siteWebProxy createPolicyRevision <json>

catocli mutation policy siteWebProxy createPolicyRevision --json-file mutation.policy.siteWebProxy.createPolicyRevision.json

catocli mutation policy siteWebProxy createPolicyRevision '{"accountId":"id","policyCreateRevisionInput":{"description":"string","name":"string"},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy createPolicyRevision '{
    "accountId": "id",
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
