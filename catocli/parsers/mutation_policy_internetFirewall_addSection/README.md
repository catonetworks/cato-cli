
## CATO-CLI - mutation.policy.internetFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addSection:

`catocli mutation policy internetFirewall addSection -h`

`catocli mutation policy internetFirewall addSection <accountID> <json>`

`catocli mutation policy internetFirewall addSection 12345 "$(cat < addSection.json)"`

`catocli mutation policy internetFirewall addSection 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyAddSectionInput": {"PolicyAddSectionInfoInput": {"name": {"name": "String"}}, "PolicySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.addSection ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`accountId` [ID] - (required) N/A 