
## CATO-CLI - mutation.policy.wanFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.publishPolicyRevision:

`catocli mutation policy wanFirewall publishPolicyRevision -h`

`catocli mutation policy wanFirewall publishPolicyRevision <json>`

`catocli mutation policy wanFirewall publishPolicyRevision "$(cat < mutation.policy.wanFirewall.publishPolicyRevision.json)"`

`catocli mutation policy wanFirewall publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
