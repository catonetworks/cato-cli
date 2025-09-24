
## CATO-CLI - query.policy.dynamicIpAllocation.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.dynamicIpAllocation.policy) for documentation on this operation.

### Usage for query.policy.dynamicIpAllocation.policy:

`catocli query policy dynamicIpAllocation policy -h`

`catocli query policy dynamicIpAllocation policy <json>`

`catocli query policy dynamicIpAllocation policy "$(cat < query.policy.dynamicIpAllocation.policy.json)"`

`catocli query policy dynamicIpAllocation policy '{"dynamicIpAllocationPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy dynamicIpAllocation policy -p '{
    "dynamicIpAllocationPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.dynamicIpAllocation.policy ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyInput` [DynamicIpAllocationPolicyInput] - (required) N/A    
