
## CATO-CLI - mutation.policy.terminalServer.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.removeRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.removeRule:

`catocli mutation policy terminalServer removeRule -h`

`catocli mutation policy terminalServer removeRule <json>`

`catocli mutation policy terminalServer removeRule "$(cat < mutation.policy.terminalServer.removeRule.json)"`

`catocli mutation policy terminalServer removeRule '{"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"terminalServerRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy terminalServer removeRule -p '{
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "terminalServerRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.removeRule ####

`accountId` [ID] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
`terminalServerRemoveRuleInput` [TerminalServerRemoveRuleInput] - (required) N/A    
