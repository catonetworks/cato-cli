
## CATO-CLI - mutation.policy.tlsInspect.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.updatePolicy:

```bash
catocli mutation policy tlsInspect updatePolicy -h

catocli mutation policy tlsInspect updatePolicy <json>

catocli mutation policy tlsInspect updatePolicy --json-file mutation.policy.tlsInspect.updatePolicy.json

catocli mutation policy tlsInspect updatePolicy '{"tlsInspectPolicyMutationInput":{"revision":{"id":"id"}},"tlsInspectPolicyUpdateInput":{"additionalAttributes":{"defaultRuleAction":"INSPECT","defaultRuleUntrustedCertificateAction":"ALLOW"},"state":"ENABLED"}}'

catocli mutation policy tlsInspect updatePolicy '{
    "tlsInspectPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "tlsInspectPolicyUpdateInput": {
        "additionalAttributes": {
            "defaultRuleAction": "INSPECT",
            "defaultRuleUntrustedCertificateAction": "ALLOW"
        },
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.tlsInspect.updatePolicy ####

`accountId` [ID] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
`tlsInspectPolicyUpdateInput` [TlsInspectPolicyUpdateInput] - (required) N/A    
