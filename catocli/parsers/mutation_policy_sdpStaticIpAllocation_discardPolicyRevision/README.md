
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.discardPolicyRevision:

```bash
catocli mutation policy sdpStaticIpAllocation discardPolicyRevision -h

catocli mutation policy sdpStaticIpAllocation discardPolicyRevision <json>

catocli mutation policy sdpStaticIpAllocation discardPolicyRevision --json-file mutation.policy.sdpStaticIpAllocation.discardPolicyRevision.json

catocli mutation policy sdpStaticIpAllocation discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation discardPolicyRevision '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.discardPolicyRevision ####

`accountId` [ID] - (required) Account whose policies are accessed.
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) Parameters for this policy operation.
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) Parameters for this policy operation.
