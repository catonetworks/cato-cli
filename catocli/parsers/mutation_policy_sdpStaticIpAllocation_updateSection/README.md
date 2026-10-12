
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.updateSection) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.updateSection:

```bash
catocli mutation policy sdpStaticIpAllocation updateSection -h

catocli mutation policy sdpStaticIpAllocation updateSection <json>

catocli mutation policy sdpStaticIpAllocation updateSection --json-file mutation.policy.sdpStaticIpAllocation.updateSection.json

catocli mutation policy sdpStaticIpAllocation updateSection '{"policyUpdateSectionInput":{"id":"id","section":{"name":"string"}},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation updateSection '{
    "policyUpdateSectionInput": {
        "id": "id",
        "section": {
            "name": "string"
        }
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.updateSection ####

`accountId` [ID] - (required) N/A
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
