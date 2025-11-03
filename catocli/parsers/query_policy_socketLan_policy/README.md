
## CATO-CLI - query.policy.socketLan.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.socketLan.policy) for documentation on this operation.

### Usage for query.policy.socketLan.policy:

```bash
catocli query policy socketLan policy -h

catocli query policy socketLan policy <json>

catocli query policy socketLan policy "$(cat < query.policy.socketLan.policy.json)"

catocli query policy socketLan policy '{"socketLanPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy socketLan policy '{
    "socketLanPolicyInput": {
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
catocli query policy socketLan policy | jq '.data.policy.socketLan.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy socketLan policy | jq -r '.data.policy.socketLan.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.socketLan.policy ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyInput` [SocketLanPolicyInput] - (required) N/A    
