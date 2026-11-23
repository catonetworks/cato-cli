
## CATO-CLI - mutation.policy.applicationControl.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.applicationControl.discardPolicyRevision:

```bash
catocli mutation policy applicationControl discardPolicyRevision -h

catocli mutation policy applicationControl discardPolicyRevision <json>

catocli mutation policy applicationControl discardPolicyRevision --json-file mutation.policy.applicationControl.discardPolicyRevision.json

catocli mutation policy applicationControl discardPolicyRevision '{"applicationControlPolicyMutationInput":{"revision":{"id":"id"}},"policyDiscardRevisionInput":{"id":"id"}}'

catocli mutation policy applicationControl discardPolicyRevision '{
    "applicationControlPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyDiscardRevisionInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.applicationControl.discardPolicyRevision ####

`accountId` [ID] - (required) Account whose policies are accessed.
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) Parameters for this policy operation.
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) Parameters for this policy operation.
