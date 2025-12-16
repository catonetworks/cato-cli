
## CATO-CLI - mutation.policy.wanFirewall.removeSubPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.removeSubPolicy) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeSubPolicy:

```bash
catocli mutation policy wanFirewall removeSubPolicy -h

catocli mutation policy wanFirewall removeSubPolicy <json>

catocli mutation policy wanFirewall removeSubPolicy --json-file mutation.policy.wanFirewall.removeSubPolicy.json

catocli mutation policy wanFirewall removeSubPolicy '{"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanFirewallRemoveSubPolicyInput":{"wanFirewallPolicyRefInput":{"by":"ID","input":"string"}}}'

catocli mutation policy wanFirewall removeSubPolicy '{
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanFirewallRemoveSubPolicyInput": {
        "wanFirewallPolicyRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.wanFirewall.removeSubPolicy ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
`wanFirewallRemoveSubPolicyInput` [WanFirewallRemoveSubPolicyInput] - (required) N/A    
