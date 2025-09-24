
## CATO-CLI - mutation.policy.tlsInspect.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.discardPolicyRevision:

`catocli mutation policy tlsInspect discardPolicyRevision -h`

`catocli mutation policy tlsInspect discardPolicyRevision <json>`

`catocli mutation policy tlsInspect discardPolicyRevision "$(cat < mutation.policy.tlsInspect.discardPolicyRevision.json)"`

`catocli mutation policy tlsInspect discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
