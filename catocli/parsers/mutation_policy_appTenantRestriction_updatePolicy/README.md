
## CATO-CLI - mutation.policy.appTenantRestriction.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updatePolicy:

```bash
catocli mutation policy appTenantRestriction updatePolicy -h

catocli mutation policy appTenantRestriction updatePolicy <json>

catocli mutation policy appTenantRestriction updatePolicy --json-file mutation.policy.appTenantRestriction.updatePolicy.json

catocli mutation policy appTenantRestriction updatePolicy '{"appTenantRestrictionPolicyMutationInput":{"revision":{"id":"id"}},"appTenantRestrictionPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy appTenantRestriction updatePolicy '{
    "appTenantRestrictionPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "appTenantRestrictionPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.appTenantRestriction.updatePolicy ####

`accountId` [ID] - (required) Account whose policies are accessed.
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) Parameters for this policy operation.
`appTenantRestrictionPolicyUpdateInput` [AppTenantRestrictionPolicyUpdateInput] - (required) Parameters for this policy operation.
