
## CATO-CLI - mutation.policy.siteWebProxy.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.siteWebProxy.addSection) for documentation on this operation.

### Usage for mutation.policy.siteWebProxy.addSection:

```bash
catocli mutation policy siteWebProxy addSection -h

catocli mutation policy siteWebProxy addSection <json>

catocli mutation policy siteWebProxy addSection --json-file mutation.policy.siteWebProxy.addSection.json

catocli mutation policy siteWebProxy addSection '{"accountId":"id","policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"siteWebProxyPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy siteWebProxy addSection '{
    "accountId": "id",
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    },
    "siteWebProxyPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.siteWebProxy.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`siteWebProxyPolicyMutationInput` [SiteWebProxyPolicyMutationInput] - (required) N/A    
