
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.addRule) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.addRule:

```bash
catocli mutation policy sdpStaticIpAllocation addRule -h

catocli mutation policy sdpStaticIpAllocation addRule <json>

catocli mutation policy sdpStaticIpAllocation addRule --json-file mutation.policy.sdpStaticIpAllocation.addRule.json

catocli mutation policy sdpStaticIpAllocation addRule '{"sdpStaticIpAllocationAddRuleInput":{"at":{"position":"AFTER_RULE","ref":"id"},"rule":{"description":"string","enabled":true,"ip":"192.0.2.1","name":"string","source":{"user":{"by":"ID","input":"string"}}}},"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy sdpStaticIpAllocation addRule '{
    "sdpStaticIpAllocationAddRuleInput": {
        "at": {
            "position": "AFTER_RULE",
            "ref": "id"
        },
        "rule": {
            "description": "string",
            "enabled": true,
            "ip": "192.0.2.1",
            "name": "string",
            "source": {
                "user": {
                    "by": "ID",
                    "input": "string"
                }
            }
        }
    },
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.addRule ####

`accountId` [ID] - (required) N/A
`sdpStaticIpAllocationAddRuleInput` [SdpStaticIpAllocationAddRuleInput] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
