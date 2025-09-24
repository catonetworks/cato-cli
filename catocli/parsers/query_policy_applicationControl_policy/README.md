
## CATO-CLI - query.policy.applicationControl.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.applicationControl.policy) for documentation on this operation.

### Usage for query.policy.applicationControl.policy:

`catocli query policy applicationControl policy -h`

`catocli query policy applicationControl policy <json>`

`catocli query policy applicationControl policy "$(cat < query.policy.applicationControl.policy.json)"`

`catocli query policy applicationControl policy '{"applicationControlPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy applicationControl policy -p '{
    "applicationControlPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.applicationControl.policy ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyInput` [ApplicationControlPolicyInput] - (required) N/A    
