
## CATO-CLI - mutation.policy.clientConnectivity.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.addSection) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.addSection:

```bash
catocli mutation policy clientConnectivity addSection -h

catocli mutation policy clientConnectivity addSection <json>

catocli mutation policy clientConnectivity addSection --json-file mutation.policy.clientConnectivity.addSection.json

catocli mutation policy clientConnectivity addSection '{"clientConnectivityPolicyMutationInput":{"revision":{"id":"id"}},"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}}}'

catocli mutation policy clientConnectivity addSection '{
    "clientConnectivityPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.addSection ####

`accountId` [ID] - (required) Account whose policies are accessed.
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) Parameters for this policy operation.
`policyAddSectionInput` [PolicyAddSectionInput] - (required) Parameters for this policy operation.
