
## CATO-CLI - mutation.policy.remotePortFwd.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.updateSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updateSection:

`catocli mutation policy remotePortFwd updateSection -h`

`catocli mutation policy remotePortFwd updateSection <json>`

`catocli mutation policy remotePortFwd updateSection "$(cat < mutation.policy.remotePortFwd.updateSection.json)"`

`catocli mutation policy remotePortFwd updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
