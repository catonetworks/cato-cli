
## CATO-CLI - query.policy.terminalServer.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.terminalServer.policy) for documentation on this operation.

### Usage for query.policy.terminalServer.policy:

```bash
catocli query policy terminalServer policy -h

catocli query policy terminalServer policy <json>

catocli query policy terminalServer policy "$(cat < query.policy.terminalServer.policy.json)"

catocli query policy terminalServer policy '{"terminalServerPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy terminalServer policy '{
    "terminalServerPolicyInput": {
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
catocli query policy terminalServer policy | jq '.data.policy.terminalServer.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy terminalServer policy | jq -r '.data.policy.terminalServer.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.terminalServer.policy ####

`accountId` [ID] - (required) N/A    
`terminalServerPolicyInput` [TerminalServerPolicyInput] - (required) N/A    
