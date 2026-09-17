
## CATO-CLI - mutation.policy.internetFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.addSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addSection:

```bash
catocli mutation policy internetFirewall addSection -h

catocli mutation policy internetFirewall addSection <json>

catocli mutation policy internetFirewall addSection --json-file mutation.policy.internetFirewall.addSection.json

catocli mutation policy internetFirewall addSection '{"internetFirewallPolicyMutationInput":{"revision":{"id":"id"}},"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}}}'

catocli mutation policy internetFirewall addSection '{
    "internetFirewallPolicyMutationInput": {
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

#### Operation Arguments for mutation.policy.internetFirewall.addSection ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
