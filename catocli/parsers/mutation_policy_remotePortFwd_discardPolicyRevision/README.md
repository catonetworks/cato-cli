
## CATO-CLI - mutation.policy.remotePortFwd.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.discardPolicyRevision:

`catocli mutation policy remotePortFwd discardPolicyRevision -h`

`catocli mutation policy remotePortFwd discardPolicyRevision <json>`

`catocli mutation policy remotePortFwd discardPolicyRevision "$(cat < mutation.policy.remotePortFwd.discardPolicyRevision.json)"`

`catocli mutation policy remotePortFwd discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
