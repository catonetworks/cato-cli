
## CATO-CLI - mutation.policy.remotePortFwd.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.removeRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.removeRule:

`catocli mutation policy remotePortFwd removeRule -h`

`catocli mutation policy remotePortFwd removeRule <json>`

`catocli mutation policy remotePortFwd removeRule "$(cat < mutation.policy.remotePortFwd.removeRule.json)"`

`catocli mutation policy remotePortFwd removeRule '{"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"remotePortFwdRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy remotePortFwd removeRule -p '{
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "remotePortFwdRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.removeRule ####

`accountId` [ID] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
`remotePortFwdRemoveRuleInput` [RemotePortFwdRemoveRuleInput] - (required) N/A    
