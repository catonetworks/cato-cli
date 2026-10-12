
## CATO-CLI - query.policy.sdpStaticIpAllocation.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.sdpStaticIpAllocation.policy) for documentation on this operation.

### Usage for query.policy.sdpStaticIpAllocation.policy:

```bash
catocli query policy sdpStaticIpAllocation policy -h

catocli query policy sdpStaticIpAllocation policy <json>

catocli query policy sdpStaticIpAllocation policy --json-file query.policy.sdpStaticIpAllocation.policy.json

catocli query policy sdpStaticIpAllocation policy '{"sdpStaticIpAllocationPolicyInput":{"revision":{"id":"id","type":"PRIVATE"}}}'

catocli query policy sdpStaticIpAllocation policy '{
    "sdpStaticIpAllocationPolicyInput": {
        "revision": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'
```

#### Operation Arguments for query.policy.sdpStaticIpAllocation.policy ####

`accountId` [ID] - (required) N/A
`sdpStaticIpAllocationPolicyInput` [SdpStaticIpAllocationPolicyInput] - (required) N/A
