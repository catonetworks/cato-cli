
## CATO-CLI - mutation.policy.siteWebProxy.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.discardPolicyRevision:

```bash
catocli mutation policy siteWebProxy discardPolicyRevision -h

catocli mutation policy siteWebProxy discardPolicyRevision <json>

catocli mutation policy siteWebProxy discardPolicyRevision --json-file mutation.policy.siteWebProxy.discardPolicyRevision.json

catocli mutation policy siteWebProxy discardPolicyRevision '{"accountId":"id","policyDiscardRevisionInput":{"id":"id"},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy discardPolicyRevision '{
    "accountId": "id",
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
