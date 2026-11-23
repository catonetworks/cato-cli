
## CATO-CLI - mutation.policy.splitTunnel.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.publishPolicyRevision:

```bash
catocli mutation policy splitTunnel publishPolicyRevision -h

catocli mutation policy splitTunnel publishPolicyRevision <json>

catocli mutation policy splitTunnel publishPolicyRevision --json-file mutation.policy.splitTunnel.publishPolicyRevision.json

catocli mutation policy splitTunnel publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"splitTunnelPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy splitTunnel publishPolicyRevision '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "splitTunnelPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.publishPolicyRevision ####

`accountId` [ID] - (required) Account whose policies are accessed.
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) Parameters for this policy operation.
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) Parameters for this policy operation.
