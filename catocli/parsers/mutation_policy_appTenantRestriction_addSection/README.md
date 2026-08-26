
## CATO-CLI - mutation.policy.appTenantRestriction.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.addSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addSection:

```bash
catocli mutation policy appTenantRestriction addSection -h

catocli mutation policy appTenantRestriction addSection <json>

catocli mutation policy appTenantRestriction addSection --json-file mutation.policy.appTenantRestriction.addSection.json

catocli mutation policy appTenantRestriction addSection '{"appTenantRestrictionPolicyMutationInput":{"revision":{"id":"id"}},"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}}}'

catocli mutation policy appTenantRestriction addSection '{
    "appTenantRestrictionPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.appTenantRestriction.addSection ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
