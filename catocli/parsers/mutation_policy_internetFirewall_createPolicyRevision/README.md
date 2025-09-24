
## CATO-CLI - mutation.policy.internetFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.createPolicyRevision:

`catocli mutation policy internetFirewall createPolicyRevision -h`

`catocli mutation policy internetFirewall createPolicyRevision <json>`

`catocli mutation policy internetFirewall createPolicyRevision "$(cat < mutation.policy.internetFirewall.createPolicyRevision.json)"`

`catocli mutation policy internetFirewall createPolicyRevision '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyCreateRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy internetFirewall createPolicyRevision -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
