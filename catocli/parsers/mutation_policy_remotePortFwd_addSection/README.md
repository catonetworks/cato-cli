
## CATO-CLI - mutation.policy.remotePortFwd.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.addSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.addSection:

`catocli mutation policy remotePortFwd addSection -h`

`catocli mutation policy remotePortFwd addSection <json>`

`catocli mutation policy remotePortFwd addSection "$(cat < mutation.policy.remotePortFwd.addSection.json)"`

`catocli mutation policy remotePortFwd addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd addSection -p '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
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


#### Operation Arguments for mutation.policy.remotePortFwd.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
