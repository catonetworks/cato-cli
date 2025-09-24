
## CATO-CLI - mutation.policy.terminalServer.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.moveSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.moveSection:

`catocli mutation policy terminalServer moveSection -h`

`catocli mutation policy terminalServer moveSection <json>`

`catocli mutation policy terminalServer moveSection "$(cat < mutation.policy.terminalServer.moveSection.json)"`

`catocli mutation policy terminalServer moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
