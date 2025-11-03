
## CATO-CLI - query.policy.internetFirewall.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.internetFirewall.policy) for documentation on this operation.

### Usage for query.policy.internetFirewall.policy:

```bash
catocli query policy internetFirewall policy -h

catocli query policy internetFirewall policy <json>

catocli query policy internetFirewall policy "$(cat < query.policy.internetFirewall.policy.json)"

catocli query policy internetFirewall policy '{"internetFirewallPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy internetFirewall policy '{
    "internetFirewallPolicyInput": {
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
catocli query policy internetFirewall policy | jq '.data.policy.internetFirewall.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy internetFirewall policy | jq -r '.data.policy.internetFirewall.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.internetFirewall.policy ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyInput` [InternetFirewallPolicyInput] - (required) N/A    
