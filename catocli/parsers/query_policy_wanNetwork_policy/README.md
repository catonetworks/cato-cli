
## CATO-CLI - query.policy.wanNetwork.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.wanNetwork.policy) for documentation on this operation.

### Usage for query.policy.wanNetwork.policy:

```bash
catocli query policy wanNetwork policy -h

catocli query policy wanNetwork policy <json>

catocli query policy wanNetwork policy "$(cat < query.policy.wanNetwork.policy.json)"

catocli query policy wanNetwork policy '{"wanNetworkPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy wanNetwork policy '{
    "wanNetworkPolicyInput": {
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
catocli query policy wanNetwork policy | jq '.data.policy.wanNetwork.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy wanNetwork policy | jq -r '.data.policy.wanNetwork.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.wanNetwork.policy ####

`accountId` [ID] - (required) N/A    
`wanNetworkPolicyInput` [WanNetworkPolicyInput] - (required) N/A    
