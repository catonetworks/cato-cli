
## CATO-CLI - mutation.policy.terminalServer.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.addSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.addSection:

```bash
catocli mutation policy terminalServer addSection -h

catocli mutation policy terminalServer addSection <json>

catocli mutation policy terminalServer addSection --json-file mutation.policy.terminalServer.addSection.json

catocli mutation policy terminalServer addSection '{"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"terminalServerPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy terminalServer addSection '{
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    },
    "terminalServerPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.terminalServer.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
