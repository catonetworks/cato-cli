
## CATO-CLI - mutation.policy.wanFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.createPolicyRevision:

`catocli mutation policy wanFirewall createPolicyRevision -h`

`catocli mutation policy wanFirewall createPolicyRevision <json>`

`catocli mutation policy wanFirewall createPolicyRevision "$(cat < mutation.policy.wanFirewall.createPolicyRevision.json)"`

`catocli mutation policy wanFirewall createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
