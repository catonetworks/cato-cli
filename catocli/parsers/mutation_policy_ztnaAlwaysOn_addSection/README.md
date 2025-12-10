
## CATO-CLI - mutation.policy.ztnaAlwaysOn.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.addSection) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.addSection:

```bash
catocli mutation policy ztnaAlwaysOn addSection -h

catocli mutation policy ztnaAlwaysOn addSection <json>

catocli mutation policy ztnaAlwaysOn addSection --json-file mutation.policy.ztnaAlwaysOn.addSection.json

catocli mutation policy ztnaAlwaysOn addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn addSection '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
