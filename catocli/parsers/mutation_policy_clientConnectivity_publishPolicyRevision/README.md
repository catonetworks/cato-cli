
## CATO-CLI - mutation.policy.clientConnectivity.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.publishPolicyRevision:

```bash
catocli mutation policy clientConnectivity publishPolicyRevision -h

catocli mutation policy clientConnectivity publishPolicyRevision <json>

catocli mutation policy clientConnectivity publishPolicyRevision --json-file mutation.policy.clientConnectivity.publishPolicyRevision.json

catocli mutation policy clientConnectivity publishPolicyRevision '{"clientConnectivityPolicyMutationInput":{"revision":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'

catocli mutation policy clientConnectivity publishPolicyRevision '{
    "clientConnectivityPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.publishPolicyRevision ####

`accountId` [ID] - (required) Account whose policies are accessed.
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) Parameters for this policy operation.
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) Parameters for this policy operation.
