
## CATO-CLI - mutation.policy.ztnaAlwaysOn.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.moveSection) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.moveSection:

```bash
catocli mutation policy ztnaAlwaysOn moveSection -h

catocli mutation policy ztnaAlwaysOn moveSection <json>

catocli mutation policy ztnaAlwaysOn moveSection --json-file mutation.policy.ztnaAlwaysOn.moveSection.json

catocli mutation policy ztnaAlwaysOn moveSection '{"policyMoveSectionInput":{"id":"id","to":{"position":"AFTER_SECTION","ref":"id"}},"ztnaAlwaysOnPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn moveSection '{
    "policyMoveSectionInput": {
        "id": "id",
        "to": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
