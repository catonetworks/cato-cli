
## CATO-CLI - query.policy.remotePortFwd.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.remotePortFwd.policy) for documentation on this operation.

### Usage for query.policy.remotePortFwd.policy:

`catocli query policy remotePortFwd policy -h`

`catocli query policy remotePortFwd policy <json>`

`catocli query policy remotePortFwd policy "$(cat < query.policy.remotePortFwd.policy.json)"`

`catocli query policy remotePortFwd policy '{"remotePortFwdPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy remotePortFwd policy -p '{
    "remotePortFwdPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.remotePortFwd.policy ####

`accountId` [ID] - (required) N/A    
`remotePortFwdPolicyInput` [RemotePortFwdPolicyInput] - (required) N/A    
