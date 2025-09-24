
## CATO-CLI - mutation.policy.terminalServer.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.terminalServer.createPolicyRevision:

`catocli mutation policy terminalServer createPolicyRevision -h`

`catocli mutation policy terminalServer createPolicyRevision <json>`

`catocli mutation policy terminalServer createPolicyRevision "$(cat < mutation.policy.terminalServer.createPolicyRevision.json)"`

`catocli mutation policy terminalServer createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
