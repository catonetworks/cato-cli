
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.removeRule) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.removeRule:

```bash
catocli mutation policy sdpStaticIpAllocation removeRule -h

catocli mutation policy sdpStaticIpAllocation removeRule <json>

catocli mutation policy sdpStaticIpAllocation removeRule --json-file mutation.policy.sdpStaticIpAllocation.removeRule.json

catocli mutation policy sdpStaticIpAllocation removeRule '{"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}},"sdpStaticIpAllocationRemoveRuleInput":{"id":"id"}}'

catocli mutation policy sdpStaticIpAllocation removeRule '{
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "sdpStaticIpAllocationRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.removeRule ####

`accountId` [ID] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
`sdpStaticIpAllocationRemoveRuleInput` [SdpStaticIpAllocationRemoveRuleInput] - (required) N/A
