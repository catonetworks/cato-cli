
## CATO-CLI - query.policy.socketLan.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.socketLan.policy) for documentation on this operation.

### Usage for query.policy.socketLan.policy:

`catocli query policy socketLan policy -h`

`catocli query policy socketLan policy <json>`

`catocli query policy socketLan policy "$(cat < query.policy.socketLan.policy.json)"`

`catocli query policy socketLan policy '{"socketLanPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy socketLan policy -p '{
    "socketLanPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.socketLan.policy ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyInput` [SocketLanPolicyInput] - (required) N/A    
