
## CATO-CLI - mutation.policy.appTenantRestriction.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.publishPolicyRevision:

```bash
catocli mutation policy appTenantRestriction publishPolicyRevision -h

catocli mutation policy appTenantRestriction publishPolicyRevision <json>

catocli mutation policy appTenantRestriction publishPolicyRevision --json-file mutation.policy.appTenantRestriction.publishPolicyRevision.json

catocli mutation policy appTenantRestriction publishPolicyRevision '{"appTenantRestrictionPolicyMutationInput":{"revision":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'

catocli mutation policy appTenantRestriction publishPolicyRevision '{
    "appTenantRestrictionPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.policy.appTenantRestriction.publishPolicyRevision ####

`accountId` [ID] - (required) Account whose policies are accessed.
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) Parameters for this policy operation.
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) Parameters for this policy operation.
