
## CATO-CLI - mutation.policy.terminalServer.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.updateSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.updateSection:

`catocli mutation policy terminalServer updateSection -h`

`catocli mutation policy terminalServer updateSection <json>`

`catocli mutation policy terminalServer updateSection "$(cat < mutation.policy.terminalServer.updateSection.json)"`

`catocli mutation policy terminalServer updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
