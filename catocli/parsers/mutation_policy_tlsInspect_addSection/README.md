
## CATO-CLI - mutation.policy.tlsInspect.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.addSection) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.addSection:

```bash
catocli mutation policy tlsInspect addSection -h

catocli mutation policy tlsInspect addSection <json>

catocli mutation policy tlsInspect addSection --json-file mutation.policy.tlsInspect.addSection.json

catocli mutation policy tlsInspect addSection '{"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"tlsInspectPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy tlsInspect addSection '{
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    },
    "tlsInspectPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.tlsInspect.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
