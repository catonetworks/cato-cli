
## CATO-CLI - mutation.policy.terminalServer.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.removeSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.removeSection:

`catocli mutation policy terminalServer removeSection -h`

`catocli mutation policy terminalServer removeSection <json>`

`catocli mutation policy terminalServer removeSection "$(cat < mutation.policy.terminalServer.removeSection.json)"`

`catocli mutation policy terminalServer removeSection '{"policyRemoveSectionInput":{"id":"id"},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
