
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.publishPolicyRevision:

```bash
catocli mutation policy sdpStaticIpAllocation publishPolicyRevision -h

catocli mutation policy sdpStaticIpAllocation publishPolicyRevision <json>

catocli mutation policy sdpStaticIpAllocation publishPolicyRevision --json-file mutation.policy.sdpStaticIpAllocation.publishPolicyRevision.json

catocli mutation policy sdpStaticIpAllocation publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation publishPolicyRevision '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.publishPolicyRevision ####

`accountId` [ID] - (required) N/A
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
