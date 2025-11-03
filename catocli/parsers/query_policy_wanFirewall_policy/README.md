
## CATO-CLI - query.policy.wanFirewall.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.wanFirewall.policy) for documentation on this operation.

### Usage for query.policy.wanFirewall.policy:

```bash
catocli query policy wanFirewall policy -h

catocli query policy wanFirewall policy <json>

catocli query policy wanFirewall policy "$(cat < query.policy.wanFirewall.policy.json)"

catocli query policy wanFirewall policy '{"wanFirewallPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy wanFirewall policy '{
    "wanFirewallPolicyInput": {
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
catocli query policy wanFirewall policy | jq '.data.policy.wanFirewall.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy wanFirewall policy | jq -r '.data.policy.wanFirewall.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.wanFirewall.policy ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyInput` [WanFirewallPolicyInput] - (required) N/A    
