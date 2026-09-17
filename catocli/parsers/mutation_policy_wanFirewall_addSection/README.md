
## CATO-CLI - mutation.policy.wanFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.addSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.addSection:

```bash
catocli mutation policy wanFirewall addSection -h

catocli mutation policy wanFirewall addSection <json>

catocli mutation policy wanFirewall addSection --json-file mutation.policy.wanFirewall.addSection.json

catocli mutation policy wanFirewall addSection '{"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"wanFirewallPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy wanFirewall addSection '{
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
        "section": {
            "name": "string"
        }
    },
    "wanFirewallPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.wanFirewall.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
