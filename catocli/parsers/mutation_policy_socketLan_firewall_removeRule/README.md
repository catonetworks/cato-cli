
## CATO-CLI - mutation.policy.socketLan.firewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.firewall.removeRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.firewall.removeRule:

```bash
catocli mutation policy socketLan firewall removeRule -h

catocli mutation policy socketLan firewall removeRule <json>

catocli mutation policy socketLan firewall removeRule --json-file mutation.policy.socketLan.firewall.removeRule.json

catocli mutation policy socketLan firewall removeRule '{"socketLanFirewallRemoveRuleInput":{"id":"id"},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketLan firewall removeRule '{
    "socketLanFirewallRemoveRuleInput": {
        "id": "id"
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.firewall.removeRule ####

`accountId` [ID] - (required) N/A    
`socketLanFirewallRemoveRuleInput` [SocketLanFirewallRemoveRuleInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
