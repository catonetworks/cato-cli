
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.moveSection) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.moveSection:

```bash
catocli mutation policy sdpStaticIpAllocation moveSection -h

catocli mutation policy sdpStaticIpAllocation moveSection <json>

catocli mutation policy sdpStaticIpAllocation moveSection --json-file mutation.policy.sdpStaticIpAllocation.moveSection.json

catocli mutation policy sdpStaticIpAllocation moveSection '{"policyMoveSectionInput":{"id":"id","to":{"position":"AFTER_SECTION","ref":"id"}},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation moveSection '{
    "policyMoveSectionInput": {
        "id": "id",
        "to": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.moveSection ####

`accountId` [ID] - (required) N/A
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
