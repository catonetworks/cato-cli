
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.createPolicyRevision:

```bash
catocli mutation policy sdpStaticIpAllocation createPolicyRevision -h

catocli mutation policy sdpStaticIpAllocation createPolicyRevision <json>

catocli mutation policy sdpStaticIpAllocation createPolicyRevision --json-file mutation.policy.sdpStaticIpAllocation.createPolicyRevision.json

catocli mutation policy sdpStaticIpAllocation createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation createPolicyRevision '{
    "policyCreateRevisionInput": {
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

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.createPolicyRevision ####

`accountId` [ID] - (required) N/A
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
