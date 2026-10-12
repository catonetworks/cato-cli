
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.addSection) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.addSection:

```bash
catocli mutation policy sdpStaticIpAllocation addSection -h

catocli mutation policy sdpStaticIpAllocation addSection <json>

catocli mutation policy sdpStaticIpAllocation addSection --json-file mutation.policy.sdpStaticIpAllocation.addSection.json

catocli mutation policy sdpStaticIpAllocation addSection '{"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation addSection '{
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
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

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.addSection ####

`accountId` [ID] - (required) N/A
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
