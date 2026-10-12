
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.moveRule) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.moveRule:

```bash
catocli mutation policy sdpStaticIpAllocation moveRule -h

catocli mutation policy sdpStaticIpAllocation moveRule <json>

catocli mutation policy sdpStaticIpAllocation moveRule --json-file mutation.policy.sdpStaticIpAllocation.moveRule.json

catocli mutation policy sdpStaticIpAllocation moveRule '{"policyMoveRuleInput":{"id":"id","to":{"position":"AFTER_RULE","ref":"id"}},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "to": {
            "position": "AFTER_RULE",
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

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.moveRule ####

`accountId` [ID] - (required) N/A
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
