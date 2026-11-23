
## CATO-CLI - mutation.policy.applicationControl.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.removeSection) for documentation on this operation.

### Usage for mutation.policy.applicationControl.removeSection:

```bash
catocli mutation policy applicationControl removeSection -h

catocli mutation policy applicationControl removeSection <json>

catocli mutation policy applicationControl removeSection --json-file mutation.policy.applicationControl.removeSection.json

catocli mutation policy applicationControl removeSection '{"applicationControlPolicyMutationInput":{"revision":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'

catocli mutation policy applicationControl removeSection '{
    "applicationControlPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.applicationControl.removeSection ####

`accountId` [ID] - (required) Account whose policies are accessed.
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) Parameters for this policy operation.
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) Parameters for this policy operation.
