
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

`accountId` [ID] - (required) N/A
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
