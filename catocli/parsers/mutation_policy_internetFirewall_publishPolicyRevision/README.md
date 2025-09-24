
## CATO-CLI - mutation.policy.internetFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.publishPolicyRevision:

`catocli mutation policy internetFirewall publishPolicyRevision -h`

`catocli mutation policy internetFirewall publishPolicyRevision <json>`

`catocli mutation policy internetFirewall publishPolicyRevision "$(cat < mutation.policy.internetFirewall.publishPolicyRevision.json)"`

`catocli mutation policy internetFirewall publishPolicyRevision '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy internetFirewall publishPolicyRevision -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
