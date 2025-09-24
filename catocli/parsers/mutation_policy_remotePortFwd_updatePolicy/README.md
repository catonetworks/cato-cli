
## CATO-CLI - mutation.policy.remotePortFwd.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updatePolicy:

`catocli mutation policy remotePortFwd updatePolicy -h`

`catocli mutation policy remotePortFwd updatePolicy <json>`

`catocli mutation policy remotePortFwd updatePolicy "$(cat < mutation.policy.remotePortFwd.updatePolicy.json)"`

`catocli mutation policy remotePortFwd updatePolicy '{"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"remotePortFwdPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy remotePortFwd updatePolicy -p '{
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "remotePortFwdPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.updatePolicy ####

`accountId` [ID] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
`remotePortFwdPolicyUpdateInput` [RemotePortFwdPolicyUpdateInput] - (required) N/A    
