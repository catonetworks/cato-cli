
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

`accountId` [ID] - (required) Account whose policies are accessed.
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) Parameters for this policy operation.
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) Parameters for this policy operation.
