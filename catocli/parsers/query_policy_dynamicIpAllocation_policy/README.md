
## CATO-CLI - query.policy.dynamicIpAllocation.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.dynamicIpAllocation.policy) for documentation on this operation.

### Usage for query.policy.dynamicIpAllocation.policy:

```bash
catocli query policy dynamicIpAllocation policy -h

catocli query policy dynamicIpAllocation policy <json>

catocli query policy dynamicIpAllocation policy "$(cat < query.policy.dynamicIpAllocation.policy.json)"

catocli query policy dynamicIpAllocation policy '{"dynamicIpAllocationPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy dynamicIpAllocation policy '{
    "dynamicIpAllocationPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'
```

## Advanced Usage
### Additional Examples
- Parse the query response using jq to get names and ids only
- Parse the query response using jq to get names and ids with index included:

# Parse the query response using jq to get names and ids only

```bash
# Parse the query response using jq to get names and ids only
catocli query policy dynamicIpAllocation policy | jq '.data.policy.wanNdynamicIpAllocationetwork.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy dynamicIpAllocation policy | jq -r '.data.policy.dynamicIpAllocation.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.dynamicIpAllocation.policy ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyInput` [DynamicIpAllocationPolicyInput] - (required) N/A    
