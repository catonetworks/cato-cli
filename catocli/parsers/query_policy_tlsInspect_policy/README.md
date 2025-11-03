
## CATO-CLI - query.policy.tlsInspect.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.tlsInspect.policy) for documentation on this operation.

### Usage for query.policy.tlsInspect.policy:

```bash
catocli query policy tlsInspect policy -h

catocli query policy tlsInspect policy <json>

catocli query policy tlsInspect policy "$(cat < query.policy.tlsInspect.policy.json)"

catocli query policy tlsInspect policy '{"tlsInspectPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy tlsInspect policy '{
    "tlsInspectPolicyInput": {
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
catocli query policy tlsInspect policy | jq '.data.policy.tlsInspect.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy tlsInspect policy | jq -r '.data.policy.tlsInspect.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.tlsInspect.policy ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyInput` [TlsInspectPolicyInput] - (required) N/A    
