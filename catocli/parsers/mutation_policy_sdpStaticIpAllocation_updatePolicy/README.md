
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.updatePolicy:

```bash
catocli mutation policy sdpStaticIpAllocation updatePolicy -h

catocli mutation policy sdpStaticIpAllocation updatePolicy <json>

catocli mutation policy sdpStaticIpAllocation updatePolicy --json-file mutation.policy.sdpStaticIpAllocation.updatePolicy.json

catocli mutation policy sdpStaticIpAllocation updatePolicy '{"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}},"sdpStaticIpAllocationPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy sdpStaticIpAllocation updatePolicy '{
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "sdpStaticIpAllocationPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.updatePolicy ####

`accountId` [ID] - (required) Account whose policies are accessed.
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) Parameters for this policy operation.
`sdpStaticIpAllocationPolicyUpdateInput` [SdpStaticIpAllocationPolicyUpdateInput] - (required) Parameters for this policy operation.
