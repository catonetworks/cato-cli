
## CATO-CLI - mutation.policy.siteWebProxy.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.publishPolicyRevision:

```bash
catocli mutation policy siteWebProxy publishPolicyRevision -h

catocli mutation policy siteWebProxy publishPolicyRevision <json>

catocli mutation policy siteWebProxy publishPolicyRevision --json-file mutation.policy.siteWebProxy.publishPolicyRevision.json

catocli mutation policy siteWebProxy publishPolicyRevision '{"accountId":"id","policyPublishRevisionInput":{"description":"string","name":"string"},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy publishPolicyRevision '{
    "accountId": "id",
    "policyPublishRevisionInput": {
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

#### Operation Arguments for mutation.policy.siteWebProxy.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
