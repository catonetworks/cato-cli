
## CATO-CLI - mutation.policy.internetFirewall.removeSubPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.removeSubPolicy) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeSubPolicy:

```bash
catocli mutation policy internetFirewall removeSubPolicy -h

catocli mutation policy internetFirewall removeSubPolicy <json>

catocli mutation policy internetFirewall removeSubPolicy --json-file mutation.policy.internetFirewall.removeSubPolicy.json

catocli mutation policy internetFirewall removeSubPolicy '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"internetFirewallRemoveSubPolicyInput":{"internetFirewallPolicyRefInput":{"by":"ID","input":"string"}}}'

catocli mutation policy internetFirewall removeSubPolicy '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "internetFirewallRemoveSubPolicyInput": {
        "internetFirewallPolicyRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.internetFirewall.removeSubPolicy ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`internetFirewallRemoveSubPolicyInput` [InternetFirewallRemoveSubPolicyInput] - (required) N/A    
