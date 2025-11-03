
## CATO-CLI - query.policy.appTenantRestriction.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.appTenantRestriction.policy) for documentation on this operation.

### Usage for query.policy.appTenantRestriction.policy:

```bash
catocli query policy appTenantRestriction policy -h

catocli query policy appTenantRestriction policy <json>

catocli query policy appTenantRestriction policy "$(cat < query.policy.appTenantRestriction.policy.json)"

catocli query policy appTenantRestriction policy '{"appTenantRestrictionPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'

catocli query policy appTenantRestriction policy '{
    "appTenantRestrictionPolicyInput": {
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
catocli query policy appTenantRestriction policy | jq '.data.policy.appTenantRestriction.policy.rules[].rule | {name: .name, id: .id}'
```

# Parse the query response using jq to get names and ids with index included:

```bash
# Parse the query response using jq to get names and ids with index included:
catocli query policy appTenantRestriction policy | jq -r '.data.policy.appTenantRestriction.policy.rules[] | "\(.rule.index) | \(.rule.name) | \(.rule.id)"'
```


#### Operation Arguments for query.policy.appTenantRestriction.policy ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyInput` [AppTenantRestrictionPolicyInput] - (required) N/A    
