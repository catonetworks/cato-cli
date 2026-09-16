
## CATO-CLI - mutation.policy.siteWebProxy.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.updatePolicy:

```bash
catocli mutation policy siteWebProxy updatePolicy -h

catocli mutation policy siteWebProxy updatePolicy <json>

catocli mutation policy siteWebProxy updatePolicy --json-file mutation.policy.siteWebProxy.updatePolicy.json

catocli mutation policy siteWebProxy updatePolicy '{"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}},"siteWebProxyPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy siteWebProxy updatePolicy '{
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "siteWebProxyPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.updatePolicy ####

`accountId` [ID] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
`siteWebProxyPolicyUpdateInput` [SiteWebProxyPolicyUpdateInput] - (required) N/A    
