
## CATO-CLI - mutation.policy.terminalServer.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.terminalServer.discardPolicyRevision:

`catocli mutation policy terminalServer discardPolicyRevision -h`

`catocli mutation policy terminalServer discardPolicyRevision <json>`

`catocli mutation policy terminalServer discardPolicyRevision "$(cat < mutation.policy.terminalServer.discardPolicyRevision.json)"`

`catocli mutation policy terminalServer discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
