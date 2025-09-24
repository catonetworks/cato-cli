
## CATO-CLI - query.policy.tlsInspect.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.tlsInspect.policy) for documentation on this operation.

### Usage for query.policy.tlsInspect.policy:

`catocli query policy tlsInspect policy -h`

`catocli query policy tlsInspect policy <json>`

`catocli query policy tlsInspect policy "$(cat < query.policy.tlsInspect.policy.json)"`

`catocli query policy tlsInspect policy '{"tlsInspectPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy tlsInspect policy -p '{
    "tlsInspectPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.tlsInspect.policy ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyInput` [TlsInspectPolicyInput] - (required) N/A    
