
## CATO-CLI - query.policy.remotePortFwd.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.remotePortFwd.policy) for documentation on this operation.

### Usage for query.policy.remotePortFwd.policy:

```bash
catocli query policy remotePortFwd policy -h

catocli query policy remotePortFwd policy <json>

catocli query policy remotePortFwd policy "$(cat < query.policy.remotePortFwd.policy.json)"

catocli query policy remotePortFwd policy '{"remotePortFwdPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy remotePortFwd policy '{
    "remotePortFwdPolicyInput": {
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
catocli query policy remotePortFwd policy | jq '.data.policy.remotePortFwd.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy remotePortFwd policy | jq -r '.data.policy.remotePortFwd.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.remotePortFwd.policy ####

`accountId` [ID] - (required) N/A    
`remotePortFwdPolicyInput` [RemotePortFwdPolicyInput] - (required) N/A    
