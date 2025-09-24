
## CATO-CLI - mutation.policy.terminalServer.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.terminalServer.updatePolicy:

`catocli mutation policy terminalServer updatePolicy -h`

`catocli mutation policy terminalServer updatePolicy <json>`

`catocli mutation policy terminalServer updatePolicy "$(cat < mutation.policy.terminalServer.updatePolicy.json)"`

`catocli mutation policy terminalServer updatePolicy '{"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"terminalServerPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy terminalServer updatePolicy -p '{
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "terminalServerPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.updatePolicy ####

`accountId` [ID] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
`terminalServerPolicyUpdateInput` [TerminalServerPolicyUpdateInput] - (required) N/A    
