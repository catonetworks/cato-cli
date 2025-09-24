
## CATO-CLI - mutation.policy.terminalServer.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.terminalServer.publishPolicyRevision:

`catocli mutation policy terminalServer publishPolicyRevision -h`

`catocli mutation policy terminalServer publishPolicyRevision <json>`

`catocli mutation policy terminalServer publishPolicyRevision "$(cat < mutation.policy.terminalServer.publishPolicyRevision.json)"`

`catocli mutation policy terminalServer publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
