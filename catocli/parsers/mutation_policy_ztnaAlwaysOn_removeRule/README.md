
## CATO-CLI - mutation.policy.ztnaAlwaysOn.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.removeRule) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.removeRule:

```bash
catocli mutation policy ztnaAlwaysOn removeRule -h

catocli mutation policy ztnaAlwaysOn removeRule <json>

catocli mutation policy ztnaAlwaysOn removeRule --json-file mutation.policy.ztnaAlwaysOn.removeRule.json

catocli mutation policy ztnaAlwaysOn removeRule '{"ztnaAlwaysOnPolicyMutationInput":{"revision":{"id":"id"}},"ztnaAlwaysOnRemoveRuleInput":{"id":"id"}}'

catocli mutation policy ztnaAlwaysOn removeRule '{
    "ztnaAlwaysOnPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "ztnaAlwaysOnRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.removeRule ####

`accountId` [ID] - (required) Account whose policies are accessed.
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) Parameters for this policy operation.
`ztnaAlwaysOnRemoveRuleInput` [ZtnaAlwaysOnRemoveRuleInput] - (required) Parameters for this policy operation.
