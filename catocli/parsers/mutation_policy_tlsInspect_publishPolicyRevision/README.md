
## CATO-CLI - mutation.policy.tlsInspect.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.publishPolicyRevision:

`catocli mutation policy tlsInspect publishPolicyRevision -h`

`catocli mutation policy tlsInspect publishPolicyRevision <json>`

`catocli mutation policy tlsInspect publishPolicyRevision "$(cat < mutation.policy.tlsInspect.publishPolicyRevision.json)"`

`catocli mutation policy tlsInspect publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
