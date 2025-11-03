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