
## CATO-CLI - mutation.policy.applicationControl.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.removeRule) for documentation on this operation.

### Usage for mutation.policy.applicationControl.removeRule:

`catocli mutation policy applicationControl removeRule -h`

`catocli mutation policy applicationControl removeRule <json>`

`catocli mutation policy applicationControl removeRule "$(cat < mutation.policy.applicationControl.removeRule.json)"`

`catocli mutation policy applicationControl removeRule '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"applicationControlRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy applicationControl removeRule -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "applicationControlRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.removeRule ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`applicationControlRemoveRuleInput` [ApplicationControlRemoveRuleInput] - (required) N/A    
