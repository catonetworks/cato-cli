
## CATO-CLI - mutation.policy.tlsInspect.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.removeRule) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.removeRule:

`catocli mutation policy tlsInspect removeRule -h`

`catocli mutation policy tlsInspect removeRule <json>`

`catocli mutation policy tlsInspect removeRule "$(cat < mutation.policy.tlsInspect.removeRule.json)"`

`catocli mutation policy tlsInspect removeRule '{"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"tlsInspectRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy tlsInspect removeRule -p '{
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "tlsInspectRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.removeRule ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
`tlsInspectRemoveRuleInput` [TlsInspectRemoveRuleInput] - (required) N/A    
