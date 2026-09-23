
## CATO-CLI - query.policy.privateAccess.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.privateAccess.policy) for documentation on this operation.

### Usage for query.policy.privateAccess.policy:

```bash
catocli query policy privateAccess policy -h

catocli query policy privateAccess policy <json>

catocli query policy privateAccess policy --json-file query.policy.privateAccess.policy.json

catocli query policy privateAccess policy '{"privateAccessPolicyInput":{"revision":{"id":"id","type":"PRIVATE"}}}'

catocli query policy privateAccess policy '{
    "privateAccessPolicyInput": {
        "revision": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'
```

#### Operation Arguments for query.policy.privateAccess.policy ####

`accountId` [ID] - (required) N/A    
`privateAccessPolicyInput` [PrivateAccessPolicyInput] - (required) N/A    
