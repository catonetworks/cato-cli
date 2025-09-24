
## CATO-CLI - mutation.policy.remotePortFwd.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.moveSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.moveSection:

`catocli mutation policy remotePortFwd moveSection -h`

`catocli mutation policy remotePortFwd moveSection <json>`

`catocli mutation policy remotePortFwd moveSection "$(cat < mutation.policy.remotePortFwd.moveSection.json)"`

`catocli mutation policy remotePortFwd moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
