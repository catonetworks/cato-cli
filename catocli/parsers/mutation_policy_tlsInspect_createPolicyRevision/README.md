
## CATO-CLI - mutation.policy.tlsInspect.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.createPolicyRevision:

`catocli mutation policy tlsInspect createPolicyRevision -h`

`catocli mutation policy tlsInspect createPolicyRevision <json>`

`catocli mutation policy tlsInspect createPolicyRevision "$(cat < mutation.policy.tlsInspect.createPolicyRevision.json)"`

`catocli mutation policy tlsInspect createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
