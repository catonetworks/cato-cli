
## CATO-CLI - mutation.policy.sdpStaticIpAllocation.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.sdpStaticIpAllocation.updateRule) for documentation on this operation.

### Usage for mutation.policy.sdpStaticIpAllocation.updateRule:

```bash
catocli mutation policy sdpStaticIpAllocation updateRule -h

catocli mutation policy sdpStaticIpAllocation updateRule <json>

catocli mutation policy sdpStaticIpAllocation updateRule --json-file mutation.policy.sdpStaticIpAllocation.updateRule.json

catocli mutation policy sdpStaticIpAllocation updateRule '{"sdpStaticIpAllocationPolicyMutationInput":{"revision":{"id":"id"}},"sdpStaticIpAllocationUpdateRuleInput":{"id":"id","rule":{"description":"string","enabled":true,"ip":"192.0.2.1","name":"string","source":{"user":{"by":"ID","input":"string"}}}}}'

catocli mutation policy sdpStaticIpAllocation updateRule '{
    "sdpStaticIpAllocationPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "sdpStaticIpAllocationUpdateRuleInput": {
        "id": "id",
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
    }
}'
```

#### Operation Arguments for mutation.policy.sdpStaticIpAllocation.updateRule ####

`accountId` [ID] - (required) N/A
`sdpStaticIpAllocationPolicyMutationInput` [SdpStaticIpAllocationPolicyMutationInput] - (required) N/A
`sdpStaticIpAllocationUpdateRuleInput` [SdpStaticIpAllocationUpdateRuleInput] - (required) N/A
