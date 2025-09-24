
## CATO-CLI - mutation.policy.tlsInspect.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.updatePolicy:

`catocli mutation policy tlsInspect updatePolicy -h`

`catocli mutation policy tlsInspect updatePolicy <json>`

`catocli mutation policy tlsInspect updatePolicy "$(cat < mutation.policy.tlsInspect.updatePolicy.json)"`

`catocli mutation policy tlsInspect updatePolicy '{"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"tlsInspectPolicyUpdateInput":{"state":"ENABLED","tlsInspectConfigInput":{"defaultRuleAction":"INSPECT","defaultRuleUntrustedCertificateAction":"ALLOW"}}}'`

`catocli mutation policy tlsInspect updatePolicy -p '{
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "tlsInspectPolicyUpdateInput": {
        "state": "ENABLED",
        "tlsInspectConfigInput": {
            "defaultRuleAction": "INSPECT",
            "defaultRuleUntrustedCertificateAction": "ALLOW"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.updatePolicy ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
`tlsInspectPolicyUpdateInput` [TlsInspectPolicyUpdateInput] - (required) N/A    
