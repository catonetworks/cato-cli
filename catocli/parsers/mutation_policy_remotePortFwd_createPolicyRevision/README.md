
## CATO-CLI - mutation.policy.remotePortFwd.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.createPolicyRevision:

`catocli mutation policy remotePortFwd createPolicyRevision -h`

`catocli mutation policy remotePortFwd createPolicyRevision <json>`

`catocli mutation policy remotePortFwd createPolicyRevision "$(cat < mutation.policy.remotePortFwd.createPolicyRevision.json)"`

`catocli mutation policy remotePortFwd createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
