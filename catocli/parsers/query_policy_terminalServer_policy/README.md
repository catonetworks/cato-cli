
## CATO-CLI - query.policy.terminalServer.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.terminalServer.policy) for documentation on this operation.

### Usage for query.policy.terminalServer.policy:

`catocli query policy terminalServer policy -h`

`catocli query policy terminalServer policy <json>`

`catocli query policy terminalServer policy "$(cat < query.policy.terminalServer.policy.json)"`

`catocli query policy terminalServer policy '{"terminalServerPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy terminalServer policy -p '{
    "terminalServerPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.terminalServer.policy ####

`accountId` [ID] - (required) N/A    
`terminalServerPolicyInput` [TerminalServerPolicyInput] - (required) N/A    
