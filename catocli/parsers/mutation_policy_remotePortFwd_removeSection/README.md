
## CATO-CLI - mutation.policy.remotePortFwd.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.removeSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.removeSection:

`catocli mutation policy remotePortFwd removeSection -h`

`catocli mutation policy remotePortFwd removeSection <json>`

`catocli mutation policy remotePortFwd removeSection "$(cat < mutation.policy.remotePortFwd.removeSection.json)"`

`catocli mutation policy remotePortFwd removeSection '{"policyRemoveSectionInput":{"id":"id"},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
