# Parse the query response using jq to get names and ids only

```bash
# Parse the query response using jq to get names and ids only
catocli query policy wanFirewall policy | jq '.data.policy.wanFirewall.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy wanFirewall policy | jq -r '.data.policy.wanFirewall.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```