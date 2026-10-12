
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.removeSection) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.removeSection:

```bash
catocli mutation policy sdpStaticIpAllocation removeSection -h

catocli mutation policy sdpStaticIpAllocation removeSection <json>

catocli mutation policy sdpStaticIpAllocation removeSection --json-file mutation.policy.sdpStaticIpAllocation.removeSection.json

catocli mutation policy sdpStaticIpAllocation removeSection '{"policyRemoveSectionInput":{"id":"id"},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation removeSection '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.removeSection ####

`accountId` [ID] - (required) N/A
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
