
## CATO-CLI - mutation.policy.remotePortFwd.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.publishPolicyRevision:

`catocli mutation policy remotePortFwd publishPolicyRevision -h`

`catocli mutation policy remotePortFwd publishPolicyRevision <json>`

`catocli mutation policy remotePortFwd publishPolicyRevision "$(cat < mutation.policy.remotePortFwd.publishPolicyRevision.json)"`

`catocli mutation policy remotePortFwd publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
